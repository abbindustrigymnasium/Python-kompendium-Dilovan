# 4.1
# a = range(1000001) # hämtar alla värden från 0-1000000
# print(sum(a)) # adderar alla dessa och skriver ut det


# 4.2
# b = list(range(1,500,2)) # hämtar alla udda tal, börjar med 1 och går upp 2 per gång så nästa blir 3 osv till 500
# print(sum(b)) # adderar alla dessa udda tal


# 4.3
# regi = ["Anna", "Eva", "Erik", "Lars", "Karl"] # de registrerade
# avanm = ["Anna", "Erik", "Karl"] # de avanmälda
# for delete in avanm:     # kallar de avanmälda för deleter
#     regi.remove(delete)  #tar bort de avanmälda från registrerade 
# print(regi) # skriver ut resultatet


# 4.4
# förnamn =[" Maria ", " Erik ", " Karl "] # alla förnamn
# efternamn =[" Svensson ", " Karlsson ", " Andersson "] # alla efternamn
# for fö in förnamn:      #kallar alla förnamn fö
#     for ef in efternamn: # alla efternamn för ef
#         print(fö + ef) # skriver ut alla kombinationer man kan och matchar allt, skriver ut detta också