
s = "abcabcbb"

high = 0
for i in range(len(s)):
    unused = []
    for j in range(i, len(s)):

        if s[j] not in unused:
            unused.append(s[j])
        elif s[j] in unused:
            break
    if len(unused) > high:
        high = len(unused)
if len(unused) > high:
    high = len(unused)
    
print(high)
