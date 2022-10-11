class Car:

    def __init__(self, *args):
        self.make = args[0] # starter som en public variabel -> property
        self.model = args[1]
        self.bhp = args[2]
        self.mph = args[3]

    def get_make(self):
        print('in getter')
        return self.__make

    def set_make(self, make):
        print('In Setter')
        self.__make = make

    make = property(get_make, set_make)

