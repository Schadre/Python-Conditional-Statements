# Convert numeric grades to letter grades. Assume grades are between 0 to 100
# Research academic grade values

student_grade = int(input("Insert the numerical value of your grade and I will tell you the letter version: "))

if student_grade <= 59:
    print("F")
elif student_grade <= 69:
    print("D")
elif student_grade <= 79:
    print("C")
elif student_grade <= 89:
    print("B")
elif student_grade <= 100:
    print("A")