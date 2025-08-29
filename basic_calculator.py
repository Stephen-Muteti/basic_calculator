class BasicCalculator:
	def __init__(self):
		pass

	def calculator_start(self):
		try:
			num1 = float(input("Enter the first number: "))
			operation = input("Enter your desired operation: ")
			num2 = float(input("Enter the second number: "))
			operation_function = {
			'*': lambda x, y : x * y,
			'+': lambda x, y : x + y,
			'/': lambda x, y : x / y if y != 0 else "Cannot divide by zero",
			'-': lambda x, y : x - y
			}
			if not operation in operation_function:
				print("The operation you entered is invalid")
				return None
			print(f"{num1} {operation} {num2} = {operation_function[operation](num1, num2)}")
		except ValueError:
			print("Invalid input! Enter numeric values only")

# Run the calculator
calculator = BasicCalculator()
not_ended = True
while not_ended:
	print("-------------------------------------------------------")
	calculator.calculator_start()
	end = input("Quit : Y/N: ")
	not_ended = end.lower() == 'n'
