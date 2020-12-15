from stacks_and_queues.stacks_and_queues import Queue , Node

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.type = _type


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = 'Cat'


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = 'Dog'


class AnimalShelter:
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()
        self.animal_order = Queue()

    def enqueue(self, animal):

        if animal.type == 'Cat':
            self.cats.enqueue(animal)
            self.animal_order.enqueue('Cat')
        else:
            self.dogs.enqueue(animal)
            self.animal_order.enqueue('Dog')
   

    def dequeue(self, preference=None):

        try:
            if not preference:
                preference = self.animal_order.dequeue()
            if preference.lower() == 'cat':
                animal = self.cats.dequeue()
            elif preference.lower() == 'dog':
                animal = self.dogs.dequeue()
        except AttributeError as err:
            raise AttributeError('There is no animals!')
