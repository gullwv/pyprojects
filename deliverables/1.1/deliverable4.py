# File: deliverable4.py
# modified on 11/19/18 by gull; original 'chaos.py' reated 2/12/15 by Kevin Grimsley
# a simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20) :
        x = 3.9 * x * (1 - x)
        print(x)
main()
