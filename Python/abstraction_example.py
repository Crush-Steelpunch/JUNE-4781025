from abc import ABC, abstractmethod

class Animal(ABC):
    babies = 0
    def reproduce(self):
        self.babies += 1


    @abstractmethod
    def eat(self):
        pass


class dog(Animal):
    def reproduce(self):
        self.babies += 6

    def eat(self):
        return 'Woofs down the food. Geddit?'


rover = dog()
rover.reproduce()
print(rover.babies)
print(rover.eat())