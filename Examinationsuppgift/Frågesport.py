import random # För att kunna slumpa värden
import requests # För att kunna hantera API:er
import msvcrt # För att registrera endast en knapptryckning/den första tryckningen
import os # För att göra saker i terminalen, göra det snyggt
import time # Fixa saker som har med tid att göra, t.ex. delays 
# Vi tar frågorna från en URL med en viss kategori, kommer längre ner i koden0
def escape(str): # När man hämtar frågor från API:en kan det förekomma konstiga tecken, funktionen ska byta ut dessa
    str = str.replace("&amp;", "&") # Byter ut tecknets grundkod mot det vi ser när vi använder programmet
    str = str.replace("&#039;", "\'")
    str = str.replace("&quot;", "\"")
    return str # Returnerar, skickar tillbaks alla våra nya värden

def clear(): # För att rensa och göra snyggt i terminalen
    os.system('cls') # Rensar allt

def text(text):# För att kunna skriva i en rubrik och få den centrerad och snygg
    mellanrumm=""
    längd=((58-len(text))/2)-1 # Vår längd är maxlängden-textens längd/2 och -1 för att få centrering
    while längd >= 0:
        mellanrumm+=" " # Lägger på mellanrum beroende på längden
        längd-=1
        header="                             |"+mellanrumm+text+mellanrumm+"|" # Skriver ut det centrerat
    print(header) # Vi vill ha en maxlängd på texten som är 58

def line(line = 1): # Vilken typ av linje som vi vill ha, beroende på siffra som skrivs in
    if line == 1:
        print("                             |---------------------------------------------------------|")
    elif line == 2:
        print("                             /=========================================================\\")
    elif line == 3:
        print("                             \=========================================================/")
    elif line == 4:  
        print("                             |=========================================================|")
    elif line == 5:
        print("                                                                                        ")

def svar(text): # Där användaren skriver in sitt svar
    svar = input("                             | "+text+" > ")
    return svar # Returnerar för att kunna användas

def echo(text): # Bara skriva ut saker snyggt
    print("                             | "+text+"               ")

def cats(): # Våra kategorier
    line(2)                                                                                          
    print("                            |~| Music |~| Sports |~|  Computers  |~| History |~| Film |~|")
    line(3)

clear() # Rensar först allt
line(2) # Allting under är bara snyggt ui, beheöver inte kommenteras, beskriver för användarna hur allt funkar
text("WELCOME TO GEOPARDY!!")
line(3)
time.sleep(3) # Som delay, vi säger att den ska vänta 3 sekunder innan nästa sak kommer upp
text("Today you'll be three participants playing a quiz")
line()
time.sleep(3)
text("The quiz will contain 5 different categories ")
line()
time.sleep(2)
text(" Each category will contain 3 questions")
line()
time.sleep(3)
text("Each participant will also be assigned a key ")
text(" This key will act as your button")
line(4)
time.sleep(3)
del1 = svar("Participant 1") # Deltagare 1 får skriva sitt namn
echo(" ")
echo("Welcome "+del1+" your key is A") # Deltagare 1 får tangenten A
line(4)
time.sleep(1)
del2 = svar("Participant 2") # Deltagare 2 får skriva sitt namn
echo(" ")
echo("Welcome "+del2+" your key is G") # Deltagare 2 får tangent G
line(4)
time.sleep(1)
del3 = svar("Participant 3") # Deltagare 3 får skriva sitt namn
echo(" ")
echo("Welcome "+del3+" your key is L") # Deltagare 3 får tangent L
line(4) 
time.sleep(2)
clear()
line(4)
text("The higher powers will now choose who'll get to start") # Ska randomisa vem som börjar
line(4)
time.sleep(3)

space = "                             " # Hårdkodat mellanrum
Rounds, Musik, Film, Historia, Teknik, Sport, p1, p2, p3 = 15, 2, 2, 2, 2, 2, 0, 0, 0 # Värdet på alla variabler
# Antalet rundor som körs (Rounds), antal frågor inom varje kategori (Musik-Sport) och allas poäng (p1-p3)
poäng = [p1, p2, p3] # Array med allas poäng, deltagare 1 (del1) = p1 osv
deltagare = [del1, del2, del3] # Array med alla deltagare
RandDel = random.sample(deltagare, 1) #Här vill hämta en deltagare slumpmässigt från deltagare arrayen
ActiveDel = '\n'.join(map(str, RandDel)) #För att skriva ut det snyggt utan konstiga tecken
echo("IT-Jesus has said that "+ActiveDel+" will start") #Vi säger att denna person får börja
time.sleep(3)

def ShowCats(ActiveDel, Rounds, Musik, Film, Historia, Teknik, Sport): # Funktion för att visa och välja kategori
    clear() # Rensar allt tidigare
    text("These are the categories that you can choose from")
    text("Choose only one category ")
    cats()
    Choice = svar("Your choice") # Vilken kategori du väljer
    while Rounds >= 1: # Medan rundor/frågor är fler än 1 körs detta, det betyder att alla frågor inte är slut än

        if Choice.lower() == "music": # Om deltagaren väljer musik
            
            if Musik >= 0: # Medan vi har musikfrågor
                Rounds-=1 # Tar bort en "runda" för att veta att vi kört en gång
                Url = (requests.get("https://opentdb.com/api.php?amount=3&category=12&type=multiple")).json() # Url blir musik
                var = Musik # Vi sätter en allmän variabel som har värdet av Musik
                Musik -= 1 # Tar bort 1 från Musik eftersom att vi kör en fråga
                Title = "Music" # Vår rubrik, snygg ui
                ShowFråga(Musik, Film, Historia, Teknik, Sport, ActiveDel, Rounds, Url, var, Title) # Anropas för att printa fråga
            else:
                SlutPåFrågor(ActiveDel, Rounds, Musik, Film, Historia, Teknik, Sport) # Anropas när dessa frågor är slut

        elif Choice.lower() == "sports": # Om deltagaren väljer sport
            
            if Sport >= 0: # Medan vi har sportfrågor
                Rounds-=1 # Tar bort en "runda" för att veta att vi kört en gång
                Url = (requests.get("https://opentdb.com/api.php?amount=3&category=21&type=multiple")).json() # Url blir sport
                var = Sport # Vi sätter en allmän variabel som har värdet av Sport
                Sport -= 1 # Tar bort 1 från Sport eftersom att vi kör en fråga
                Title = "Sports " # Vår rubrik, snygg ui
                ShowFråga(Musik, Film, Historia, Teknik, Sport, ActiveDel, Rounds, Url, var, Title) # Anropas för att printa fråga
            else:
                SlutPåFrågor(ActiveDel, Rounds, Musik, Film, Historia, Teknik, Sport) # Anropas när dessa frågor är slut

        elif Choice.lower() == "computers": # Om deltagaren väljer teknik
    
            if Teknik >= 0: # Medan vi har teknikfrågor
                Rounds-=1 # Tar bort en "runda" för att veta att vi kört en gång
                Url = (requests.get("https://opentdb.com/api.php?amount=3&category=18&type=multiple")).json() # Url blir teknik
                var = Teknik # Vi sätter en allmän variabel som har värdet av Teknik
                Teknik -= 1 # Tar bort 1 från Teknik eftersom att vi kör en fråga
                Title = "Computers" # Vår rubrik, snygg ui
                ShowFråga(Musik, Film, Historia, Teknik, Sport, ActiveDel, Rounds, Url, var, Title) # Anropas för att printa fråga
            else:
                SlutPåFrågor(ActiveDel, Rounds, Musik, Film, Historia, Teknik, Sport) # Anropas när dessa frågor är slut

        elif Choice.lower() == "history": # Om deltagaren väljer historia
             
            if Historia >= 0: # Medan vi har historiefrågor
                Rounds-=1 # Tar bort en "runda" för att veta att vi kört en gång
                Url = (requests.get("https://opentdb.com/api.php?amount=3&category=23&type=multiple")).json() # Url blir historia
                var = Historia # Vi sätter en allmän variabel som har värdet av Historia
                Historia -= 1 # Tar bort 1 från Historia eftersom att vi kör en fråga
                Title = "History" # Vår rubrik, snygg ui
                ShowFråga(Musik, Film, Historia, Teknik, Sport, ActiveDel, Rounds, Url, var, Title) # Anropas för att printa fråga
            else:
                SlutPåFrågor(ActiveDel, Rounds, Musik, Film, Historia, Teknik, Sport) # Anropas när dessa frågor är slut

        elif Choice.lower() == "film": # Om deltagaren väljer film
             
            if Film >= 0: # Medan vi har filmfrågor
                Rounds-=1 # Tar bort en "runda" för att veta att vi kört en gång
                Url = (requests.get("https://opentdb.com/api.php?amount=3&category=11&type=multiple")).json() # Url blir film
                var = Film # Vi sätter en allmän variabel som har värdet av Film
                Film -= 1 # Tar bort 1 från Film eftersom att vi kör en fråga
                Title = "Film " # Vår rubrik, snygg ui
                ShowFråga(Musik, Film, Historia, Teknik, Sport, ActiveDel, Rounds, Url, var, Title) # Anropas för att printa fråga
            else:
                SlutPåFrågor(ActiveDel, Rounds, Musik, Film, Historia, Teknik, Sport) # Anropas när dessa frågor är slut

        else: # Om personen stavar fel eller skriver något annat
            line(1)
            text("You must enter one of the 5 categories ") # Säger att personen måste skriva en av kategorierna
            line(1)
            time.sleep(2)
            ShowCats(ActiveDel, Rounds, Musik, Film, Historia, Teknik, Sport) # Börjar om

     # När alla 15 rundor är klara, skrivs poängen ut
    else:
        clear()
        line(4)
        text("We are out of questions") # Säger att frågorna är slut
        line(4)
        echo(del1+" got "+str(poäng[deltagare.index(del1)])+" points ") # Poäng för deltagare 1
        line(1)
        echo(del2+" got "+str(poäng[deltagare.index(del2)])+" points ") # Poäng för deltagare 2
        line(1)
        echo(del3+" got "+str(poäng[deltagare.index(del3)])+" points ") # Poäng för deltagare 3
        time.sleep(3)
        exit()

def ShowFråga(Musik, Film, Historia, Teknik, Sport, ActiveDel, Rounds, Url, var, Title):
    clear() # Rensar allt tidigare
    f = random.randint(0, var) # Väljer en siffra mellan 0-4, denna representerar vilken fråga vi ska printa (av 5 frågor)
    line(4)
    text(Title) # Skriver ut vår rubrik
    line(4)
    echo(escape(Url['results'][f]['question'])) # Beroende på url:en så printar vi en av de 3 frågorna i den
    total = [Url['results'][f]['incorrect_answers'][0], Url['results'][f]['incorrect_answers'][1], Url['results'][f]['correct_answer']]
    # Total är en array med alla våra alternativ, vi tar in 2 felaktiga svar och det korrekta för att använda dessa som alternativ
    # f sätts in för att skriva ut alla alternativ på samma frågo medan 0 och 1 är för att skriva ut det första och andra fel svar
    arrange = random.sample(total, len(total)) # Istället för att arangera alla värden och skriva ut ett kastar vi om alla värden
    # arrange kommer vara en ny array med alternativen men i slumpad ordning
    comb = '\n'+space+"| 1: "+escape(arrange[0]),'\n'+space+"| 2: "+escape(arrange[1]),'\n'+space+"| 3: "+escape(arrange[2]) 
    # "comb" För att skriva ut alla alternativ med en siffra framför, skriver ut allting under varandra ('\n')
    # - Använder test för att lägga till mellanrum anpassat för min ui, en rad/alternativ
    echo(' '.join(map(str, comb))) # Skirva ut det snyggt
    line(1)                                                   
    Svar = int(input("                             | Answer > ")) # Deltagarens svar
    line(1)
    if Svar == str((arrange.index(Url['results'][f]['correct_answer']))+1): # Om svaret skulle ha värdet av svarets placering i den slumpade
        # -arrayn arrange kommer vi att ha svaret. Men alternativet är alltid 1 större än värdet i en array därför +1. String(str) för att känna av bokstäver
        echo("You were right "+ActiveDel) # Meddalar om rätt
        poäng[deltagare.index(ActiveDel)] += 1 # Tar värdet av deltagarens namn i array deltagare och lägger in det i poäng och lägger
        # -till 1 poäng
        echo(ActiveDel+" has "+str(poäng[deltagare.index(ActiveDel)])+" points right now") # Meddelar om antal rätt just nu
        del Url['results'][f] # Raderar frågan från url:en
        line(5)
        time.sleep(2)
        ShowCats(ActiveDel, Rounds, Musik, Film, Historia, Teknik, Sport) # Samma deltagare får välja ny kategori
    else: # Om svaret är fel
        echo("You were wrong. The correct answer was "+Url['results'][f]['correct_answer']) # Meddela att det var fel
        del Url['results'][f] # Raderar frågan från url:en
        time.sleep(2)
        OnpressShow(ActiveDel, Rounds, Musik, Film, Historia, Teknik, Sport) # Ny deltagare får väljas vi knapptryckning (alla är med)

def OnpressShow(ActiveDel, Rounds, Musik, Film, Historia, Teknik, Sport):
    clear()
    line(1)
    text("Press your button first to pick a new category ")
    line(1)
    knapp = msvcrt.getch().decode('utf-8') # För att känna 1 knapp, utf-8 = vilken knapp/tecken som helst 
    if knapp == "a": # Deltagare 1 knapp
        echo(del1+" was first")
        ActiveDel = del1 # Ändra den aktiva deltagaren
        time.sleep(2)
        ShowCats(ActiveDel, Rounds, Musik, Film, Historia, Teknik, Sport) # Ny deltagare får välja kategori
    elif knapp == "g": # Deltagare 2 knapp
        echo(del2+" was first")
        ActiveDel = del2 # Ändra den aktiva deltagaren
        time.sleep(2)
        ShowCats(ActiveDel, Rounds, Musik, Film, Historia, Teknik, Sport) # Samma
    elif knapp == "l": # Deltagare 3 knapp
        echo(del3+" was first")
        ActiveDel = del3 # Ändra den aktiva deltagaren
        time.sleep(2)
        ShowCats(ActiveDel, Rounds, Musik, Film, Historia, Teknik, Sport) # Samma
    else:
        line(1)
        text("One of you pressed the wrong key, let's start over ") # Meddelar att nån tryckte på fel knapp
        line(1)
        time.sleep(2)
        OnpressShow(ActiveDel, Rounds, Musik, Film, Historia, Teknik, Sport) # Startar om
        
def SlutPåFrågor(ActiveDel, Rounds, Musik, Film, Historia, Teknik, Sport): # FUnktion för när frågorna är slut
    clear()
    line(4)
    text("Questions for this category are out, choose a new one") # Meddelar deltagaren om frågorna är slut
    line(4) 
    time.sleep(2)
    ShowCats(ActiveDel, Rounds, Musik, Film, Historia, Teknik, Sport) # Får välja en ny kategori   
ShowCats(ActiveDel, Rounds, Musik, Film, Historia, Teknik, Sport) # Anropar funktionen, startar allt