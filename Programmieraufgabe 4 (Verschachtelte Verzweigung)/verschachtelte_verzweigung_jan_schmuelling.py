#Programm:       Übungsaufgabe verschachtelte Verzweigung
#Author:         J. Schmülling
#Änderungsdatum: 03.02.2025

rabatt_bis_500 = 0.02
rabatt_bis_1000 = 0.05
rabatt_ueber_1000 = 0.1
sonderrabatt_ab_10_jahre = 0.15

def calc():
    while True:
        try:
            stueckpreis = float(input(f"{'Stückpreis des Artikels:':<30}"))
            stueckzahl = float(input(f"{'Gekaufte Stückzahl:':<30}"))
            geschaeftsbeziehung = float(input(f"{'Geschäftsbeziehung in Jahren:':<30}"))

            if stueckzahl > 500:
                if stueckzahl > 1000:
                    if geschaeftsbeziehung > 10:
                        gewaehrter_rabatt = sonderrabatt_ab_10_jahre
                    else:
                        gewaehrter_rabatt = rabatt_ueber_1000
                else:
                    gewaehrter_rabatt = rabatt_bis_1000
            else:
                gewaehrter_rabatt = rabatt_bis_500

            print("-"*40)

            normal_preis = stueckzahl * stueckpreis
            rabatt_betrag = normal_preis * gewaehrter_rabatt
            endpreis = normal_preis - rabatt_betrag

            print(f"{'Normalpreis:':<20}{normal_preis:<10.2f} EUR")
            print(f"{'Rabattsatz:':<20}{gewaehrter_rabatt*100:<10.2f} %")
            print(f"{'Rabatt:':<20}{rabatt_betrag:<10.2f} EUR")
            print(f"{'Endpreis:':<20}{endpreis:<10.2f} EUR")
            return
        except ValueError:
            print("Fehlerhafte Eingabe")

calc()