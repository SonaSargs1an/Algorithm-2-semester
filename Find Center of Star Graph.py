def find(edges):
    checked = []
    for edge in edges:
        for centre in edge:
            if centre not in checked:
                checked.append(centre)
            else:
                return centre

print(f"ex 1 =  {find([[10, 20], [30, 10], [10, 40]])}")   
print(f"ex 2 = {find([[7, 8], [9, 7], [7, 11], [12, 7]])}") 