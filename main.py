def game():
  print("Welkom bij Galgje!") 
  
  woorden = ("informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk")
  import random
  r = random.randint(1,10)
  gekozenwoord = woorden[r]
  print(gekozenwoord)
  aantalbeurten = 10
  gekozenletters = []
  
  def beurt():
    global aantalbeurten
    print(f"Nog maar {aantalbeurten} pogingen!")
    aantalbeurten = aantalbeurten - 1
    gekozenletter = input("kies een letter")
  
    streepjes = []
    for letter in gekozenwoord:
     if gekozenletter == letter:
        streepjes.append(gekozenletter)
     else:
        streepjes.append('_')
  
    print(streepjes)
    if aantalbeurten == 0:
      print("GAME OVER")
      c = input("Nog een keer spelen?")
      if(c=="ja"):
        game()
    c = input("nog een letter?")
    if(c=="ja"):
      beurt()
    else:
      print("GAME OVER")
    
  
  beurt()
game()