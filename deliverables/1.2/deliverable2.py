# deliverable2.py
# A program to convert Celsius temps to Fahrenheit
# modified on 1/4/19, original convert.py by Susan C.

def main():
	print("This program converts the temperature in degrees Celsius to degrees Fahrenheit")
	celsius = eval(input("What is the Celsius temperature? "))
	fahrenheit = 9 / 5 * celsius + 32
	print("The temperature is", fahrenheit, "degrees Fahrenheit.")
	input("Press \'Enter\' to quit.")
main()
