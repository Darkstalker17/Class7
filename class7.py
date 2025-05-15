'''
Identity operator
Outline:
Write a program to illustrate the use of 'is' identity operator
'''
x = 5
if (type(x) is int):
    print("TRUE")
else:
    print("FALSE")
y = 6.54
if (type(y) is int):
    print("FALSE")
else:
    print("TRUE")
a = 20
b = 201
if a is b:
    print("a and b are identical")
else:
    print("Both are not identical")
'''
Bitwise operator
Outline:
Write a program to apply the right shift and left shift bitwise operator.
'''
a = 10
print(a>>1)
'''
Grading system
Outline:
Write a program to show students grades by entering five subject marks and calculating average marks and grades.
For example, if the average is between 91 to 100 grade is A+, A is between 81 to 90, and so on, do it till grade E?
'''
m_grade = int(input("Enter Your marks in Math: "))
s_grade = int(input("Enter Your marks in Science: "))
e_grade = int(input("Enter Your marks in English: "))
h_grade = int(input("Enter Your marks in History: "))
g_grade = int(input("Enter Your marks in Geography: "))
g = (m_grade + s_grade + e_grade + h_grade + g_grade)/5
if g >= 91 and g<=100:
    print("Your grade is A+")
elif g >= 81 and g<=90:
    print("Your grade is A")
elif g >= 71 and g<=80:
    print("Your grade is B")
elif g >= 61 and g<=70:
    print("Your grade is C")
elif g >= 51 and g<=60:
    print("Your grade is D")
elif g >= 41 and g<=50:
    print("Your grade is E")
else:
    print("You Failed")