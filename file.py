
import os
print(os.getcwd())#GET THE PATH OF THIS FILE
# # O/P c:\Users\rafal\Videos\python-training-with-kumar-lecturs\practice and notes\File-IO


print(os.listdir())#LIST ALL FILES AND FOLDER IN THIS DIR
# #O/P['file.py']


print(os.mkdir("textf"))#CREATE NEW DIR IN THIS DIR 
print(os.listdir())
#o/p['file.py', 'textf']now 2 because by os.mkdir we created a folder(textf)

print(os.chdir("./textf"))
print(os.getcwd())



# ************************************OPEN METHOD*****************************************************************
# Opening A File
# Python has a built-in open() function to open a file. This function returns a file object, also called a handle, as it is used to read or modify the file accordingly

# open(
#     file,
#     mode='r',
#     buffering=-1,
#     encoding=None,
#     errors=None,
#     newline=None,
#     closefd=True,
#     opener=None,
# )


##MODES 

# 'r'       open for reading (default)
# 'w'       open for writing, truncating the file first
# 'x'       create a new file and open it for writing
# 'a'       open for writing, appending to the end of the file if it exists
# 'b'       binary mode
# 't'       text mode (default)
# '+'       open a disk file for updating (reading and writing)
# 'U'       universal newline mode (deprecated)

#3 operation we need 1-create folder 2- read or write 3-close it
file_open=open("new_fil.py",'a')#OPEN FILE (CREATE)mode a will create this file now the output is newfile.py-->see the fileio dir has new file created
print(file_open)

write_in_file=file_open.write("#hello world \n #love python \n #hi \n #h")
print(write_in_file)

print(file_open.close())
# write_in_file=file_open.write("#hello world \n #love python \n #hi \n l")we closed the file so no operation will run after closing file



file2=open('server.py','x')#mode x for open and write
file2.write("#ABCDEFGHIJK")
print(file2)



# ****************************************#  Exceptional Handling in Python *************************************************************
#in any language if we have 100 lines of code and we have the error in the line 50 so , the other 50 lines will not be excuted due to error in the first 50 lines 
#to handle the error and let the other 50 lines to excute WE USE EXEPTIONAL HANDLEING ERROR (TRY -->THIS LINE THAT HAS ERROR, EXCEPT-->BLOCK, FINALLY BLOCK)

#  Exceptional Handling in Python  - assigment(30mins)
# try
# except
# finally 

# try - except - handle the errors

R=open("ex.txt",'r')#no directory called ex.txt 
# o/pFileNotFoundError: [Errno 2] No such file or directory: 'ex.txt'
print(R)
print("hello world")
print(1+2)
print(pow(2))
# here the 3 lines after error will not be excuted due to this error


#now will try exceptional handeling:
try:
    R=open("ex.txt",'r')#this error
except Exception as e:
    print(e)
    print("after exception")#after error
    
print("after try - except block flow")#after error
print("Try "+"Except")
print(10+2)
#OUTPUT WILL BE GIVE THE LINE THAT HAS THIS ERRROR AND EXCUTE THE LINES THAT THEY DO NOT HAVE ERRORS
#O/P [Errno 2] No such file or directory: 'ex.txt'
# after exception
# after try - except block flow
# Try Except
# 12



T=open("file3.txt",mode="w")#mode w also craete new file besides a
print(dir(T),type(T))#dir method list all methods that use in T
# #o/p ['_CHUNK_SIZE', '__class__', '__del__', '__delattr__',
# #  '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', 
# # '__exit__', '__format__', '__ge__', '__getattribute__',
# #  '__gt__', '__hash__', '__init__', '__init_subclass__', 
# # '__iter__', '__le__', '__lt__', '__ne__', '__new__',
# #  '__next__', '__reduce__', '__reduce_ex__',
# #  '__repr__', '__setattr__', '__sizeof__',
# #  '__str__', '__subclasshook__', '_checkClosed',
# #  '_checkReadable', '_checkSeekable', '_checkWritable',
# #  '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding',
# #  'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode',
# #  'name', 'newlines', 'read', 'readable', 'readline', 'readlines',
# #  'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable',
# #  'write', 'write_through', 'writelines'] <class '_io.TextIOWrapper'>
# T.close() # closed (no operation after closing)



m=open("file4.html", mode="a")
m.write("<h1>hello</h1>")
m.close()# we closed it if we want to open it again see line 127 x=open(filename,mode -->if there is no mode by defalt is read)
x=open("file4.html")#default mode is read so here we can not write on it in line 129 will get an error due to read mode we can read only if we add mode a or w we can do it 
print(f"read data is {x.read()}")
# print(f"read data is {x.readlines()}")
# print(f"read data is {x.read()}")
print(f"location is {x.tell()}")# tell method giv as the length of string 
print(f"spesfic location is {x.seek(0)}")# 0
print(f"reading data at location 0  is {x.read()}")#gives the data in index 0 which is the whole content inside file4.html
print(f"spesfic location is {x.seek(5)}")# 0
print(f"location is {x.tell()}")
print(f"reading data at location 0  is {x.read()}")
x.close()

#EX1 LOOP THROUGH A MODE FIRST OPEN (CREATE) 2-WRITE 3- CLOSE 4- ACTIVATE READ MODE (DEFAULT MODE OPEN(FILENAME)) 5- LOOP THROUGH READ FILE

data=open("list.py", mode="a")# with mode a every time we run and with write will add new content to file 
data.write("hello python lovers \n")
data.close()
read_data=open("list.py")
print("***************", type(read_data))
for i in read_data:
    print(f"charecters are: {i}")
    

#EX2 LOOP THROUGH W MODE FIRST OPEN (CREATE) 2-WRITE 3- CLOSE 4- ACTIVATE READ MODE (DEFAULT MODE OPEN(FILENAME)) 5- LOOP THROUGH READ FILE
data=open("list2.py", mode="w")# with mode w every time we run and with write will not add new content to file except twhat we wrote
data.write("print('hello python lovers')\n")
data.write("print('hellow world') \n")
data.write("print(1+5) \n")
data.close()
read_data=open("list2.py")
print("***************", type(read_data))
for i in read_data:
    print(f"charecters are: {i}")
    #here if we run it multiple times, we will get  same output(simply its not like a (append) will add every time we run the code)









