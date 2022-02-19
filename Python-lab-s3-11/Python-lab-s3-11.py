#Python programme to get the size of a plain file
import os

a = os.stat("C:/Users/USER/Desktop/Labs/Python-lab/Python-lab-s-3/Python-lab-s3-11/Python-lab-s3-11.txt")

print("The file size is:",a.st_size,"bytes")