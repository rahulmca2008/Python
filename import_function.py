import Functions
import Functions as fn  # alias name
from Functions import test_1
sum_number = Functions.add_number(5,7)
sub_number = fn.subtract_number(5,7)
print(sum_number)
print(sub_number)
test_1("hi","hello")
fn.test_1("dev","raju")
Functions.test_1("hello1",'hello2')

if __name__=='__main__':
    print('from main')