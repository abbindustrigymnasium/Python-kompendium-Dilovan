import requests, random, os, time # För att hantera urls, slumpa saker, snygga till i terminalen och hantera tid
AntalFrågor, poäng, M = 9, 0, (requests.get("https://opentdb.com/api.php?amount=10&type=multiple")).json() # Bestämmer olika variabler, antal frågor(-1) i spelet antal poäng från början samt URL där frågorna kommer ifrån
def ree(poäng, AntalFrågor): # Min funktion för frågesporten
    if AntalFrågor >=0: # Medan vi fortfarande har frågor
        x = random.randint(0, AntalFrågor); AntalFrågor-=1 # Vi ska randomisera en fråga från url:en genom att att slumpa ett värde från 0-10, vi tar sedan bort 1 för att vi kört 1 gång
        tot = random.sample(([M['results'][x]['incorrect_answers'][0], M['results'][x]['incorrect_answers'][1], M['results'][x]['correct_answer']]), 3) # Vi slumpar placeringen av alla alternativ, två fel och ett rätt. Vi skriver 3 i slutet för att vi har 3 värden
        os.system('cls'), print("Write 1, 2 or 3 as your answer"), print(), print(M['results'][x]['question'],'\n'+" | 1: "+tot[0],'\n'+" | 2: "+tot[1],'\n'+" | 3: "+tot[2]); svar = input("Answer > ")
        # Allting ovanför är för ui. Rensar allt, skriver info till användare och skriver ut frågan samt alla alternativ och ber användaren om svar. \n är till för att skriva saker på en ny rad
        if svar == str((tot.index(M['results'][x]['correct_answer']))+1): # Personen får rätt om svaret skulle ha samma värde som det rätta svarets placering i arrayen med alternativ (tot). +1 för alternativen börjar inte på 0
            del M['results'][x]; poäng+=1 # Vi raderar frågan vi använt och ger användaren 1 poäng
            print(), print("You were right "), print("You now have "+str(poäng)+" points") # Säger att användaren hade rätt och skriver ut hens poäng
            time.sleep(3), os.system('cls'), ree(poäng, AntalFrågor) # Väntar en stund, rensar allt och anropar funktionen igen
        print(), print("Wrong, the correct answer was", M['results'][x]['correct_answer']), time.sleep(3), os.system('cls') # Om användaren har fel skriv det rätta svaret
        del M['results'][x]; ree(poäng, AntalFrågor) # Raderar frågan vi använt om anropar frågefunktionen igen                             
    else: os.system('cls'), print("We are out of questions. You got "+str(poäng)+" points"), exit() # Om alla frågor är slut skriv det och ge användaren hens poäng. Stäng ner programmet
ree(poäng, AntalFrågor) # Startar spelet