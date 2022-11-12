import random
x=random.randint(1,10)
print(x)



#choice method # choice()	Returns a random element from the given sequence
listy=[10,20,30,40]
choice=random.choice(listy)


import random as r # alias
some_list =["Google","MS","Amazon","Netflix","Yahhoo","TCS"]

a= r.choice(some_list)
print(a)

some_list2= [1,2,3,4.212322]
b= r.choice(some_list2)
print(b)


# randrange()	Returns a random number between the given range
even_rand=r.randrange(0,100,2)#start,stop,step here will give all even random num
print(even_rand)


for i in range(10):
    res = r.randrange(1,10,3)#odd num
    print(res, end =" ")

#shuffle()	Takes a sequence and returns the sequence in a random order


str_list=("Hemanth Python Student".split())
print(f"original string list is {str_list} ")
r.shuffle(str_list)
print(f"shuffled string list is :{str_list}")



# sample()	Returns a given sample of a sequence(here will get 4 random num from the list x for ex output:sample of x is [31, 1, 266, 134])
x=r.sample([1,23,1,31,134,55,266],4)
print(f"sample of x is {x}")


# random()	Returns a random float number between 0 and 1
float_random=r.random()
round_float_num=round(float_random,2)
print("float random num ",float_random,"rounded to ",round_float_num)


#summary
# import random as r
# r.randint(start, stop)
# r.randrange(start,stop,step)
# r.shuffle(seq)  - changes the order of seq
# r.sample(seq,12) - extract the data
# r.choice(seq)  - returns random  ele from seq
# r.random()    - return random float num from 0-1




# ***************************generate strong random password ***************************************************
# Upper
# lower
# special
# number
# limit >=8
# pwd=""
# upper_char="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # upper_list=upper_char.split()
# # print(upper_list)
# lower_char=upper_char.lower()
# # lower_list=lower.split()
# symbols="#$%^&*()@!+?"
# num=str(r.randrange(1,10,1))
# pwd+=upper_char+lower_char+symbols+num
# # pwd=r.sample(pwd_random,8)

# print(pwd)

print("Welcome to Password Generator")
letters_lower = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
letters_upper = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
symbols = ['@', '&', '%', '$', '!', '#', '^', '(', ')']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letter_input_lowercase = int(input("how many lowercase letter you want? "))
letter_input_upercasecase = int(input("how many upercase letter you want? "))
symbol_input = int(input("how many symbols you want? "))
number_input = int(input("how many numbers you want? "))
password=[]
for lower_char in range(letter_input_lowercase):
    password.append(r.choice(letters_lower))
for upper_char in range(letter_input_upercasecase):
    password.append(r.choice(letters_upper))
for symbol in range(symbol_input):
    password.append(r.choice(symbols))
for num in range(number_input):
    password.append(r.choice(numbers))
r.shuffle(password)
print(f"your password is :{''.join(password)}")





