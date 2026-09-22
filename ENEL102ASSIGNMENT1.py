# %%Q1
import math

def f(x):
    return x**2 * math.sin(0.1 * x**2)

total = sum(f(x) for x in range(-3,5))
print("x =", total)

# %% Q2
import math

def f(x, i):
    return math.sqrt(i) * x**2 * math.sin(0.1 * (x-i)**2)

doublesum = sum(
    sum(f(x, i) for x in range(-3, 5))
    for i in range(1,4))

print("x =", doublesum)

# %%Q3
import math
x = math.sqrt(3)
y = 0.3 * x**2 + math.sqrt(x)
z = math.sqrt(math.e) + x - math.log(x) - math.log(x, 10)

v = math.sqrt(math.tanh(x*y*z))

print("v =", v)

# %%Q4
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4, 500) # 0 to 4 w/ 500 points
y = np.tanh(x)

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("tan(h)")
plt.title( "y = tanh(x)")
plt.grid(True)
plt.show()


# %% Q5
import numpy as np # for complex numbers
x = -4 + 1j
y = 3j

z = np.array([x**y, x*(y**2), np.exp(np.sqrt(x))])

magnitude_sqrd = np.sum(np.abs(z)**2)

print(f"The magnitude squared is {magnitude_sqrd:.2f}")

# Q6 
m = np.abs(z)
p = np.angle(z) # angle does in rad and deg does in deg

print(f"m = {m}\np = {p}")

# %% Q7
import numpy as np

x = np.array([[1, 2, -3],
             [4, 8, 8],
             [2, 2, 4]])

y = x + x.T @ x + x @ x @ x # @ is the matrix multiplication, can't use *
print(f"y = {y}")
# %% Q8 triple check ts cuz my 0s are neg !!
import numpy as np

A = np.array([[1, 2, -3],
              [4, 8, 8],
              [2, 2, 4]])

B = np.array([[5, 5, -3],
              [4, 8, 8],
              [2, 2, 4]])

zeros = np.zeros((3,3)) # 3x3 zero matrix

big_array = np.block([[A, B],
                      [zeros, A]
                      ])

x = np.array([1,0,0,0,0,0])
result = np.linalg.solve(big_array, x)

print(f"The solution is {result}")
# %% Q9
