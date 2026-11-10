print("Enter marks obtained in 5 subjects")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne + markTwo + markThree + markFour + markFive
avg = int(tot / 5)

validRange = range(0, 101)
if avg not in validRange:
    print("Invalid input!")
elif avg in range(91, 101):
    print("your grade is A1")
elif avg in range(81, 91):
    print("your grade is A2")
elif avg in range(71, 81):
    print("your grade is A3")
elif avg in range(61, 71):
    print("your grade is B1")
elif avg in range(51, 61):
    print("your grade is B2")
elif avg in range(41, 51):
    print("your grade is B3")
elif avg in range(31, 41):
    print("your grade is C1")
elif avg in range(21, 31):
    print("your grade is C2")
elif avg in range(11, 21):
    print("your grade is C3")
elif avg in range(0, 11):
    print("your grade is F")