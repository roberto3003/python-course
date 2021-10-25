my_list = [
       {
        'a' : [1,2,3],
        'b' : 2,
        'c' : 'Hello',
        'd' : True
        },
       {
           'a' : [4,5,6],
           'b' : 'hello',
           'c' : False
           }
       ]

print(my_list[0]['a'][1]) #2

my_dict = {
        123 : [1,2,3],
        True : 'Hello'
        }

print(123 in my_dict) #True
print(my_dict.get('age')) #None

print('size' in my_dict) #False
print(True in my_dict) #True

print('Hello' in my_dict.values()) #True
print(my_dict.items()) #dict_items([(123, [1, 2, 3]), (True, 'Hello')])
my_dict2 = my_dict.copy()
my_dict.clear()
print(my_dict) #{}
print(my_dict2) #{123: [1, 2, 3], True: 'Hello'}
my_dict2.pop(123)
print(my_dict2) #{True: 'Hello'}
my_dict2.update({True: "World"})
print(my_dict2) #{True: "World"}
my_dict2.update({'name' : 'Roberto'})
print(my_dict2) #{True: 'World', 'name': 'Roberto'}
