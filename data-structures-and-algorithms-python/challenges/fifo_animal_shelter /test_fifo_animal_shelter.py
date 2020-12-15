import pytest

from fifo_animal_shelter import Animal, AnimalShelter, Cat, Dog


class TestAnimalShelter:

    @pytest.fixture()
    def shelter(self):
        return AnimalShelter()

    @pytest.fixture()
    def cat(self):
        return Cat('kitten', 5)

    @pytest.fixture()
    def dog(self):
        return Dog('Jessi', 4)

    def test_enqueue_multiple_cats(self, shelter):
        cat1 = Cat('cat_1', 1)
        cat2 = Cat('cat_2', 2)
        assert shelter.cats.front is None
        shelter.enqueue(cat1)
        shelter.enqueue(cat2)
        assert shelter.cats.front.value.name == 'cat_1'



    def test_enqueue_mixed_animals(self, shelter):
        assert shelter.dogs.front is None
        assert shelter.cats.front is None
        cat1 = Cat('cat_1', 1)
        dog1 = Dog('dog_1', 1)
        shelter.enqueue(cat1)
        shelter.enqueue(dog1)




 
