"""if the current file is run standalone by user __name__ will be set to '__main__' otherwise
if imported it will be module name"""
def test_1(

        msg1: str,
        msg2: str,
):
    """ This function is to display message"""
    print(f"your message is : {msg1}")
    print(f"your another is : {msg2}")

def add_number(
        number1:int, # parameter1
        number2:int, # parameter2
):
    """ To add two numbers"""
    return number1+number2

def subtract_number(
        number1:int, # parameter
        number2:int, # parameter
):
    """ To subtract two numbers"""
    return number1-number2


if __name__ == '__main__':
    msg1 = input("Enter message1")
    msg2 = input("Enter message2")
    test_1(msg1,msg2)
    total = add_number(2,3) # positional arguments
    print(f"Sum of two numbers using positional arguments : {total}")
    total = add_number(number2=3,number1=2) # keyword arguments
    print(f"Sum of two numbers using keyword arguments : {total}")
    total = subtract_number(2, 3)  # positional arguments
    print(f"Subtract of two numbers using positional arguments : {total}")
    total = subtract_number(number2=2, number1=3)  # keyword arguments
    print(f"Subtract of two numbers using keyword arguments : {total}")
else:
    print('called from import module')
