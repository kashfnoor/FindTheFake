import time

def FindFake(coins):
    weighings = 0
    n = len(coins)

    groups = [(0, 3), (3, 6), (6, 8)]  # Group A, B, C

    weighings += 1
    sumA = sum(coins[groups[0][0]:groups[0][1]])
    sumB = sum(coins[groups[1][0]:groups[1][1]])

    if sumA < sumB:
        target_group = groups[0]  #groupA
    elif sumB < sumA:
        target_group = groups[1]  #groupB
    else:
        target_group = groups[2]  #groupC

    weighings += 1
    start, end = target_group

    for i in range(start, end - 1):  
        if coins[i] < coins[i + 1]:
            return i + 1, weighings  
        elif coins[i + 1] < coins[i]:
            return i + 2, weighings

    return end, weighings

coins = [10] * 8

fake_index = int(input("Enter the index of fake coin (1-8): "))
coins[fake_index - 1] = 9

start_time = time.perf_counter_ns()

fake_coin, weighings = FindFake(coins)

end_time = time.perf_counter_ns()
execution_time = end_time - start_time


print("\nFake coin found at position:", fake_coin)
print("Number of weighings:", weighings)

best_case = weighings
worst_case = weighings


print("Best Case Time (weighings):", best_case)
print("Worst Case Time (weighings):", worst_case)

print("\nExecution Time:", execution_time, "seconds")