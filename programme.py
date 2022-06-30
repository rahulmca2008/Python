# Given an array , could you please tell the frequency of elements
# sort an array in python
# Given in list of element, sum of two element is z
# write a palindrone programme
# write a fibonacci programme
# write a programme to get maximum sum of any 2 numbers

list1 = ['rakesh', 'devraju', 'mukesh', 'devraju', 'rakesh', 'mukesh', 'devraju', 'suresh']
list2 = [2,3,5,3,2,1,2,3,20]

def freq_list_element(list1):
    """ to count the frequency of elements in list"""
    dict1 = {}
    for index, value in enumerate(list1):
        if dict1.get(value) is not None:
            dict1[value] = dict1[value] + 1
        else:
            dict1[value] = 1
    print(dict1)
    return dict1
freq_list_element(list1[:])


def sort_element(list1):
    n = len(list1)
    for i in range(n):
        for j in range(i,n,1):
            if list1[i]>list1[j]:
                list1[i],list1[j] = list1[j],list1[i]
    print(list1)
    return list1


sort_element(list2[:])


def sum_element(list1,z):
    n = len(list1)
    for i in range(n):
        for j in range(i,n,1):
            if ((i!=j) & ((list1[i]+list1[j])==z)):
                print(list1[i],list1[j])
                return list1[i],list1[j]


sum_element(list2[:],8)

def palindrone(str1):
    if str1 == str1[::-1]:
        return True
    else:
        return False


print(palindrone('amma'),palindrone('raman'))

def palindrone_digit(number):
    num = str(number)
    if num == num[::-1]:
        return True
    return False
print(palindrone_digit(121),palindrone_digit(1234))

def maximum_sum(list1):
    max_sum = 0
    n = len(list1)
    for i in range(n):
        for j in range(i+1,n,1):
            if (list1[i] + list1[j])>max_sum:
                max_sum = list1[i] + list1[j]
    return max_sum


print(maximum_sum(list2))


def max_sum_two_elements(list1):
    list1 = sorted(list1)
    return list1[-1] + list1[-2]


print(max_sum_two_elements(list2[:]))









