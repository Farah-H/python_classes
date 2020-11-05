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
print(f'Jack\'s Attributes: coward = {jack.coward}, cute = {jack.cute}, fluffy = {jack.fluffy}')
jack.purr(jack.cute,jack.coward, jack.fluffy)

print(f'Shinny\'s Attributes: coward = {shinny.coward}, cute = {shinny.cute}, fluffy = {shinny.fluffy}')
shinny.purr(shinny.cute,shinny.coward, shinny.fluffy)

print(f'Garfield\'s Attributes: coward = {garfield.coward}, cute = {garfield.cute}, fluffy = {garfield.fluffy}')
garfield.purr(garfield.cute,garfield.coward, jack.fluffy)

# change the class variables values in each object and display
jack.coward = True
print(f'Jack\'s new Attributes: coward = {jack.coward}, cute = {jack.cute}, fluffy = {jack.fluffy}')
jack.purr(jack.cute,jack.coward, jack.fluffy)

shinny.fluffy = False
print(f'Shinny\'s new Attributes: coward = {shinny.coward}, cute = {shinny.cute}, fluffy = {shinny.fluffy}')
shinny.purr(shinny.cute,shinny.coward, shinny.fluffy)

garfield.cute = False
print(f'Garfield\'s new Attributes: coward = {garfield.coward}, cute = {garfield.cute}, fluffy = {garfield.fluffy}')
garfield.purr(garfield.cute,garfield.coward, jack.fluffy)