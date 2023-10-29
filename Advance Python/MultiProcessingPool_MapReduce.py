'''def f(n):
    return n*n

if __name__ == '__main__':
    array = [1,2,3,4,5]
    result = []
    for num in array:
        result.append(f(num))
    print(result)'''

from multiprocessing import Pool
'''import time

def f(n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum

if  __name__ == '__main__':
    t1 = time.time()
    p = Pool()
    result = p.map(f,range(100000))
    
    p.close()
    p.join()
    
    print('Pool Took : ',time.time() - t1)
    
    t2 = time.time()
    result = []

    for x in range(100000):
        result.append(f(x))
    print('Serial Processing Took : ',time.time()-t2)

print('----------Pool Arguments----------')'''

def fun(num):
    return num*num

if __name__ == '__main__':
    p1 = Pool(processes=3)
    res = p1.map(fun,[2,3,4])
    for n in res:
        print(n)