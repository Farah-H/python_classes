# creating a dog class

# how to create a class
# syntax : class Name_of_class starting with capital letter
# good naming convention is required

# classes are a way to bring functionality together
class Dog:
    
    # defining class variable
    animal_kind = 'canine'

    # self refers to current class
    def bark(self):
        return 'woof'

# in order to execute a class we have to create an object of this class, instanciation
# we can use this to create multiple objects of each class
fido = Dog()
print(fido.animal_kind)
print(fido.bark())

lassie = Dog()
print(lassie.bark())

# any change we make on the object we create will NOT have any impact on other objects of the class
fido.animal_kind = 'Big Dog'
print(fido.animal_kind)
print(lassie.animal_kind)