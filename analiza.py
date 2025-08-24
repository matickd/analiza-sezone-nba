import re
import csv
import json

def ocisti_html(besedilo):
    return re.sub(r'<.*?>', '', besedilo).strip()

def regular_season(html):
    vzorec_rednidelsezone = r'<div[^>]+id="div_per_game_stats"[^>]*>(.*?)<\/div>'
    najdi_rednidel = re.search(vzorec_rednidelsezone, html, flags=re.DOTALL)
    return najdi_rednidel.group(1) if najdi_rednidel else ""

def playoffs(html):
    vzorec_playoffs = r'<div[^>]+id="div_per_game_stats_post"[^>]*>(.*?)<\/div>'
    najdi_playoffs = re.search(vzorec_playoffs, html, flags=re.DOTALL)
    return najdi_playoffs.group(1) if najdi_playoffs else ""

def izvleci_igralce(html_fragment):
    vrstice = re.findall(r'<tr[^>]*?>(.*?)</tr>', html_fragment, flags=re.DOTALL)
    igralci = []
    for vrstica in vrstice:
        if not re.search(r'<td', vrstica):
            continue

        ime_match = re.search(r'<th.*?><a[^>]*>(.*?)</a>', vrstica, flags=re.DOTALL)
        ime = ocisti_html(ime_match.group(1)) if ime_match else "NEZNANO"

        pozicija_match = re.search(r'data-stat="pos"[^>]*>(.*?)</td>', vrstica, flags=re.DOTALL)
        pozicija = ocisti_html(pozicija_match.group(1)) if pozicija_match else "NEZNANO"

        celice = re.findall(r'<td[^>]*?>(.*?)</td>', vrstica, flags=re.DOTALL)
        if len(celice) < 29:
            continue

        ekipa = ocisti_html(celice[2])
        if ekipa == "2TM":
            continue

        igralec = {
            "ime": ime,
            "ekipa": ekipa,
            "pozicija": pozicija,
            "tekme": ocisti_html(celice[4]),
            "točke": ocisti_html(celice[28]),
            "podaje": ocisti_html(celice[23]),
            "skoki": ocisti_html(celice[22])
        }

        igralci.append(igralec)
    return igralci

def varna_stevilka(x):
    try:
        return float(x)
    except (ValueError, TypeError):
        return 0.0

def najboljsi_po_kljucu(igralci, kljuc, n=10):
    return sorted(igralci, key=lambda x: varna_stevilka(x[kljuc]), reverse=True)[:n]

def shrani_csv(igralci, ime_datoteke):
    ključi = ["ime", "ekipa", "pozicija", "tekme", "točke", "podaje", "skoki"]
    with open(ime_datoteke, "w", encoding="utf-8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=ključi, delimiter=';')
        writer.writeheader()

        for igralec in igralci:
            igralec_copy = igralec.copy()
            for kljuc in ["točke", "podaje", "skoki"]:
                igralec_copy[kljuc] = f"'{igralec_copy[kljuc]}'"  # številke pretvori v besedilo z apostrofom
            writer.writerow(igralec_copy)

def shrani_json(igralci, ime_datoteke):
    with open(ime_datoteke, "w", encoding="utf-8") as f:
        json.dump(igralci, f, ensure_ascii=False, indent=2)

# === GLAVNI DEL ===

with open("statistika.html", encoding="utf-8") as f:
    html = f.read()

html_regular = regular_season(html)
html_playoffs = playoffs(html)

igralci_regular = izvleci_igralce(html_regular)
igralci_playoffs = izvleci_igralce(html_playoffs)

# === Prikaz in shranjevanje TOP 10 po ključih ===

statistike = ["točke", "podaje", "skoki"]

for kljuc in statistike:
    print(f"\nTop 10 igralcev po {kljuc} - redna sezona:")
    top_regular = najboljsi_po_kljucu(igralci_regular, kljuc)
    for i in top_regular:
        print(f"{i['ime']} ({i['ekipa']}): {i[kljuc]} {kljuc.upper()}")

    print(f"\nTop 10 igralcev po {kljuc} - končnica:")
    top_playoffs = najboljsi_po_kljucu(igralci_playoffs, kljuc)
    for i in top_playoffs:
        print(f"{i['ime']} ({i['ekipa']}): {i[kljuc]} {kljuc.upper()}")

    # Shrani za redno sezono
    shrani_csv(top_regular, f"top10_{kljuc}_redna.csv")
    shrani_json(top_regular, f"top10_{kljuc}_redna.json")

    # Shrani za končnico
    shrani_csv(top_playoffs, f"top10_{kljuc}_koncnica.csv")
    shrani_json(top_playoffs, f"top10_{kljuc}_koncnica.json")



shrani_csv(igralci_regular, "igralci_redna_sezona.csv")
shrani_json(igralci_regular, "igralci_redna_sezona.json")
shrani_csv(igralci_playoffs, "igralci_koncica.csv")
shrani_json(igralci_playoffs, "igralci_koncica.json")