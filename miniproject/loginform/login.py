print('===Userlogin===')

username = input('Please input your name:')
if (len(username)>=6 and len(username)<=20):
    password = input('please input your password:')
    if (len(password)>=6 and len(password)<=20 and (password) == 'mypwd12345'):
        print('Welcome to my home of liberty {} @ {}'.format(username,password))
    else:
        print('Invalid Password')
else:
    print('Invalid Username')
