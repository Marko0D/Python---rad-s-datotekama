datotečni_objekt=open("Podaci.txt", "r")
with open("Podaci.txt", "r") as datoteka:
    sadrzaj = datoteka.read()
    print(sadrzaj)
with open("Podaci.txt", "r") as datoteka:
    prvi_redak = datoteka.readline()
    print(f"Prvi redak: '{prvi_redak.strip()}'")
    
with open("Podaci.txt", "r") as datoteka:
    for redak in datoteka:
        print(f"Pročitani redak: '{redak.strip()}'")
