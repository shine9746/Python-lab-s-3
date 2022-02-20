#Python programme to copy contents from one file to another file
with open("C:/Users/USER/Desktop/Labs/Python-lab/Python-lab-s-3/Python-lab-s3-13/Python-lab-s3-13-f1.txt","r") as Fileone:

 with  open("C:/Users/USER/Desktop/Labs/Python-lab/Python-lab-s-3/Python-lab-s3-13/Python-lab-s3-13-f2.txt","w") as Filetwo:

    for x in Fileone:
        Filetwo.write(x)
with open("C:/Users/USER/Desktop/Labs/Python-lab/Python-lab-s-3/Python-lab-s3-13/Python-lab-s3-13-f2.txt","r") as Filetwo:
      r =  Filetwo.read()
      print("Contents in second file is : ")
      print(r)
