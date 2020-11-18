#Python-program X  - XXXXXXX - date time
#Python2

# DEl X



räknare = 0

while räknare < 3 :
	print("Python")
	räknare += 1
	
print("")


print("Ge ungntemperatur °C :")
ugntemperatur = int(input())

if 150 > ugntemperatur > 0 :
	print("Öka värmen!")
elif 200 > ugntemperatur > 150:
	print("Bra! Lägg i kakan!")
elif ugntemperatur > 200 :
	print("Sänk värmen!")
else :
	print("Temperaturen i ungen, inte i frysen!")