print(" === User Login Of Online network disk === ")

username = input("Please input your username:")

if (len(username)>= 6 and len(username) <=20):

   print("Your username is", username)
   password = input("Please input your password:")

   if (len(password) >= 6 and len(password) <= 20):
       if (password == 'mypwd12345'):
           print("Your password is", password)
           print("Welcome the Online network disk!~~~")
       else:
           print("Try Again, Because this is  Invalid Password")

   else:
       for x in range(3):
           print("Try Again, Because this is  Invalid Password")
           password = input("Please input your password:")
           if (len(password) >= 6 and len(password) <= 20):
               if (password == 'mypwd12345'):
                   print("Your password is", password)
                   print("Welcome the Online network disk!~~~")
               else:
                   print("Try Again, Because this is  Invalid Password")


else:
   print("invalid username")