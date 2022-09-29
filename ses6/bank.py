class Bank:
    
    def __init__(self):
        self.accounts = []

class Customer:
    
    def __init__(self, name, acc):
        self.name = name
        if type(acc) == Account:
            self.acc = acc
        else:
            print('Wrong type')


class Account:
    
    def __init__(self, accno):
        self.accno = accno

