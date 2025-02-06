from caluculator_art import logo
def addition(n1,n2):
    return n1+n2
def subtraction(n1,n2):
    return n1-n2
def multiplication(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations={
    "+":addition,
    "-":subtraction,
    "*":multiplication,
    "/":divide
    }
def calculator():
    print(logo)
    num1=float(input("what is the first number:"))
    #num2=int(input("what is the second number:"))
    for symbol in operations:
        print(symbol)
    should_continue=True

    while should_continue:
        operational_symbol=input("pick an operation from the above list:")
        num2=float(input ("what is the next number:"))
        calculation_function=operations[operational_symbol]
        answer=calculation_function(num1,num2)

        print(f"{num1} {operational_symbol} {num2} = {answer}")
        
        if input("type 'y' to continue calculating with {answer}, or type 'n' to exit to satrt new calculation:")=="y":
            num1=answer
        else:
            should_continue=False
            calculator()
calculator()
             
    
