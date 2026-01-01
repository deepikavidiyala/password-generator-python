import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
special_chars=['~','`','!','@','#','$','%','^','&','*','(',')']
print("--- Welcome To The Password Generator ---")
noofletters=int(input("How many letters you want in your password? "))
noofnumbers=int(input("How many numbers you want in your password? "))
noofsymbols=int(input("How many symbols you want in your password? "))
password=""
for i in range(noofletters):
    password=password+random.choice(letters)
for j in range(noofnumbers):
    password+=random.choice(numbers)
for k in range(noofsymbols):
    password+=random.choice(special_chars)
password_list=list(password)
random.shuffle(password_list)
newpassword=" ".join(password_list)
print(f"Your password was ready : {newpassword}")