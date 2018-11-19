n = open("./output/o.txt", "r",encoding="utf8")  # open file, read-only
s = open("./output/s.txt", "w",encoding="utf8") # open file, write
lines = n.readlines()
lines.sort()
for line in lines:
	s.write(line)
n.close()
s.close()
