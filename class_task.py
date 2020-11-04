# Task

# create a Cat class
class Cat:

# Create 2 class level variables 
    coward = False
    cute = True
    fluffy = True
# one function which returns 'MEOWWWWWWW', added some details :)
    def purr(self,cute,coward,fluffy):
        if cute and fluffy:
            print('You approach this adorable cat..')
            if coward:
                print('Oh no! You scared the cat away.')
            else:
                print('MEOWWWWWW')
        else: 
            print('Ohh that cat looks kind of grumpy. Let\'s walk away for now.')

# create 3 objects 
jack = Cat()
shinny = Cat()
garfield = Cat()

# display all information with each object
print(jack.coward)
print(jack.cute)
jack.purr(jack.cute,jack.coward, jack.fluffy)

print(shinny.coward)
print(shinny.cute)
shinny.purr(shinny.cute,shinny.coward, shinny.fluffy)

print(garfield.coward)
print(garfield.cute)
garfield.purr(garfield.cute,garfield.coward, jack.fluffy)

# change the class variables values in each object and display
jack.coward = True
print(jack.coward)
print(jack.cute)
print(jack.fluffy)
jack.purr(jack.cute,jack.coward, jack.fluffy)

shinny.fluffy = False
print(shinny.coward)
print(shinny.cute)
print(shinny.fluffy)
shinny.purr(shinny.cute,shinny.coward, shinny.fluffy)

garfield.cute = False
print(garfield.coward)
print(garfield.cute)
print(shinny.fluffy)
garfield.purr(garfield.cute,garfield.coward, jack.fluffy)