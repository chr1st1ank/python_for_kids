# Programmierbeispiele

In der folgenden Übersicht findest du Beispiele und Erklärungen, wie bestimmte Aufgaben mit Python gelöst werden können.

## Variablen und Datentypen

Variablen können benutzt werden, wenn der Computer sich etwas merken soll. Du kannst Werte oder Zeichenketten darin
speichern. Variablennamen kann man sich frei ausdenken. Allerdings darf man dabei nur normale Buchstaben und Zahlen 
verwenden, sowie das Zeichen "_". Man benutzt dabei normalerweise nur Kleinbuchstaben.

Hier ein paar Beispiele:
```python
text = "Ein kleiner Satz zum merken"

zahl = 12345
kommazahl = 4.5
```

Fällt dir etwas auf? Für den Satz, den wir in der Variablen `text` gespeichert haben, haben wir Anführungszeichen 
gebraucht. Das liegt daran, dass wir eine Zeichenkette gespeichert haben. Die Variable hat jetzt den Typ "Zeichenkette"
(englisch "string").
Die anderen beiden Variablen haben jeweils einen Zahlentyp. `zahl` ist vom Typ "integer", das heißt "ganze Zahl".
`kommazahl` ist vom Typ "float", das heißt Kommazahl.

Hier haben wir also drei Typen:
- string: Eine Zeichenkette. Zeichenketten kann man miteinander vergleichen oder verändern, zum Beispiel Wörter anhängen.
- integer: Eine Ganzahl. Mit ihr kann man rechnen.
- float: Eine Kommazahl. Auch damit kann man rechnen. 


## Zeichenketten einlesen und ausgeben

Eine Zeile ausgeben:
```
print("Dieser Text wird ausgegeben")
```

Eine Zeile einlesen und dazu mit einer Frage oder Ähnlichem auffordern. Die Eingabe wird in der Variablen `text` gespeichert:
```
text = input("Was möchtest du mir sagen?")
```

Den Inhalt einer Variablen in eine Zeichenkette einfügen und beides zusammen ausgeben. Dazu braucht man ein `f` vor dem
Anführungszeichen und um die Variable macht man geschweifte Klammern `{}`:
```
print(f"Das ist der Text: {text}")
```

## Umgang mit Zahlen
Zeichenketten in eine Zahl umwandeln und eine Zahl in eine Zeichenkette umwandeln:
```
# Zahl zu Zeichenkette:
text = str(24)

# Zeichenkette zu Zahl (für Ganzzahlen):
zahl = int("45")

# Zeichenkette zu Zahl (für Kommazahlen):
zahl = float("45")
```

Mit Zahlen rechnen und das Ergebnis in einer Variablen `ergebnis` speichern:
```
ergebnis = 5 + 7

ergebnis = 8 - 4

ergebnis = 4 / 2

ergebnis = 2 * 2
```

## Wahrheitswerte

Wenn du Werte miteinander vergleichst, dann erhältst du einen Wahrheitswert, den du beispielsweise für Bedingungen
benutzen kannst, wenn der Computer etwas entscheiden soll.

Ein Wahrheitswert ist immer entweder wahr (englisch "True") oder falsch (englisch "False").

Um einen Wahrheitswert zu bekommen, benutzt man die Vergleichsoperatoren (`==`, `>`, `<`).
Sind zwei Werte gleich?
```
4 == 5

variable == 5
```

Ist ein Wert größer oder kleiner?
```python
4 > 5

variable < 7
```

## Wenn/dann-Bedingungen

Wenn der Computer etwas entscheiden soll, kann man dafür eine Wenn/dann-Bedingung nutzen (Englisch: if/else).
Wenn die Bedingung erfüllt ist, führt er die eine Aufgabe aus, wenn sie nicht erfüllt ist, dann die andere.

Einfache Wenn/dann-Bedingung:
```python
if variable == 5:
    print("Die Variable hat den Wert 5")
else:
    print("Die Variable ist nicht 5")
```

Doppelte Wenn/dann-Bedingung:
```python
if variable == 5:
    print("Die Variable hat den Wert 5")
elif variable == 7:
    print("Die Variable hat den Wert 7")
else:
    print("Die Variable ist weder 5 noch 7")
```

