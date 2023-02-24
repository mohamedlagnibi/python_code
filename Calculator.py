try:
    #Arithmetic Operation
    print("""Select a number of Operation you would to do:
         1 : Addition
         2 : Substraction
         3 : Multiplication
         4 : Division
         5 : Exponentiation
         6 : Quit
    """)
    class Number:
        def __init__(self, num1, num2):
            self.num1 = num1
            self.num2 = num2
            
        def addition(self): 
            return num1 + num2
        
        def substraction(self):
            return num1 - num2
        
        def multiplication(self):
            return num1 * num2
        
        def division(self):
            return num1 / num2
            
        def exponentiation(self):
            return num1 ** num2

                   
    def calculation():
        if choice == 1:
            print(f"{num1} + {num2} = {number.addition()}")   
        elif choice == 2:
            print(f"{num1} - {num2} = {number.substraction()}")
        elif choice == 3:
            print(f"{num1} * {num2} = {number.multiplication()}")
        elif choice == 4:
            print(f"{num1} / {num2} = {number.division()}")
        elif choice == 5:
            print(f"{num1} ** {num2} = {number.exponentiation()}")
        
                
    choice = int(input("Enter number of operation: ")) # prompts from users
    
    if choice <= 5:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        number = Number(num1, num2)
        calculation()
    elif choice == 6:
        print("Goodbye")
    else:
        print("Invalid choice")
             
except ValueError:
    print("Error: Please enter an intger number")
except ZeroDivisionError:
    print("Error: you can't divide by Zero")
