def add():
    fn=float(input("Enter first number"))
    rn=float(input("Enter second number"))
add = fn + sn
print(fn, "+" , rn, add)

def substract():
    fn=float(input("Enter first number"))
    rn=float(input("Enter second number"))
substract = fn - rn
print(fn, "-"  , rn, substract)

def multiply():
    fn=float(input("Enter first number"))
    rn=float(input("Enter second number"))
multiply = fn * rn
print(fn, "*" , sn, multiply)

def divide():
    fn=float(input("Enter first number"))
    rn=float(input("Enter second number"))
divide = fn / rn
print(fn, "/" , rn, divide)

while True:
    userInput = int(input("pilih rumus yang akan di pakai \n1. add\n2. substract\n3. multiply\n4. divide\n\n"))
    elif(userInput == 1):
        add()
    elif(userInput == 2):
        substract()
    elif(userInput == 3):
        multiply
    elif(userInput == 4):
        divide
        