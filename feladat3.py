#Kérjünk be 5 db egész számot és írjuk ki, hogy a szám pozitív vagy negatív.
for x in range(1,6,1):
    szam = int(input("Kérem a számot"))
    if szam > 0:
        print("pozitiv")
    else:
        print("negativ")