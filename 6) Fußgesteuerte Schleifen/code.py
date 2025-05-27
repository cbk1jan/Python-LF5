anschaffungswert = float(input("Bitte geben Sie den Anschaffungswert ein: "))
laufzeit = int(input("Bitte geben Sie die Nutzungsdauer in Jahren ein: "))

abschreibungsbetrag = anschaffungswert / laufzeit
jahr = 1
restwert = anschaffungswert
print(f"{"Jahr"} | {"Abschreibungsbetrag"} | {"Restwert":<10}")
print("-" * 40)
while True:
    print(f"{jahr:<4} | {abschreibungsbetrag:<19.2f} | {restwert:<10.2f}")
    restwert = restwert - abschreibungsbetrag
    jahr += 1
    if restwert <= 0:
        break
