from collections import Counter
n = int(raw_input())
words = [raw_input().strip() for _ in range(n)]
counts = Counter(words)
print len(counts)
for word in words:
    value = counts.pop(word, None)
    if value == None:
        continue
    else:
        print value,