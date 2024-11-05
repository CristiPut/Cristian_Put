import random
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]
litere_incercate = []


incercari_ramase = 6

print("servus, ai intrat in jocul spanzuratoarea")
print("cuvantul pe care trebuie sa-l ghicesti: " + " ".join(progres))
print(f"incercari ramase: {incercari_ramase}\n")


while incercari_ramase > 0 and "_" in progres:
    litera = input("introdu o litera: ").lower()


    if len(litera) != 1 or not litera.isalpha():
        print("Eroare: introdu o singura litera")
        continue


    if litera in litere_incercate:
        print("ai folosit aceeasi litera, foloseste alta litera")
        continue


    litere_incercate.append(litera)


    if litera in cuvant_de_ghicit:
        for index, caracter in enumerate(cuvant_de_ghicit):
            if caracter == litera:
                progres[index] = litera
        print("bravo, ai ghicit o litera!")
    else:
        incercari_ramase -= 1
        print(f"litera '{litera}' nu se regaseste in aceest cuvant. incercari ramase: {incercari_ramase}")


    print("Progres: " + " ".join(progres))
    print()


if "_" not in progres:
    print(f"bravo, ai nimerit cuvantul: '{cuvant_de_ghicit}'!")
else:
    print(f"ai pierdut jocul, cuvantul necunoscut era: '{cuvant_de_ghicit}'.")
