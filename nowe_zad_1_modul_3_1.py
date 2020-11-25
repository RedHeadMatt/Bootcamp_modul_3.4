# Nowa wersja z zadania 1 z modułu 3.1

print("\n\n##### NOWA WERSJA WERSJA - zad 1 z modułu 3.1 #####\n")

counter = 0

shoppingListDict = {"piekarnia": ["chleb", "bułki", "pączek"], "warzywniak":["marchew", "seler", "rukola"]}

shoppingListCapit = {key: [word.capitalize() for word in shoppingListDict[key] ] for key in shoppingListDict }

for key, value in shoppingListCapit.items():
    print(f"Ide do {key.capitalize()} i kupuje {value}")
    counter = counter + len(value)

print(f"\nW sumie kupuje {counter} produktow")




