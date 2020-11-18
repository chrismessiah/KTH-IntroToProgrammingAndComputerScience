#Python-program 3  - COMMENTARY - juli 2, 2012 11:28 em
#Python version - 3
# OBS INTE KORBAR!!!

# DEL 3

# 3.1, 3.2, 3.3 Listor



# Listor skrivs med hjälp av klamrar [ ]

namnlista = 3 * [None]

# namnlista blir då en variabel som har plats för 3 olika värden som i nollte, första och andra rutan med noll som första platsen

# Programmerare är lite lustiga på det sättet att 0 betyder första plats i en lista. Detta gäller i flera programspråk, t ex Java och C++.

# Sedan för tilldelning gäller:


namnlista[0] = 47

# namnlista har nu värdet 47 i nollte rutan
# Om man vill tilldela andra plats i listan ett nytt värde använder man  indexet 1

namnlista[1] = "hej"

# För att skriva alla värden som finns i listan kan man skriva som nedan

print(namnlista)

# eller för en specifik plats på listan

print(namnlista[1])

# för att skriva en lista och visa den i OMVÄND ORDNING:
	
antal_namn = int(input("Hur många rader på listan? "))
namnlista = antal_namn * [None]
i = 0
while i < antal_namn:
	namnlista[i] = input("Ange namnet: ")
	i += 1
j = antal_namn - 1
while j >= 0:
	print(namnlista[j])
	j -= 1



print("")
#________________________________________________________________________________________________



# 3.4 Moduler

# Stora program delar man upp i mindre delar med bland annat funktioner. Funktionerna kan placeras i olika filer. En fil med en samling av funktioner kallas för modul. För att vi ska kunna använda en viss funktion från en viss modul måste vi importera tillhörande modul innan anropet av funktionen. Import kan man göra med en enkel import-sats som vi förklarar nedan.

# återanvända kod!

# kortare program!

# importeringen gör man med hjälp av reserverade orden "from", "import" och modulnamnet.

# Anta att vi behöver beräkna roten ur 23 i ett program. i modulen math finns en funktion som heter sqrt(x) som beräknar roten ur x och returnerar svaret. För att använda funktionen ska man importera modulen genom att skriva följande sats:

from math import *
print(sqrt (23))

# import-satsen behöver endast vara med en enda gång. Ett bra ställe för import-satser är därför i början av programmet.


print("")
#________________________________________________________________________________________________

# 3.5 Random

# importera modulen "random"

from random import *
s_tal = random()
print (s_tal)

# random() funktionen genererar slumpmässiga tal från 0 till 1 i decimaler
# för slumpmässig generation av heltal gäller randint() funktionen

h_tal = randint(0,10)
print(h_tal)

# denna kräver dock att man sätter en begränsning fr.o.m vilket t.o.m vilket tal






















































