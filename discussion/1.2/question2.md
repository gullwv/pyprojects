# 1.2, discussion question 2

since i can't mark down inside codeboxes, i have resorted to placing comments at the end of each line

```py
# File: chaos.py (this is a comment. i will be putting comments at the ends of each line, describing the identifiers, expressions, and types of statements.)
# Created 2/12/15 by Kevin Grimsley (comment.)
# A simple program illustrating chaotic behavior. (comment.)

def main(): #assignment. main is an identifier, def is a keyword.
    print("This program illustrates a chaotic function") #output. print is an identifier. "This program illustrates a chaotic function" is a literal.
    x = eval(input("Enter a number between 0 and 1: ")) #input. x, eval, and input are identifiers. "Enter a number between 0 and 1: " is a literal.
    for i in range(10) : #loop. i and range are identifiers. 10 is a literal.
        x = 3.9 * x * (1 - x) #arithmetic. x is an identifier. 3.9 and 1 are literals.
        print(x) #output. x and print are identifiers.
main() #function call. main is an identifier.
```
