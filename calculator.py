def calculate(num1, num2, operation):
  if operation not in ['+', '-', '*', '/']:
    raise ValueError("Invalid operation. Please choose one of '+', '-', '*', or '/'.")

  if operation == '/' and num2 == 0:
    raise ValueError("Division by zero is not allowed.")

  if operation == '+':
    return num1 + num2
  elif operation == '-':
    return num1 - num2
  elif operation == '*':
    return num1 * num2
  else:
    return num1 / num2

def main():
  while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    try:
      result = calculate(num1, num2, operation)
      print("Result:", result)
    except ValueError as e:
      print("Error:", e)

if __name__ == "__main__":
  main()
