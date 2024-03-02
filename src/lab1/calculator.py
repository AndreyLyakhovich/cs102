print("Hello, this is a simple calculator in Python")
print(
    "You can use your terminal to type first number and second number and choose which operation you want to use from the four available ones"
)

q1 = float(input("Type the first number: "))
q2 = float(input("Type the second number: "))

OPER = int(
    input(
        "Which operation you want to use? \n Type 1 to use addition \n Type 2 to use subtraction \n Type 3 to use division \n Type 4 to use multiplication \n"
    )
)

if OPER == 1:
    RES = q1 + q2
    OP = "Addition"
if OPER == 2:
    RES = q1 - q2
    OP = "Subtraction"
if OPER == 3:
    RES = float(q1 / q2)
    OP = "Division"
if OPER == 4:
    RES = q1 * q2
    OP = "Multiplication"
print("RESult of ", OP, " = ", RES)
