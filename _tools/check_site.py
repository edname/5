#!/usr/bin/env python3
"""Check static routes, metadata, JSON-LD, links, assets and sitemap coverage."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://karpenko.lt'

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.ids, self.links, self.assets = path, [], [], []
        self.meta, self.canonicals, self.h1, self.title = {}, [], 0, ''
        self.in_title, self.in_json, self.json_text, self.schemas = False, False, '', []
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag == 'h1': self.h1 += 1
        if tag == 'title': self.in_title = True
        if tag == 'a' and 'href' in a: self.links.append(a['href'])
        if tag in ('img', 'script') and 'src' in a: self.assets.append(a['src'])
        if tag == 'link' and a.get('rel') in ('stylesheet', 'icon'): self.assets.append(a['href'])
        if tag == 'link' and a.get('rel') == 'canonical': self.canonicals.append(a['href'])
        if tag == 'meta': self.meta[a.get('name', a.get('property'))] = a.get('content', '')
        if tag == 'script' and a.get('type') == 'application/ld+json': self.in_json = True
    def handle_data(self, data):
        if self.in_title: self.title += data
        if self.in_json: self.json_text += data
    def handle_endtag(self, tag):
        if tag == 'title': self.in_title = False
        if tag == 'script' and self.in_json:
            self.schemas.append(json.loads(self.json_text))
            self.in_json, self.json_text = False, ''

files = [ROOT/'index.html', *sorted(p for p in ROOT.glob('*/index.html') if not p.parent.name.startswith(('.', '_')))]
pages = {p.resolve(): Page(p) for p in files}
errors = []
def check(ok, message):
    if not ok: errors.append(message)

for path, page in pages.items():
    name = str(path.relative_to(ROOT))
    route = '/' if path == ROOT/'index.html' else '/' + path.parent.name + '/'
    expected = BASE + route
    check(page.h1 == 1, f'{name}: expected one H1')
    check(len(page.ids) == len(set(page.ids)), f'{name}: duplicate IDs')
    check(page.canonicals == [expected], f'{name}: incorrect canonical {page.canonicals}')
    check(page.meta.get('og:url') == expected, f'{name}: incorrect OG URL')
    check(page.meta.get('og:title') == page.title, f'{name}: title/OG mismatch')
    check(bool(page.meta.get('description')), f'{name}: missing description')
    check(page.meta.get('description') == page.meta.get('og:description'), f'{name}: description/OG mismatch')
    check(bool(page.schemas), f'{name}: missing JSON-LD')
    if route != '/':
        graph = page.schemas[0]['@graph']
        check(any(n.get('@type') == 'BreadcrumbList' for n in graph), f'{name}: missing breadcrumb schema')
        check(any(n.get('@type') == 'Service' and n.get('url') == expected for n in graph), f'{name}: wrong service schema')
    for href in page.links + page.assets:
        url = urlsplit(href)
        if url.scheme and not (url.scheme == 'https' and url.netloc == 'karpenko.lt'): continue
        if url.netloc and url.netloc != 'karpenko.lt': continue
        part = unquote(url.path)
        target = ((ROOT / part.lstrip('/')) if part.startswith('/') else (path.parent / part)) if part else path
        if target.is_dir(): target /= 'index.html'
        target = target.resolve()
        check(target.exists(), f'{name}: missing target {href}')
        if url.fragment and target in pages:
            check(url.fragment in pages[target].ids, f'{name}: missing fragment {href}')

for attr in ['title', 'description']:
    values = [p.title if attr == 'title' else p.meta[attr] for p in pages.values()]
    check(len(set(values)) == len(values), f'Duplicate {attr}')

ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
urls = [e.text for e in ET.parse(ROOT/'sitemap.xml').findall('s:url/s:loc', ns)]
check(set(urls) == {p.canonicals[0] for p in pages.values()}, 'Sitemap does not match canonical pages')
check(len(urls) == len(set(urls)), 'Duplicate sitemap URLs')
check('Sitemap: https://karpenko.lt/sitemap.xml' in (ROOT/'robots.txt').read_text(), 'Missing sitemap in robots.txt')
check('noindex' in Page(ROOT/'404.html').meta.get('robots',''), '404 should be noindex')
home_links = pages[(ROOT/'index.html').resolve()].links
for path in files[1:]:
    check('/'+path.parent.name+'/' in home_links, f'Orphan service page: {path.parent.name}')

if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(pages)} pages; unique metadata, canonical URLs, schema, links, assets and sitemap.')
