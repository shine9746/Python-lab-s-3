#Python programme to combine each lines of first file with the corresponding lines of the second file.
with open("C:/Users/USER/Desktop/Labs/Python-lab/Python-lab-s-3/Python-lab-s3-14/Python-lab-s3-14-f1.txt","r") as File1:
  with open("C:/Users/USER/Desktop/Labs/Python-lab/Python-lab-s-3/Python-lab-s3-14/Python-lab-s3-14-f2.txt","r") as File2:
      with open("C:/Users/USER/Desktop/Labs/Python-lab/Python-lab-s-3/Python-lab-s3-14/Python-lab-s3-14-f3.txt","w") as File3:
     
       f1 = File1.readlines()
       f2= File2.readlines()
      
        
       for x in range(len(f1)):

        m = f1[x].strip() + " " +f2[x]           #striped,seperated and combined

        File3.write(m)
      

with open("C:/Users/USER/Desktop/Labs/Python-lab/Python-lab-s-3/Python-lab-s3-14/Python-lab-s3-14-f3.txt","r") as File3:
   
        r = File3.read()
        print("The combined lines of first file and second file are : \n")
        print(r)


