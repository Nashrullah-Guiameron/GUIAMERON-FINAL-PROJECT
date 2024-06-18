a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

row_sums = []
col_sums = [0]*len(a[0])

for i in range(len(a)):
    row_sum = 0
    for j in range(len(a[i])):
        row_sum += a[i][j]
        col_sums[j] += a[i][j]
    row_sums.append(row_sum)

print('Sum of Row:', row_sums)
print('Sum of Column:', col_sums)