#Python programme to print n lines of a text file
with open("C:/Users/USER/Desktop/Labs/Python-lab/Python-lab-s-3/python-lab-s3-2/Python-lab-s3-2.txt","r") as textFile:

  n = int(input("Enter a number between 1 and 5 : "))

  for x in range(n):

   print(textFile.readline())

