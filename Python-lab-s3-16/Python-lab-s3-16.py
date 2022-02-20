#Python programme to remove newline characters
with open("C:/Users/USER/Desktop/Labs/Python-lab/Python-lab-s-3/Python-lab-s3-16/Python-lab-s3-16.txt",'r') as file:
    
   
   a =  file.readlines()

   b=list(a)

   print("Orginal list : ",b, '\n')

   b = [x.strip() for x in a] #removing new line
 

print("After removal of newline characters : ")

print(",".join(b))

