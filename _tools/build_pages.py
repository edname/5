#!/usr/bin/env python3
"""Regenerate committed static service pages; GitHub Pages needs no build step."""
from pathlib import Path
from html import escape
import json
import re

ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://karpenko.lt'
PAGES = [
    {
        'slug': 'ginekologo-konsultacija-vilniuje',
        'label': 'Ginekologės konsultacija',
        'title': 'Ginekologės konsultacija Vilniuje | G. Karpenko klinika',
        'description': 'Privati ginekologė G. Karpenko Vilniuje: konsultacija, apžiūra ir individualaus ištyrimo aptarimas. Gedvydžių g. 25. Registracija telefonu +370 5 230 2235.',
        'heading': 'Ginekologės konsultacija Vilniuje',
        'lead': 'Laikas Jūsų klausimams, atidi apžiūra ir individualus dėmesys moters sveikatai.',
        'content': '''
            <p>Privačioje klinikoje Jus priima gydytoja akušerė-ginekologė G. Karpenko. Per konsultaciją galite ramiai aptarti savo sveikatą, pasitikrinti ar pasikalbėti apie atsiradusius negalavimus. Privačia praktika gydytoja užsiima nuo 1997 metų, o pacientes priima Gedvydžių g. 25, Vilniuje.</p>
            <h2>Ką galima aptarti per konsultaciją?</h2>
            <p>Vizitas skirtas būtent Jūsų klausimams. Galite kreiptis dėl ginekologinių nusiskundimų, ankstesnių tyrimų rezultatų, profilaktinės apžiūros, kontracepcijos ar nėštumo priežiūros. Registruojantis verta trumpai pasakyti, dėl ko norėtumėte atvykti.</p>
            <p>Taip pat galite kreiptis dėl sunkumų pastoti ir savijautos pokyčių artėjant menopauzei ar jai prasidėjus. Gydytoja aptars Jūsų situaciją ir galimą tolesnį ištyrimą.</p>
            <h2>Pokalbis, apžiūra ir tolesni žingsniai</h2>
            <p>Konsultacija prasideda nuo pokalbio apie savijautą ir sveikatos istoriją. Apžiūros bei tyrimų poreikis aptariamas su Jumis. Jei dėl apžiūros nerimaujate, galite paprašyti paaiškinti jos eigą ir užduoti rūpimus klausimus.</p>
            <p>Jeigu reikalingas ultragarsinis tyrimas, daugiau apie jį rasite puslapyje <a href="/ginekologine-echoskopija-vilniuje/">ginekologinė echoskopija</a>. Jei norite pasitikrinti be konkretaus nusiskundimo, skaitykite apie <a href="/profilaktinis-ginekologinis-patikrinimas/">profilaktinę ginekologinę patikrą</a>.</p>
            <h2>Prieš atvykstant į kliniką</h2>
            <p>Galite užsirašyti norimus aptarti klausimus ir pasiruošti turimus ankstesnių tyrimų atsakymus bei informaciją apie vartojamus vaistus. Taip per pokalbį bus lengviau prisiminti Jums svarbias aplinkybes. Dėl pasiruošimo konkrečiai apžiūrai pasiteiraukite registruodamasi.</p>
            <h2>Konsultacijos kaina ir registracija</h2>
            <p>Dėl konsultacijos kainos, galimų papildomų tyrimų ir priėmimo laiko prašome skambinti <a href="tel:+37052302235">+370 5 230 2235</a>. Registruojantis galima patikslinti, kokios paslaugos planuojamos ir kiek jos kainuotų.</p>
        ''',
        'faq': [
            ('Ar galima atvykti pirmajai ginekologo konsultacijai?', 'Taip, galite registruotis pirmajai konsultacijai. Pasakykite, kad tai pirmas Jūsų vizitas, ir išsakykite rūpimus klausimus ar nerimą.'),
            ('Ar kiekvienos konsultacijos metu atliekama echoskopija?', 'Klinikoje atliekami echoskopiniai tyrimai, tačiau konkretaus tyrimo poreikis aptariamas su gydytoja. Registruojantis pasiteiraukite ir dėl jo kainos.'),
        ],
        'sources': [],
    },
    {
        'slug': 'ginekologine-echoskopija-vilniuje',
        'label': 'Ginekologinė echoskopija',
        'title': 'Ginekologinė echoskopija Vilniuje | G. Karpenko',
        'description': 'Ginekologinė echoskopija G. Karpenko klinikoje Vilniuje. Informacija apie ultragarsinį tyrimą, pasiruošimą ir registraciją telefonu +370 5 230 2235.',
        'heading': 'Ginekologinė echoskopija Vilniuje',
        'lead': 'Ultragarsinis tyrimas ir jo rezultatų aptarimas su gydytoja akušere-ginekologe.',
        'content': '''
            <p>Echoskopinius tyrimus klinikoje atlieka gydytoja akušerė-ginekologė G. Karpenko. Tai ginekologinio ištyrimo dalis. Dėl ginekologinės echoskopijos Vilniuje galite registruotis telefonu, trumpai nurodydama, ar kreipiatės dėl konkretaus nusiskundimo, ar dėl ankstesnio tyrimo aptarimo.</p>
            <h2>Transabdominalinė ir transvaginalinė echoskopija</h2>
            <p>Klinikoje atliekama transabdominalinė echoskopija (per pilvo sieną) ir transvaginalinė echoskopija (makštiniu davikliu). Tyrimo būdą gydytoja parenka pagal vizito tikslą ir individualią situaciją, aptarusi jį su Jumis.</p>
            <p>Echoskopija, dar vadinama ultragarsiniu tyrimu, leidžia vaizdu įvertinti vidaus organus. Tyrimui naudojamos garso bangos, o ne rentgeno spinduliai. Ginekologijoje ultragarsas padeda įvertinti gimdą ir kiaušides.</p>
            <p>Tyrimo rezultatai vertinami kartu su Jūsų savijauta ir sveikatos istorija. Vien echoskopijos gali nepakakti visiems klausimams atsakyti – tolesnį ištyrimą gydytoja aptaria pagal individualią situaciją.</p>
            <h2>Kaip pasiruošti tyrimui?</h2>
            <p>Pasiruošimas priklauso nuo tyrimo būdo. Registruodamasi pasiteiraukite, ar reikės atvykti pilna šlapimo pūsle, ir laikykitės Jums pateiktų nurodymų.</p>
            <p>Jeigu turite ankstesnių echoskopijų aprašus ar kitų tyrimų atsakymus, galite juos atsinešti. Taip pat verta užsirašyti klausimus, kuriuos norėtumėte aptarti. Jei nerimaujate, paprašykite paaiškinti tyrimo eigą. Pajutusi diskomfortą, pasakykite gydytojai; galite paprašyti tyrimą sustabdyti.</p>
            <h2>Echoskopija ir konsultacija</h2>
            <p>Registruodamasi patikslinkite, ar norėtumėte <a href="/ginekologo-konsultacija-vilniuje/">ginekologo konsultacijos</a> su echoskopiniu tyrimu. Konkrečių tyrimų poreikis ir jų apimtis nustatomi individualiai, o informacija apie paslaugų kainą suteikiama telefonu.</p>
            <p>Jeigu ieškote informacijos apie nėščiųjų priežiūrą ar akušerinę echoskopiją, apsilankykite <a href="/nestumo-prieziura-vilniuje/">nėštumo priežiūros</a> puslapyje. Jame aptariamos nėščiosioms skirtos klinikos paslaugos.</p>
            <h2>Kur atliekamas tyrimas?</h2>
            <p>Klinika įsikūrusi Gedvydžių g. 25, Vilniuje. Vizito laiką, echoskopijos kainą ir pasiruošimą aptarkite telefonu <a href="tel:+37052302235">+370 5 230 2235</a>.</p>
        ''',
        'faq': [
            ('Ar echoskopija ir ultragarsinis tyrimas reiškia tą patį?', 'Taip, tai du to paties tyrimo metodo pavadinimai. Registruojantis galite vartoti bet kurį iš jų.'),
            ('Ar prieš tyrimą reikia gerti vandens?', 'Tai priklauso nuo tyrimo būdo. Registruodamasi pasiteiraukite, kaip pasiruošti būtent Jums numatytam tyrimui.'),
        ],
        'sources': [('NHS: apie ultragarsinį tyrimą ir pasiruošimą (anglų kalba)', 'https://www.nhs.uk/tests-and-treatments/ultrasound-scan/')],
    },
    {
        'slug': 'nestumo-prieziura-vilniuje',
        'label': 'Nėštumo priežiūra',
        'title': 'Nėštumo priežiūra Vilniuje | G. Karpenko klinika',
        'description': 'Nėščiųjų priežiūra Vilniuje: ginekologinė apžiūra, vaisiaus širdies tonų klausymas priežiūros metu ir transabdominalinė echoskopija. G. Karpenko klinika.',
        'heading': 'Nėščiųjų priežiūra Vilniuje',
        'lead': 'Gydytojos akušerės-ginekologės dėmesys Jums ir besivystančiam nėštumui.',
        'content': '''
            <p>Nėščiąsias klinikoje priima gydytoja akušerė-ginekologė G. Karpenko. Vizito metu galite aptarti savijautą, turimų tyrimų atsakymus ir tolesnę priežiūrą. Klinika įsikūrusi Gedvydžių g. 25, Vilniuje.</p>
            <h2>Nėščiosios apžiūra ir pirmasis vizitas</h2>
            <p>Klinikoje atliekama nėščiosios ginekologinė apžiūra. Registruodamasi nurodykite vizito priežastį ir, jei žinote, nėštumo savaitę. Gydytoja aptars Jūsų savijautą ir reikalingą priežiūrą.</p>
            <p>Pirmojo pokalbio metu naudinga aptarti turimus tyrimų rezultatus, ankstesnių nėštumų informaciją, vartojamus vaistus bei kitus sveikatos klausimus. Jei turite ankstesnių išrašų, galite juos atsinešti. Registruojantis pasiteiraukite, kokia informacija būtų naudinga Jūsų vizitui.</p>
            <h2>Nėščiųjų priežiūra ir vaisiaus stebėjimas</h2>
            <p>Nėščiosios priežiūros paslaugos apima matavimus ir vaisiaus širdies tonų klausymą, atsižvelgiant į nėštumo laiką ir vizito poreikį. Klinikoje taip pat atliekama transabdominalinė akušerinė echoskopija – ultragarsinis tyrimas per pilvo sieną. Konkretaus apsilankymo apimtį aptarkite su gydytoja.</p>
            <p>Apsilankymų ir tyrimų planas derinamas pagal nėštumo laiką, jo eigą ir Jūsų sveikatos aplinkybes.</p>
            <h2>Klausimai, kuriuos verta aptarti</h2>
            <ul>
                <li>Kokios priežiūros reikės artimiausiu nėštumo laikotarpiu?</li>
                <li>Kokius turimus tyrimų atsakymus atsinešti?</li>
                <li>Kada numatyti kitą apsilankymą ir kokių tyrimų gali reikėti?</li>
                <li>Kokia konsultacijos bei numatomų tyrimų kaina?</li>
            </ul>
            <p>Jeigu pirmiausia norite bendros <a href="/ginekologo-konsultacija-vilniuje/">akušerės-ginekologės konsultacijos</a>, tai galite pasakyti registruodamasi. Gydytoja skirs laiko Jums rūpimiems klausimams aptarti.</p>
            <h2>Registracija nėštumo priežiūrai</h2>
            <p>Dėl priėmimo laiko, priežiūros apimties ir kainų skambinkite <a href="tel:+37052302235">+370 5 230 2235</a>. Jei dalį tyrimų jau atlikote kitoje įstaigoje, paminėkite tai registruodamasi, kad būtų galima aptarti Jūsų vizito poreikį.</p>
        ''',
        'faq': [
            ('Kokios nėščiųjų priežiūros paslaugos teikiamos?', 'Klinikoje atliekama nėščiosios ginekologinė apžiūra, priežiūra su matavimais ir vaisiaus širdies tonų klausymu bei transabdominalinė echoskopija. Vizito apimtį ir laiką suderinkite registruodamasi.'),
            ('Ar nėštumo priežiūra apima visus tyrimus už vieną kainą?', 'Apie paslaugų apimtį ir konkrečių konsultacijų bei tyrimų kainas teiraukitės registruodamasi. Registruojantis patikslinkite, kas įskaičiuota į Jums reikalingos paslaugos kainą.'),
        ],
        'sources': [('NHS: apie nėštumo priežiūrą ir apsilankymus (anglų kalba)', 'https://www.nhs.uk/pregnancy/your-pregnancy-care/your-antenatal-care-and-appointments/')],
    },
    {
        'slug': 'kontracepcijos-parinkimas',
        'label': 'Kontracepcijos parinkimas',
        'title': 'Kontracepcijos parinkimas Vilniuje | G. Karpenko',
        'description': 'Individualus kontracepcijos parinkimas Vilniuje: hormoninių ir nehormoninių būdų aptarimas su gydytoja G. Karpenko. Registracija +370 5 230 2235.',
        'heading': 'Individualus kontracepcijos parinkimas',
        'lead': 'Konsultacija apie apsisaugojimo nuo nėštumo būdus, atsižvelgiant į Jūsų sveikatą ir poreikius.',
        'content': '''
            <p>Dėl hormoninės ir nehormoninės kontracepcijos privačioje klinikoje Vilniuje konsultuoja gydytoja G. Karpenko. Parenkant metodą atsižvelgiama į sveikatos istoriją, gyvenimo būdą ir individualią organizmo reakciją į kontraceptines priemones.</p>
            <h2>Pasirinkimas prasideda nuo pokalbio</h2>
            <p>Kontracepcijos būdai skiriasi naudojimu ir tinkamumu konkrečiam žmogui. Konsultacijos metu svarbu aptarti, ko tikitės iš pasirinkto metodo, kokias priemones jau naudojote ir kaip jautėtės jas vartodama.</p>
            <p>Per konsultaciją galima palyginti hormoninius ir nehormoninius būdus, aptarti jų naudojimą, galimą nepageidaujamą poveikį ir Jums svarbius pasirinkimo kriterijus.</p>
            <h2>Kontracepcinės spiralės įvedimas ir pašalinimas</h2>
            <p>Klinikoje atliekamas kontracepcinės spiralės įvedimas ir pašalinimas. Konsultacijos metu aptariama, ar šis kontracepcijos būdas Jums tinka. Registruodamasi pasakykite, kokios procedūros reikia, ir pasiteiraukite dėl pasiruošimo bei spiralės įsigijimo. Spiralės kaina į įvedimo paslaugos kainą neįskaičiuota.</p>
            <p>Spiralė neapsaugo nuo lytiškai plintančių infekcijų. Taisyklingai naudojami prezervatyvai padeda sumažinti jų perdavimo ir neplanuoto nėštumo riziką.</p>
            <h2>Kaip pasiruošti konsultacijai?</h2>
            <p>Pagalvokite, kokių priemonių esate bandžiusi, ar turėjote nepageidaujamų reakcijų ir kokie klausimai Jums svarbiausi. Turėkite informaciją apie vartojamus vaistus ir sveikatos istoriją. Jei domitės konkrečia priemone ar procedūra, jos prieinamumą pasitikrinkite registruodamasi.</p>
            <p>Jeigu norėtumėte kartu aptarti kitus moters sveikatos klausimus, registruokitės <a href="/ginekologo-konsultacija-vilniuje/">ginekologo konsultacijai</a>. Dėl reguliarios sveikatos priežiūros taip pat galite skaityti apie <a href="/profilaktinis-ginekologinis-patikrinimas/">profilaktinį patikrinimą</a>.</p>
            <h2>Konsultacija G. Karpenko klinikoje</h2>
            <p>Gydytoja priima Gedvydžių g. 25, Vilniuje. Registracijos telefonu <a href="tel:+37052302235">+370 5 230 2235</a> metu galėsite suderinti vizito laiką ir sužinoti konsultacijos kainą. Dėl vaistų ar konkrečių priemonių skyrimo sprendžiama per individualią konsultaciją.</p>
        ''',
        'faq': [
            ('Ar konsultuojate dėl nehormoninės kontracepcijos?', 'Taip. Klinikoje parenkami hormoniniai ir nehormoniniai kontracepcijos būdai, atsižvelgiant į individualią sveikatos istoriją bei poreikius.'),
            ('Ar galima aptarti anksčiau netikusią priemonę?', 'Taip, per konsultaciją papasakokite, kokią priemonę naudojote ir kokių klausimų ar nepageidaujamų reakcijų turėjote. Tai svarbi informacija individualiam pasirinkimui.'),
        ],
        'sources': [('Pasaulio sveikatos organizacija: kontracepcijos metodai (anglų kalba)', 'https://www.who.int/news-room/fact-sheets/detail/family-planning-contraception')],
    },
    {
        'slug': 'profilaktinis-ginekologinis-patikrinimas',
        'label': 'Profilaktinė patikra',
        'title': 'Profilaktinė ginekologinė patikra Vilniuje | G. Karpenko',
        'description': 'Profilaktinis ginekologinis patikrinimas Vilniuje: individuali konsultacija, apžiūra ir prevencijos klausimai G. Karpenko klinikoje, Gedvydžių g. 25.',
        'heading': 'Profilaktinis ginekologinis patikrinimas',
        'lead': 'Laikas pasirūpinti savo sveikata ir aptarti profilaktiką su gydytoja.',
        'content': '''
            <p>Profilaktinius ginekologinius patikrinimus privačioje klinikoje Vilniuje atlieka gydytoja G. Karpenko. Tai galimybė aptarti sveikatą ir prevenciją, net jei šiuo metu neturite konkretaus nusiskundimo. Vizito apimtis derinama individualiai.</p>
            <h2>Ką galima aptarti profilaktinio vizito metu?</h2>
            <p>Per konsultaciją galite užduoti klausimus apie ankstesnių patikrų rezultatus, tolesnį stebėjimą, krūties ir gimdos kaklelio vėžio prevenciją. Gydytoja įvertina Jūsų sveikatos istoriją ir aptaria, kokia apžiūra ar tyrimai reikalingi.</p>
            <p>Patikros apimtis priklauso nuo Jūsų amžiaus, sveikatos istorijos ir ankstesnių tyrimų rezultatų. Jei registruodamasi norite konkretaus tyrimo, paminėkite jį ir pasiteiraukite apie prieinamumą, pasiruošimą bei kainą. <a href="/ginekologine-echoskopija-vilniuje/">Echoskopinis tyrimas</a> ir gimdos kaklelio patikra yra skirtingos ištyrimo dalys.</p>
            <h2>Gimdos kaklelio vėžio prevencija</h2>
            <p>Gimdos kaklelio vėžio prevencinėje programoje, priklausomai nuo amžiaus ir tyrimų rezultatų, atliekamas citologinis arba aukštos rizikos žmogaus papilomos viruso (ŽPV) tyrimas. Kam skirta programa ir kaip dažnai tikrintis, skelbia Valstybinė ligonių kasa.</p>
            <p>Dėl dalyvavimo valstybės finansuojamoje programoje kreipkitės į savo šeimos gydytoją. G. Karpenko klinikoje teikiamų tyrimų prieinamumą, kainą ir apmokėjimo sąlygas pasitikslinti kviečiame registruojantis.</p>
            <h2>Ką atsinešti ir apie ką pagalvoti?</h2>
            <p>Jeigu turite ankstesnių patikrų ar tyrimų atsakymus, atsineškite juos į vizitą. Naudinga prisiminti, kada paskutinį kartą tikrinotės ir ar buvo rekomenduota papildoma kontrolė. Galite užsirašyti klausimus, kuriuos norėtumėte aptarti ramiai, neskubėdama.</p>
            <p>Jeigu atsirado naujų nusiskundimų, pasakykite apie juos registruodamasi. Tokiu atveju vizito tikslas gali būti ne vien profilaktika, bet ir <a href="/ginekologo-konsultacija-vilniuje/">ginekologinė konsultacija dėl konkretaus sveikatos sutrikimo</a>.</p>
            <h2>Registracija profilaktinei patikrai</h2>
            <p>Gydytoja G. Karpenko priima Gedvydžių g. 25, Vilniuje. Telefonu <a href="tel:+37052302235">+370 5 230 2235</a> galite suderinti vizito laiką ir pasiteirauti paslaugų kainų. Dėl tolesnių patikrų dažnumo pasitarkite individualios konsultacijos metu.</p>
        ''',
        'faq': [
            ('Ar galima pasitikrinti, kai niekuo nesiskundžiu?', 'Taip, profilaktiškai galima kreiptis ir neturint nusiskundimų. Kokios apžiūros ar tyrimų reikės, aptarsite su gydytoja.'),
            ('Ar echoskopija pakeičia gimdos kaklelio prevencinius tyrimus?', 'Ne. Tai skirtingi tyrimai, skirti skirtingiems klausimams įvertinti. Apie Jums reikalingą patikrą ir tyrimų pasirinkimą pasitarkite su gydytoja.'),
        ],
        'sources': [('Valstybinė ligonių kasa: gimdos kaklelio vėžio prevencija', 'https://ligoniukasa.lrv.lt/lt/veiklos-sritys/informacija-gyventojams/ligu-prevencijos-programos/gimdos-kaklelio-vezio-prevencija/')],
    },
]



def sections(content):
    """Keep the reviewed copy, giving its existing headings semantic sections."""
    parts = re.split(r'(?=<h2>)', content.strip())
    return parts[0], [f'<section class="text-section">{part}</section>' for part in parts[1:]]


def page_body(page, faq, sources, links):
    slug = page['slug']
    intro, parts = sections(page['content'])
    title_html = f'<h1>{escape(page["heading"])}</h1>'
    if slug != 'apie-klinika':
        motif = 'tree' if slug in ('nestumo-prieziura-vilniuje', 'profilaktinis-ginekologinis-patikrinimas') else 'sun'
        title_html = f'<div class="page-title-heading">{title_html}<img class="page-ornament" src="/assets/baltic-{motif}.svg" width="40" height="50" alt="" aria-hidden="true" /></div>'
    heading = f'<header class="page-title">{title_html}<p class="service-lead">{escape(page["lead"])}</p></header>'
    if slug == 'apie-klinika':
        rows = []
        for part in parts:
            match = re.fullmatch(r'<section class="text-section"><h2>(.*?)</h2>(.*?)</section>', part.strip(), re.S)
            title, body = match.groups()
            rows.append(f'<section class="clinic-chapter"><h2>{title}</h2><div class="chapter-copy">{body}</div></section>')
        content = f'<div class="clinic-introduction"><span class="clinic-intro-ornament" aria-hidden="true"><img src="/assets/baltic-tree.svg" width="48" height="60" alt="" /></span><div>{intro}</div></div><div class="clinic-chapters">{"".join(rows)}</div>'
    elif slug == 'paslaugos':
        content = '<div class="service-catalog">' + page['content'] + '</div><p class="catalog-note">Dėl paslaugų kainų ir vizito laiko kviečiame <a href="/kontaktai/">susisiekti telefonu »</a></p>'
    elif slug == 'kontaktai':
        content = page['content']
    elif slug == 'ginekologo-konsultacija-vilniuje':
        content = f'<div class="article-intro">{intro}</div><div class="consultation-layout"><div class="consultation-flow">{"".join(parts[:2])}</div><div class="visit-memo">{"".join(parts[2:])}</div></div>'
    elif slug == 'ginekologine-echoskopija-vilniuje':
        content = f'<div class="article-intro">{intro}</div><div class="examination-layout"><div>{parts[0]}{parts[2]}</div><div class="preparation-note">{parts[1]}</div></div><div class="address-strip">{parts[3]}</div>'
    elif slug == 'nestumo-prieziura-vilniuje':
        content = f'<div class="article-intro">{intro}</div><div class="pregnancy-layout"><div class="care-sequence">{parts[0]}{parts[1]}</div><div class="questions-note">{parts[2]}</div></div><div class="address-strip">{parts[3]}</div>'
    elif slug == 'kontracepcijos-parinkimas':
        content = f'<div class="article-intro">{intro}</div><div class="discussion-columns">{parts[0]}{parts[1]}</div><div class="preparation-band">{parts[2]}</div><div class="address-strip">{parts[3]}</div>'
    else:
        content = f'<div class="article-intro">{intro}</div><div class="prevention-layout"><div>{parts[0]}{parts[2]}</div><div class="prevention-note">{parts[1]}</div></div><div class="address-strip">{parts[3]}</div>'
    related = f'<nav class="related-services" aria-label="Kitos klinikos paslaugos"><h2>Kitos paslaugos</h2><ul>{links}</ul></nav>' if page in PAGES else ''
    return f'<article class="tailored-page page-{slug}">{heading}{content}{faq}{sources}</article>{related}'


def build():
    home = (ROOT / 'index.html').read_text()
    header = home[home.index('            <header'):home.index('            <main')]
    header = header.replace('href="./"', 'href="/"').replace('src="assets/', 'src="/assets/')
    header = header.replace(' aria-current="page"', '')
    footer = home[home.index('            <footer>'):home.index('        <script>', home.index('            <footer>'))]
    clinic = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', home, re.S)[1])
    clinic.pop('@context', None)
    analytics = re.search(r'            <script async src="https://www.googletagmanager.com/.*?</script>\s*<script>.*?</script>', home, re.S)[0]
    info_pages = json.loads((ROOT / '_tools/info-pages.json').read_text())
    for page in PAGES + info_pages:
        url = f'{BASE}/{page["slug"]}/'
        breadcrumbs = {
            '@type': 'BreadcrumbList',
            'itemListElement': [
                {'@type': 'ListItem', 'position': 1, 'name': 'Pradžia', 'item': BASE + '/'},
                {'@type': 'ListItem', 'position': 2, 'name': page['label'], 'item': url},
            ],
        }
        schema = {'@context': 'https://schema.org', '@graph': [clinic, breadcrumbs, {
            '@type': 'WebPage', '@id': url + '#webpage', 'url': url,
            'name': page['title'], 'description': page['description'], 'inLanguage': 'lt',
            'mainEntity': {'@id': url + '#service'},
        }, {
            '@type': 'Service', '@id': url + '#service', 'name': page['heading'],
            'url': url, 'provider': {'@id': BASE + '/#klinika'},
            'areaServed': {'@type': 'City', 'name': 'Vilnius'},
        }]}
        is_service = page in PAGES
        active_path = '/paslaugos/' if is_service else f'/{page["slug"]}/'
        page_header = header.replace(f'href="{active_path}"', f'href="{active_path}" aria-current="page"')
        if is_service:
            breadcrumbs['itemListElement'].insert(1, {'@type': 'ListItem', 'position': 2, 'name': 'Paslaugos', 'item': BASE + '/paslaugos/'})
            breadcrumbs['itemListElement'][-1]['position'] = 3
        else:
            schema['@graph'].pop()
            schema['@graph'][-1].pop('mainEntity')
        breadcrumb_parent = '<a href="/paslaugos/">Paslaugos</a><span aria-hidden="true">»</span>' if is_service else ''
        links = '\n'.join(
            f'<li><a href="/{p["slug"]}/"' + (' aria-current="page"' if p == page else '') + f'>{escape(p["label"])}</a></li>'
            for p in PAGES if p != page
        )
        faq = '\n'.join(f'<details class="question"><summary>{escape(q)}</summary><p>{escape(a)}</p></details>' for q, a in page.get('faq', []))
        sources = ''
        if page.get('sources'):
            sources = '<section class="source-note"><h2>Papildoma informacija</h2><ul>' + ''.join(
                f'<li><a href="{escape(url)}">{escape(label)}</a></li>' for label, url in page['sources']
            ) + '</ul></section>'
        faq_section = f'<section class="service-faq" aria-labelledby="klausimai"><h2 id="klausimai">Dažniausi klausimai</h2>{faq}</section>' if faq else ''
        output = f'''<!DOCTYPE html>
<html lang="lt" prefix="og: https://ogp.me/ns#">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>{escape(page['title'])}</title>
        <meta name="description" content="{escape(page['description'], quote=True)}" />
        <link rel="canonical" href="{url}" />
        <meta property="og:type" content="website" />
        <meta property="og:locale" content="lt_LT" />
        <meta property="og:site_name" content="G. Karpenko privati ginekologijos klinika" />
        <meta property="og:title" content="{escape(page['title'], quote=True)}" />
        <meta property="og:description" content="{escape(page['description'], quote=True)}" />
        <meta property="og:url" content="{url}" />
        <meta property="og:image" content="{BASE}/assets/klinika.jpg" />
        <meta property="og:image:type" content="image/jpeg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="584" />
        <meta property="og:image:alt" content="Įėjimas į G. Karpenko kliniką Gedvydžių g. 25, Vilniuje" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="{escape(page['title'], quote=True)}" />
        <meta name="twitter:description" content="{escape(page['description'], quote=True)}" />
        <meta name="twitter:image" content="{BASE}/assets/klinika.jpg" />
        <meta name="twitter:image:alt" content="Įėjimas į G. Karpenko kliniką Gedvydžių g. 25, Vilniuje" />
        <link rel="icon" type="image/png" sizes="120x120" href="/assets/favicon.png" />
        <link rel="stylesheet" href="/css/styles.css?v=services-25" />
        <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, indent=2)}</script>
{analytics}
    </head>
    <body id="pradzia">
        <a class="skip-link" href="#turinys">Pereiti prie turinio</a>
        <div class="site-sheet">
{page_header}            <main id="turinys">
                <nav class="breadcrumbs" aria-label="Puslapio vieta"><a href="/">Pradžia</a><span aria-hidden="true">»</span>{breadcrumb_parent}<span aria-current="page">{escape(page['label'])}</span></nav>
                {page_body(page, faq_section, sources, links)}
            </main>
{footer}    </body>
</html>
'''
        dest = ROOT / page['slug'] / 'index.html'
        dest.parent.mkdir(exist_ok=True)
        dest.write_text(output)
        print(dest.relative_to(ROOT))


if __name__ == '__main__':
    build()
