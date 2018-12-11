# File: deliverable6.py
# original chaos.py 2/12/15 by Kevin Grimsley, modified 12/11/18 by gull
# A simple program illustrating chaotic behavior.

def main():
	print("This program will output 100 iterations of three algebraically equivalent eq.")
	x = eval(input("Enter a number for value x between 0 and 1: "))
	y = x
	z = y
	print("===--- x = 3.9 * x * (1 - x) ---===")
	for a in range(100) :
		x = 3.9 * x * (1 - x)
		print(x)
	print("===--- x = 3.9 * (x - x * x) ---===")
	for b in range(100) :
		y = 3.9 * (y - y * y)
		print(y)
	print("===--- x = 3.9 * x - 3.9 * x * x ---===")
	for c in range(100) :
		z = 3.9 * z - 3.9 * z * z
		print(z)

# - gull notes -
#
# now these should all theoretically be the exact same, right?
# wrongo. floats are what we in the buisness world call "super hecking inaccurate".
# due to their really teensy inaccuracies (since they're all really just approximations of numbers), everything falls apart when you try to get this small.
# tl;dr: dont use floats, damnit.
#

main()
