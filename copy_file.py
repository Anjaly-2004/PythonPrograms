# Copy odd lines from one file to another

f1 = open("sample.txt", "r")
f2 = open("odd.txt", "w")

lines = f1.readlines()

for i in range(len(lines)):
    if i % 2 == 0:
        f2.write(lines[i])

f1.close()
f2.close()

print("Odd lines copied successfully")
