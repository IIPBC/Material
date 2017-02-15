# -*- coding:utf-8 -*-


class Animal(object):
    """ docstring for Animal 
    """
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)


class Dog(Animal):
    """docstring for Dog"""
    def __init__(self, name, chases_cats):
        Animal.__init__(self, name, "Dog")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return self.chases_cats


class Cat(Animal):
    """docstring for Cat"""
    def __init__(self, name, species, hates_dogs):
        super(Cat, self).__init__(name, "Cat")
        self.hates_dogs = hates_dogs

    def hatesDogs(self):
        return self.hates_dogs


if __name__ == '__main__':
    pass
