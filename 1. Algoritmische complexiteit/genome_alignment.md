# Exercises 1.3:
n = lees acties (30 mil)
m = dataset size (2gb * n)

Algoritme	Gemiddelde tijd	Gemiddelde ruimte
Quick sort	n*log(n)	log(m)
Heap sort	n*log(n)	1
Insertion sort	n2	1

## 1. Hoeveel tijd is er nodig voor het uitvoeren van de sortering met gebruik van elk van deze algoritmen? Welk algoritme(n) presteert het beste?
qSort, t= gedeelde eerste plek, RAM= beste
hSort, t= gedeelde eerste plek, RAM= gedeelde laatste plek
iSort, t= langzaamst, RAM= gedeelde laatste plek
## 2. Hoeveel ruimte is er nodig voor het uitvoeren van de sortering met gebruik van elk van deze algoritmen? Welk algoritme(n) presteert het beste op zowel tijd als ruimte?
quick sort is het beste omdat je daar maar de log ruimte nodig hebt en in snelheid ook n*log(n) is.
## 3. In het worst-case scenario, gebruikt Quick Sort n2 tijd en m space. Hoe veel meer tijd en ruimte is dit vergeleken met de gemiddelde tijd/ruimte? Wat gebeurt er met de tijd en ruimte als je 60 miljoen leesacties gaat sorteren?
30*log(30) = 44.3 mil vs 30^2 = 900 mil in tijd
log(30) = 1.47 mil vs 30 mil in ruimte.