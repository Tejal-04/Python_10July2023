a = ['hey','bro',"you'r",'awesome']
for i in a:
    print(i)

itr = iter(a)
print(itr)
print(next(itr))
print(next(itr))
print(next(itr))    
print(next(itr))

print('List Iteration')
for element in [1,2,3,4,5]:
    print(element)

print('Tuple Iteration')
for element in (1,2,3,4,5):
    print(element)    

print('Dictionary Iteration')
for key in {'one':1,'two':2,'three':3}:
    print(key)

print('String Iteration')
for char in 'Tejal':
    print(char)    

print('File Text Iteration')
for line in open('funny1.txt'):
    print(line)    

# for reverse iterating
rev_itr = reversed(a)
print(next(rev_itr))
print(next(rev_itr))
print(next(rev_itr))
print(next(rev_itr))

print(dir(a))