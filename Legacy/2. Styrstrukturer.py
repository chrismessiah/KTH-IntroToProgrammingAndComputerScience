#Python-program 2  - COMMENTARY - juli 2, 2012 6:19 em
#Python version - 2.6 ...?
# OBS INTE KORBAR!!!

# DEl 2

# 2.0 Villkor

# Problem: Mamma ska resa till mormor over helgen. Hon ar orolig for att lille Lasse, som ska vara alldeles ensam hemma, kommer att kla sig far tunt och vill darfor ha ett program som hjalper honom med kladseln.

# For att kunna skriva ett sadant program behover vi lara oss 2 saker: hur man laser inmatning fran tangentbordet och hur man jamfor tal.

print""
#________________________________________________________________________________________________

# 2.1 Inlasning

# variebeln "temperatur" kommer ha vardet som programmet skrev pa tangentbordet

print "Ge utetemperatur: " 
temperatur = input()

# Eller den forkortade versionen!

temperatur = input("Ge utetemperatur: ")

# input() (sedan version 3.0) laser allt som text for berakningar med variabeln temperatur maste du konvertera till heltal med int()

temperatur = int(input("Ge utetemperatur: "))

# om det inte behover vara ett heltal eller ett reellt tal sa andvant eval() istallet

temperatur = eval(input("Ge utetemperatur: "))

# Det intryckta oavsett om siffra eller bokstav ar vardet pa "temperatur" med [ENTER]

print""
#________________________________________________________________________________________________

# 2.2 Villkor

temperatur = input("Ge utetemperatur: ")
if int(temperatur) < 5:
	print "Ta pa dig halsduk, lille van!" 
	
# struktur på if-sats

# if [BOOLESKT UTTRYCK] :
# 	 [EN ELLER FLERA SATSER SOM SKA EXEKVERAS]

# booleskt varde = True eller False
# andvand [TAB] for indentering If-satsen slutar när det kommer en icke-indenterad sats

# Observera att konverteringen fran text till tal med int() kan goras pa andra platser dar man vill att temperatur ska hanteras som ett tal. Det vanliga ar att gora det direkt vid inlasningen 


print""
#________________________________________________________________________________________________


# 2.3 Konstanter


# En konstant skrivs pa samma satt som en variabel bortsett fran att det ar stora bokstaver och _ isallet for [mellanslag]
# EN_KONSTANT = ?

MAMMAS_FRYSPUNKT = 5
temperatur = int(input("Ge utetemperatur: "))
if temperatur < MAMMAS_FRYSPUNKT:
    print("Ta pa dej en halsduk, lille van!")

# en konstant kan inte andra funktionen i ett program men gor det lattare att modifiera och fortydliga

print""
#________________________________________________________________________________________________


# 2.4 Else-del i if-sats

# man kan lagga till [ELSE] för att definera en instruktion for ovriga utslag

MAMMAS_FRYSPUNKT = 5
temperatur = int(input("Ge utetemperatur: "))
if temperatur < MAMMAS_FRYSPUNKT:
    print("Ta pa dej en halsduk, lille van!")    
else:
    print("Mammas gullgubbe slipper halsduk!")





# man kan lagga till ytterligare villkor genom [ELIF]

MAMMAS_FRYSPUNKT = 5
CELSIUS_FRYSPUNKT = 0
temperatur = int(input("Ge utetemperatur: "))
if temperatur < CELSIUS_FRYSPUNKT:
    print("Ta på dej halsduk och mössa!")
elif temperatur < MAMMAS_FRYSPUNKT:
    print("Ta på dej en halsduk!")
else:
    print("Mammas gullgubbe slipper halsduk!")


print""
#________________________________________________________________________________________________


# 2.5 Flera villkor

min = 5
max = 10
b = 0
print "Definera a som siffra:"
a = int(input())

if a < min: 
	min = a
	print min
elif a > max: 
	max = a
	print max
else:
	b += 1
	print b
	
print""
#________________________________________________________________________________________________


# 2.6 Likhet

# under testning av likhet anvands dubbla likhetstecken [==] ett enkelt likhetstecken ar endast tilldelnnig [=]

betyg = 2123
if betyg == 2000:
    print "Du har precis kommit in pa hogskolan" 
elif betyg > 2000:
    print "Du har kommit in pa hogskolan" 
else:
    print "Du har inte kommit in pa hogskolan"

# man kan aven gora villkaren inom varann

if x > 2:
  if y > 4:
    print("blå")
  elif x == y: 
    print("gul")
  else: 
    print("röd")
else:
  print("grön")


print""
#________________________________________________________________________________________________


# 2.7 While-slingor 

# While ar upprepningar

antal_varv = 0
while antal_varv < 5 :
	print "Python"
	antal_varv += 1

# [antal_varv] är raknaren som har startvardet 0 resten ar while-satsen som liknar if-satsen

# da [antal_varv] ar mindre an 5 kommer de indragna rader exekveras

# [print "Python"] syftar till att den ska printa det varje varv som villkoret foljs

# [antal_varv += 1] menar att efter varje varv kommer raknaren öka startvardet med 1

# annat exempel:

i=0
while i < 5:
  v = i * 2
  print(v, " ")
  i += 2



print""
#________________________________________________________________________________________________



# 2.8 Hur exekveras programmet?

antal_varv = 0
while antal_varv < 5 :
	print "Python"
	antal_varv += 1

# i de forsta fem varven for while villoret [TRUE] men efter det blir det [FALSE]




print""
#________________________________________________________________________________________________


# 2.9 En oandlig while-slinga

antal_varv = 0
while antal_varv < 5 :
  print("Python")

# [antal_varv] forandras ej, denna slinga ar oandlig! 


print""
#________________________________________________________________________________________________


# 2.10 Struktur pa while-sats

# while <BOOLESKT UTTRYCK> :
# 	 <EN ELLER FLERA SATSER SOM SKA EXEKVERAS>

# identisk med if-satsen bara man byter ut det mot while


print""
#________________________________________________________________________________________________


# 2.11 När ska man använda en while-sats?


tal = int(input("Gissa ett tal mellan 1 och 100:"))
while tal != 74 :
  tal = int(input("fel, försök igen:"))
print("Grattis du gissade rätt!")


# VAD FAN MENAR DE MED [!] ??


#________________________________________________________________________________________________
#________________________________________________________________________________________________
# E.N.D







































