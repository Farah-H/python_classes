# Python Classes 
## OOP (Object Oriented Programming)
### There are 4 pillars of OOP:
- Inheritance
    - Inheritance in OOP = When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods.
- Encapsulation
    -  It refers to the bundling of data with the methods that operate on that data. Encapsulation is used to hide the values or state of a structured data object inside a class, preventing unauthorized parties' direct access to them.
- Abstraction
    - Its main goal is to handle complexity by hiding unnecessary details from the user.
- Polymorphism
    - It describes the concept that different classes can be used with the same interface. Each of these classes can provide its own implementation of the interface. [Source](https://stackify.com/oop-concept-polymorphism/#:~:text=Polymorphism%20is%20one%20of%20the,with%20different%20sets%20of%20parameters.)

### ``class`` is the main factor that is used to implement any of these pillars
- What are classes? 

Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.

[Source](https://docs.python.org/3/tutorial/classes.html)

- Why would we use classes? 
When you are creating similar objects, the use of classes ensures that you don't need to repeat yourself and define basic properties, I also means you can 'inherit' basic properties from the class. 

## How to create a `class` 

### Pre-Requisites 
It is easier to complete this task when using a code editor, such as Visual Studio Code or PyCharm. You can learn how to [install VSC](https://docs.microsoft.com/en-us/visualstudio/install/install-visual-studio?view=vs-2019) or [install PyCharm](https://www.jetbrains.com/help/pycharm/quick-start-guide.html) using these hyperlinks. 

To create a task use the syntax:
```python
class Class_name:  # note the capitalisation and colon
    attrinute_1 = something # note the indentation
```
You can also define functions within classess, for example, all dogs bark:

```python
class Dog():

    annoying = True

    def bark(self,annoying):
        if annoying:
            return 'WOOOF WOOF WOOF WOOF WOOF WOOF WOOF'
        else return 'WOOF' 
```
To use a class, you need to create an *instance* of it using the following syntax:
```python
filo = Dog()
```

You can change the attributes of an object, *without* changing the attributes of the class, or any other objects using the following syntax:

```python
filo.annoying = True
```

And we can call the functions inside the class using the syntax:
```python
print(filo.bark(filo.annoying)) # this would return 'WOOF WOOF WOOF WOOF' 
```
## Tasks
1. Create a `Cat()` class
2. Create 2 class level variables
3. Create 3 objects of the class
4. display all information of each object
5. change the class variables in each object and display