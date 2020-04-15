def convertToInt(binary):
    answer = 0
    swap = binary
    swap.reverse()
    
    for i in range (0, len(swap)):
        if (swap[i] == 1):
            val = 2 ** i
            answer += val
    
    print(answer)

convertToInt([1,0,0,0,1,0,0,0])
convertToInt([1,0,1,1,0,0])