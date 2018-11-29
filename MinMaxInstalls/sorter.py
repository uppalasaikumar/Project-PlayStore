o = open("./output/o.txt", "r")                   #opens the file as a readonly
s = open("./output/s.txt", "w")                #opens the files as a writeonly

lines = o.readlines()                                        #reads the whole file
lines.sort()                                                 #sorts the file

for line in lines:                                           #writes in a new file
  s.write(line)

o.close()
s.close()