# deliverable10.py
# A program to convert kilometers to miles
# (heavily!) modified by gull, original convert.py by Susan C.

def main():
	mark = 0
	while True:
		try:
			loop = eval(input("How many distances do you wish to convert? "))
			break
		except:
			print("Please input a number.")
			continue	
	print("Every time you're prompted, please input the amount of kilometers you wish to convert into miles. (To exit at any time, press Ctrl+C. This ends the program.)")
	for i in range(int(loop)):
		while True:
			if i==0 and mark==0:
				kilometers = input("What is the number of kilometers? ")
			else:
				kilometers = input("? ")
			try:
				kilometers = eval(kilometers)
			except:
				print("Please enter a number.")
				mark = 1
				continue
			miles = kilometers * 0.62
			print("The distance is", miles, "miles.")
			break

main()
