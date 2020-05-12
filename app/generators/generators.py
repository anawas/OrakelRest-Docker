import random

class NumberGenerator:

    def __init__(self):
        pass

    def get_lucky_number(self):
        return random.randint(1, 20)


class SpellGenerator:
    def __init__(self):
        self.spells = [
            "Nutze den Tag",
            "Heute ist dein Glückstag",
            "Beginne den Tag mit einem Lächeln"]

    def get_lucky_spell(self):
        index = random.randint(0, len(self.spells)-1)
        return self.spells[index]


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

