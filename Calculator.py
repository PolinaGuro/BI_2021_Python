number1 = int(input())
operation = input()
number2 = int(input())

if operation == '+':
  print(number1 + number2)
elif operation == '-':
  print(number1 - number2)
elif operation == '*' or operation == 'x':
  print(number1 * number2)
elif operation == '/' and number2 == 0:
  print('Zero error')
else:
  print (number1 / number2)