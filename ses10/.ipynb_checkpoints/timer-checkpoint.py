import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        val = func(*args)
        end = (time.time()) - start
        print(f'Time elepsed: {end}')
        return val
    return wrapper