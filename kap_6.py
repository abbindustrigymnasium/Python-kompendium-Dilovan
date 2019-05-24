import requests

# 6.1
# i = str(input("nummer")) # ber om ett nummer
# url = "http://77.238.56.27/examples/numinfo/?integer=" + i # lägger till nummret till api:n
# r = requests.get(url) # hämtar den slutgiltiga url med siffran
# hej = r.json() # får in dictonary värdet
# print(hej) # skriver ut resultatet och informationen

# 6.2
# praktiskt taget som 6.1 fast nu bet din star och skriver ut vädret för ditt område
# q = str(input("stad"))
# url = "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/" + q
# p = requests.get(url)
# ge = p.json()
# print(ge)

# 6.3
# url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" # url för artist databasen
# q = requests.get(url) # hämtar url

# svar = q.json() # ger samma som i uppgifterna ovan
# print("Dessa artister finns:") # skriver ut artister
# print() # space

# for artist in svar["artists"]: # kommer skriva ut alla namn från listan artister med en for loop
#     print(artist["name"]) # skriver ut här

# svar = svar["artists"] # svaret är alla artister
# print() # space
# art = str(input("Välj artist ")) # ber om en artist

# for artister in svar:  # tar fram alla artister
#     if artister["name"] == art: # matchar de med din artist
#         url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" + artister["id"] # nytt url matchar din artist med deras id
#         q = requests.get(url) 
#         svar = q.json() 
#         print(svar) # skriver ut infon om artisten du vill