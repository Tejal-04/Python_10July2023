import argparse

'''if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    print(parser)
    args = parser.parse_args()
    print(args)'''

'''if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--number1',help='First Number')
    parser.add_argument('--number2',help='Second Number')
    parser.add_argument('--operation',help='Operation')
    
    args = parser.parse_args()
    print(args.number1)
    print(args.number2)
    print(args.operation)

    num1 = int(args.number1)
    num2 = int(args.number2)
    result = None

    if args.operation == 'add':
        result = num1 + num2
    elif args.operation == 'subtract':
        result = num1 - num2
    elif args.operation == 'multiply':
        result = num1 * num2
    else:
        print('Unsupported Operation')    
    print('Result : ',result)'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--number1',help='First Number')
    parser.add_argument('--number2',help='Second Number')
    parser.add_argument('--operation',help='Operation',choices=['add','subtract','multiply'])

    args = parser.parse_args()
    print(args.number1)
    print(args.number2)
    print(args.operation)

    num1 = int(args.number1)
    num2 = int(args.number2)
    result = None

    if args.operation == 'add':
        result = num1 + num2
    elif args.operation == 'subtract':
        result = num1 - num2
    elif args.operation == 'multiply':
        result = num1 * num2
    print('Result : ',result)            