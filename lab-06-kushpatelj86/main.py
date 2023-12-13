import calculator
import json
print("Welcome to the tester")



def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
            
        except ValueError:
            print("Input is valid")



def main():
    print("Welcome to the calculator")
    num1 = get_float_input("Enter number 1: ")
    num2 = get_float_input("Enter number 2: ")
    
    try:
        adding = calculator.add(num1,num2)
        subb = calculator.subtract(num1,num2)
        mult =calculator.multiply(num1,num2)
        div = calculator.divide(num1,num2)
    except ZeroDivisionError:
        div = "You can't divide by 0"
    
    


    testvals = {"num1": num1,"num2": num2}
    results = {"addition": adding,"subtraction" : subb, "multiplication" : mult, "division" : div }
    fiename = input("Enter the file name: ")

    try:

        with open(fiename,'w') as jsonfile:
            json.dump(testvals, jsonfile)
            json.dump(results, jsonfile)
    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    main()