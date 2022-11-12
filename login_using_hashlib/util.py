user_data=[]
def generate_pwd(pwd):
    import hashlib
    return hashlib.md5(pwd.encode()).hexdigest()



def user_input(data):
    global user_data
    user_data.append(data)

def encrypt_data():
    global user_data
    for info in user_data:
        for k   in info:
            if k=="pwd":
                info[k]=generate_pwd(info[k])
    return user_data
