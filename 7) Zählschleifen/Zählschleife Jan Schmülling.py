Kapital = float(input("Geben Sie das Startkapital ein: "))
Zinssatz = float(input("Geben Sie den Zinssatz in Prozent ein: "))
Laufzeit = int(input("Geben Sie die Laufzeit in Jahren ein: "))

Zinssatz = Zinssatz / 100

for Jahr in range(1, Laufzeit + 1):
    Zinsen = Kapital * Zinssatz
    Kapital += Zinsen
    print(f"Kapital am Ende von Jahr {Jahr}: {Kapital:>15.2f}")