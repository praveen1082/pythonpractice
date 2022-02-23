class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, i am {self.name}")


john = Person("john")
john.talk()

praveen = Person("praveen")
praveen.talk()
