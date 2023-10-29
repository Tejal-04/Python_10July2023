import time
import threading

def calc_square(numbers):
    print('Calculate Square of Numbers')
    for num in numbers:
        time.sleep(0.2)
        print('Square : ',num * num)

def calc_cube(numbers):
    print('Calculate Cube of Numbers')
    for num in numbers:
        time.sleep(0.2)
        print('Cube : ',num * num * num)

arr = [2,3,8,9]
t = time.time()
calc_square(arr)
calc_cube(arr)
print('Done in : ',time.time() - t)

print('----------Using Multithreading----------')

def cal_square(number):
    print('Calculate Square of Numbers')
    for n in number:
        time.sleep(0.2)
        print('Square : ',n * n)

def cal_cube(number):
    print('Calculate Cube of Numbers')
    for n in number:
        time.sleep(0.2)
        print('Cube : ',n * n * n)

array = [2,3,8,9]
tm = time.time()
t1 = threading.Thread(target=cal_square,args=(array,))
t2 = threading.Thread(target=cal_cube,args=(array,))

t1.start()
t2.start()

t1.join()
t2.join()

print('Done in : ',time.time() - tm)