# deliverable8.py
# modified by gull, original by Susan C. Feb 13 2015
# A program to compute the value of an investment
# carried a user-specified amount of years into the future

def main():
	print("This program calculates the future value")
	print("of an investment over a user-specified amount of years.")
	while True:
		try:
			principal = eval(input("Enter the principal: "))
			break
		except:
			print("Please input a number.")
			continue
	while True:
		try:
			rate = eval(input("Enter the rate: "))
			break
		except:
			print("Please input a number.")
			continue
	while True:
		try:
			periods = eval(input("Enter the amount of periods in a year: "))
			break
		except:
			print("Please input a number.")
			continue
	while True:
		try:
			year = eval(input("Enter the amount of years to compute: "))
			break
		except:
			print("Please input a number.")
			continue
	for i in range(year*periods):
		principal = principal * (1 + rate)
	print("The value in", year, "years is: ", principal)

main()
