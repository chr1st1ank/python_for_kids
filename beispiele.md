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

## Funktionen

Bisher haben wir alles was der Computer tun soll untereinander geschrieben. Wenn er es mehrfach tun sollte,
haben wir es mehrfach hingeschrieben.

Man kann Dinge, die man mehrmals braucht aber auch in einer sogenannten "Funktion" zusammenfassen, die man
dann immer wieder benutzen kann. Eine Funktion, kann Variablen entgegennehmen und welche zurückgeben.

### Fertige Funktionen
Es gibt ganz viele fertige Funktionen, die man einfach benutzen kann. Einige Beispiele hast du schon 
gesehen. Zum Beispiel die Funktion `print()`, die etwas auf dem Bildschirm ausgibt.
Die Funktion print gibt alle Variablen aus, die du ihr zwischen den Klammern übergibst.
Zum Beispiel: `print("Hallo")`

Es gibt noch viel 
mehr Funktionen, für die man ein "Paket" importieren muss. Zum Beispiel die Funktion `randint()`, die
eine zufällige Zahl ausgibt. So zum Beispiel bekommst du eine Zahl zwischen zwei und fünf.

```python
from random import randint

randint(2, 5)
``` 
Diese Funktion nimmt zwei Variablen entgegen und gibt eine zurück.

Wenn du die Funktion mehrfach brauchst, musst du sie trotzdem nur einmal importieren.

### Eigene Funktionen
Du kannst auch eine eigene Funktion schreiben. Zum Beispiel folgende Funktion, die 
zwei Variablen entgegennimmt. Sie rechnet die beiden Zahlen zusammen und gibt dann zurück,
wie viel die Summe ist:

```python
def summe(zahl1, zahl2):
    return zahl1 + zahl2
```

Das was hinter "return" kommt, ist der Rückgabewert der Funktion. Du kannst also dann
woanders diesen Wert benutzen. Zum Beispiel:

```python
ergebnis1 = summe(2, 5)
ergebnis2 = summe(3, 8)
```

Hier benutzen wir unsere eigene Funktion zweimal und speichern jeweils das Ergebnis.


## Schleifen

Wenn du Dinge immer wiederholen willst, so kannst du eine Schleife benutzen. Zum 
Beispiel gibt folgende Schleife die Zahlen von 1 bis 10 aus:

```python
for zahl in range(1, 11):
    print(zahl)
``` 

Die Funktion `range(erste_zahl, ende_zahl)` gibt dabei der Reihe nach Zahlen 
zurück, angefangen von `erste_zahl`. Sie hört aber auf, bevor sie die Zahl `ende_zahl`
erreicht. 


## Das Dictionary

"Dictionary" ist englisch und bedeutet "Wörterbuch". In Python ist ein Dictionary ein
Object, in dem man Dinge genau wie in einem Wörterbuch unter einem bestimmten 
Stichwort ablegen und später wiederfinden kann. Das Stichwort nennt man den "Key", 
das bedeutet "Schlüssel". Das Ding, das man unter so einem Key ablegt, nennt man den
"Wert" oder englisch "Value".

Anlegen eines leeren Dictionary, speichern von zwei Werten und Ausgabe eines der Werte:
```python
d = {}

d["schluessel"] = "Wert"
d[5] = 12345

print(d[5])
print(d["schluessel"])
``` 

Man kann auch einen Wert wie folgt wieder löschen:
```python
del d[5]
``` 
Jetzt ist nur noch der Key "schluessel" enthalten.

Alle vorhandenen Keys oder Werte bekommt man so:
```python
d.keys()

d.values()
```

Wenn man nicht weiß, ob ein bestimmter Key (hier "x") vorhanden ist, so kann man dazu 
eine Wenn-Bedingung benutzen:
```python
d = {1: "ein Wert", 2: "noch ein Wert"}

if x in d:
    print("x ist als Key in d vorhanden")
else:
    print("x ist nicht als Key in d vorhanden")
```
