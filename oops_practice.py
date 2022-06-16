class dog():
    #class object attribute same for any instance of class
    #not required to pass this as parameter
    species = 'mammal'

    def __init__(self, breed, name, spots):
        #attribute: passed in as arguements
        #assign it using self.attribute name
        #what if we dont use self?
        #what if a particular instance has more attributes?
        #how to declare datetype of the parameter?

        self.breed = breed
        self.name = name
        
        #boolean
        self.spots = spots

    #operations or action this object will take oince given instruction(s)
    def bark(self, x):
        if x == 'request':
            print("who let the dogs out")
        else:
            print("no bark")

my_dog = dog(breed = "sheperd", name = "julie", spots = True)
type(my_dog)

my_dog.bark("request")

class Circle():

    #class obejct attribute
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius
    
    def get_circum(self):
        return self.radius * self.pi * 2

my_circle  = Circle(30)

my_circle.radius
my_circle.get_circum()



class Animal():

    def __init__(self) -> None:
        print("Animal Created")
        pass

myanimal = Animal()

class Dog(Animal):

    def __init__(self) -> None:
        Animal.__init__(self)
        print("dog created")

    def bark(self):
        print("bark")
mydog = Dog()

mydog.bark()

def generator():
    yield "welcome"
    yield "to"
    yield "simplilearn"

gen_object = generator()

type(gen_object)

for i in gen_object:

    print (i)