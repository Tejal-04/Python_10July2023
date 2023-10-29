def remote_control_next():
    yield 'cnn'
    yield 'espn'
    yield 'wwe'

itr = remote_control_next()
print(itr)
print(next(itr))
print(next(itr))
print(next(itr))    

print('Using for loop')
for c in remote_control_next():
    print(c)