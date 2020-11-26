# Stara wersja programu z zadania 1.3

print("##### STARA WERSJA - program z zadania 1.3 #####\n")
productsList = ["roquefort", "stilton", "brie", "gouda", "edam", "parmezan", "mozzarella", "czechosłowacki ser z owczego mleka", "listek miętowy"]

pricesList = ["12.5", "11.24", "9.30", "8.55", "11", "16.5", "14", "122.32", "20"]

weightList = ["2", "1", "1", "1", "1", "3.5", "0.13", "0.22", "0.20"]

purchaseValue = 0

print("LISTA ZAKUPOW:")
print("\n")

if len(productsList) == len(pricesList) and len(productsList) == len(weightList):
  for i in range(len(pricesList)):
    printOutput = f"{productsList[i]:<35} {float(weightList[i]):^10.2f} kg {float(pricesList[i]):>10.2f} PLN"
    purchaseValue += float(pricesList[i])
    print(printOutput)
else:
  print("Zle zrobilem liste...")

print(f"\nRAZEM: {purchaseValue} PLN")

print("TO BEDZIE KOLEJNY COMMIT NA GIT!")

print("I NASTEPNY COMMIT!")

print("POGUBILEM SIE Z LICZBA COMMITOW! :)")

print("TERAZ NOWY BRANCH!")



