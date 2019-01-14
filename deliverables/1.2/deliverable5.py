# deliverable5.py
# A program to convert Celsius temps to Fahrenheit
# modified by gull, original convert.py by Susan C.

def main():
	celsius = -10
	print("This program prints a table of Celsius temperatures and their Fahrenheit equivalents in intervals of ten, from 0c to 100c.")
	print()
	print("+-----+-----+")
	print("|cels.|fahr.|")
	print("+-----+-----+")
	for i in range(11):
		celsius = celsius + 10
		fahrenheit = 9 / 5 * celsius + 32
		print('|{:5.1f}|{:5.1f}|'.format(celsius, fahrenheit))
		print('+-----+-----+')

main()
