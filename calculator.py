from simpleeval import simple_eval

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
operation = input('Enter operation (+, -, *, /): ')

print(f"Result: {simple_eval(f'{num1} {operation} {num2}')}")

numbry = '5490 + 2389 - 1234 * 2 / 5'

print(simple_eval(numbry))