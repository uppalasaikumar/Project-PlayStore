n = open("./out.txt", "r")  # open file, read-only
s = open("./sor.txt", "w") # open file, write
lines = n.readlines() # reading the lines
lines.sort()        # implementing sorting by sorting method
for line in lines:  # iterating through each line
	s.write(line)   # writing the output to the file
n.close()           # closing the file  
s.close()
