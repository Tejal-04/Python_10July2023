import time

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ + " : " + ' took ' + str((end-start) * 1000) + ' milisecond ')
        return result
    return wrapper

@time_it
def calc_square(numbers):
    result = []
    for num in numbers:
        result.append(num * num)
    return result

@time_it
def calc_cube(numbers):
    result = []
    for num in numbers:
        result.append(num * num * num)
    return result

arr = range(1,100000)
out_squ = calc_square(arr)
#print(out_squ)
out_cube = calc_cube(arr)
#print(out_cube)        