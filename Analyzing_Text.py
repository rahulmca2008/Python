filenames = ['textfiles/Alice_in_Wonderland.txt','textfiles/moby_dick.txt']
def count_words(filename):
    try:
        with open(filename,encoding='utf-8') as f: # when system encoding and the file encoding does not match,
            # in that case encoding argument is used
            contents = f.read()
    except FileNotFoundError :
        print('file not found')
    else:
        words = contents.split(" ")
        num_words = len(words)
        print(f"The file {filename}  has about {num_words} words")


for filename in filenames:
    count_words(filename)


