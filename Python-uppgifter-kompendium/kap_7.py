# 7.1
# a = int(input("ange multiplikationstabell")) # ber om multitabell 
# num = 1 # vårt första värde i multitabellen
# c = 4 # antal gånge (-1) som tabellen körs

# while num < c: # medan vårt första värde är mindre än antal gånge vi kör
#     b = a*num # # kommer vi multiplicera ditt tal med första värdet
#     num += 1 # sedan addera standardtalet med 1
#     print(b) # skriver ut alla värden vi får
#     if num == c: # fortsätter så till vårt startvärde körts 3 ggr
#         e = input("fortsätt?") # ber om fortsättning eller inte
#         if e.lower() =="ja": # om ja, fortsätt med while loopen genom att lägga till 3 omgångar till
#             c += 3
#         elif e.lower() =="nej": # stänger av vid nej

# 7.2
# import random # för att slumpa värde
# a = random.randint(0,99) # slumpar värde mellan 0 och 99
# b = int(input("Guess")) # ber dig gissa
# c = 0 # våra försök

# while a > b: # medan din gissning är mindre än talet
#     print("Higher") # ber dig säga något högre
#     b = int(input("Guess")) # gissa igen
#     c += 1 # lägg till ett försök på dig

#     while a < b: # blir det lägre nästa gång gör tvärtom
#         print("Lower")
#         b = int(input("Guess"))
#         c += 1 # lägg till et försök på dig

# while a < b: # samma sak som innan fast inverterat för att kunna fixa alla kombinationer av gissningar för att hålla på hela tiden
#     print("Lower")
#     b = int(input("Guess"))
#     c += 1

#     while a > b:
#         print("Higher")
#         b = int(input("Guess"))
#         c += 1

# if a == b: # när du gissar rätt
#     c += 1 # lägg på ett till försök
#     print("The answer is", a,",", "it took you", c, "tries") # säg att du fick rätt efter x antal försök