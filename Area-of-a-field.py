length = input("length of the field in feet: ")
width = input("width of the field in feet: ")
length = int(length)
width = int(width)
area = length*width
acres = area/43560
acres = str(acres)
print("The area of the field is " + acres + " acres")