#Python programme to read text file line by line and store into a array
with open("C:/Users/USER/Desktop/Labs/Python-lab/Python-lab-s-3/Python-lab-s3-7/Python-lab-s3-7.txt",'r') as file:
    
   
   array =  file.readlines()

   array=list(array)

   array = [x.strip() for x in array] #removing new line
 

print(" Array :",array)

