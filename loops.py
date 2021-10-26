#iterable - list, dictionary, tuple, set, string

for item in (1,2,3,4,5):
    print(item) #1 2 3 4 5

user = {
        'name' : 'Bobby',
        'age' : 47,
        'can_swim' : True
        }

for item in user:
# for item in user.keys():
    print(item) # name, age, can_swim

for item in user.items():
    print(item) # ('name', 'Bobby) ('age', 47) ('can_swim', True)

for item in user.values():
    print(item) # Bobby, 47, True

for key, value in user.items():
    print(key, value) # name Bobby  age 47  can_swim True

for k, v in user.items():
    print(k, v) # name Bobby  age 47  can_swim True


my_list = [1,2,3,4,5]

counter = 0
for n in my_list:
   counter = counter + n 
print(counter) #15

for _ in range(1,6):
    print(_*2) #2 4 6 8 10

for _ in range(0, 10, 2):
    print(_) #0 2 4 6 8

for i, char in enumerate('Hello'):
    print(i, char) #0 H  1 e   2 l   3 l   4 o

for n,char in enumerate(list(range(100))):
    if char== 50:
        print(f'index of 50 is {n}')

i = 0
while i < 10:
    print(i)
    i = i + 1

for letter in 'Python':
   if letter == 'h':
      break
   print(f'Current Letter : {letter}') #P y t

for letter in 'Python':
   if letter == 'h':
      continue
   print(f'Current Letter : {letter}') #P y t o n

for letter in 'Python': 
   if letter == 'h':
      pass
      print(f'This is pass block')
   print(f'Current Letter : {letter}') #P y t 'This is pass block' h o n

picture = [
        [0,0,0,1,0,0,0],
        [0,0,1,1,1,0,0],
        [0,1,1,1,1,1,0],
        [1,1,1,1,1,1,1],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        ]

for row in picture:
    for pixel in row:
        if pixel == 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print(' ')

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates) #['b', 'n']
