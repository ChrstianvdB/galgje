import random
woorden = ("informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk")

print("Welkom bij Galgje!") 

r = random.randint(1,10)
gekozenwoord = woorden[r]
print(gekozenwoord)
aantalbeurten = 10
gekozenletters = []
  
def beurt():
  global aantalbeurten
  print(f"Nog maar {aantalbeurten} pogingen!")
  aantalbeurten = aantalbeurten - 1
  gekozenletter = input("kies een letter \n")  
  gekozenletters.append(gekozenletter)  
  streepjes = []
  
  for letter in gekozenwoord:    
    if letter in gekozenletters:
      streepjes.append(letter)
    else:
      streepjes.append('_')
  
  print(streepjes)
  if aantalbeurten == 0:
    print("GAME OVER")
    c = input("Nog een keer spelen?")
    if c=="ja":
      beurt()
      
  beurt() 
    
  
beurt()