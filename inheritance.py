
#inheritance in python
#class Dog:
 #   def walk(self):
  #      print("walk")


# class Cat:
  #  def walk(self):
   #     print("Walk")

#this is not a good practice if the objects have same properties we have to make it available in super class and inherit
# the property of super class by sub class
#dry - don't repeat yourself

class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark )):: vow vow")


class Cat(Mammal):
    def meow(self):
        print("meow meow meow")

Dog1 = Dog()
Dog1.walk()
Dog1.bark()
cat = Cat()
cat.walk()
cat.meow()