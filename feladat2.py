#2, Kérünk be a felhasználótól 5 db egész számot és írjuk ki azokat amelyek 2 vel és 3al oszthatóak.
for x in range(1,6,1):
    szam = int(input("Adj meg egy számot: "))
    if szam %2 ==0 and szam %3 ==0:
        print("Osztható")
    else:
        print("Nem osztható")