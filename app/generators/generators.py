import random

# Erzeugt eine Zufallszahl im Bereich [1..20[
# Todo: Die Zahl mit einem etwas spannenderen Algorithmus erzeugen
#       Z.B. mit dem Geburtstdatum oder der aktuellen Datum
class NumberGenerator:
    def __init__(self):
        pass

    def get_lucky_number(self):
        return random.randint(1, 20)


# Wählt zufällig einen Spruch aus der Liste
# Todo: Die Sprüche von einem File oder aus einer DB einlesen
class SpellGenerator:
    def __init__(self):
        self.spells = [
            "Nutze den Tag",
            "Heute ist dein Glückstag",
            "Beginne den Tag mit einem Lächeln"]

    def get_lucky_spell(self):
        index = random.randint(0, len(self.spells)-1)
        return self.spells[index]


# Wählt zufällig ein Symbol aus der Liste
# Todo: Das Symbol als Bild zurückgeben
class SymbolGenerator:
    def __init__(self):
        self.symbols = [
            "Kleeblatt",
            "Kaminfeger",
            "Schweinchen",
            "Räppler"]

    def get_lucky_symbol(self):
        index = random.randint(0, len(self.symbols)-1)
        return self.symbols[index]

