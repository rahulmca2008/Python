import json
# javascript object notation

numbers = [2,3,5,9,12]
filename = "jsonfiles/numbers.json"
with open(filename,'w') as f:
    json.dump(numbers,f)
with open(filename,'r') as f:
    print(json.load(f))
username = input("enter any name")
with open(filename,'a') as f:
    json.dump(username,f)