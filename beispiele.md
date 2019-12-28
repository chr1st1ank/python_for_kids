# Programmierbeispiele

In der folgenden Übersicht findest du Beispiele, wie bestimmte Aufgaben mit Python gelöst werden können.

## Text einlesen und ausgeben

Eine Zeile ausgeben:
```
print("Dieser Text wird ausgegeben")
```

Eine Zeile einlesen und dazu mit einer Frage oder Ähnlichem auffordern. Die Eingabe wird in der Variablen `text` gespeichert:
```
text = input("Was möchtest du mir sagen?")
```

Den Inhalt einer Variablen in einen Text einfügen und beides zusammen ausgeben. Dazu braucht man ein `f` vor dem
Anführungszeichen und um die Variable macht man geschweifte Klammern `{}`:
```
print(f"Das ist der Text: {text}")
```

## Umgang mit Zahlen
Text in eine Zahl umwandeln und eine Zahl in Text umwandeln:
```
# Zahl zu Text:
text = str(24)

# Text zu Zahl (für Ganzzahlen):
zahl = int("45")

# Text zu Zahl (für Kommazahlen):
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