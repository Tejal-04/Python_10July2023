'''
num = int(input("enter a number : "))
if num%2 == 0:
    print("Even")
else:
    print("Odd")
'''

indian = ['samosa','daal','naan']
chinese = ['egg role','pot sticker','fried rice']
italian = ['pizza','pasta','risotto']
dish = input("Enter dish name : ")
if dish in indian:
    print('Indian')
elif dish in chinese:
    print('Chinese')
elif dish in italian:
    print('Italian')
else:
    print('I dont know which cuisine is',dish)            