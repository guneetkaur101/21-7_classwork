a = [1,2,3,0,1,1,4,5,2,3]

dup_items = []
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.append(x)

print(dup_items)
