username  = input('What\'s your username?\n')
password = input('Enter your password\n')
hidden_password = '*'*(len(password))

print (f"""hei {username}, your password {hidden_password} is {len(password)} 
letter/s long""")
