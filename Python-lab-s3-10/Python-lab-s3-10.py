#Python programme to count the words frequency on a text file
with open("C:/Users/USER/Desktop/Labs/Python-lab/Python-lab-s-3/Python-lab-s3-10/Python-lab-s3-10.txt", 'r') as File:

 a = File.read().strip()  #read and stripped unwanted nlines


b = {}   
	
words = a.casefold().split(" ")  #splited into word and caseinsensitive
		
	
for x in words:
	if x in b:
		b[x] += 1
	else:
		b[x] = 1
print("Repeating words of text file is:")
for x in b:
	print(x,":",b[x])


