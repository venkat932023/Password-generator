import random
letters=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',
         'Q','W','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
symbols=['!','@','#','$','%','^','&','*','(',')']
numbers=['1','2','3','4','5','6','7','8','9','0']
print("Welcome to password generator!")
n_l=int(input("How many letters you want in your password?\n"))
n_s=int(input("How many symbols you want in your password?\n"))
n_n=int(input("How many numbers you want in your password?\n"))
password_list=[]
for i in range(1,n_l+1):
    char=random.choice(letters)
    password_list+=char
for i in range(1,n_s+1):
    char=random.choice(symbols)
    password_list+=char
for i in range(1,n_n+1):
    char=random.choice(numbers)
    password_list+=char
random.shuffle(password_list)
password=""
for char in password_list:
    password+=char
print(f"You new password is {password}")