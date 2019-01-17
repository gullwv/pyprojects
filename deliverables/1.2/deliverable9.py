# deliverable9.py
# A program to convert Fahrenheit temps to Celsius
# (heavily!) modified by gull, original convert.py by Susan C.

def main():
	mark = 0
	while True:
		try:
			loop = eval(input("How many temperatures do you wish to convert? "))
			break
		except:
			print("Please input a number.")
			continue	
	print("Every time you're prompted, please input a temperature you wish to convert into Celsius. (To exit at any time, press Ctrl+C. This ends the program.)")
	for i in range(int(loop)):
		while True:
			if i==0 and mark==0:
				fahrenheit = input("What is the Fahrenheit temperature? ")
			else:
				fahrenheit = input("? ")
			try:
				fahrenheit = eval(fahrenheit)
			except:
				print("Please enter a number.")
				mark = 1
				continue
			celsius = (fahrenheit - 32) * 5 / 9
			print("The temperature is", celsius, "degrees Celsius.")
			break

main()
