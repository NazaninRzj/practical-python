# bounce.py
#
# Exercise 1.5

first_hight = 100
for i in range(1,10):
    second_hight = 3/5 * first_hight
    print(i, round(second_hight,4))
    first_hight = second_hight