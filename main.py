print("Welkom bij Galgje!") 

woorden = ("informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk")
import random
r = random.randint(1,10)
gekozenwoord = woorden[r]
print(gekozenwoord)
gekozenletter = input("kies een letter")
streepjes = []
for letter in gekozenwoord:
  if gekozenletter == letter:
    streepjes.append(gekozenletter)
  else:
    streepjes.append("_")

print(streepjes)