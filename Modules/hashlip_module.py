import hashlib as hsh

passwd="rafal90"

# then sending to SHA256()

result = hsh.sha256(passwd.encode())
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA256 is : ",result )

print(result.hexdigest()) #0-9 a=10,b=11, 15=f




import hashlib
print("********************",hashlib.sha1("rafal".encode()).hexdigest())



str1 = "Swati@123"

# then sending to SHA256()
result = hsh.md5(str1.encode())
  
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of MD5 is : ")
print("^^^^^^^^^^^^^^^^^",result.hexdigest())