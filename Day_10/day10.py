from  art import logo
print(logo)
def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return  n1 * n2

def div(n1,n2):
    return  n1 / n2

operators ={
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}
def calculator():
    shude_accumulate = True
    num1 = float(input("What's the first number?:"))

    while shude_accumulate:
        for symbol in operators:
            print(symbol)
        operation_symbol = input("Pick an option:")
        num2 = float(input("What's the next number?:"))
        result = operators[operation_symbol](num2 , num2)
        print(f"{num1} {operation_symbol} {num2} = {result} ")

        choice = input(f"Type 'y' to continue calcuting with {result}, or type 'n' to start new")

        if choice == "y":
            num1 = result
        else:
            shude_accumulate = False
            print("\n" * 200)
            calculator()

calculator()