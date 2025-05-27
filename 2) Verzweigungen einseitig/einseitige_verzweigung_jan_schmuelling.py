#Programm:       Übungsaufgabe einseitige Verzweigung
#Author:         J. Schmülling
#Änderungsdatum: 03.02.2025

zinssatz_pro_jahr = 0.005
grenzbetrag = 2000

#kontostand = 0          #nicht nötig
#neuer_kontostand = 0    #nicht nötig

def get_kontostand():           #funktion öffnen wegen while schleife
    while True:
        try:
            zinsen = 0                                                          #ausführen des folgenden codes "versuchen"
            kontostand = float(input(f"{'Kontostand eingeben:':<25}"))          #input in float umwandeln und den wert in die variable kontostand schreiben
            print("-"*40)
            if kontostand >= grenzbetrag:                                       #einseitige verzweigung "wenn kontostand größer oder gleich grenzbetrag ist, mache folgendes:"
                zinsen = kontostand * (zinssatz_pro_jahr / 12)                  

            neuer_kontostand = kontostand + zinsen

            print(f"{'Kontostand:':<25}{kontostand:.2f}")
            print(f"{'Zinsen:':<25}{zinsen:.2f}")
            print(f"{'Neuer Kontostand:':<25}{neuer_kontostand:.2f}")
            return
        except ValueError:                                                      #gegenstück zu "try": wenn das ausführen nicht möglich war bzw ein fehler auftritt.
            print("Nur Zahlen erlaubt")

get_kontostand()