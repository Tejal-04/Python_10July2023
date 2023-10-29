import time
import multiprocessing

'''def calc_square(numbers):
    for n in numbers:
        time.sleep(5)
        print('Square : ' + str(n*n))

def calc_cube(numbers):
    for n in numbers:
        time.sleep(5)
        print('Cube : ' + str(n*n*n))

if __name__ == '__main__':
    arr = [2,3,4,5]
    
    p1 = multiprocessing.Process(target=calc_square,args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube,args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Done!')'''

print('-------------------------------------------------')

square_result = []
def cal_square(number):
    global square_result
    for num in number:
        print('Square : ' + str(num*num))
        square_result.append(num*num)
    print('Within a Process : result' + str(square_result))

if __name__ == '__main__':
    array = [6,7,8,9]

    process = multiprocessing.Process(target=cal_square,args=(array,))
    process.start()
    process.join()

    print('Result : ' + str(square_result))
    print('Done!')