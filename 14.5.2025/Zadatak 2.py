with open("Rezultat.txt", "w") as datoteka:
    datoteka.write("Ovo je prvi redak teksta.\n")
    datoteka.write("Ovo je drugi redak teksta.\n")
    datoteka.write("Ovo je treći redak teksta.\n")
with open("Rezultat.txt", "a") as datoteka:
    datoteka.write("Ovo je četvrti redak teksta.\n")
    datoteka.write("Ovo je peti redak teksta.\n")

