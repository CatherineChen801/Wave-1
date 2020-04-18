d = int(input("Day(s): "))
h = int(input("Hour(s): "))
m = int(input("Minute(s): "))
s = int(input("Seconds: "))
t = d*86400+h*3600+m*60+s
t = str(t)
print("The duration is " + t + " seconds")