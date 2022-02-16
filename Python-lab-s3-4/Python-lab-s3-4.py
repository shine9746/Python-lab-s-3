#Python programme to read n lines of a text file
with open("C:/Users/USER/Desktop/Labs/Python-lab/Python-lab-s-3/Python-lab-s3-4/Python-lab-s3-4.txt","r") as textFile:
   a = textFile.readlines()
   n = int(input("Enter the last n lines : "))
   b = a[-n:]

print("The last n lines of text file is : ")

for x in b:
    print(x)
   



