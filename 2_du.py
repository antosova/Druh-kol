import csv
import copy
import sys

suma_tyden = 0
suma_rok = 0
pocitadlo_radku = 1
radek = [] 
minimum = sys.float_info.max
maximum = sys.float_info.min

novy_rok = False
stary_rok = 0
pocitadlo_dnu_v_roku = 1

f = open('out_tydenni.csv', 'w',newline='')                             # Vytvoření csv výstupu se sedmidenními průtoky řeky
writer_tydenni = csv.writer(f)

try:                                                                       
	with open("Data_prutok.csv", encoding="utf-8", newline='') as f:     
		reader = csv.reader(f, delimiter=",")
		for row in reader:
			if pocitadlo_radku % 7 == 1:                                # Zápis řádku prvního dne v týdnu do proměnné radek 
				radek = copy.deepcopy(row)
			if pocitadlo_radku % 7 == 0:
				radek[3] = round(suma_tyden/7,4)						# Zapis průměrného průtoku do proměnné radek
				writer_tydenni.writerow(radek)                          # Zápis proměnné radek do csv souboru
				suma_tyden = 0
			if float(row[3]) < 0:
				print("Data obsahují zápornou hodnotu průtoku.")
				sys.exit()
			suma_tyden += float(row[3])
			if float(row[3]) > maximum:
				maximum = float(row[3])
				maxDen = copy.deepcopy(row)
			if float(row[3]) < minimum:
				minimum = float(row[3])	
				minDen = copy.deepcopy(row)		
			pocitadlo_radku+=1

	if pocitadlo_radku % 7 != 0:                                        # Poslední průměr program spočítá z tolika dat, kolik je k dispozici
		radek[3] = round(suma_tyden/(pocitadlo_radku % 7),4)
		writer_tydenni.writerow(radek)

	f.close()


	with open("Data_prutok.csv", encoding="utf-8", newline='') as f:    # řádky 48 - 53 - slouží ke zjištění, kterým rokem začíná dataset
		reader = csv.reader(f, delimiter=",")
		for row in reader:												
			stary_rok = int(row[2].split(".")[2])
			radek = copy.deepcopy(row)
			break

	f = open('out_rocni.csv', 'w',newline='')							# Vytvoření csv výstupu se ročními průtoky řeky
	writer_rok = csv.writer(f)

	with open("Data_prutok.csv", encoding="utf-8", newline='') as f:
		reader = csv.reader(f, delimiter=",")
		for row in reader:
			rok = int(row[2].split(".")[2])
			if stary_rok == rok: 
				novy_rok = False
			else: 
				novy_rok = True
			if novy_rok == True:                                        # Jestliže se změní rok v datech zapíše se řádek do csv souboru
				radek[3] = round(suma_rok/pocitadlo_dnu_v_roku,4)
				pocitadlo_dnu_v_roku = 0
				suma_rok = 0
				stary_rok = rok
				writer_rok.writerow(radek)
				radek = copy.deepcopy(row)
			suma_rok += float(row[3])
			pocitadlo_dnu_v_roku += 1

	radek[3] = round(suma_rok/pocitadlo_dnu_v_roku,4)                   # Zapsání posledního roku v datasetu
	writer_rok.writerow(radek)

	f.close()

except FileNotFoundError:                                               
	print("Soubor není.")
except: 
	print("Něco se šíleně pokazilo.")

print ("Minimální průtok byl dne " + str(minDen[2]) + ". Hodnota průtoku byla" + str(minDen[3]))
print ("Maximální průtok byl dne " + str(maxDen[2]) + ". Hodnota průtoku byla" + str(maxDen[3]))
