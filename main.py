import random
woorden = ("informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk")

aantalbeurten = 15
gekozenletters = []  
gekozenwoord = ""

def game():
  global aantalbeurten, gekozenwoord, gekozenletters
  
  print("Welkom bij Galgje!") 
    
  r = random.randint(1,10)
  gekozenwoord = woorden[r]
  print(gekozenwoord)
  aantalbeurten = 15  
  gekozenletters = []  
  
  beurt()

def beurt():
    global aantalbeurten, gekozenletters
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
      
    print(" ".join(streepjes))
    
    if aantalbeurten == 0:
      print("GAME OVER")
      c = input("Nog een keer spelen?")
      if c=="ja":
        game()
      else:
        print("Jawel")
        game()
            
    beurt() 
        
      
game()
