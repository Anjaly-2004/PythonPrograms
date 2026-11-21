import csv

f = open("sample.csv", "r")

reader = csv.reader(f)

for row in reader:
    print(row)

f.close()
