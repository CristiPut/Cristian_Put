meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []


cate_ceafa_era_la_inceput = meniu.count("ceafa")
cata_ceafa_s_a_comandat = comenzi.count("ceafa")
pret_ceafa = preturi[1][1]
castig_ceafa = cata_ceafa_s_a_comandat * pret_ceafa
cati_papanasi_erau_la_inceput = meniu.count("papanasi")
cati_papanasi_s_au_comandat = comenzi.count("papanasi")
pret_papanasi = preturi[0][1]
castig_papanasi = cati_papanasi_erau_la_inceput * pret_papanasi
cat_gulas_era_la_inceput = meniu.count("guias")
cat_gluas_s_a_comandat = comenzi.count("guias")
pret_guias = preturi[2][1]
castig_gulas = cat_gulas_era_la_inceput * pret_guias
while studenti :
    studentul = studenti.pop(0)
    comanda = comenzi.pop(0)
    print(f" Studentul {studentul} a comandat {comanda}")
    tavi.pop()
    istoric_comenzi.append([studentul, comanda])
print(f"S-au comandat {cati_papanasi_s_au_comandat} papanasi, {cata_ceafa_s_a_comandat} ceafa, {cat_gluas_s_a_comandat} guias ")
print(f"Mai sunt {len(tavi)} tavi")