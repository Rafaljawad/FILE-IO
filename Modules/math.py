#basic if we import just amth we write math.method
import math

math.gcd(10,20)

#2
import math as mt # we used alias 
mt.gcd(10,20)

# 3
from math import pi , gcd# if we write from math import method so here we do not need math.method
gcd(10,20)


# 4 code complexity
from math import *# here all the methods will be imported and no need to math.method
gcd(10,20)



from math import factorial
print(factorial(2))#O/P 2



print(f"math methods are: {dir(math)}") 