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
        'label': 'Ginekologo konsultacija',
        'title': 'Ginekologo konsultacija Vilniuje | G. Karpenko klinika',
        'description': 'Privati gydytojos akušerės-ginekologės konsultacija Vilniuje: pokalbis, apžiūra ir individualus ištyrimas. G. Karpenko klinika, Gedvydžių g. 25.',
        'heading': 'Ginekologo konsultacija Vilniuje',
        'lead': 'Laikas Jūsų klausimams, atidi apžiūra ir individualus dėmesys moters sveikatai.',
        'content': '''
            <p>Privačioje klinikoje Jus priima gydytoja akušerė-ginekologė G. Karpenko. Per konsultaciją galite ramiai aptarti savo sveikatą, pasitikrinti ar pasikalbėti apie atsiradusius negalavimus. Privačia praktika gydytoja užsiima nuo 1997 metų, o pacientes priima Gedvydžių g. 25, Vilniuje.</p>
            <h2>Ką galima aptarti per konsultaciją?</h2>
            <p>Vizitas skirtas būtent Jūsų klausimams. Galite kreiptis dėl ginekologinių nusiskundimų, ankstesnių tyrimų rezultatų, profilaktinės apžiūros, kontracepcijos ar nėštumo priežiūros. Registruojantis verta trumpai pasakyti, dėl ko norėtumėte atvykti.</p>
            <p>Klinikoje atliekama ginekologinių ligų diagnostika ir gydymas, įskaitant virusinius, bakterinius bei grybelinius susirgimus. Konsultacijos ir apžiūros metu aptariama, koks ištyrimas reikalingas Jūsų situacijoje.</p>
            <h2>Pokalbis, apžiūra ir tolesni žingsniai</h2>
            <p>Pokalbio metu galite papasakoti apie savijautą, sveikatos istoriją ir tai, kas kelia nerimą. Gydytoja skiria laiko išklausyti bei atsakyti į klausimus. Apžiūros ir tyrimų poreikį gydytoja aptaria su Jumis, atsižvelgdama į sveikatos istoriją ir vizito priežastį.</p>
            <p>Jeigu reikalingas ultragarsinis tyrimas, daugiau apie jį rasite puslapyje <a href="/ginekologine-echoskopija-vilniuje/">ginekologinė echoskopija</a>. Jei norite pasitikrinti be konkretaus nusiskundimo, skaitykite apie <a href="/profilaktinis-ginekologinis-patikrinimas/">profilaktinę ginekologinę patikrą</a>.</p>
            <h2>Prieš atvykstant į kliniką</h2>
            <p>Galite užsirašyti norimus aptarti klausimus ir pasiruošti turimus ankstesnių tyrimų atsakymus bei informaciją apie vartojamus vaistus. Taip per pokalbį bus lengviau prisiminti Jums svarbias aplinkybes. Dėl pasiruošimo konkrečiai apžiūrai pasiteiraukite registruodamasi.</p>
            <h2>Konsultacijos kaina ir registracija</h2>
            <p>Dėl konsultacijos kainos, galimų papildomų tyrimų ir priėmimo laiko prašome skambinti <a href="tel:+37052302235">+370 5 230 2235</a>. Registruojantis galima patikslinti, kokios paslaugos planuojamos ir kiek jos kainuotų.</p>
        ''',
        'faq': [
            ('Kokia gydytoja mane priims?', 'Jus priims gydytoja akušerė-ginekologė G. Karpenko. Ji konsultuoja, atlieka apžiūras ir rūpinasi tolesne priežiūra, todėl sugrįžusi bendrausite su ta pačia gydytoja.'),
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
            <h2>Kas yra ginekologinė echoskopija?</h2>
            <p>Echoskopija, dar vadinama ultragarsiniu tyrimu, leidžia vaizdu įvertinti vidaus organus. Tyrimui naudojamos garso bangos, o ne rentgeno spinduliai. Ginekologijoje ultragarsas padeda gydytojai įvertinti mažojo dubens organus ir papildyti konsultacijos bei apžiūros informaciją.</p>
            <p>Tyrimo rezultatai vertinami kartu su Jūsų savijauta ir sveikatos istorija. Vien echoskopijos gali nepakakti visiems klausimams atsakyti – tolesnį ištyrimą gydytoja aptaria pagal individualią situaciją.</p>
            <h2>Kaip pasiruošti tyrimui?</h2>
            <p>Pasiruošimas priklauso nuo numatomo ultragarsinio tyrimo būdo. Todėl registruodamasi pasiteiraukite, kaip pasiruošti būtent Jūsų vizitui. Vienoda taisyklė dėl šlapimo pūslės pripildymo visiems echoskopiniams tyrimams netinka.</p>
            <p>Jeigu turite ankstesnių echoskopijų aprašus ar kitų tyrimų atsakymus, galite juos atsinešti. Taip pat verta užsirašyti klausimus, kuriuos norėtumėte aptarti. Apie nerimą ar diskomfortą pasakykite gydytojai – tyrimo eigą galima paaiškinti prieš jį pradedant.</p>
            <h2>Echoskopija ir konsultacija</h2>
            <p>Registruodamasi patikslinkite, ar norėtumėte <a href="/ginekologo-konsultacija-vilniuje/">ginekologo konsultacijos</a> su echoskopiniu tyrimu. Konkrečių tyrimų poreikis ir jų apimtis nustatomi individualiai, o informacija apie paslaugų kainą suteikiama telefonu.</p>
            <p>Jeigu ieškote informacijos apie nėštumo nustatymą ar vaisiaus stebėjimą, apsilankykite <a href="/nestumo-prieziura-vilniuje/">nėštumo priežiūros</a> puslapyje. Jame aptariamos nėščiosioms skirtos klinikos paslaugos.</p>
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
        'description': 'Nėštumo nustatymas ir nėščiųjų priežiūra Vilniuje. Gydytojos G. Karpenko konsultacijos, vaisiaus stebėjimas ir tyrimų aptarimas. Gedvydžių g. 25.',
        'heading': 'Nėštumo nustatymas ir priežiūra Vilniuje',
        'lead': 'Gydytojos akušerės-ginekologės dėmesys Jums ir besivystančiam nėštumui.',
        'content': '''
            <p>Nėštumo nustatymu ir nėščiųjų priežiūra klinikoje rūpinasi gydytoja G. Karpenko. Per tolesnius vizitus su ja galite aptarti savijautos pokyčius, tyrimų atsakymus ir naujai kilusius klausimus. Pacientės priimamos Vilniuje, Gedvydžių g. 25. Gydytoja privačia praktika užsiima nuo 1997 metų ir skiria laiko konsultacijai bei Jūsų klausimams.</p>
            <h2>Nėštumo nustatymas</h2>
            <p>Jeigu norite patvirtinti nėštumą ir aptarti tolesnę priežiūrą, registruodamasi nurodykite vizito priežastį. Klinikoje atliekamas ankstyvas nėštumo nustatymas, o reikalingas ištyrimas parenkamas pagal individualią situaciją.</p>
            <p>Pirmojo pokalbio metu naudinga aptarti turimus tyrimų rezultatus, ankstesnių nėštumų informaciją, vartojamus vaistus bei kitus sveikatos klausimus. Jei turite ankstesnių išrašų, galite juos atsinešti. Registruojantis pasiteiraukite, kokia informacija būtų naudinga Jūsų vizitui.</p>
            <h2>Nėščiųjų priežiūra ir vaisiaus stebėjimas</h2>
            <p>Klinikos paslaugos apima nėščiųjų priežiūrą, vaisiaus stebėjimą ir tyrimus nėštumo metu. Vizitai suteikia galimybę aptarti savijautą, tyrimų atsakymus bei tolesnius priežiūros žingsnius.</p>
            <p>Apsilankymų ir ištyrimo planas priklauso nuo nėštumo eigos bei sveikatos aplinkybių. Konkrečius tyrimus ir jų laiką aptarkite su gydytoja.</p>
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
            ('Ar galima kreiptis dėl nėštumo nustatymo?', 'Taip. Ankstyvas nėštumo nustatymas yra viena iš klinikos paslaugų. Dėl tinkamo vizito laiko ir pasiruošimo susisiekite telefonu.'),
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
            <p>Kontracepcijos būdai skiriasi naudojimu ir tinkamumu konkrečiam žmogui. Konsultacijos metu svarbu aptarti, ko tikitės iš pasirinkto metodo, kokias priemones jau naudojote ir kaip jautėtės jas vartodama. Draugei tinkantis pasirinkimas nebūtinai atitiks Jūsų poreikius.</p>
            <p>Pasaulio sveikatos organizacija nurodo, kad metodo pasirinkimas priklauso nuo asmens sveikatos, pageidavimų ir poreikių. Sveikatos priežiūros specialisto konsultacija padeda įvertinti tinkamas galimybes.</p>
            <h2>Hormoniniai ir nehormoniniai būdai</h2>
            <p>Klinikoje aptariami abu kontracepcijos tipai. Galite klausti apie naudojimo ypatumus, metodo tinkamumą ir tai, ką daryti, jei anksčiau pasirinkta priemonė Jums netiko. Sprendimas priimamas individualiai, įvertinus Jūsų sveikatos aplinkybes.</p>
            <p>Kontracepcijos pasirinkimas ir apsauga nuo lytiškai plintančių infekcijų nėra tas pats klausimas. Prezervatyvai gali padėti apsisaugoti ir nuo nėštumo, ir nuo šių infekcijų; kitų kontracepcijos metodų paskirtį bei ribas aptarkite per konsultaciją.</p>
            <h2>Kaip pasiruošti konsultacijai?</h2>
            <p>Pagalvokite, kokių priemonių esate bandžiusi, ar turėjote nepageidaujamų reakcijų ir kokie klausimai Jums svarbiausi. Turėkite informaciją apie vartojamus vaistus ir sveikatos istoriją. Jei domitės konkrečia priemone ar procedūra, jos prieinamumą pasitikrinkite registruodamasi.</p>
            <p>Jeigu norėtumėte kartu aptarti kitus moters sveikatos klausimus, registruokitės <a href="/ginekologo-konsultacija-vilniuje/">ginekologo konsultacijai</a>. Dėl reguliarios sveikatos priežiūros taip pat galite skaityti apie <a href="/profilaktinis-ginekologinis-patikrinimas/">profilaktinį patikrinimą</a>.</p>
            <h2>Konsultacija G. Karpenko klinikoje</h2>
            <p>Gydytoja priima Gedvydžių g. 25, Vilniuje. Registracijos telefonu <a href="tel:+37052302235">+370 5 230 2235</a> metu galėsite suderinti vizito laiką ir sužinoti konsultacijos kainą. Vaistų ar konkrečių priemonių paskyrimas sprendžiamas individualios konsultacijos metu.</p>
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
            <p>Profilaktinė patikra nėra vienodas tyrimų paketas visoms moterims. Jei registruodamasi norite konkretaus tyrimo, paminėkite jį ir pasiteiraukite apie prieinamumą, pasiruošimą bei kainą. <a href="/ginekologine-echoskopija-vilniuje/">Echoskopinis tyrimas</a> ir gimdos kaklelio patikra yra skirtingos ištyrimo dalys.</p>
            <h2>Gimdos kaklelio vėžio prevencija</h2>
            <p>Lietuvoje vykdoma gimdos kaklelio vėžio prevencinė programa. Valstybinė ligonių kasa skelbia, kam ji skirta, kokie tyrimai atliekami ir kokiu dažnumu. Ši informacija padeda suprasti programos sąlygas, tačiau individualius sveikatos klausimus verta aptarti su gydytoja.</p>
            <p>Dėl dalyvavimo valstybės finansuojamoje programoje kreipkitės į savo šeimos gydytoją. Dėl paslaugų apmokėjimo G. Karpenko privačioje klinikoje teiraukitės registruodamasi – informacija apie prevencinę programą savaime nereiškia, kad vizitas klinikoje bus kompensuojamas.</p>
            <h2>Ką atsinešti ir apie ką pagalvoti?</h2>
            <p>Jeigu turite ankstesnių patikrų ar tyrimų atsakymus, atsineškite juos į vizitą. Naudinga prisiminti, kada paskutinį kartą tikrinotės ir ar buvo rekomenduota papildoma kontrolė. Galite užsirašyti klausimus, kuriuos norėtumėte aptarti ramiai, neskubėdama.</p>
            <p>Jeigu atsirado naujų nusiskundimų, pasakykite apie juos registruodamasi. Tokiu atveju vizito tikslas gali būti ne vien profilaktika, bet ir <a href="/ginekologo-konsultacija-vilniuje/">ginekologinė konsultacija dėl konkretaus sveikatos sutrikimo</a>.</p>
            <h2>Registracija profilaktinei patikrai</h2>
            <p>Gydytoja G. Karpenko priima Gedvydžių g. 25, Vilniuje. Telefonu <a href="tel:+37052302235">+370 5 230 2235</a> galite suderinti vizito laiką ir pasiteirauti paslaugų kainų. Dėl tolesnių patikrų dažnumo pasitarkite individualios konsultacijos metu.</p>
        ''',
        'faq': [
            ('Ar galima pasitikrinti, kai niekuo nesiskundžiu?', 'Taip, profilaktinė patikra skirta ir tuomet, kai nėra konkretaus nusiskundimo. Kokie patikrinimai Jums reikalingi, aptariama su gydytoja.'),
            ('Ar echoskopija pakeičia gimdos kaklelio prevencinius tyrimus?', 'Ne. Tai skirtingi tyrimai, skirti skirtingiems klausimams įvertinti. Apie Jums reikalingą patikrą ir tyrimų pasirinkimą pasitarkite su gydytoja.'),
        ],
        'sources': [('Valstybinė ligonių kasa: gimdos kaklelio vėžio prevencija', 'https://ligoniukasa.lrv.lt/lt/veiklos-sritys/informacija-gyventojams/ligu-prevencijos-programos/gimdos-kaklelio-vezio-prevencija/')],
    },
]


def build():
    home = (ROOT / 'index.html').read_text()
    header = home[home.index('            <header'):home.index('            <main')]
    header = header.replace('href="./"', 'href="/"').replace('src="assets/', 'src="/assets/')
    header = re.sub(r'href="#(apie|paslaugos|registracija|kontaktai)"', r'href="/#\1"', header)
    contact = home[home.index('                <section class="contact"'):home.index('            </main>')]
    footer = home[home.index('            <footer>'):home.index('    </body>')]
    clinic = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', home, re.S)[1])
    clinic.pop('@context', None)
    analytics = re.search(r'            <script async src="https://www.googletagmanager.com/.*?</script>\s*<script>.*?</script>', home, re.S)[0]
    for page in PAGES:
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
        links = '\n'.join(
            f'<li><a href="/{p["slug"]}/"' + (' aria-current="page"' if p == page else '') + f'>{escape(p["label"])}</a></li>'
            for p in PAGES
        )
        faq = '\n'.join(f'<section class="question"><h3>{escape(q)}</h3><p>{escape(a)}</p></section>' for q, a in page['faq'])
        sources = ''
        if page['sources']:
            sources = '<section class="source-note"><h2>Papildoma informacija</h2><ul>' + ''.join(
                f'<li><a href="{escape(url)}">{escape(label)}</a></li>' for label, url in page['sources']
            ) + '</ul></section>'
        output = f'''<!DOCTYPE html>
<html lang="lt">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>{escape(page['title'])}</title>
        <meta name="description" content="{escape(page['description'], quote=True)}" />
        <link rel="canonical" href="{url}" />
        <meta property="og:type" content="website" />
        <meta property="og:locale" content="lt_LT" />
        <meta property="og:title" content="{escape(page['title'], quote=True)}" />
        <meta property="og:description" content="{escape(page['description'], quote=True)}" />
        <meta property="og:url" content="{url}" />
        <meta property="og:image" content="{BASE}/assets/klinika.jpg" />
        <link rel="icon" href="/assets/favicon.ico" />
        <link rel="stylesheet" href="/css/styles.css?v=services-2" />
        <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, indent=2)}</script>
{analytics}
    </head>
    <body>
        <a class="skip-link" href="#turinys">Pereiti prie turinio</a>
        <div class="site-sheet">
{header}            <main id="turinys">
                <nav class="breadcrumbs" aria-label="Puslapio vieta"><a href="/">Pradžia</a><span aria-hidden="true">»</span><span aria-current="page">{escape(page['label'])}</span></nav>
                <div class="service-page-layout">
                    <article class="service-content">
                        <header class="service-page-heading">
                            <p class="section-kicker">G. Karpenko klinika · Vilnius</p>
                            <h1>{escape(page['heading'])}</h1>
                            <p class="service-lead">{escape(page['lead'])}</p>
                        </header>
{page['content']}
                        <section class="service-faq" aria-labelledby="klausimai"><h2 id="klausimai">Dažniausi klausimai</h2>{faq}</section>
                        {sources}
                    </article>
                    <aside class="visit-sidebar service-page-sidebar" aria-label="Registracija ir paslaugos">
                        <section class="appointment" aria-labelledby="appointment-title">
                            <p class="section-kicker">Privati praktika nuo 1997 metų</p>
                            <h2 id="appointment-title">Registracija vizitui</h2>
                            <div class="ornament" aria-hidden="true">❧</div>
                            <p>Jus priima pati gydytoja<br>akušerė-ginekologė G. Karpenko.</p>
                            <a class="appointment-phone" href="tel:+37052302235">+370 5 230 2235</a>
                            <a class="button" href="tel:+37052302235">Skambinti į kliniką</a>
                            <p class="appointment-note">Gedvydžių g. 25, Vilnius<br>Vizito laikas derinamas telefonu.</p>
                            <p class="phone-note">Gydytoja registraciją derina pati. Konsultacijos metu jos dėmesys skirtas pacientei, todėl ne visada pavyksta atsiliepti telefonu. Jei neprisiskambinote, maloniai prašome paskambinti vėliau. Ačiū už supratingumą.</p>
                        </section>
                        <nav class="service-menu" aria-label="Klinikos paslaugos"><h2>Klinikos paslaugos</h2><ul>{links}</ul></nav>
                    </aside>
                </div>
{contact}            </main>
{footer}    </body>
</html>
'''
        dest = ROOT / page['slug'] / 'index.html'
        dest.parent.mkdir(exist_ok=True)
        dest.write_text(output)
        print(dest.relative_to(ROOT))


if __name__ == '__main__':
    build()
