#Programm:       Übungsaufgabe zweiseitige Verzweigung
#Author:         J. Schmülling
#Änderungsdatum: 03.02.2025

grenzbetrag = 100000
niedrige_provision = 0.05
hohe_provision = 0.075

def calc():
    while True:
        try:
            umsatz = float(input(f"{'Umsatz eingeben:':<35}"))

            if umsatz >= grenzbetrag:
                provision = umsatz * hohe_provision
            else:
                provision = umsatz * niedrige_provision
            print("-"*50)
            print(f"{'Die Umsatzprovision beträgt: ':<35}{provision:.2f} EUR")
            return
        except ValueError:
            print("Nur Zahlen erlaubt!")

calc()