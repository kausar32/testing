def factorial(number):
	if number < 0:
		raise ValueError("Factorial is not defined for negative numbers")

	result = 1
	for value in range(2, number + 1):
		result *= value
	return result


if __name__ == "__main__":
	number = int(input("Enter a non-negative integer: "))
	print(f"{number}! = {factorial(number)}")

print("hello fraaands")