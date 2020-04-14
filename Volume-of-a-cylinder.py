h = input("The height of the cylinder is: ")
h = float(h)
r = input("The radius of the cylinder is: ")
r = float(r)
import math
pi = math.pi
v = h*pi*r**2
v = "%0.1f" % v
v = str(v)
print("The volume of the cylinder is " + v + " cubic units")