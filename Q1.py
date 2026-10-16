# Write a program to read a file and count how many vowels are present in its content


f = open("text.txt", "r")

data = f.read()
count = 0

for ch in data:
    if ch.lower() in "aeiou":
        count = count + 1

print("Total vowels:", count)

f.close()
