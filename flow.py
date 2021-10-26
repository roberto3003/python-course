is_old = False
has_license = True

if is_old and has_license:
    print('OK')
elif is_old:
    print('You can drive')
elif has_license:
    print('You are licensed and thereof you can drive')
else:    
    print('You are not of age')

is_friend = False
is_user = False
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message) #message allowed

if is_friend or is_user:
    print('best friends forever') #best friends forever

if not is_friend:
    print('We are not friends')

is_magician = True
is_expert = True

if is_magician and is_expert:
    print("You are a master magician")

if is_magician and not is_expert:
    print("At least you are getting there")

if not is_magician:
    print("You need magic powers")


