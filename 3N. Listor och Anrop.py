# Array of 3, empty
namelist = 3*[None]

# First elem contains 'Tosh'
namelist[0] = "Tosh"

# Prints entire list
print(namelist)

# ******************** MODULER ********************
# En fil med en samling av funktioner kallas för modul
# För att vi ska kunna använda en viss funktion från en 
# viss modul måste vi importera tillhörande modul innan 
# anropet av funktionen. 
from math import *	# imports sqrt and so on

# imports random() {val from 0-1}, randint(1,3) {val of 1,2 or 3}
from random import *