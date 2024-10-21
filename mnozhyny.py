coordinates = input("введіть координати: ").split()
A = set(map(int,coordinates ))
B = set()

A_list = list(A)

for i in range(len(A_list)):
    for j in range (i + 1, len(A_list)):
        distance = abs(A_list[i] - A_list[j])
        B.add(distance)
    
print("відстані між точками: ", B)