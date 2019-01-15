# deliverable6.py
# modified by gull, original by Susan C. Feb 13 2015
# A program to compute the value of an investment
# carried a user-specified amount of years into the future

def main():
	print("This program calculates the future value")
	print("of an investment over a user-specified amount of years.")
	principal = eval(input("Enter the initial principal: "))
	apr = eval(input("Enter the annual interest rate: "))
	year = eval(input("Enter the amount of years to compute: "))
	for i in range(year):
		principal = principal * (1 + apr)
	print("The value in", year, "years is: ", principal)

main()
