l1 = [2, 4, 3]
l2 = [5, 6, 4]
outList = []

strL1 = ""
strL2 = ""
for i in range(len(l1) - 1, -1, -1):
    print(i)
    strL1 += str(l1[i])

for i in range(len(l2) - 1, -1, -1):
    print(i)
    strL2 += str(l2[i])
print(strL1)
print(strL2)
nitls = str(int(strL2) + int(strL1))

llol = [int((nitls[char])) for char in range(len(str(nitls)) - 1, -1, -1)]
for char in range(len(str(nitls)) - 1, -1, -1):
    print(nitls[char])

print(llol)
