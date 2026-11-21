import csv

# Creating a dictionary
data = [
    {"Name": "Anagha", "Age": 20, "Course": "Python"},
    {"Name": "Ammu", "Age": 21, "Course": "Java"},
    {"Name": "Arya", "Age": 19, "Course": "C++"}
]

# Writing dictionary to CSV file
f = open("student.csv", "w", newline="")

writer = csv.DictWriter(f, fieldnames=["Name", "Age", "Course"])

writer.writeheader()
writer.writerows(data)

f.close()

# Reading CSV file
f = open("student.csv", "r")

reader = csv.reader(f)

print("Contents of CSV file:")

for row in reader:
    print(row)

f.close()
