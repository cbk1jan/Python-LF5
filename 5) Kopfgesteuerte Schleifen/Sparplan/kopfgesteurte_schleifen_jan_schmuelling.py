# Programm:       Übungsaufgabe kopfgesteuerte Schleifen
# Author:         J. Schmülling
# Änderungsdatum: 31.03.2025

kapital = 1

while kapital > 0:
    print("S P A R P L A N")
    print("-"*50)
    kapital = float(input("Bitte geben Sie Ihr Startkapital ein: "))

    if (kapital > 0):

        anlagedauer = float(input("Bitte geben Sie die Anlagedauer in Jahren ein: "))
        print("-"*50)

        if (anlagedauer <= 2):
            zinssatz = 0.028
        elif (anlagedauer <= 10):
            zinssatz = 0.038
        elif (anlagedauer > 10):
            zinssatz = 0.045
        else:
            print("Fehler")

        index = 1

        while (index <= anlagedauer):
            zinsen = kapital * zinssatz
            kapital = kapital + zinsen

            print(f"{"Jahr:" :<10} {index :<10} {" Betrag:":<10} {kapital :<10.2f}")
            index = index + 1
        print("-"*50)
    else:
        print("und tschüss...")