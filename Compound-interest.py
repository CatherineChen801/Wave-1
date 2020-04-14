#A = P(1 + R/100)T
p = input("Amount of money: $")
p = float(p)
r = 0.04
t = input("Number of years: ")
t = float(t)
T = int(t)
T = str(T)
ci = p*(1+r)*t
ci = "%0.2f" % ci
ci = str(ci)
print("The compound interest for " + T + " years is " + ci)