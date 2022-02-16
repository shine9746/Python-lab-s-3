#Python programme to append  text to a file and display it
with open("C:/Users/USER/Desktop/Labs/Python-lab/Python-lab-s-3/python-lab-s3-3/Python-lab-s3-3.txt","a") as textFile:

 
  a = input("Enter to add : ")

  textFile.write(a)

  textFile = open("C:/Users/USER/Desktop/Labs/Python-lab/Python-lab-s-3/python-lab-s3-3/Python-lab-s3-3.txt","r")
  
  
print(textFile.read())