from random import randint

zahl1 = randint(1, 20)
zahl2 = randint(1, 30)
ergebnis = zahl1 + zahl2

print(f"Wie viel ist {zahl1}+{zahl2}?")
eingabe = input()
eingabe = int(eingabe)

if eingabe == ergebnis:
    print("Das ist richtig!")
else:
    print(f"Falsch! {zahl1} + {zahl2} = {ergebnis}!")
