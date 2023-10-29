'''# user defined exception
try:
    raise MemoryError('memory error')
except MemoryError as e:
    print(e)'''

class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    def print_exception(self):
        print('User defined exception : ',self.msg)

try:
    raise Accident('Crash between two cars')
except Accident as e:
    e.print_exception()


# using finally statement
'''def process_file():
    try:
        f = open('funny.txt')
        x = 1/0
    except FileNotFoundError as e:
        print('Inside Except')
    f.close()

process_file()'''

def process_file():
    try:
        f = open('funny.txt')
        x = 1/0
    except FileNotFoundError as e:
        print('Inside Except')
    finally:
        print('Cleaning up File')
        f.close()

process_file()                