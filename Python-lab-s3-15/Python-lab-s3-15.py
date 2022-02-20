#Python programme to read a random line from a file
import random
with open("C:/Users/USER/Desktop/Labs/Python-lab/Python-lab-s-3/Python-lab-s3-16/Python-lab-s3-16.txt","r") as file:

        read = file.readlines()

        randm = random.choice(read)

        print("The random line in file is: ",randm)

                  