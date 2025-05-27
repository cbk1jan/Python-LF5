#Programm:       Übungsaufgabe kopfgesteuerte Schleifen
#Author:         J. Schmülling
#Änderungsdatum: 01.04.2025

einlage = 1

while einlage > 0:
    print("O N E  M I L L I O N")
    print("-"*50)
    try:
        einlage = float(input("Anlagebetrag in EUR: "))
        zinssatz = float(input("Verzinsung in %: "))

        if einlage > 0:
            if zinssatz > 0:
                kontostand = einlage
                jahr = 1
                while kontostand < 1000000:
                    kontostand = kontostand + (kontostand * zinssatz/100)
                    print(f"Nach dem {jahr} Jahr: - {kontostand:>15.2f} EUR")
                    jahr = jahr + 1
            else:
                print("Zinssatz muss über 0 sein")
                print("-"*50)
        else:
            print("Einlage muss über 0 sein")
            print("-"*50)
    except ValueError:
        print("Falsche Eingabe. Nur positive zahlen und keine Buchstaben")
        print("-"*50)