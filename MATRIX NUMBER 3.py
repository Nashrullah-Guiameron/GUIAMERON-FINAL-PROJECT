a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

for i in range(len(a)):
    for j in range(len(a[i])):
        if i==j:
            print(a[i][j])

primary_diagonal = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if i==j:
            primary_diagonal = primary_diagonal + a[i][j]

print(primary_diagonal)
print()
print()
n = 3
for i in range(len(a)):
    for j in range(len(a[i])):
        if i+j == (n-1):
            print(a[i][j])

primary_diagonal = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if i+j == (n-1):
            primary_diagonal = primary_diagonal + a[i][j]

print(primary_diagonal)