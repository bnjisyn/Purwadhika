# ### basic syntax
# zip(data iterables1, data iterables2)
# akan menghasilkan object Zip, perlu dikonversi

A = [1,2,3,4,5]
B = ["A", "B", "C", "D", "E"]

zip_A = list(zip(A, B))
zip_B = dict(zip(B, A))

print(zip_A)
print(zip_B)

A = [1,2,3,4,5]
B = ["A", "B", "C"]

zip_E = dict(zip(A, B))

print(zip_E)