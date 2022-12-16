# szoveg = "ezegyszöveg"
# if "v" in szoveg:
#     print("benne van")
# else: print("nincs benne")

# szoveg = "ezegyszöveg"
# beker = input("Kérem a betűt!")
# if beker in szoveg:
#     print(f"{beker} betü benne van a szövegben")
# else: print(f"{beker} betü nincs benne  a szövegben")



# szoveg = "KEDD"
# print(szoveg.lower())



# hetnapjai =["hétfő","kedd","szerda","csütörtök","péntek","szombat","vasárnap"]

# beker = input("Kérem a napot!").lower()

# if beker in hetnapjai:
#     print(f"{beker} nap benne van a listában")
# else:
#     print(f"{beker} nap nincs a listában")


focistak =["Ronaldo","Messi","Benzema","Salah","Veratti","Rashford","Ramos"]

focistak_kisbetu = [item.lower() for item in focistak]
focistak_nagybetu = [item.upper() for item in focistak]

beker = input("Kérem a focistát!").upper()

if beker in focistak:
     print(f"{beker} focista benne van a csapatban")
else:
     print(f"{beker} focista nincs benne a csapatban")






