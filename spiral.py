import turtle as t
import math

while True:
    try:
        radius = float(input("Nhập giá trị bán kính lớn nhất của đường xoắn ốc: "))
        if radius > 0:
            break
        else:
            print("Nhập số dương nhé bạn!")
            print()
    except ValueError:
        print("Nhập giá trị là số nhé bạn tôi ơi.")
        print()

t.speed(100)
i = 0
check = 0
while True:
    t.circle(i,20)
    x, y = t.position()
    i += 1
    check = math.sqrt(x**2+y**2)
    if check > radius:
        print("{:.2f}".format(check))
        break

t.done()