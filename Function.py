def get_matrix(n, m, value):
    mat=[]
    for a in range(0, n):
        mat1=[]
        for b in range(0, m):
            mat1.append(value)
        mat.append(mat1)
        return mat

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)