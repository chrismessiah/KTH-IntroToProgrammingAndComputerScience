#Python-program X  - XXXXXXX - juli 4, 2012 12:05 em
#Python 3.2.3

# ORDLISTA


VARIABEL = 3
# #tilldelningsoperator "="
# vaiabeln "VARIABEL" får värdet 3 genom tilldelningsoperatorn

VARIABEL2 = "Stina"
# Variabeln kan ocksa ha ett varde av ["BOKSTAVER"]


längd = VARIABEL
# variabeln "längd" får variabeln "VARIABEL"s värde


print("Hello World!")
# Visar "Hello World!" i konsollen

print(VARIABEL)
# Visar variabeln "VARIABEL"s värde i konsollen

print(1001)
# visar värdet "1001" i konsollen

print ("Charles is", 19, "years old")
# "" för ett värde av bokstäver
# värden av bokstäver och siffor måste separeras genom kommatecken ","
# tex print ("Jag är", 19, "år gammal")


namn = 'Anna'
telefon = '06509911122'
print (namn, "har telefon", telefon)
# print visar värdet för "namn", skriver ut "har telefon" och skriver ut värdet för "telefon"


längd1 = längd + 1
#Algebra..


KONSTANT_ETT = ""
# konstanter skrivs med stora bokstäver och "_" istället för " "
# "" innebär att KONSTANT_ETT har inget värde



längd2 = 3
längd2 += 2
# uppräkningsoperator "+="

# längd2 har nu värdet 5

längd3 = 4
längd4 = längd3 + 3
# Samma sak, värdet 7


print("")
#________________________________________________________________________________________________


GE_VÄRDE = input()
# input() innebär att värdet ska skrivas in i konsollen under körningen

GE_VÄRDE2 = input("Ge värdet till GE_VÄRDE2: ")
# det innanför input("...") visas i konsollen sp man vet vilket värde som ska anges

VALFRI_SIFFRA = int(input("Ge heltal eller reel siffra: "))
# det inskrivna värdet förväntas vara reela siffror

REEL_SIFFRA = eval(input("Ge valfri siffra: "))
# samma sak bara att siffran kan vara vad som helst!

if int(REEL_SIFFRA) < 5:
	print ("Ta pa dig halsduk, lille van!" )
# "if" är en villkorsbegränsning, om det inknappade värdet följer villkoret initeras de indragna slingorna, i detta fall under 5 
# de ingragra raderna är de som tillhör if-slingan
# kan bara finnas ett if-villkor

elif 5 < int(REEL_SIFFRA) < 10 :
	print("Skit i halsduken")
# "elif" är samma sak som "if" bara att det kan finnas oändligt många

else :
	print("Gör vad fan du vill")
# "else" avslutar villkorsslingan genom att ge ett villkor för alla andra värden.


ANTAL_VARV = 0
while ANTAL_VARV == 0 :
	print("Det nollte varvet")
	ANTAL_VARV += 1
	print(ANTAL_VARV)
# == är "lika med"
# Så länge "ANTAL_VARV" är lika med noll kommer slingan att repeteras



#________________________________________________________________________________________________









































