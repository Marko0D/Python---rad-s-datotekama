radi=True
while radi==True:
    print("---Jednostavna Bilježnica---")
    print("1. Dodaj novu bilješku")
    print("2. Pregledaj sve bilješke")
    print("3. Izlaz")
    print("Odaberite opciju (1-3)")
    unos=int(input())
    if unos==1:
        a=input("Unesi tekst koji želiš dodati u bilježnicu:")
        with open("biljeznica.txt", "a") as datoteka:
                datoteka.write(a)
                datoteka.write("\n")
                datoteka.close()
                print("Bilješka je uspješno spremljena!")
    elif unos==2:
        with open("biljeznica.txt", "r") as datoteka:
                sadrzaj = datoteka.read()
                if not sadrzaj.strip():
                    print("Datoteka ne sadrži bilješke!")
                    datoteka.close()
                else:
                    print(sadrzaj)
                    datoteka.close()
    elif unos==3:
            radi=False
            print("Doviđenja!")
