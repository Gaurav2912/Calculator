from art import logo
from replit import clear
# clear consol
# def clear(): return print("\n"*100)

# Addition
def add(a, b): return a + b

# Subtraction
def sub(a, b): return a - b

# Multiplication
def multi(a, b): return a * b

# Division
def divi(a, b): return a / b

# dictionary for calulator
operation_dict = {
  '+':add,
  '-':sub,
  '*':multi,
  '/':divi
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number : "))
  active = True
  
  while active:
    for operation in operation_dict:
      print(operation)
    
    optr = input("Pick an operation : ")
    
    num2 = float(input("What's the secound number : "))
    
    function = operation_dict[optr]
    answer = function(num1, num2)
    
    print(f"{num1} {optr} {num2} = {answer}.")
    
    answer = function(answer,num2)
    conti = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ")
    
    if conti == 'y':
      num1 = answer
    else:
      clear()
      active = False
      calculator()

calculator()