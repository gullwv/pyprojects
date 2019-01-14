# deliverable4.py
# A program to convert Celsius temps to Fahrenheit
# modified by gull, original convert.py by Susan C.

def main():
	mark = 0
	while True:
		try:
			loop = eval(input("How many temperatures do you wish to convert? "))
			break
		except:
			print("Please input a number.")
			continue	
	print("Every time you're prompted, please input a temperature you wish to convert into Fahrenheit. (To exit at any time, press Ctrl+C. This ends the program.)")
	for i in range(int(loop)):
		while True:
			if i==0 and mark==0:
				celsius = input("What is the Celsius temperature? ")
			else:
				celsius = input("? ")
			try:
				celsius = eval(celsius)
			except:
				print("Please enter a number.")
				mark = 1
				continue
			fahrenheit = 9 / 5 * celsius + 32
			print("The temperature is", fahrenheit, "degrees Fahrenheit.")
			break

main()
