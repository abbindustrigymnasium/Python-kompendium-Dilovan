# 8.1
# print("Ange först en distans i siffror sedan prefix, 'km' eller 'miles' ") # meddelande till användare
# print()
# dist = int(input("Ange distans ")) # ber om en distans
# pre = input("Ange prefix ") #  ber om prefix, km eller miles

# def km_to_miles(dist, pre):
#     a = dist*0.621371192 # multiplicerar med detta om km
#     print(dist, pre, "är ungefär", a, "miles") # skriver ut det

# def miles_to_km(dist, pre):
#     a = dist*1.609344 # multiplicerar med detta om miles
#     print(dist, pre, "är ungefär", a, "km") # skriver ut det

# if pre.lower() == "km": # om ditt prefix är km vill gör göra det till miles
#     km_to_miles(dist, pre) 

# elif pre.lower() == "miles": # samma fast tvärtom
#     miles_to_km(dist, pre)
    
# else:
#     print("Du måste skriva 'km' eller 'miles' som prefix") # säger att du endast får skriva miles eller km som prefix


# 8.2
# import requests # för url,  dictonarys
# url = input("Skriv url ") # ber dig mata in ett url
# def get(url): # behövs egentligen inte funktion men det var uppgiften
#     b = requests.get(url) # fixar till url:en som i kap 6
#     c = b.json()
#     print(c) # skriver ut det som dictonary med alla information
# get(url) # anropar funktionen


# Hör ihop med 8.3 och 8.4
# import os # för att fixa i terminalen

# def line(dots=False): # sätter det till falskt från börjarn
#     if dots==False:
#         print("--------------------------------") # skriver ut detta om falskt
#     else:
#         print("********************************") # annars detta

# def header(text): # hämtar tesxt från användaren
#     mellanrumm=""
#     längd=((30-len(text))/2)-1 # längden av texten för att centrera det, -1 för att göra det i mitten
#     while längd >= 0: # medan det är > 0 lägger vi på mellanrum till vi kommer till texten
#         mellanrumm+=" "
#         längd-=1 # gör detta tills mellanrummet blir lika långt som längd
#         header="|"+mellanrumm+text+mellanrumm+"|" # skriver ut våra mellanrum tillsammans med text mellan
#     print(header) # skriver ut detta

# def echo(text):
#     print("| "+text) # sätter bara ett tecken framför text

# def prompt(text):
#     str(input("| "+text+" >")) # gör vår text till en input

# def clear():
#     os.system('cls') # rensar hela terminalen från text med os


# 8.3
# # skriver bara ut allt snyggt
# line()
# header("EXEMPEL")
# line(True)
# echo("dett är ett exempel på hur")
# echo("Ett gränssnitt kan se ut")
# line()
# header("vad vill du göra")
# line()
# echo("A | visa bla")
# echo("B | döda")
# echo("C | äta")
# echo("D | orkar inte skriva av")
# line()
# prompt("Val")


# 8.4
# vi hämtar basically kod från 6.3 men gör det snyggt
# import requests
# url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
# r = requests.get(url)
# svar = r.json()

# def promppt(text):
#     url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" # url för artister
#     r = requests.get(url)
#     svar = r.json()
#     svar = svar["artists"] # alla artister
#     art = str(input("Selection > ")) # ber dig välja artist 
#     for artister in svar:
#         if artister["name"] == art: # samma sak som i 6.3 vi matchar din artist med hens id och skriver ut info 
#             url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" + artister["id"]
#             r = requests.get(url)
#             svar = r.json()
#             print(svar)

# def start(): # skriver ut saker snyggt, fin startsida
#     line()
#     header("ARTIST DATABASE")
#     line()
#     echo("Welcome to a world of Music!")
#     line()
#     echo("L | List artists")
#     echo("V | View artist profile")
#     echo("E | Exit application")
#     line()
#     prompppt("Selection > ") # ditt val

# def prompppt(text):
#     val = (input("| "+text))

#     if val.lower() == "l": # om du väljer L
#         clear()
#         line()
#         header("ARTIST DATABASE")
#         line()
#         for artist in svar["artists"]: # skriver ut alla artister
#             echo(artist["name"])
#         line()
#         echo("L | List artists")
#         echo("V | View artist profile")
#         echo("E | Exit application")
#         line()
#         prompppt("Selection ") # låter dig välja något nytt

#     elif val.lower() == "v": # om V 
#         clear()
#         line()
#         header("ARTIST DATABASE")
#         line()
#         for artist in svar["artists"]: # skriver ut alla artister
#             echo(artist["name"])
#         line()
#         echo("Choose artist")
#         line()
#         promppt("Selection ") # låter dig välja en artist och visar hens information i funktionen inann start()

#     elif val.lower() == "e": # om e
#         clear()
#         line(True)
#         header("Good bye") # säger hejdå
#         line(True)

#     else: # om du inte förstår något
#         clear() # rensa allt
#         line(True)
#         echo("You have to write 'L','V' or 'E'") # säg till personen vad hen ska göra
#         start() # gå tillbaks till start
# start() # anropar startsidan
# 0706341144-jocke