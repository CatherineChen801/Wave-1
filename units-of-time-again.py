day = 86400
hour = 3600
minute = 60
second = 1
d = 0
h = 0
m = 0
s = 0
s = int(input("Number of seconds: "))

d = s//day
d = str(d)
h = s//hour%24
if h <10:
    h = str(0) + str(h)
    h = str(h)
m = s%hour//minute
if m <10:
    m = str(0) + str(m)
    m = str(m)
s = s//second
if s <10:
    s = str(0) + str(s)
    s = str(s)
print("The time is: " + d + ":" + h + ":" + m + ":" + s)