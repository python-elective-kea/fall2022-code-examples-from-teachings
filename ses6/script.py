# declare a class
class Person:
    pass


claus = Person() # create a new instance of Person
anna = Person()

# create an initializer
class Person: 

    type = 'Mammel' # class variable

    def __init__(self, name):
        self.name = name   # instance variable

    def __len__(self):
        return 1200


# overloading

class Person:
    
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]
        elif len(args) == 3:
            self.blablabla = args[2]


# Arv

class Person:
    def __init__(self, *args):
        self.name = args[0]


class Student(Person):
    
    def __init__(self, name, stid):
        Person.__init__(self, name)
        self.student_id = stid

class Instructor:
    pass

class Teacher(Person, Instructor):
    def __init__(self, *args):
        Person.__init__(self, name)
        Instructor.__init__(self.age)


























