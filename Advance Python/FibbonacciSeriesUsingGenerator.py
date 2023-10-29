def fib():
    a,b = 0, 1
    while True:
        yield a
        a,b = b, a+b
        
lst = []
for f in fib():
    if f > 50:
        break
    lst.append(f)
print(lst)