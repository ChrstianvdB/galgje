import random
woorden = ("informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk")

aantalbeurten = 15
gekozenletters = []  
gekozenwoord = ""

def game():
  global aantalbeurten, gekozenwoord, gekozenletters
  
  print("Welkom bij Galgje!")
  print("type 'SpelUitleg' voor een uitleg van de regels")
    
  r = random.randint(1,10)
  gekozenwoord = woorden[r]
  aantalbeurten = 15  
  gekozenletters = []  
  
  beurt()

def beurt():
    global aantalbeurten, gekozenletters
    print(f"Nog maar {aantalbeurten} pogingen!")
    aantalbeurten = aantalbeurten - 1
    gekozenletter = input("kies een letter \n")  
    if gekozenletter == "SpelUitleg":
      print("Je weet het wel, -1 poging voor domheid")
      beurt()
    if gekozenletter == "":
      print("Wel iets invullen he, -1 poging voor domheid")
      beurt()
    if gekozenletter == "Suicide":
      aantalbeurten = aantalbeurten - aantalbeurten
    gekozenletters.append(gekozenletter)  
    streepjes = []
    if gekozenletter ==gekozenwoord:
      print("YOU WIN!")
      c = input("Nog een keer spelen? \n")
      if c=="ja":
        game()
      else:
        print("Jawel")
        game()
      
    for letter in gekozenwoord:    
      if letter in gekozenletters:
        streepjes.append(letter)
      else:
        streepjes.append('_')
      
    print(" ".join(streepjes))
    
    if aantalbeurten == 0:
      print("GAME OVER")
      c = input("Nog een keer spelen? \n")
      if c=="ja":
        game()
      if c=="rick":
        print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        game()
      if c=="PickleRick":
        print("https://www.youtube.com/watch?v=ML5UI-0JS_Q")
        game()
      if c=="roadhouse":
        print("https://www.youtube.com/watch?v=wqWADN0UubA")
        game()
      if c=="fuck":
        print("https://www.youtube.com/watch?v=Rc0cQLDFncs")
        game()
      if c=="pride":
        print("https://www.youtube.com/watch?v=03MkRR4eGNg")
        game()
      if c=="moo":
        print("https://www.youtube.com/watch?v=ELBVeRDflV0")
        game()
      if c=="SIUUU":
        print("https://www.youtube.com/shorts/QwSnhQaw0qk")
      if c=="kermitsuicide":
        print("https://www.youtube.com/watch?v=fGMViTfNPkQ")
      if c=="noohe":
        print("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Pug_portrait.jpg/1200px-Pug_portrait.jpg")
      else:
        print("Jawel")
        game()
            
    beurt() 
        
      
game()