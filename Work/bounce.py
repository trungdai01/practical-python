# bounce.py
#
# Exercise 1.5
height = 100
bounce_back = 3/5
bounces = 0

while bounces < 10:
    height = round(height * bounce_back, 4)
    bounces = bounces + 1
    print(bounces, height)