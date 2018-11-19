import csv

c = open("mapperOutput.txt", "w")

with open("googleplaystore.csv", "rb") as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    line_count = 0;
    for row in reader:
        if (line_count != 0):
            if (len(row) == 13):
                price = row[7].replace("$", "")
                installs = row[5].replace("+", "").replace(",", "")
                c.write(price + "," + installs + "\n")
        line_count += 1

c.close()