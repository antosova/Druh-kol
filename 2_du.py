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
rok = 1
with open("Data_prutok.csv", encoding="utf-8", newline='') as f:
	reader = csv.reader(f, delimiter=",")
	for row in reader:
		suma_tyden += float(row[3])
		if pocitadlo_radku % 7 == 0:
			suma_tyden = round(suma_tyden/7,4)
			print (suma_tyden)
			suma_tyden = 0
		pocitadlo_radku+=1

print("průmery za rok:")
with open("Data_prutok.csv", encoding="utf-8", newline='') as f:
	reader = csv.reader(f, delimiter=",")
	for row in reader:
		suma_rok += float(row[3])
		if rok % 4 == 1:
			if pocitadlo_radku % 366 == 0:
				suma_rok = round(suma_rok/366,4)
				print (suma_rok)
				suma_rok = 0
				rok+=1
		if pocitadlo_radku % 365 == 0:
				suma_rok = round(suma_rok/365,4)
				print (suma_rok)
				suma_rok = 0
				rok+=1
		pocitadlo_radku+=1
   
