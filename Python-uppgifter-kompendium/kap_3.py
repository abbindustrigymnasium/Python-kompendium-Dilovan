# ska alltid stå kvar
man = ["Erik", "Lars", "Karl", "Anders", "Johan"]
kvinna =["Maria", "Anna", "Lina", "Bla", "?"]

# 3.1
# skriver ut första värdet från man, 3:e från kvinna, 5:e från kvinna och andra för man
# print(man[0],",", kvinna[2],",", kvinna[4],",", man[1]) 


# 3.2
# print(man, ",", kvinna) # skriver ut alla mans och kvinnonamn
# del man[1] # tar bort andra värdet från man
# del man[2] # tar bort tredje värdet från man
# del kvinna[0] # tar bort första värdet från kvinna
# print(man, ",", kvinna) # skriver återigen ut alla kvinno och mans namn


# 3.3
# print(man,",",kvinna) # skriver ut alla mans och kvinnonamn
# man.append("Dilovan") # lägger till mitt namn bland männens
# print(man,",",kvinna) # skriver återigen ut männens och kvinnornas namn, nu med mitt bland männen


# 3.4
# man.sort() # sorterar männens namn i bokstavsordning
# kvinna.sort() # samma med kvinnorna
# print(man,",",kvinna) # skriver ut alla kvinno och mans namn fast i storleksordning nu


# 3.5
# Btw var ganska lat här, orkade inte gör det bra
# print(man) # skriver alla mans namn
# print(kvinna) # skriver alla kvinnonamn
# print() # space
# print("Skriv namnet du vill ta bort") # ber användaren ta bort ett namn
# a = int(input("För män, skriv som ett nummer, 0-4")) # beskrivning för männen
# b = int(input("För kvinnor, skriv som ett nummer, 0-4")) # beskrivning för kvinnor
# del man[a] # tar bort värdet från männen
# del kvinna[b] # samma fast med kvinnor
# print(man,",",kvinna) # skriver ut alla namn