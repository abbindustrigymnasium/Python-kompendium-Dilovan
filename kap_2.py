# 2.1
# citat = "datatyper har inbyggda metoder" # vår quote
# print(citat.upper()) # Skriver ut det med bara stora bokstäver .upper()


# 2.2
# a = float(input("ange ett decimaltal")) # float, för att känna av ett decital
# b = round(a) # avrundar talet du skrivit in
# print("ditt tal avrundades till", b) # presenterar det för användaren


# 2.3
# a = input("förnamn?") # ber om förnamn från användare
# b = input("efternamn?") # ber om efternamn från användare
# print("Hejsan", a, b) # hälsar på användaren genom att använda inputs från punkt 1 & 2


# 2.4
# a = int(input("ålder?")) # ber om användarens ålder, en siffra
# b = int(18) # bestämmer siffran 18 till variabeln b
# c = b-a # tar alltid bort användarens ålder från 18
# if a>=b: # om användarens ålder är mer än 18
#     print("du är myndig") # skriv att hen är myndig
# else:
#     print("du är myndig om", c, "år") # skriv annars skillnaden mellan användarens ålder och 18


# 2.5
# import math # ett annat sätt att räkna/avrunda siffror så att de alltid går uppåt

# x = int(input("hur många elever finns det?")) # ber om antal elever som finns
# a = int(input("hur många vill äta 2st vanliga korvar?")) # vill veta hur många som äter 2 vanliga
# b = int(input("hur många vill äta 3st vanliga korvar?")) # vill veta hur många som äter 3 vanliga
# c = int(input("hur många vill äta 2st veganska korvar?")) # vill veta hur många som äter 2 ovanliga
# d = int(input("hur många vill äta 3st veganska korvar?")) # vill veta hur många som äter 3 ovanliga

# vankorv = int((a*2)+(b*3)) # räknar ut antalet vanliga korvar
# vegkorv = int((c*2)+(d*3)) # räknar ut antalet ovanliga korvar

# vanlig_förp = math.ceil(vankorv/8) # det går 8 vanliga/förpackning, avrundar antal pack uppåt
# vegansk_förp = math.ceil(vegkorv/4) # det går 4 ovanliga/förpackning, avrundar antalet pack uppåt
# läsk = int(x) # läsk är samma som antal elever, läsk/elev

# van_pris = math.ceil(vanlig_förp*20.95) # avrundar priset för vanliga förpackningar uppåt
# veg_pris = math.ceil(vegansk_förp*34.95) # avrundar priset för veganska förpackningar uppåt
# läsk_pris = math.ceil(x*13.95) # avrundar priset för läsk uppåt
# tot_pris = läsk_pris+van_pris+veg_pris # totala priset är förpackningar + läsk

# # presenterar allt för användaren
# print(vanlig_förp, "st förpackningar med vanlig korv köps in, kostnaden blir", van_pris, "kr")
# print(vegansk_förp, "st förpackningar med vegansk korv köps in, kostnaden blir", veg_pris, "kr")
# print(läsk, "st läsk köps in, kostnaden blir", läsk_pris, "kr")
# print("totalkostnaden blir ca", tot_pris,"kr")