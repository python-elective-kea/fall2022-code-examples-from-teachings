class P:
    def __init__(self, name, alias):
        self.name = name # public variable -> property
        self.__alias = alias

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name)  == str:
            self.__name = name
        else:
            print('no no no')

    def __str__(self):
        return 'kjsdfhkjdshfk'

    def __repr__(self):
        return 'repr jgdljkdlgjkflgjdlgjfl'

l = [P('Claus', 'clbo')]
