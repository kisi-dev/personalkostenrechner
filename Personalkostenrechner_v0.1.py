LOGO = r"""
  _  __ ___  ____  ___
 | |/ /|_ _|/ ___||_ _|
 | ' /  | | \___ \ | |
 | . \  | |  ___) || |
 |_|\_\|___||____/|___|
   data . automation . ai
   > Personalkostenrechner  v0.1
"""
print(LOGO)

mitarbeiter = input("Name des Mitarbeiters? ")
stunden_text = input("Wie viele Stunden? ")
stunden_text = stunden_text.replace(",", ".")
stunden = float(stunden_text)

stundensatz_text = input("Wie hoch ist der Stundensatz? ")
stundensatz_text = stundensatz_text.replace(",", ".")
stundensatz = float(stundensatz_text)

personalkosten = stunden * stundensatz
print()
print(f"Personalkosten für {mitarbeiter}: {personalkosten:.2f} Euro")
print()
input("Enter drücken zum Beenden ...")