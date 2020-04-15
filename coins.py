def change(amount, coins, answer, solution):
    for coin in coins:
        leftOver = amount - coin
        print("Left over is "  + str(leftOver) + " " + str(amount) +  " " + str(coin))
        if (leftOver > 0):
            solution.append(coin)
            print(solution)
            change(leftOver, coins, answer, solution)
        if (leftOver == 0):
            solution.append(coin)
            answer.append(solution)
            print("Found Solution " + str(answer))
            return
        if (leftOver < 0):
            print("LESS THAN ZERO")
            return

    return len(answer)



change(4, [1,2,3],[],[])


# For N = 4 and C = {1,2,3} there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}

# So given the input
# [1, 2, 3], 4
# Output 4

# For N = 10 and C = {2, 5, 3, 6} there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}
# So given input
# [2, 5, 3, 6], 10
# Output 5
