def addop():
    print("Enter Two values for Addition:")
    a, b = float(input()), float(input())
    print("sum({},{})={}".format(a, b, a + b))
def subop():
    print("Enter Two values for Substraction:")
    a, b = float(input()), float(input())
    print("sub({},{})={}".format(a, b, a - b))

def mulop():
    print("Enter Two values for Multiplication:")
    a, b = float(input()), float(input())
    print("Mul({},{})={}".format(a, b, round(a * b, 2)))

def divop():
    print("Enter Two values for Division:")
    a, b = float(input()), float(input())
    print("Normal Division({},{})={}".format(a, b, a / b))
    print("Floor Division({},{})={}".format(a, b, a // b))
def modop():
    print("Enter Two values for Modulo Division:")
    a, b = float(input()), float(input())
    print("ModDiv({},{})={}".format(a, b, a % b))

def expop():
    a, b = float(input("Enter Base:")), float(input("Enter Power:"))
    print("power({},{})={}".format(a, b, a ** b))