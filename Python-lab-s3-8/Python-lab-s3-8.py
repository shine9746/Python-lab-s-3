#Python programme to find the longest word in a text file
with open("C:/Users/USER/Desktop/Labs/Python-lab/Python-lab-s-3/Python-lab-s3-8/Python-lab-s3-8.txt", 'r') as File:
             
              Word = File.read().split()
              Length = len(max(Word, key=len))
              

              for x in Word:
                      if(len(x)== Length):

                        print("The longest word is ",x, "and the length is",Length,"." )
 

 