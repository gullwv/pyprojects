# challenge3.py
# by gull on 12/12/18
# find the batting average of some fellow

def main():
	name=str(input("What is the batter's name? "))
	hits=eval(input("How many hits? "))
	atbats=eval(input("How many at bats? "))
	print(name, "has a batting average of ." + str(1/(atbats/hits)) + ".")
	
main()
