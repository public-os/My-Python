ele = [1,2,4,4,3,1,1,2]
freq = {}
for i in ele:
    freq[i]=freq.get(i,0)+1
# print(freq)
result = []
while freq:
    max_key = max(freq, key=freq.get)
    result.extend([max_key] * freq[max_key])
    del freq[max_key]
print(result)