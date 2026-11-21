# Reading a file line by line and storing it into a list

f = open("sample.txt", "r")

lines = []

for line in f:
    lines.append(line.strip())

f.close()

print("List of lines:")
print(lines)
