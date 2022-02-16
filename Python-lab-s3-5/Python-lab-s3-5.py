#Python programme to read text file line by line and store into a list
with open("C:/Users/USER/Desktop/Labs/Python-lab/Python-lab-s-3/Python-lab-s3-4/Python-lab-s3-4.txt",'r') as file:
    
   
   a =  file.readlines()

   b=list(a)

   b = [x.strip() for x in a] #removing new line
 

print("As List :",b)

print(type(b))
