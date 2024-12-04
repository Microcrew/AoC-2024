"""
#Part 1

left = []
right = []
with open('Input_Day1.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        splitline= line.split("   ")
        left.append(int(splitline[0]))
        right.append(int(splitline[1]))

left.sort()
right.sort()

ans = 0
for i in range(len(left)):
    ans += abs(left[i] - right[i])

print(ans)
"""

#Part 2

left = []
right = []
with open('Input_Day1.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        splitline= line.split("   ")
        left.append(int(splitline[0]))
        right.append(int(splitline[1]))


ans = 0
for i in range(len(left)):
    ans += left[i]*right.count(left[i])

print(ans)
