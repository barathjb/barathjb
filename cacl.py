import re

calc_on = True
previous = 0
print('''
        ***Advanced calculator***
        Type "quit" to exit
        '''
      )
def runcalc():
    global calc_on
    global previous

    if previous == 0:
        equation = input("Enter the equation:")
    else:
        equation=input(str(previous))

    if equation == "quit":
        print("Bye")
        calc_on = False

    else:
        #regex to remove text and unneccessary symbols
        #equation = re.sub('[A-Za-z,\'\"]',"",equation)
        equation = re.sub('[^+^-^*^/^.^\d+]',"",equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous=eval(str(previous)+equation)
            #round off 0 decimals
            if previous==round(int(previous)):
                previous=round(int(previous))


while calc_on:
    runcalc()
