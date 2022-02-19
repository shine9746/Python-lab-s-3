#Python programme to write a list to text file
with open("C:/Users/USER/Desktop/Labs/Python-lab/Python-lab-s-3/Python-lab-s3-12/Python-lab-s3-12.txt","a") as File:

 List = File.write("apple,mango,pineapple,guava,plum,cherry")
with open("C:/Users/USER/Desktop/Labs/Python-lab/Python-lab-s-3/Python-lab-s3-12/Python-lab-s3-12.txt","r") as File:

 List = File.read().split(" ")

 x = list(List)
 print("List = " ,x)
 print(type(x))



