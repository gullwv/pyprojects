# deliverable7.py
# modified by gull, original by Susan C. Feb 13 2015
# A program to compute the value of an investment
# carried a user-specified amount of years into the future

def main():
	print("This program calculates the future value")
	print("of an investment over a user-specified amount of years.")
	while True:
		try:
			invper = eval(input("Enter the amount to invest each year: "))
			break
		except:
			print("Please input a number.")
			continue
	while True:
		try:
			apr = eval(input("Enter the annual interest rate: "))
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
	principal = invper
	for i in range(year):
		if i != 0:
			principal = principal + invper
		principal = principal * (1 + apr)
	print("The value in", year, "years is: ", principal)

main()
