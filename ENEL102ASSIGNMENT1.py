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
import math
y = math.tanh(x)

# %%
