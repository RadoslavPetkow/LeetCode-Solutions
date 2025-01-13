matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

reversed_matrix = [[] for _ in range(len(matrix))]

for i in matrix[::-1]:
    for j in range(len(i)):
        reversed_matrix[j].append(i[j])

print(reversed_matrix)