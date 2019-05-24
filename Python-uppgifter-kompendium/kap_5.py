# 5.1
# # vet att jag gjorde det hårdkodat men orkade inte göra det bra, kunde ha matchar arrays
# kön = input("Kön:") # ber om kön
# hår = input("Hårfärg:") # ber om hårfärg
# ögon = input("Ögonfärg:") # ber om ögonfärg
# #hårdkodar det för att matcha med olika kändisar, tog inte med så mång
# if kön == "man": # om könet är man kollar vi sedan på hårfärg och till sist ögonfärg och mathcar utifrån det
#     if hår == "brun":
#         if ögon == "brun":
#             print("Matchar med Daniel Radcliffe") # skriver ut kändisen du matchar med

#     elif hår == "röd":
#         if ögon == "blå":
#             print("Rupert grint") # skriver ut kändisen du matchar med
    
#     elif hår == "svart":
#         if ögon == "brun":
#             print("Matchar med Josef Stalin") # skriver ut kändisen du matchar med

#     elif hår == "blond":
#         if ögon == "blå":
#             print("Matchar med Donald Trump") # skriver ut kändisen du matchar med
    
#     elif hår == "vitt":
#         if ögon == "blå":
#             print("Matchar med kungen") # skriver ut kändisen du matchar med

# elif kön == "kvinna": # om det blir kvinna istället går vi vidare på samma sätt som med männen
#     if hår == "brun":
#         if ögon == "brun":
#             print("Emma Watson och Selena Gomez") # skriver ut kändisarna du matchar med

# else:
#     print("du matchar inte med nån kändis") # skriver ut att du inte matchar med nån kändis


# 5.2
# ålder = int(input("ålder")) # ber om ålder av användaren
# söm = [14, 13, 12, 11.5, 11, 11, 10.5, 10, 10, 10, 9.5, 9, 9, 9, 9, 8.5, 8] # alla tider för alla åldrar

# if ålder > 16: # om du är över 16 gäller följande
#     print("Du är", ålder, "år och behöver därför sova i ca", söm[16], "timmar") # du kommer alltid behöva sova 8 h
# elif ålder == 0: # för att jag inte vet hur länge 0 åringar sover
#     print("gå lägg dig")
# else: # annars kommer du alltid behöva sova det vardet av array som är 1 mindre än din ålder
#     print("Du är", ålder, "år och behöver därför sova i ca", söm[ålder-1], "timmar") 


# # 5.3
# land = input("land") # ber om land från användare
# # bestämmer vilka land som är i norden, . lower() gör att man kan skriva hur man vill
# if land.lower() == "danmark" or land.lower() == "finland" or land.lower() == "sverige" or land.lower() == "norge" or land.lower() == "island":
#     print("detta land tillhör norden") # om din input tillhör någon av nordens länder skriv så
# # samma som innan fast i storbritannien
# elif land.lower() == "england" or land.lower() == "nordirland" or land.lower() == "skottland" or land.lower() == "wales":
#     print("detta land tillhör storbritanien") # skriver ut om du lever i storbritannien
# else:
#     print("detta land tillhör varken norden eller storbritanien") # om ditt land inte ligge i någon skriv så