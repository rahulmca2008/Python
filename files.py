# read a file
with open("D:/HariTech/Batch1/digits.txt",'r') as f:
    print(f.read())
with open("textfiles/digits.txt",'r') as f:
    contents = f.read() # when pointer reaches to the end , it keeps one blank space which is new line
    print(contents.rstrip()) # rstrip is used for remove whitespace from right end.
with open('textfiles/digits.txt') as f:
    lines = f.readlines() # readlines gives an iterator list.
for line in lines:
    print(line)
# by default, python reads from text file as a string, if you want to interpret it as interget ,
# do typecast to int or in case of float , do it in float

# write into file
with open('writetext.txt','w') as f:
    f.write("This is my first writing txt file\n")
    f.write("This is my second line\n")
    f.write("This is my third line\n")

with open('writetext.txt','a') as f:
    f.write("This is my fourth line")
