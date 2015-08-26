# menu en python
import os

def menu(principal, op1,op2,op3,op4,op5):
    
    print(" MENU".center(45, "-"))
    print("\n\t\t -%s- \n"%(principal.upper().title()),
          "\n\t1- %s"%(op1.capitalize()),
          "\n\t2- %s"%(op2.capitalize()),
          "\n\t3- %s"%(op3.capitalize()),
          "\n\t4- %s"%(op4.capitalize()),
          "\n\t5- %s"%(op5.capitalize()),)
    print("".center(45, "-"))
#menu("principal","uno","dos","tres","cuarto","cinco")
