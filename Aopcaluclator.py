import sys
from Aop_menu import menu
from Arthimatic_operations import addop,subop,mulop,divop,modop,expop
def aopcalculator():
    while(True):
        menu()
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                addop()
            case 2:
                subop()
            case 3:
                mulop()
            case 4:
                divop()
            case 5:
                modop()
            case 6:
                expop()
            case 7:
                print("Thx for using this Programing")
                sys.exit()
            case _:
                print("Ur Selection of Operation is wrong-try again")