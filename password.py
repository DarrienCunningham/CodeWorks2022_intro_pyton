password = "Password123"
trial = 3

while trial > 0:
    if user_password == password:
        print("Welcome User")

    else:
        print("Error: Password Incorrect")
        trial = trial - 1
