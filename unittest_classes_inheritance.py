import unittest
from classes_inheritance import *


def setUpModule():
    print "Setup before all"

def tearDownModule():
    print "Tear Down after all"


class Test(unittest.TestCase):

    def setUp(self):
        self.some_animal = Animal()
        self.doggy = Dog()
        self.kitty = Cat()
        self.vasya = SphynxCat()
        self.petya = Rooster()

    def tearDown(self):
        print "Delete instances after all tests"


class Test(unittest.TestCase):

    def test_some_animals_tail(self):
        self.assertEqual(some_animal.tail, 1)

    def test_some_animals_paw(self):
        self.assertEqual(some_animal.paw, 4)

    def test_some_animals_wool(self):
        self.assertEqual(some_animal.wool, True)

    def test_doggy_tail(self):
        self.assertEqual(doggy.tail, 1)

    def test_doggy_paw(self):
        self.assertEqual(doggy.paw, 4)

    def test_doggy_wool(self):
        self.assertEqual(doggy.wool, True)

    def test_doggy_say_someting(self):
        self.assertEqual(doggy.say_someting(), 'Woof-woof')

    def test_kitty_tail(self):
        self.assertEqual(kitty.tail, 1)

    def test_kitty_paw(self):
        self.assertEqual(kitty.paw, 4)

    def test_kitty_wool(self):
        self.assertEqual(kitty.wool, True)

    def test_kitty_say_someting(self):
        self.assertEqual(kitty.say_someting(), 'Meow-meow')

    def test_vasya_tail(self):
        self.assertEqual(vasya.tail, 1)

    def test_vasya_paw(self):
        self.assertEqual(vasya.paw, 4)

    def test_vasya_wool(self):
        self.assertEqual(vasya.wool, False)

    def test_vasya_say_someting(self):
        self.assertEqual(vasya.say_someting(), 'Murr-murr')

    def test_petya_tail(self):
        self.assertEqual(petya.tail, 1)

    def test_petya_paw(self):
        self.assertEqual(petya.paw, 2)

    def test_petya_wool(self):
        self.assertEqual(petya.wool, False)

    def test_petya_say_someting(self):
        self.assertEqual(petya.say_someting(), 'Cocorico')


if __name__ == '__main__':
    unittest.main()
