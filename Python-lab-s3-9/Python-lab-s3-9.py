#Python programme to count the number of lines in a text file
with open("C:/Users/USER/Desktop/Labs/Python-lab/Python-lab-s-3/Python-lab-s3-9/Python-lab-s3-9.txt", 'r') as File:

  count=0

  file = File.read().split("\n")

  for x in file:
		 if x:
		  count += 1
print("The number of lines in text file is : ",count)
