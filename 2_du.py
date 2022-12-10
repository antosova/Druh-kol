import csv

"""# Otevřeme a přečteme soubor Data_prutok.csv
with open("Data_prutok.csv", encoding="utf-8", newline='') as f:
	reader = csv.reader(f, delimiter=",")
	for row in reader:
		print(row)
with open("Data_prutok.csv", encoding="utf-8", newline='') as f:
	reader = csv.reader(f, delimiter=",")
	for row in range(7):
		(prutoky) = (next(reader)[3])
		print (prutoky)
prutoky_list = []
prutoky_list.append(prutoky)
print(prutoky_list)
#def průměr_7(součet_průtoků, pocet_prutoků):"""

suma_tyden = 0
suma_rok = 0
pocitadlo_radku = 1

with open("Data_prutok.csv", encoding="utf-8", newline='') as f:
	reader = csv.reader(f, delimiter=",")
	for row in reader:
		suma_tyden += float(row[3])
		if pocitadlo_radku % 7 == 0:
			suma_tyden = round(suma_tyden/7,4)
			print (suma_tyden)
			suma_tyden = 0
		pocitadlo_radku+=1

novy_rok = False
stary_rok = 0
pocitadlo_dnu_v_roku = 0
radek = []

with open("Data_prutok.csv", encoding="utf-8", newline='') as f:
	reader = csv.reader(f, delimiter=",")
	for row in reader:
		stary_rok = int(row[2].split(".")[2])
		radek = row
		break



print("průmery za rok:")
with open("Data_prutok.csv", encoding="utf-8", newline='') as f:
	reader = csv.reader(f, delimiter=",")
	for row in reader:
		rok = int(row[2].split(".")[2])
		pocitadlo_dnu_v_roku += 1
		if stary_rok == rok: 
			novy_rok = False
		else: 
			novy_rok = True
		if novy_rok == True:
			radek = row
			radek[3] = round(suma_rok/pocitadlo_dnu_v_roku,4)
			pocitadlo_dnu_v_roku = 0
			suma_rok = 0
			stary_rok = rok
			print(radek)
		suma_rok += float(row[3])

radek[3] = round(suma_rok/pocitadlo_dnu_v_roku,4)
print (radek)
"""Otevřeme si soubor `parkoviste.csv` pro čtení a `pr.csv` pro zápis (parametr `"w"`)
# \ na konci prvního řádku je proto, aby šel druhý open napsat na nový řádek
with open("parkoviste.csv", encoding="utf-8", newline='') as f, \
	open("pr.csv","w",encoding="utf-8", newline='') as fout:
	reader = csv.reader(f, delimiter=";")
	next(reader)
	# Vytvoříme si zapisovací objekt pro CSV nad výstpním souborem
	writer = csv.writer(fout)
	for row in reader:
		# Pokud sloupec pr neobsahuje `true` libovolně velkými písmeny, řádek přeskočíme
		if row[3].lower() != 'true':
			continue
		#writer.writerow([row[0],row[-1]]) # Ekvivalentní s řádky níže
		# Z načteného řádku vyextrahujeme jméno a kapacitu
		name = row[0]
		capa = row[-1]
		# Vytvoříme si výstupní řádek jako seznam sloupců
		outrow = [name, capa]
		# Zapíšeme řádek do výstupního souboru
		writer.writerow(outrow)"""