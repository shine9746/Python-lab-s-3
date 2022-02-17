#Python programme to read a text file and store into a variable
with open("C:/Users/USER/Desktop/Labs/Python-lab/Python-lab-s-3/Python-lab-s3-6/Python-lab-s3-6.txt","r") as file :

  a = file.readlines()
  a = [x.strip() for x in a]
  
print("a = ",' , '.join(a))

