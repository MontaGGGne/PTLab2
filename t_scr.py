import math

f = 25
c = 24
h = 26

o = 2.6

print(math.floor(o))

print(f"f - {int(f/10 + (0.5 if f/10 > 0 else -0.5))*10}")
print(f"c - {int(c/10 + (0.5 if c/10 > 0 else -0.5))*10}")
print(f"h - {int(h/10 + (0.5 if h/10 > 0 else -0.5))*10}")