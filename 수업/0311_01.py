# import keyword
# print(keyword.kwlist)

# import calendar
# print(calendar.month(2025, 3))

import datetime
now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)

import tkinter as tk
base = tk.Tk()

import turtle as t
t.shape("turtle")
t.speed(1)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.exitonclick()
