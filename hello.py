print("hello")
print('hello, world!')
import sys

print(sys.version_info)
print(sys.version)

print("-------------------------")

# import this

# import turtle

# turtle.pensize(4)
# turtle.pencolor('red')

# turtle.forward(100)
# turtle.right(200)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)

# turtle.mainloop()

# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))


year = int(input('请输入年份: '))
# 如果代码太长写成一行不便于阅读 可以使用\对代码进行折行
is_leap = year % 4 == 0 and year % 100 != 0 or \
          year % 400 == 0
print(is_leap)