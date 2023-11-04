
lst = [2, 4, 5, 3, 1]
new_lst = []
val = None

for item in range(len(lst-1)):
    if val == None or lst[item] < lst[val]:
        val = item
new_lst.append(lst[val]) 








