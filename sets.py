my_list = [1,1,2,2,3,3,4]
print(set(my_list)) #{1,2,3,4}

my_set = {1,2,3,4,5,5}
print(my_set) # {1,2,3,4,4,5}

my_set.add(6)
print(my_set) # {1,2,3,4,5,6}
print(2 in my_set) #True
print(len(my_set)) #6

new_set = my_set.copy()
my_set.clear()
print(my_set) #set()
print(new_set) # {1,2,3,4,5,6}

set1 = {1,2,3,4,5}
set2 = {1,2,3,4,5,6,7,8,9}
print(set2.difference(set1)) #{6,7,8,9}
#set1.discard(1)
#print(set1) #{2,3,4,5}
#set2.difference_update(set1)
#print(set2) #{1,6,7,8,9}

print(set2.intersection(set1)) #{1,2,3,4,5}
print(set2 & set1) #{1,2,3,4,5}

set3 = set1.union(set2)
print(set3) #{1, 2, 3, 4, 5, 6, 7, 8, 9}

set3 = set1|set2
print(set3) #{1, 2, 3, 4, 5, 6, 7, 8, 9}

