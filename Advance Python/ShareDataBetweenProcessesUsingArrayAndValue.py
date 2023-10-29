import multiprocessing

result = []
def calc_square(numbers):
    global result
    for n in numbers:
        result.append(n*n)
    print('Inside Process : ' + str(result))

if __name__ == '__main__':
    numbers = [2,3,4,5]

    p = multiprocessing.Process(target=calc_square,args=(numbers,))
    p.start()
    p.join()

    print('Outside Process : ' + str(result))

print('---------------------------------------------------')

# Using Array
print('Using Array')

def cal_square(number,res):
    for idx,num in enumerate(number):
        res[idx] = num * num

if __name__ == "__main__":
    array = [2,3,5]
    ans = multiprocessing.Array('i',3)
    process = multiprocessing.Process(target=cal_square,args=(array,ans))
    process.start()
    process.join()
    print('Result : ', ans[:])

print('---------------------------------------------------')

# Using Value
print('Using Value')

def c_square(no,r,v):   # no->number, r->result, v->value
    v.value = 5.67
    for idx,num in enumerate(no):
        r[idx] = num*num

if __name__ == '__main__':
    no = [2,3,4]
    r = multiprocessing.Array('i',3)
    v = multiprocessing.Value('d',0.0)
    p1 = multiprocessing.Process(target=c_square,args=(no,r,v))
    p1.start()
    p1.join()
    print('Value : ',v.value)