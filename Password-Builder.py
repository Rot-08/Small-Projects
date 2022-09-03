import string, random


def PasswordGenerate(passwordlength):

    #Takes an idea of what the user wants as a password 
    
    base = input("please enter an idea of what your password should look like: ")
    rems = passwordlength - len(base)
    characterSet = string.ascii_letters + string.digits + string.punctuation
    
    
    #Adds some random characters and Creates a password of the required length
    password = "".join(random.choice(characterSet) for i in range(rems))
    password = base + password

    print(password)


PasswordGenerate(10)