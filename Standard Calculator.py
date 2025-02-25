a = float(input("Enter a number:"))
b = input("Enter a mathematical operation:")
c = float(input("Enter another number:"))
while b == "+":
	print(a+c)
while b == "-":
	print(a-c)
while b == "*":
	print(a*c)
while b == "/":
	print(a/c)
else:
	print("Unsupported mathematical operation. Please try again.")

