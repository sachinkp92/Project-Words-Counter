#Words Counter

my_file=open("file.txt","r")
count=0
for line in my_file:
    words=line.split(" ")
    count+=len(words)
my_file.close()
print("Numbers of words in a text file:",count)


