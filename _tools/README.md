# Static website pages

The repository is served directly by GitHub Pages on `gh-pages`, with the custom domain in `CNAME`. All public pages are committed HTML. No browser-side router, package installation or deployment build is required. A small homepage-only script redirects old section bookmarks to their new static pages.

Edit the home page in `index.html` and the service copy in `PAGES` in `_tools/build_pages.py`. Main navigation page copy lives in `_tools/info-pages.json`. That script reuses the home page header, footer and clinic identity to keep those details consistent across pages.

From the repository root:

```sh
python3 _tools/build_pages.py
python3 _tools/check_site.py
python3 -m http.server 8000 --bind 127.0.0.1
```

Commit the generated service directories with any template changes. Update the sitemap and its `lastmod` dates when published content changes; dates must reflect actual edits. If adding a new service, update the service index in `_tools/info-pages.json` and the sitemap as well. Main navigation pages are linked from the home page; service details are reachable through `/paslaugos/`. Use trailing-slash canonical URLs consistently. `css/styles.css` is shared by every page; its query version should change when a release needs a cache refresh.

`seo-research.json` records the keyword clusters, observed sources, scope constraints and measurement limitations. It is not a search-volume report. The `_tools` directory is maintenance material, excluded by GitHub Pages' default Jekyll handling of underscore-prefixed directories.

Before publishing, run the checks, review the pages at desktop and mobile widths, and verify that descriptions accurately reflect clinic services. Prices, qualifications, clinical review attribution, procedure availability and opening hours require actual clinic information.

## Puslapių išdėstymas

`page_body()` generatoriuje parenka išdėstymą pagal puslapio paskirtį. Esamas tekstas skaidomas pagal H2 antraštes; keičiant jų skaičių ar tvarką reikia atnaujinti atitinkamą kompoziciją. Klinikos įėjimo nuotrauka rodoma tik kontaktų puslapyje. Paslaugų puslapiuose bendrą registracijos šoninę skiltį pakeičia konkrečiai temai skirti informaciniai blokai ir apatinė paslaugų navigacija.

Registracija sujungta su `/kontaktai/`. `/registracija/` paliktas kaip statinis nukreipimas su canonical į kontaktus ir `noindex`; sitemap jo neįtraukia. Meniu ir vidinės registracijos nuorodos veda tiesiai į kontaktus.

## Gautas paslaugų kainoraštis

2026-10-06 gauto klinikos kainoraščio nuotrauka išsaugota `sources/paslaugu-kainorastis-gautas-2026-10-06.jpg`, o perrašytos paslaugos ir kainos – `clinic-price-list.json`. Pradiniame lape buvo 19 įkainotų eilučių ir atskira laboratorinių tyrimų pastaba. Dabartinis JSON atnaujintas pagal gydytojos pataisytą lapą: 11 paliktų ir 8 nebeatliekamos paslaugos; abi ranka pakeistos apžiūrų kainos vartotojo patvirtintos: po 70 Eur. Nuotrauka yra pirminis šaltinis; JSON įrašai išlaiko kainų intervalus, akušerijos ir ginekologijos skirstymą bei spiralės įvedimo kainos išimtį.

Tai projekto medžiaga, automatiškai į viešus puslapius neįtraukiama. Kainoraščio data ir galiojimo pradžia lape nenurodytos; gavimo data jų neatstoja. Prieš skelbiant kainas patikslinti jų aktualumą. Apžiūros kainos nevadinti konsultacijos kaina, nes lape tai skirtingos eilutės; skirtingų paslaugų nesujungti į numanomus vizito paketus. Telefonas šaltinyje užrašytas senu formatu; svetainėje išlieka dabartinis `+370 5 230 2235`.

2026-10-06 palyginimas su esamu svetainės turiniu išsaugotas `service-coverage-audit.json`: kiekvienai kainoraščio eilutei pateikta aprėptis, teksto įrodymas arba trūkumas ir siūloma vieta svetainėje. Tai turinio palyginimas, ne naujų viešų tekstų publikacija.

### Gydytojos pataisymai

Vadovautis `sources/paslaugu-kainorastis-patikslintas-2026-10-06.jpg`. Pradinis JSON ir pradinis auditas išsaugoti `sources/*-before-corrections-2026-10-06.json` tik istorijai. Laukas `availability: discontinued` reiškia, kad paslaugos nebesiūlomos; jų senos kainos saugomos tik `previous_price_eur`. 2026-10-06 vartotojas patvirtino abi kainas: ginekologinė apžiūra ir nėščiosios ginekologinė apžiūra kainuoja po 70 Eur. Neprilyginti išbrauktos atskiros vaisiaus širdies tonų paslaugos visai nėštumo priežiūrai: tonų klausymas jos sudėtyje liko neišbrauktas. Nėštumo nustatymas testu išbrauktas; kitų diagnostikos būdų prieinamumo iš šio išbraukimo nenustatome.
