import random
import string
password_length=int(input("Enter length of the password"))
lower_case="abcdefghijklmnopqrstuvwxyz"
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="1234567890"
symbols="!@#$^&*()']['{}"
string=lower_case+upper_case+numbers+symbols
var=random.sample(string,password_length)
password="".join(var)
print("PASSWORD IS:",password)