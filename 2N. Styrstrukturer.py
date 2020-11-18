# **************** inputs of strings *****************
temp = input('Ge utetemperatur: ')

# Make input to int
temp = int(input('Ge utetemperatur: '))

# avrunda till 0 decimaler
temp = round(temp,2)

# eval() ???

# *************** Villkor *******************
if temp < 5:	# KOLON inte SEMI-KOLON
	print("Ta på dig en halsduk, lille vän!")	# MÅSTE VARA IDENTERAD!!!

# KONSTANTER_SKRIVS_SÅHÄR

if temp < 5:
	print("Ta på dig en halsduk, lille vän!")
else:
	print("Mammas gullgubbe slipper halsduk!")

# If [condition]:
	# indented code1
# else:
	# indented code2

# För flera villkor används elif
if temp < 5:
	print("Ta på dig en halsduk, lille vän!")
elif temp == 5:
	print("Skit på dig")
else:
	print("Mammas gullgubbe slipper halsduk!")

# *********************** While *****************