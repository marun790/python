from abc import ABC, abstractmethod
from symtable import Function


class Animal(ABC):

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"hello {self.name}")

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)


dog = Dog(name="Buddy")
dog.greeting()
soundFunction: Function = dog.make_sound
soundFunction()
