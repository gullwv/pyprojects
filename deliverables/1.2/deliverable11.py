# deliverable11.py
# A program to convert kilobytes to kibibytes
# (heavily!) modified by gull, original convert.py by Susan C.

def main():
	mark = 0
	print("This program converts kilobytes to kibibytes.")
	while True:
		try:
			loop = eval(input("How many sizes do you wish to convert? "))
			break
		except:
			print("Please input a number.")
			continue	
	print("Every time you're prompted, please input the amount of kilobytes you wish to convert into kibibytes. (To exit at any time, press Ctrl+C. This ends the program.)")
	for i in range(int(loop)):
		while True:
			if i==0 and mark==0:
				kb = input("How many kilobytes would you like to convert? ")
			else:
				kb = input("? ")
			try:
				kb = eval(kb)
			except:
				print("Please enter a number.")
				mark = 1
				continue
			kib = kb * 0.9765625
			print("The converted size is", str(kib) + "KiB.")
			break

main()
