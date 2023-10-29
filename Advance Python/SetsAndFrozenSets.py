print('SET')
basket = {'Orange','Apple','Banana','Chiku','Mango','Apple','Banana','Chiku'}
print(type(basket))
print(basket)
'''print(basket[0])     # TypeError : 'set' object is not subscriptable'''

a = set()
a.add('Red')
print(type(a))
print(a)
a.add('Yellow')
a.add('Orange')
a.add('Pink')
print(a)
a.add('Pink')
print(a)

b = {}
print(type(b))    # <class 'dict'>
c = {'Tejal'}
print(type(c))    # <class 'set'>

numbers = [1,2,3,4,5,1,2,3]
unique_numbers = set(numbers)
print(unique_numbers)
unique_numbers.add(6)
print(unique_numbers)

print('------------------------------------------------')

print('FROZEN SET')
fs = frozenset(numbers)
print(type(fs))
print(fs)
"""fs.add(7)       # AttributeError: 'frozenset' object has no attribute 'add'"""

x = {'a','b','c'}
print('a' in x)
print('p' in x)

for i in x:
    print(i)

y1 = {'p','q','r'}
y2 = {'p','q','x','y','z','r'}
print(y1|y2)    # {'p','q','x','y','z','r'}
print(y1&y2)    # {'p','q','r'}
print(y1<y2)    # True
print(y1>y2)    # False
print(y1-y2)    # set()
print(y2-y1)    # {'z','y','x'}