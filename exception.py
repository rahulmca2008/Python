"""
try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero")
else: # when you wan't block of code to be executed on successful completion of try block
    print('your try block is successful')
print('anyway you are proceeding')

try:
    print(0/5)
except ZeroDivisionError:
    print("you can't divide by zero")
else: # when you wan't block of code to be executed on successful completion of try block
    print('your try block is successful')
print('anyway you are proceeding')
"""
# FileNotFoundError Exception

try:
    with open('digits.txt', 'r') as f:
        contents = f.read()
except Exception as e: # Exception is generic exception for all kind of exception
    print('sorry specified file is not present in given path, please check',str(e))
else:
    print('try block executed')

"""
try:
    with open('textfiles/digits.txt','r') as f:
        contents = f.read()
except FileNotFoundError:
    print('sorry specified file is not present in given path, please check')
else:
    print("congrats your try block is through",contents)
"""
