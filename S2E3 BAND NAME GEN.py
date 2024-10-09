
# adorable title screen
print("------------------------\n|  BAND NAME GENERATOR |\n------------------------\n")
print("\n")
elementiband = []

# Simple string word pluralization (may be broken gotta fix)
animalepreferito = input("Inserire animale preferito: \n")

if animalepreferito.endswith(("o", "e")):     
    animalepreferito = animalepreferito[:-1] + "i"
elif animalepreferito.endswith("a"):
    animalepreferito = animalepreferito[:-1] + "e"

# list element append
elementiband.append (animalepreferito)
elementiband.append (" di ")
elementiband.append (input("Inserire città di provenienza: \n"))

# string conversion of list elements
nomeband = ''.join(elementiband)

# output ("x" di "y")
print("Il nome della tua band è:", nomeband)


