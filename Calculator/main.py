import re

print(" ")
print("Calculator 2000")
print("Type 'exit' to exit\n")

previous = 0
run = True


def math_equation():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation:")
    else:
            equation = input(str(previous))

    if equation == "exit":
        print("Good Bye")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:;" "ç()]', '', equation )

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)




while run:
    math_equation()