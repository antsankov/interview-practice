def rotate(arr, shift):
    answer = arr
    for i in range (0,shift):
        last = answer[-1]
        answer = [last] + answer
        answer.pop()

    print(answer)

rotate([1,2,3,4,5,6],3)

# Time complexity is O(n)
# In place would involve swapping of the different variables between a third variable.