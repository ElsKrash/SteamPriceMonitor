def vypocitej_prumer(seznam):
    soucet = 0
    neplatny = 0

    for prvek in seznam:
        try:
            soucet += int(prvek)
        except ValueError:
            neplatny += 1
            pass

    try:
        prumer = soucet / (len(seznam) - neplatny)
        return prumer
    except ZeroDivisionError:
        print("Nebyl zadán žádný platný údaj o síle bojovníků.")
    

def nacti_silu():
    seznam = []

    while True:
        prvek = input("Zadejte sílu bojovníka (pro ukončení zmáčkněte enter): ")
        if prvek == "":
            return seznam
        seznam.append(prvek)

while True:
    try:
        prumerna_sila_utocnika = int(input("Zadejte průměrnou sílu útočníka z nepřátelské armády: "))
        break
    except ValueError:
        continue
bojovnici = nacti_silu()
prumerna_sila = vypocitej_prumer(bojovnici)

if prumerna_sila == None:
    print("Nebyl zadán žádný platný údaj o síle bojovníků.")
else:
    print("Průměrná síla tvých bojovníků:", prumerna_sila)
    print("Průměrná síla nepřátel:", prumerna_sila_utocnika)
    
    if prumerna_sila >= prumerna_sila_utocnika:
        print("Gratuluji! Tvá skupina má možnost vyhrát bitvu!")
    else:
        print("Raději své bojovníky stáhni a povolej posily.")
