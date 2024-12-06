data = [[20,25,30],[12,14,16,17,18],[24,26,28,27],[20,29,24,27,28,23],[50,80]]
for i in range(0,len(data) - 1):
    min = data[i]
    index = i
    for j in range(i + 1, len(data)):
        if len(min) > len(data[j]):
            min = data[j]
            index = j
    
        data[i], data[index] = data[index], data[i]
        print(data)    
