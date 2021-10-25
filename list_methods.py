"""
append()
clear()
copy()
count()
extend()
index()
insert()
pop()
remove()
reverse()
sort()
"""

basket = [1,2,3,4,5]

basket.append(6) 
print(basket) #[1,2,3,4,5,6]

basket.insert(1, 7) 
print(basket) #[1,7,2,3,4,5,6]

basket.extend([8,9])
print(basket) #[1,7,2,3,4,5,6,8,9]

basket.pop()
print(basket) #[1,7,2,3,4,5,6,8]

basket.pop(2)
print(basket) #[1,7,3,4,5,6,8]

basket.remove(4)
print(basket) #[1,7,3,5,6,8]

"""
basket.clear()
print(basket) #[]
"""
print(basket.index(3)) #2

print(2 in basket) #True
print('4' in basket) #False

print(basket.count(6)) #1
print(basket.count(7)) #0

print(sorted(basket)) #[1,3,5,6,7,8]
print(basket) #[1,7,3,5,6,8]

basket.sort()
print(basket) #[1,3,5,6,7,8]

new_basket = basket.copy()
print(new_basket) #[1,3,5,6,7,8]

basket.clear()
print(basket) #[]
print(new_basket) #[1,3,5,6,7,8]

new_basket.reverse() 
print(new_basket) #[8,7,6,5,3,1]
print(new_basket[::-1]) #[1,2,3,4,5,6,7,8]
print(new_basket) #[8,7,6,5,3,1]
print(len(new_basket)) #6

list = list(range(1,21))
print(list) #[0, ...., 20]

a,b,c, *other, d  = ['banana', 'orange', 'apple', 'mango', 'papaya', 'strawberry']
print(a) #banana
print(b) #orange
print(c) #apple
print(other) #['mango', 'papaya']
print(d) #strawberry
