class Dog:

    def __init__(self, color, voiceText):
        self.color = color
        self.voiceText = voiceText

    def voice(self):
        print(f'{self.voiceText}')

jack = Dog('black', 'gaf gaf!')
print(jack.color)
jack.voice()

class Cat:

    def __init__(self, color, voiceText):
        self.color = color
        self.voiceText = voiceText

    def voice(self):
        print(f'{self.voiceText}')

liza = Cat('white', 'meow meow!')
print(liza.color)
liza.voice()

class Cow:

    def __init__(self, color, voiceText):
        self.color = color
        self.voiceText = voiceText

    def voice(self):
        print(f'{self.voiceText}')

murka = Cow('white', 'moo moo!')
print(murka.color)
murka.voice()


class Bear:

    def __init__(self, color, voiceText):
        self.color = color
        self.voiceText = voiceText

    def voice(self):
        print(f'{self.voiceText}')

teddy = Bear('brown', 'gr gr!')
print(teddy.color)
teddy.voice()

