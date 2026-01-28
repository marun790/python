from animal import Animal


class Mangoos(Animal):

    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Mangoos sound")


mangoos = Mangoos(name="Mangoos")
mangoos.greeting()
mangoos.make_sound()
