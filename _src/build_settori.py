# -*- coding: utf-8 -*-
"""Genera le pagine settore di FlussAI: <slug>/index.html.

Uso:  cd LANDINGPAGE_ITA && python _src/build_settori.py
Grafica, header e footer sono gli stessi della homepage (style.css, main.js, cookie-consent.js).
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://flussai.officinaquantica.it"

ICONS = """  <svg width="0" height="0" style="position:absolute" aria-hidden="true">
    <defs>
      <symbol id="i-arrow" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
      <symbol id="i-check" viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></symbol>
      <symbol id="i-x" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6 6 18"/></symbol>
      <symbol id="i-plus" viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></symbol>
      <symbol id="i-user" viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></symbol>
      <symbol id="i-db" viewBox="0 0 24 24"><ellipse cx="12" cy="5.5" rx="7.5" ry="2.8"/><path d="M4.5 5.5v13c0 1.5 3.4 2.8 7.5 2.8s7.5-1.3 7.5-2.8v-13M4.5 12c0 1.5 3.4 2.8 7.5 2.8s7.5-1.3 7.5-2.8"/></symbol>
      <symbol id="i-mail" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></symbol>
      <symbol id="i-sheet" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 10h18M3 15h18M9 4v16"/></symbol>
      <symbol id="i-users" viewBox="0 0 24 24"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6.5 6.5 0 0 1 3.5 6"/></symbol>
      <symbol id="i-file" viewBox="0 0 24 24"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h4"/></symbol>
      <symbol id="i-chat" viewBox="0 0 24 24"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></symbol>
      <symbol id="i-cart" viewBox="0 0 24 24"><circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.5 12h11.5l2-8H6.2"/></symbol>
      <symbol id="i-cal" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></symbol>
      <symbol id="i-star" viewBox="0 0 24 24"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/></symbol>
    </defs>
  </svg>"""

# ---------------------------------------------------------------- contenuti

PAGES = [
    {
        "slug": "automazione-studi-commercialisti",
        "menu": "Studi commercialisti",
        "title": "Automazione per studi commercialisti con l'AI | FlussAI",
        "description": "Documenti dei clienti riconosciuti e archiviati, fatture ed estratti conto pre-registrati, solleciti automatici. Automazioni AI su misura per studi commercialisti in tutta Italia.",
        "service": "Automazione dei processi per studi commercialisti",
        "audience": "Studi commercialisti e centri elaborazione dati",
        "kicker": "Automazione AI per studi commercialisti",
        "h1": "Lo studio che rincorre<br><em>meno</em> documenti.",
        "lead": "Raccolta documenti, pre-registrazioni, solleciti ai clienti: costruiamo automazioni AI che fanno lo smistamento al posto vostro, così il tempo dello studio torna alla consulenza.",
        "flow": [("Arriva", "Email del cliente con 14 allegati"), ("FlussAI", "Riconosce, rinomina e archivia ogni documento"), ("Pronto", "Pratica completa, mancano solo 2 ricevute")],
        "problems": ["Documenti che arrivano da email, PEC, WhatsApp e chiavette", "Fatture ed estratti conto ricopiati a mano", "Clienti da sollecitare uno per uno", "Le stesse domande sulle scadenze, ogni mese"],
        "solution": ["Un sistema AI che legge quello che arriva allo studio, capisce di che documento si tratta, lo mette al suo posto e prepara il lavoro per il collaboratore.",
                     "Il controllo resta vostro: il sistema propone, una persona dello studio verifica e conferma."],
        "tools": [("i-db", "Software contabile"), ("i-file", "Fatture elettroniche XML"), ("i-mail", "Email e PEC"), ("i-sheet", "Excel e fogli condivisi"), ("i-file", "PDF e scansioni"), ("i-chat", "WhatsApp"), ("i-cal", "Scadenzari"), ("i-users", "Anagrafica clienti")],
        "cases_title": "Cosa automatizziamo <em>nello studio</em>",
        "cases": [
            ("inv", ["PDF", "XML", "JPG"], "Archivio", "Documenti dei clienti in ordine", "L'AI riconosce fatture, F24, contratti ed estratti conto, li rinomina con una regola fissa e li salva nella cartella giusta del cliente."),
            ("mail", ["Fatture", "Estratti conto", "F24", "Pubblicità"], "Contabilità", "Pre-registrazioni pronte da controllare", "Da fatture ed estratti conto vengono estratti importi, date e controparti: il collaboratore trova la registrazione proposta e la conferma."),
            ("chat", ["Buongiorno, per la dichiarazione ci mancano le spese mediche 2025.", "Grazie, le mando stasera 👍"], "Clienti", "Solleciti che partono da soli", "Per ogni cliente il sistema sa cosa manca e manda promemoria gentili via email o WhatsApp, con i tempi che decidete voi."),
            ("rep", None, "Studio", "Il punto della settimana", "Ogni lunedì una mail con scadenze vicine, pratiche ferme e documenti ancora mancanti, cliente per cliente."),
        ],
        "keep": [("La verifica contabile e fiscale", "Ogni registrazione proposta dall'AI viene controllata e confermata da una persona dello studio."),
                 ("Firme e invii telematici", "Dichiarazioni, F24 e comunicazioni le inviate voi, come oggi. Il sistema prepara, non trasmette."),
                 ("Il rapporto con il cliente", "Consulenza, telefonate e decisioni restano allo studio. L'automazione toglie solo il lavoro di smistamento."),
                 ("I casi dubbi", "Quando un documento non è chiaro il sistema lo segnala e lo mette da parte, non tira a indovinare.")],
        "faq": [
            ("Funziona con il software contabile che usiamo?", "Dipende dal programma: molti accettano importazioni di file o collegamenti diretti, altrimenti prepariamo file pronti da importare. Lo verifichiamo nell'analisi gratuita, prima di proporvi qualsiasi cosa."),
            ("L'AI registra da sola in contabilità?", "No. Prepara la registrazione con tutti i dati estratti dal documento, ma è un collaboratore dello studio a controllarla e confermarla. Le operazioni con effetti fiscali restano sempre a una persona."),
            ("I clienti devono cambiare il modo in cui ci mandano i documenti?", "No. Possono continuare a usare email, PEC o WhatsApp. Se volete, aggiungiamo un link di caricamento semplice, ma non è obbligatorio."),
            ("I dati dei clienti dello studio sono al sicuro?", "Lavoriamo nel rispetto del GDPR: il sistema accede solo alle cartelle e alle caselle necessarie, l'intelligenza artificiale è usata tramite servizi professionali che non addestrano i modelli sui vostri dati, ogni operazione resta registrata e firmiamo con voi un accordo sul trattamento dei dati."),
            ("Quanto tempo fa risparmiare?", "Dipende dai volumi dello studio. Nell'analisi misuriamo quanto tempo vi prendono oggi le attività da automatizzare e vi diamo una stima prima di partire: niente numeri promessi a scatola chiusa."),
            ("In quanto tempo è pronta la prima automazione?", "Per un singolo processo, come l'archiviazione dei documenti o i solleciti, di solito servono dalle 2 alle 4 settimane, test compresi. Conviene partire lontano dai picchi di scadenze."),
            ("Va bene anche per uno studio piccolo?", "Sì. Si parte da un solo processo, quello che vi fa perdere più ore, con un costo proporzionato. Se funziona, si aggiunge il resto."),
            ("Lavorate in tutta Italia?", "Sì, lavoriamo da remoto con studi di tutta Italia e, quando serve, veniamo in sede per l'analisi iniziale."),
        ],
        "cta": "Quanti documenti smista<br>il tuo studio? <em>Lasciali all'AI.</em>",
        "placeholder": "Quale attività dello studio vi fa perdere più tempo?",
    },
    {
        "slug": "automazione-aziende-manifatturiere",
        "menu": "Aziende manifatturiere",
        "title": "Automazione ordini e preventivi per aziende manifatturiere | FlussAI",
        "description": "Ordini dei clienti letti e inseriti nel gestionale, preventivi in bozza in pochi minuti, stato ordine senza telefonate. Automazioni AI su misura per aziende di produzione e terzisti.",
        "service": "Automazione di ordini, preventivi e report per aziende manifatturiere",
        "audience": "Aziende manifatturiere, officine meccaniche e terzisti",
        "kicker": "Automazione AI per aziende di produzione",
        "h1": "Ordini e preventivi che<br><em>non</em> si fermano in ufficio.",
        "lead": "Per aziende di produzione, officine meccaniche e terzisti: l'AI legge ordini e richieste di offerta, li prepara nel gestionale e tiene informato il cliente. La produzione riceve dati puliti, l'ufficio smette di ricopiare.",
        "flow": [("Arriva", "Ordine in PDF con 23 righe articolo"), ("FlussAI", "Legge codici, quantità e date di consegna"), ("Pronto", "Ordine nel gestionale, 1 prezzo da verificare")],
        "problems": ["Ordini in PDF ricopiati riga per riga", "Preventivi che restano fermi per giorni", "Clienti che chiamano per sapere a che punto è l'ordine", "Excel e gestionale che non coincidono mai"],
        "solution": ["Un sistema AI collegato al vostro gestionale: legge ordini e richieste da qualsiasi cliente, riconosce gli articoli, controlla prezzi e quantità e prepara il lavoro per l'ufficio.",
                     "Quando qualcosa non torna, lo segnala a una persona invece di andare avanti da solo."],
        "tools": [("i-db", "ERP e gestionali"), ("i-mail", "Email"), ("i-file", "Ordini, DDT e PDF"), ("i-sheet", "Excel e listini"), ("i-users", "CRM"), ("i-cal", "Pianificazione"), ("i-cart", "Portali e B2B"), ("i-chat", "WhatsApp")],
        "cases_title": "Cosa automatizziamo <em>in azienda</em>",
        "cases": [
            ("inv", ["ORD", "ORD", "DDT"], "Vendite", "Ordini cliente nel gestionale", "L'AI legge ordini in PDF, Excel o nel corpo della mail, riconosce codici articolo, quantità e date e prepara l'ordine. Le differenze di prezzo vengono segnalate."),
            ("mail", ["Richieste offerta", "Ordini", "Reclami", "Fornitori"], "Ufficio commerciale", "Preventivi in bozza in pochi minuti", "Dalla richiesta del cliente il sistema raccoglie i dati, applica listini e regole e prepara una bozza che il commerciale rivede e invia."),
            ("chat", ["Il nostro ordine 4512 è già partito?", "Sì, spedito ieri con DDT 881. Consegna prevista giovedì ✓"], "Clienti", "Stato ordine senza telefonate", "Un assistente legge lo stato dal gestionale e risponde ai clienti via email o WhatsApp. Le richieste particolari passano a voi."),
            ("rep", None, "Direzione", "Report di produzione e scorte", "Articoli sotto scorta, ordini in ritardo, fatturato della settimana: un riepilogo chiaro ogni lunedì, senza aprire cinque file."),
        ],
        "keep": [("Prezzi, sconti e conferme d'ordine", "Il sistema prepara ordini e preventivi, ma l'ultima parola sui prezzi e sull'invio al cliente è vostra."),
                 ("Le date di consegna", "Il sistema propone una data in base ai dati del gestionale. Quella che promettete al cliente la decidete voi."),
                 ("Qualità e produzione", "Controlli, collaudi e scelte tecniche restano a chi conosce i pezzi e le macchine."),
                 ("Il rapporto con clienti e fornitori", "Trattative, reclami e casi delicati vengono sempre passati a una persona.")],
        "faq": [
            ("Funziona con il nostro gestionale o ERP?", "Nella maggior parte dei casi sì: ci colleghiamo tramite le funzioni di importazione o le API del gestionale, oppure tramite file condivisi. Lo verifichiamo nell'analisi gratuita prima di proporvi qualsiasi cosa."),
            ("Gli ordini arrivano in formati diversi da ogni cliente: è un problema?", "No, è proprio il caso in cui l'AI aiuta di più: legge PDF, Excel e testo delle email anche se ogni cliente usa un modello diverso. I documenti incerti finiscono in una lista da verificare."),
            ("E se l'AI legge male un codice articolo?", "Può capitare, per questo il sistema controlla che il codice esista, che prezzo e quantità siano coerenti e segnala le differenze. Ogni passaggio resta registrato e le conferme d'ordine passano da una persona."),
            ("Serve un reparto informatico interno?", "No. Ci occupiamo noi di collegamenti, test e manutenzione. A voi chiediamo solo il tempo per spiegarci come lavorate e per provare il sistema."),
            ("I nostri dati e i disegni dei clienti sono al sicuro?", "Il sistema accede solo ai dati che servono per il processo da automatizzare. L'intelligenza artificiale è usata tramite servizi professionali che non addestrano i modelli sui vostri dati e firmiamo con voi un accordo sul trattamento dei dati."),
            ("In quanto tempo è pronta la prima automazione?", "Per un singolo processo, come l'inserimento ordini o i preventivi, di solito servono dalle 2 alle 4 settimane, test su ordini reali compresi."),
            ("Quanto costa?", "Dipende dal processo e dai collegamenti necessari. Dopo l'analisi ricevete una proposta con costi e tempi chiari; si parte da un solo processo, quello che rende di più."),
            ("Lavorate in tutta Italia?", "Sì, lavoriamo da remoto con aziende di tutta Italia e, quando serve, veniamo in sede per vedere come si muovono ordini e documenti."),
        ],
        "cta": "Quante righe d'ordine<br>ricopiate a mano? <em>Smettiamola.</em>",
        "placeholder": "Quale attività dell'ufficio vi fa perdere più tempo?",
    },
    {
        "slug": "automazione-hotel",
        "menu": "Hotel e strutture ricettive",
        "title": "Automazione per hotel e strutture ricettive con l'AI | FlussAI",
        "description": "Risposte alle richieste di disponibilità, assistente per gli ospiti in più lingue, dati del check-in senza ricopiarli, report settimanali. Automazioni AI su misura per hotel, B&B e residence.",
        "service": "Automazione dei processi per hotel e strutture ricettive",
        "audience": "Hotel, B&B, residence e strutture ricettive",
        "kicker": "Automazione AI per hotel e strutture ricettive",
        "h1": "Più tempo per gli ospiti,<br><em>meno</em> per le email.",
        "lead": "Richieste di disponibilità, domande degli ospiti, dati del check-in, recensioni: automazioni AI su misura per hotel, B&B e residence, collegate al gestionale e ai canali che usate già.",
        "flow": [("Arriva", "Richiesta: 2 adulti e 1 bambino, 12-15 agosto"), ("FlussAI", "Controlla disponibilità e tariffe nel gestionale"), ("Pronto", "Preventivo in bozza, da inviare con un clic")],
        "problems": ["Le stesse domande ogni giorno: parcheggio, animali, orari", "Preventivi scritti a mano per ogni richiesta", "Dati degli ospiti ricopiati tra un programma e l'altro", "Recensioni che restano senza risposta"],
        "solution": ["Un sistema AI che risponde alle domande di routine, prepara i preventivi leggendo disponibilità e tariffe e sposta i dati degli ospiti dove servono.",
                     "La reception riceve solo le richieste che hanno davvero bisogno di una persona."],
        "tools": [("i-db", "Gestionale (PMS)"), ("i-cal", "Channel manager"), ("i-cart", "Booking engine"), ("i-mail", "Email"), ("i-chat", "WhatsApp"), ("i-sheet", "Excel"), ("i-star", "Recensioni online"), ("i-file", "Moduli e documenti")],
        "cases_title": "Cosa automatizziamo <em>in struttura</em>",
        "cases": [
            ("mail", ["Disponibilità", "Gruppi", "Modifiche", "Spam"], "Prenotazioni", "Risposte alle richieste di disponibilità", "L'AI legge la richiesta, controlla disponibilità e tariffe e prepara la risposta con il preventivo. La inviate voi, oppure parte da sola per i casi standard che scegliete."),
            ("chat", ["Is there parking at the hotel?", "Yes! Free private parking, no booking needed 🚗"], "Ospiti", "Un assistente in più lingue", "Su WhatsApp o sul sito risponde giorno e notte alle domande frequenti, in italiano, inglese, tedesco e altre lingue. Le richieste particolari passano alla reception."),
            ("inv", ["DOC", "DOC", "DOC"], "Check-in", "Dati degli ospiti senza ricopiarli", "Un modulo pre-arrivo raccoglie i dati e li porta nel gestionale. Comunicazioni alle autorità e imposta di soggiorno restano a voi, con i dati già pronti da controllare."),
            ("rep", None, "Direzione", "Report e recensioni", "Ogni settimana occupazione, provenienza degli ospiti e recensioni nuove, con una bozza di risposta per ciascuna da approvare."),
        ],
        "keep": [("L'accoglienza", "Il contatto con l'ospite in struttura, i consigli e le attenzioni restano alle persone."),
                 ("Tariffe e politiche", "Prezzi, offerte e condizioni di cancellazione li decidete voi: il sistema li applica, non li cambia."),
                 ("Allergie ed esigenze particolari", "Richieste su allergie, salute o accessibilità vengono sempre passate a una persona dello staff."),
                 ("Invii obbligatori e recensioni", "Le comunicazioni alle autorità le inviate voi; le risposte alle recensioni sono bozze che approvate prima della pubblicazione.")],
        "faq": [
            ("Funziona con il nostro gestionale e il channel manager?", "Molti gestionali alberghieri e channel manager permettono collegamenti o esportazioni di dati. Verifichiamo il vostro nell'analisi gratuita e vi diciamo con onestà cosa si può collegare."),
            ("L'assistente risponde in più lingue?", "Sì: italiano, inglese, tedesco, francese e le altre lingue dei vostri ospiti. Prima di metterlo online lo proviamo insieme con le domande che ricevete davvero."),
            ("E se l'assistente non sa la risposta?", "Non inventa: risponde solo con le informazioni che ci date sulla struttura. Se una domanda esce da quelle informazioni, la passa alla reception."),
            ("L'AI gestisce anche i pagamenti?", "No. L'assistente può indirizzare l'ospite al vostro sistema di prenotazione, ma pagamenti, caparre e rimborsi restano nei sistemi di pagamento e nelle mani dello staff."),
            ("Potete chiedere le recensioni solo agli ospiti soddisfatti?", "No, e non lo consigliamo: l'invito a lasciare una recensione parte uguale per tutti, senza filtri e senza incentivi, come prevedono le regole delle piattaforme."),
            ("I dati degli ospiti sono al sicuro?", "Lavoriamo nel rispetto del GDPR: accessi limitati ai soli dati necessari, intelligenza artificiale usata tramite servizi professionali che non addestrano i modelli sui vostri dati e un accordo scritto sul trattamento dei dati."),
            ("Quando conviene partire?", "In bassa stagione: una prima automazione richiede di solito dalle 2 alle 4 settimane, test compresi, e così è pronta quando arrivano le richieste."),
            ("Lavorate in tutta Italia?", "Sì, lavoriamo da remoto con strutture di tutta Italia e, quando serve, veniamo in sede per l'analisi iniziale."),
        ],
        "cta": "Quante email uguali<br>al giorno? <em>Rispondiamo noi.</em>",
        "placeholder": "Quale attività vi toglie più tempo agli ospiti?",
    },
]

# ---------------------------------------------------------------- template


def case_vis(kind, data):
    if kind == "inv":
        rows = "".join(f'<div class="mini-row"><b>{t}</b><span></span><em>✓</em></div>' for t in data)
        return f'<div class="case__vis case__vis--inv">{rows}</div>'
    if kind == "mail":
        tags = "".join(f'<div class="mail-tag {c}">{t}</div>' for c, t in zip("abcd", data))
        return f'<div class="case__vis case__vis--mail">{tags}</div>'
    if kind == "chat":
        return (f'<div class="case__vis case__vis--chat"><div class="bubble bubble--in sm">{data[0]}</div>'
                f'<div class="bubble bubble--out sm">{data[1]}</div></div>')
    bars = "".join(f'<i style="--h:{h}%"></i>' for h in (40, 65, 50, 80, 72, 95))
    return f'<div class="case__vis case__vis--rep"><div class="bars">{bars}</div></div>'


def jsonld(obj):
    return '<script type="application/ld+json">\n' + json.dumps(obj, ensure_ascii=False, indent=2) + "\n</script>"


def strip_tags(s):
    import re
    return re.sub(r"<[^>]+>", " ", s).replace("  ", " ").strip()


def render(p):
    url = f"{BASE}/{p['slug']}/"
    others = [o for o in PAGES if o["slug"] != p["slug"]]
    ld_main = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Service", "@id": url + "#servizio", "name": p["service"], "serviceType": "Automazione dei processi aziendali con l'intelligenza artificiale",
             "description": p["description"], "url": url, "areaServed": {"@type": "Country", "name": "Italia"},
             "audience": {"@type": "BusinessAudience", "name": p["audience"]},
             "provider": {"@type": ["Organization", "ProfessionalService"], "@id": f"{BASE}/#azienda", "name": "FlussAI", "url": f"{BASE}/",
                          "email": "info@officinaquantica.it", "telephone": "+39 351 507 3173", "logo": f"{BASE}/icon-512.png"}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "FlussAI", "item": f"{BASE}/"},
                {"@type": "ListItem", "position": 2, "name": p["menu"], "item": url}]},
        ],
    }
    ld_faq = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]}

    flow = []
    for i, (lab, txt) in enumerate(p["flow"]):
        cls = ["", " flow__step--ai", " flow__step--ok"][i]
        flow.append(f'<div class="flow__step{cls}"><small>{lab}</small><strong>{txt}</strong></div>')
        if i < 2:
            flow.append('<span class="flow__arrow"><svg class="ic"><use href="#i-arrow"/></svg></span>')

    problems = "\n".join(f'              <li><svg class="ic"><use href="#i-x"/></svg> {t}</li>' for t in p["problems"])
    solution = "\n".join(f"            <p>{t}</p>" for t in p["solution"])
    tools = "\n".join(f'            <li><svg class="ic"><use href="#{ic}"/></svg> {t}</li>' for ic, t in p["tools"])
    cases = "\n".join(
        f'          <article class="case fade">\n            {case_vis(k, d)}\n            <span class="case__cat">{cat}</span>\n            <h3>{h}</h3>\n            <p>{t}</p>\n          </article>'
        for k, d, cat, h, t in p["cases"])
    keep = "\n".join(
        f'          <div class="keep__item fade"><svg class="ic"><use href="#i-user"/></svg><div><strong>{h}</strong><p>{t}</p></div></div>'
        for h, t in p["keep"])
    faq = "\n".join(f'          <details><summary>{q}<svg class="ic"><use href="#i-plus"/></svg></summary><p>{a}</p></details>' for q, a in p["faq"])
    related = "\n".join(
        f'          <a class="sector-card fade" href="/{o["slug"]}/"><span class="case__cat">Altro settore</span><strong>{o["menu"]}</strong><p>{strip_tags(o["lead"]).split(":")[0].split(".")[0]}.</p><span class="go">Scopri <svg class="ic"><use href="#i-arrow"/></svg></span></a>'
        for o in others)
    menu_sectors = "\n".join(f'      <a href="/{o["slug"]}/">{o["menu"]}</a>' for o in others)
    foot_links = " ".join(f'<a href="/{o["slug"]}/">{o["menu"]}</a>' for o in PAGES)

    return f"""<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{p['title']}</title>
  <meta name="description" content="{p['description']}">
  <link rel="canonical" href="{url}">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#1D4ED8">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="it_IT">
  <meta property="og:site_name" content="FlussAI">
  <meta property="og:title" content="{p['title'].split(' | ')[0]}">
  <meta property="og:description" content="{p['description']}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{BASE}/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="{BASE}/og-image.jpg">
  <link rel="icon" href="/favicon.ico" sizes="48x48">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="/favicon-96x96.png" type="image/png" sizes="96x96">
  <link rel="icon" href="/icon-192.png" type="image/png" sizes="192x192">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/style.css">
  {jsonld(ld_main)}
  {jsonld(ld_faq)}
</head>
<body>
{ICONS}

  <header class="header" id="top">
    <div class="wrap header__in">
      <a href="/" class="logo" aria-label="FlussAI, vai alla home">fluss<span class="logo__ai">AI</span></a>
      <div class="header__actions">
        <button class="menu-btn" aria-expanded="false" aria-controls="menu"><span class="menu-btn__lines" aria-hidden="true"><i></i><i></i></span> Menu</button>
        <a href="#prenota" class="btn btn--blue btn--sm">Prenota una call <svg class="ic"><use href="#i-arrow"/></svg></a>
      </div>
    </div>
  </header>

  <nav class="menu" id="menu" aria-label="Menu principale" hidden>
    <div class="wrap menu__in">
      <a href="#cosa-facciamo">Cosa automatizziamo</a>
      <a href="#faq">Domande frequenti</a>
{menu_sectors}
      <a href="/">Home FlussAI</a>
      <a href="#prenota" class="menu__cta">Prenota una call gratuita <svg class="ic"><use href="#i-arrow"/></svg></a>
    </div>
  </nav>

  <main>
    <section class="hero hero--sector">
      <div class="wrap hero__copy">
        <p class="crumbs"><a href="/">FlussAI</a> › {p['menu']}</p>
        <p class="hero__kicker"><span class="pulse"></span> {p['kicker']}</p>
        <h1>{p['h1']}</h1>
        <p class="hero__lead">{p['lead']}</p>
        <div class="hero__ctas">
          <a href="#prenota" class="btn btn--blue">Prenota una call gratuita <svg class="ic"><use href="#i-arrow"/></svg></a>
          <a href="#cosa-facciamo" class="btn btn--line">Guarda cosa automatizziamo</a>
        </div>
        <div class="flow" aria-label="Esempio di automazione">
          {''.join(flow)}
        </div>
      </div>
    </section>

    <section class="blue">
      <div class="blue__grid" aria-hidden="true"></div>
      <div class="wrap blue__in">
        <div class="pb">
          <div class="pb__col fade">
            <h2 class="pb__title">Il <em>problema</em></h2>
            <ul class="pb__list">
{problems}
            </ul>
          </div>
          <div class="pb__col fade">
            <h2 class="pb__title">La <em>soluzione</em></h2>
{solution}
          </div>
        </div>
        <div class="integr fade" style="margin-bottom:0">
          <p class="integr__q"><em>Con cosa?</em></p>
          <h2 class="integr__title">Con quello che usate già</h2>
          <ul class="integr__list">
{tools}
          </ul>
        </div>
      </div>
    </section>

    <section class="cases" id="cosa-facciamo">
      <div class="wrap">
        <h2 class="big-title fade">{p['cases_title']}</h2>
        <p class="sub fade">Alcuni esempi. Ogni realtà lavora a modo suo: partiamo sempre da come lavorate voi, un processo alla volta.</p>
        <div class="cases__grid">
{cases}
        </div>
      </div>
    </section>

    <section class="keep" style="padding-top:0">
      <div class="wrap">
        <h2 class="big-title fade">Cosa resta <em>a voi</em></h2>
        <p class="sub fade">L'automazione toglie il lavoro ripetitivo, non le decisioni. Su invii, pagamenti e casi delicati c'è sempre una persona.</p>
        <div class="keep__grid">
{keep}
        </div>
      </div>
    </section>

    <section class="method" style="padding-bottom:110px">
      <div class="wrap">
        <h2 class="big-title fade">Come si <em>parte</em></h2>
        <p class="sub fade">Nessun impegno finché non avete una proposta chiara in mano.</p>
        <ol class="steps3">
          <li class="fade"><strong>Call gratuita di 30 minuti</strong><p>Ci raccontate come lavorate e quali attività vi rubano più tempo.</p></li>
          <li class="fade"><strong>Analisi e proposta</strong><p>Guardiamo il processo con chi lo svolge e vi diamo cosa automatizzare, tempi e costi.</p></li>
          <li class="fade"><strong>Costruzione e prova</strong><p>Sviluppiamo, colleghiamo ai vostri strumenti e testiamo su casi reali prima di accenderlo.</p></li>
        </ol>
      </div>
    </section>

    <section class="cta-sec" id="prenota">
      <div class="wrap">
        <div class="cta">
          <div class="blue__grid" aria-hidden="true"></div>
          <div class="cta__copy">
            <h2>{p['cta']}</h2>
            <p>Prenota una call gratuita di 30 minuti: ci racconti come lavorate e ti diciamo con onestà cosa si può automatizzare e quanto tempo risparmieresti.</p>
          </div>
          <form class="cta__form" id="lead-form" action="https://formsubmit.co/ajax/info@officinaquantica.it" method="POST" novalidate>
            <input type="hidden" name="_subject" value="FlussAI ({p['menu']}): richiesta di call gratuita">
            <input type="hidden" name="_template" value="table">
            <input type="hidden" name="pagina" value="{p['menu']}">
            <input type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true" style="display:none">
            <div class="row">
              <input name="nome" type="text" placeholder="Nome e cognome" autocomplete="name" required aria-label="Nome e cognome">
              <input name="azienda" type="text" placeholder="Azienda" autocomplete="organization" aria-label="Azienda">
            </div>
            <div class="row">
              <input name="email" type="email" placeholder="Email" autocomplete="email" required aria-label="Email">
              <input name="telefono" type="tel" placeholder="Telefono" autocomplete="tel" aria-label="Telefono">
            </div>
            <textarea name="messaggio" rows="3" placeholder="{p['placeholder']}" aria-label="{p['placeholder']}"></textarea>
            <label class="consent"><input type="checkbox" name="privacy" required> <span>Ho letto l'<a href="/privacy.html">informativa privacy</a> e acconsento a essere ricontattato.</span></label>
            <button type="submit" class="btn btn--white">Prenota la call gratuita <svg class="ic"><use href="#i-arrow"/></svg></button>
            <p class="form-msg" id="form-msg" role="status" aria-live="polite"></p>
          </form>
        </div>
      </div>
    </section>

    <section class="faq" id="faq">
      <div class="wrap wrap--narrow">
        <h2 class="big-title fade">Domande <em>frequenti</em></h2>
        <p class="sub fade">Non trovi la tua domanda? Chiedicela in call, la prima è gratuita.</p>
        <div class="faq__list fade">
{faq}
        </div>
      </div>
    </section>

    <section class="sectors">
      <div class="wrap">
        <div class="sectors__grid">
{related}
          <a class="sector-card fade" href="/"><span class="case__cat">FlussAI</span><strong>Tutte le automazioni</strong><p>Email, fatture, documenti, Excel e gestionali per ogni tipo di PMI.</p><span class="go">Vai alla home <svg class="ic"><use href="#i-arrow"/></svg></span></a>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="wrap">
      <p class="footer__big">Lascia che il lavoro <em>scorra.</em></p>
      <div class="footer__row">
        <div>
          <a href="/" class="logo logo--light">fluss<span class="logo__ai">AI</span></a>
          <p class="footer__claim">Automazione dei processi aziendali con l'AI per le PMI italiane.</p>
        </div>
        <div class="footer__contacts">
          <p><span>Telefono</span><a href="tel:+393515073173">+39 351 507 3173</a></p>
          <p><span>Email</span><a href="mailto:info@officinaquantica.it">info@officinaquantica.it</a></p>
        </div>
      </div>
      <nav class="footer__links" aria-label="Settori">{foot_links}</nav>
      <div class="footer__bottom">
        <p>© <span id="year">2026</span> FlussAI · Largo Valorsa, 23100 Sondrio · P.IVA IT01009390145</p>
        <p><a href="/privacy.html">Privacy e cookie</a> · <a href="#" data-cookie-prefs>Preferenze cookie</a></p>
      </div>
    </div>
  </footer>

  <script src="/main.js" defer></script>
  <script src="/cookie-consent.js" defer></script>
</body>
</html>
"""


if __name__ == "__main__":
    for p in PAGES:
        out = ROOT / p["slug"] / "index.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(render(p), encoding="utf-8")
        print("scritto", out.relative_to(ROOT))
