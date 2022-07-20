users = [{'name:'default user', 'email':'email@email.com', 'password':'1234'}]

def creat_user(user_name, email, password1, password2)

 for user in users:
        if user['email'] != email:
            if password1 == password2:
                users.append({'name':user_name, 'email':email, 'password':password})
                
                
                
     def get_user(email):
       for user in users:
          if email == user['email']:
          print(user)
          break
          else:
          print("Error: user not found")
        
        
        
        
   def get_all_users():
    email_list = []
          for user in users:
          email_list.append(user['email'])
          
          return email_list
         
          
 creat_user('darrien', 'darrien@adsfwsd.com', '1234', '1234')
          eamils = get_all_users()
          print(emails)
