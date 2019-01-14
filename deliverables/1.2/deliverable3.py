# deliverable3.py
# modified by gull on jan 4 2019, original by John F. May 23 2016
# A simple program to average two, er, three exam scores
# Illustrates use of multiple input

def main():
    print("This program computes the average of three exam scores. ")

    score1, score2, score3 = eval(input("Enter three scores separated by a comma: "))
    average = (score1 + score2 + score3) / 3

    print("The average of the scores is: ", average)

main()
