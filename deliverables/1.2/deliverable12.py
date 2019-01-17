# deliverable12.py
# interactive calculator
# by gull

def main():
	while True:
		print("Interactive Calculator")
		print("version 1.0")
		print("Choose an operation and two values to perform that operation on.")
		while True:
			mark = 0
			while True:
				try:
					if mark==0:
						operation = input("What operation would you like to use? \n(+ is add, - is subtract, / is divide, * is multiply, % is modulo)\n")
					else:
						operation = input("? \n(+ add, - subtract, / divide, * multiply, % modulo)\n")
					if operation=="+":
						operation = 0
						break
					elif operation=="-":
						operation = 1
						break
					elif operation=="/":
						operation = 2
						break
					elif operation=="*":
						operation = 3
						break
					elif operation=="%":
						operation = 4
						break
					else:
						print("Please input an operation.")
						mark = 1
						continue
				except:
					print("Please input an operation.")
					mark = 1
					continue
			mark = 0
			while True:
				try:
					if mark==0:
						val1 = eval(input("Input your first value.\n"))
					else:
						val1 = eval(input("? "))
					break
				except:
					print("Please input a number.")
					mark = 1
					continue
			mark = 0
			while True:
				try:
					if mark==0:
						val2 = eval(input("Input your second value.\n"))
					else:
						val2 = eval(input("? "))
					break
				except:
					print("Please input a number.")
					mark = 1
					continue
			if operation==0:
				print(val1+val2)
			elif operation==1:
				print(val1-val2)
			elif operation==2:
				try:
					print(val1/val2)
				except:
					print("stop trying to divide by zero, jerkwad")
			elif operation==3:
				print(val1*val2)
			elif operation==4:
				try:
					print(val1%val2)
				except:
					print("stop trying to divide by zero, jerkwad")
			else:
				print("So long, and thanks for all the fish!")
			try:
				select = input("Would you like to calculate more? (Y/n, default Y) ")
				if select=="n" or select=="N":
					break
				else:
					continue
			except:
				continue
		break
main()
