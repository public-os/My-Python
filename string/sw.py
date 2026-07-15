s = "l|*e*et|c**o|*de|"
words = s.split("|")
print(words)
c = 0 
for w in words:
    if not w.startswith("*") and w != "":
        c+=1
print(c)
print(4)