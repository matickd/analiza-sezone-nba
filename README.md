# Projektna naloga: Analiza NBA sezone 2024/25

## Opis
V tem projektu sem analiziral podatke igralcev iz **lige NBA za sezono 2024/25**. Podatke sem razdelil na **redno sezono** in **končnico (playoffs)**, da sem lahko primerjal statistiko igralcev in ekip v različnih delih sezone.

V analizi sem uporabil **CSV datoteki**, ki vsebujeta za vsakega igralca naslednje podatke:

- ime igralca  
- ekipa  
- pozicija  
- število odigranih tekem  
- povprečne točke na tekmo  
- povprečne podaje na tekmo  
- povprečni skoki na tekmo  

S pomočjo **Pandas** sem naredil različne analize, med drugim:

- izračunal **top 10 igralcev po točkah, podajah in skokih**, ločeno za redni del sezone in končnico  
- primerjal statistiko posameznih igralcev med redno sezono in končnico  
- izračunal **povprečne statistike ekip**  
- ustvaril različne grafične prikaze, ki prikazujejo povezave med statističnimi kategorijami (bar grafi in scatter ploti)  

---

## Kaj sem naredil v kodi

1. **Čiščenje podatkov**:  
   - odstranil sem nepotrebne znake iz številskih stolpcev  
   - pretvoril podatke v `float`  
   - odstranil manjkajoče vrednosti, da analiza ni bila napačna

2. **Top 10 igralcev**:  
   - Za **redno sezono** in **končnico** sem posebej našel najboljših 10 igralcev po **točkah, podajah in skokih**.  
   - Za vsako metriko sem prikazal tabelo in narisal graf, da se enostavno vidi, kdo izstopa.

3. **Primerjava posameznega igralca**:  
   - Izbral sem enega igralca (npr. Luka Dončić) in primerjal njegovo statistiko med redno sezono in končnico, kar omogoča vizualno primerjavo.

4. **Analiza ekip**:  
   - Izračunal povprečne statistike ekip (točke, podaje, skoki) in jih prikazal z grafom, da se vidi, katere ekipe imajo najboljše povprečje.

5. **Vizualizacije**:  
   - Ustvaril sem različne grafe, kot so bar grafi za top 10 igralcev in scatter ploti, ki prikazujejo povezave med statističnimi kategorijami.

---

## Navodila za uporabo

1. **Prenesi repozitorij** na svoj računalnik:

git clone https://github.com/matickd/analiza-sezone-nba.git

2. **Namesti zahtevane knjižnice** (če jih še nimaš):

pip install pandas matplotlib numpy

3. **Odpri Jupyter Notebook datoteko**:

analiza_notebook.ipynb

