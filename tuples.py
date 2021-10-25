my_tuple = (1,2,3,4,5)
print(my_tuple[1]) #2
print(5 in my_tuple) #True
print(my_tuple.count(5)) #1
print(my_tuple.index(5)) #4
print(len(my_tuple)) #5


new_tuple = my_tuple[1:2]
print(new_tuple) #(2,)

x,y,z, *other = (1,2,3,4,5)
print(other) #[4,5]
print(type(other)) #list



