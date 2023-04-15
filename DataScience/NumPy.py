import numpy as np
x = [(1,2,3),(4,5,6),(7,8,9)]

y = np.array(x)             # This gives matrix
print(y)
print("\n")

a = np.zeros(3)             # This gives null or zero matrix of only 1 row and 3 column (1D)
print(a)
a = np.zeros((3,2))         # This gives null or zero matrix of rows(i) = 3 and column(j) = 2
print(a)
print("\n")

b = np.ones(3)              # This gives ones matrix(every element is 1) of only 1 row and 3 column (1D)
print(b)
b = np.ones((3,3))          # This gives ones matrix(every element is 1) of 3 row and 3 column (2D)
print(b)
print("\n")

c = np.eye(3)               # This gives a unit matrix whose diagonal elements are 1. it has only one parameter (i=j)
print(c)
print("\n")

d = np.arange(10)                   # This creates a 1D array of 10 elements from 0 to 9
print(d)
d = np.arange(30).reshape(3,10)     # This creates a 2D matrix of 30 elements in 3 rows(i) and 10 columns(j) from 0 to 29
print(d)
print("\n")

e = np.linspace(0, 10, 5)
print(e)
print("\n")

f = np.random.rand(5)               # Gives any 5 random +ve and values between 0 - 1
print(f)
f = np.random.randn(5)              # Gives any 5 random +ve and -ve values between 0 - 1
print(f)
f = np.random.randint(1,100)        # Gives random number from 1 to 100
print(f)
print("\n")

x = np.arange(25).reshape(5,5)
print(x)
print(x[2][2])                      # Accessing the element of 2D array
print(x[2,2])
print(x[4][2])
print(x[4,2])
print(x[0:2,2:])
print("\n")

x = np.arange(20)
print(x)
a = x > 12                  # this gives a boolean array in which number > 12 is True and number < 12 are False
print(a)
a = x[x > 12]               # this gives a array in which number > 12
print(a)