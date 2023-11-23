# This code get 3 kinds of user inputs
# sizes is the length of the 2 subsequences eg: 3 5
# a and b are the 2 subsequences. both are get inputs as the space separated strings
# eg: for a :-1 2 3
# eg: for b :- 2 3 4 6 5
# code put a and b into integer arrays

from array import array
sizes = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
rows = sizes[0]
cols = sizes[1]
c = [[0] * (cols+1) for _ in range(rows+1)]

for i in range(rows):
    for j in range(cols):
        if(i==0 or j==0):
            c[i][j] = 0

for i in range(1,rows+1):
    for j in range(1,cols+1):
        if (a[i - 1] == b[j - 1]):
            c[i][j] = c[i - 1][j - 1] + 1
        else:
            c[i][j] = max(c[i][j - 1], c[i - 1][j])

lcs_length = c[rows][cols]
lcs_sequence = array('i', [0] * lcs_length)
i, j = rows, cols
count = 0
while i > 0 and j > 0 and count < c[rows][cols]:
        if a[i-1] == b[j-1]:
            lcs_sequence[lcs_length - 1] = a[i-1]
            i -= 1
            j -= 1
            lcs_length -= 1
            count += 1
        elif c[i - 1][j] == c[i][j - 1]:
            i -= 1
        elif c[i - 1][j] > c[i][j - 1]:
            i -= 1
        else:
            j -= 1

print(' '.join(map(str, lcs_sequence)))
