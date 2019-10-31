# This is the grading program we looked at earlier


# 4) Grading program - if score is > 90 you get an A,
##  > 80 < 90 you get a B
##  > 70 < 80 a C
##  > 60 < 70 a D
## anything else you flunk

grade = 55

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("You Flunked!")


# We changed it to a Function:

def grader(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "You Flunked!"

g = grader(60)
print(g)


# to get grades for the class use a list

grades = [75,80,90,60,65,85]

# find the class average grade and use the function, grader, we just wrote

def term_grader(grade):
    term = sum(grade) / len(grade)
    return grader(term)

print(term_grader(grades))


## Note, I cheated with the sum function:
# 
# Here is a home grown one
#

def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers

def term_grader2(grade):
    term = sum_list(grade) / len(grade)
    return grader(term)

print(term_grader2(grades))

# 1. Write a program to multiply the numbers in a list.
## Hint *= is a thing

def multiply_list(items):
    mult_num = 1
    for x in items:
        mult_num *= x
    return mult_num

nums = [ 3,5,2,4]
multiply_list(nums)



# 2. Write a program to get the largest number in a list


## Coding takes practice more than brains
## https://exercism.io/ is a good practice site for exercises like these

# A simple way

def largest(items):
    items.sort()
    return items[-1]

largest(nums)

## A do it yourself way

def my_largest(items):
    my_max = items[0]
    for x in items:
        if my_max < x:
            my_max = x
    return my_max

my_largest(nums)

# 3. Assume: 


law_class = ["Matthew", "Hunter", "Marianna", "Brittany", "Harrison", "James","Bradley"]
# Print "Hunter"

print(law_class[1])
 
 # remember a list is similar to an array in other languages it starts with 0

# 4. Print out each name in law_class
## Python provides an easy way to move through a list " for x in list: "

for x in law_class:
    print(x,end=" ")

# 5. Put the law_class in alphabetical order and print it

law_class.sort()

for x in law_class:
    print(x,end=" ")


## list -  order matters

fam = ["Tom", "Carole", "Baby Brooke"]

fam2 = ["Carole", "Tom", "Baby Brooke"]

fam == fam2    # False

## dictionary Order doesn't matter

fam = {'husband': 'Tom', 'wife': 'Carole', 'grand_baby': 'Baby Brooke'}

fam2 = {'wife': 'Carole', 'grand_baby': 'Baby Brooke', 'husband': 'Tom'}

## Dictionary like json  Javascript Object Notation   - similar notation
## json key must be string with double quotes

# { "family":
#    {"husband": "Tom", 
#     "wife": "Carole",
#      "grand baby": "baby brooke"} 
# }

fam == fam2    # True

1. ## print the keys in fam


2. ## print the values in fam

3. work through the tic tac toe board page 113 

# Tic Tac Toe  Board

theBoard = {'top-L': ' ', 'top-M':' ', 'top-R':' ',
            'mid-L': ' ', 'mid-M':' ', 'mid-R':' ',
            'low-L': ' ', 'low-M':' ', 'low-R':' '}


def printBoard(board):
    print(' '+ board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'x'
for i in range(9):
    print('Turn for ' + turn + '_ on which space? ')
    move = input()
    theBoard[move] = turn
    if turn == 'x':
        turn = '0'
    else:
        turn = 'x'

printBoard(theBoard)



