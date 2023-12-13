def early_exit(numbers):
    for num in numbers:
        try:
            if num < 0:
                break
            print(num)
        finally:
            print("End of iteration")


early_exit([2,3,5,6,4,6,2,4])




#1
def isInteger(num):
    try:
        if  not isinstance(num, int):
            raise ValueError("Not a integer")
    except ValueError:
        print("Error found")

#2
def findVaalue(nums = [1,2,3,4,5,6],index=0):
    try:
        if index < 0 or index >= len(nums):
            raise IndexError("Index not found")
    except IndexError:
            print("Error found")


#3
def strToInt(str="124"):
    try:
        itb = int(str)
        print(itb)
    except ValueError:
        print("error")
        raise
  


#4
def devide(a,b):
    try:
        if  b == 0:
            raise ZeroDivisionError("Index not found")       
    except ArithmeticError:
        print("you can't devide by 0")








#5
def concatenate(b):
  try: 
        if not isinstance(b, str): 
         raise ValueError("Not a str")
  except ValueError:
        print("Error found")


#6
def indss():
    try:
        nums = [1,2,3,4,5,6]
        ind = nums[8]
        raise ValueError("Invalid index used")
    except IndexError:
         print("Invalid index")





#7
class DivisionError(Exception):
    pass

def devide(a,b):
    if b == 0:
        raise DivisionError("devide not valid")
    return a / b


#8
class NegativeNumberError(Exception):
    pass

def print_square(a):
    if a < 0:
        raise NegativeNumberError("devide not valid")
    return a ** 2





#9
class AgeError(Exception):
    pass

def age(a):
    if a < 0 or a > 150:
        raise AgeError("invalid age")
    return a


#10
class AuthenticationError(Exception):
    pass

class LoginError(AuthenticationError):
    pass

class LogoutError(LoginError):
    pass


login = False

def logino():
    global login
    if login:
        raise LoginError("fail to login")
    login=True
    print("sucessful login")

logout = True

def logouytirew():
    global logout
    if logout:
        raise LoginError("fail to logout")
    logout=False
    print("sucessful logout")




try:
    logino()
    logino()
except LoginError as e:
    print(f"Login Error: {e}")

try:
    logouytirew()
    logouytirew()
except LogoutError as e:
    print(f"Logout Error: {e}")


#11
class DatabaseError(Exception):
    pass

class ConnectionError(DatabaseError):
    pass

class QueryError(DatabaseError):
    pass

def databaseop(op_type):
    if op_type == "query":
        raise QueryError("query not found")
    elif op_type == "connection":
        raise ConnectionError("not connected")
    else:
        print(" operation successful")

#12
class NegativeBalanceError(Exception):
    pass

money = 4000000
def withdraw(amount):
    if amount > 4000000:
        raise NegativeBalanceError("You cannt withdraw more than the balance")
    else:
        money -= amount
        print("Withdrawl sucessful")


#13
class UserError(Exception):
    pass

class UserNotFoundError(UserError):
    pass

class UserAlreadyExistsError(UserError):
    pass



def databaseop(op_type):
    if op_type == "not found":
        raise UserNotFoundError("USer not found")
    elif op_type == "already exists":
        raise ConnectionError("already exists")
    else:
        print(" operation successful")




#14

def safe_divide(a, b):
    try:
        num = a / b
        print("Division done")
        return num
    except ZeroDivisionError:
        print("Zero division error")




#15
def open_file():
    while True:
        ener = input("Enter file name")
        try:
                file1= open(ener, 'r')
                file1.close()
                break
        except FileNotFoundError as e:
            print("File not found")
