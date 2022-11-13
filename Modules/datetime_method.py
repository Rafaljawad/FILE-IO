import datetime
x=datetime.datetime.now()
print(f"date and time  is :{x}")
#o/p2022-11-12 11:32:27.944398
# print(dir(x))
print(f"year  is :{x.year}")
print(f"month  is :{x.month}")
print(f"day  is :{x.day}")
print(f"hour  is :{x.hour} {x.minute}")
print(f"today  is :{x.today}")
print(f"week day   is :{x.weekday()}")




x = datetime.datetime.now()

print(x.year)
print(x.strftime("%Y")) #It is another method to print the datetime # format specifiers
print(x.strftime("%y"))
print(x.year , x.month,x.day)
print(x.strftime("%Y - %m - %d")) #strftime("format specifiers")




#creating objects(create spesfic date and month like birthday)



x = datetime.datetime(1990, 12, 26)

print(x)



# to calculate the age by using datetime method
my_birthday = datetime.datetime(1990, 4, 13)
my_birthday_str=my_birthday.strftime("%Y - %m - %d") #strftime("format specifiers")
print(f"my birthday is {my_birthday_str}")
current_date=datetime.datetime.now()
my_age=current_date.year-my_birthday.year
print(f"my age is {my_age}")



#using function
def age_Caculator(Y,M,D):
    # create
    dob = datetime.datetime(Y,M,D)  #birthday
    
    present = datetime.datetime.now() #present day
    
#     print(dob,present)
#     print((present-dob).days)
    return (present.year - dob.year)
print(age_Caculator(1990,4,13))




# strftime()
# The datetime object has a method for formatting date objects into readable strings.

# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

# %a Weekday, short version Wed
# %A Weekday, full version Wednesday
# %w Weekday as a number 0-6, 0 is Sunday 3
# %d Day of month 01-31 31
# %b Month name, short version Dec
# %B Month name, full version December
# %m Month as a number 01-12 12
# %y Year, short version, without century 18

from datetime import date # here will use just date not date and time 

a=date(2000,8,13)
print(a)
x = date.today()# date.today gives todays date 
str_date_ab=x.strftime("%y %b %d")# small b gives apreveation of month dec,nov,jan ..etc...... small y gives just abreveation of year 22,21,20 
str_date_full_month=x.strftime("%Y %B %d")# b gives apreveation of month
print(str_date_ab)# O/P 22 Nov 13
print(str_date_full_month)# O/P 2022 November 13








