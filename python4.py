# -*- coding: utf8 -*-
import turtle               # 匯入turtle套件，允許我們使用turtle指令
window = turtle.Screen()        # 產生畫布以進行畫圖
window.bgcolor("lightgreen")# 設定畫布底色為淺綠色

marry = turtle.Turtle()         # 建立一個海龜turtle，它的名字叫marry
marry.color("hotpink")          # 設定畫筆顏色為粉紅色
marry.pensize(5)                        # 設定畫筆粗細為5個像素

for i in [0,1,2]:
    marry.forward(80)                       # 告訴海龜往前走80個單位
    marry.left(120)                         # 告訴海龜左轉120度
marry.left(180)
marry.forward(80)

john = turtle.Turtle()          # 建立一個海龜turtle，它的名字叫john
colors=["yellow", "red", "purple", "blue"]
for pen_color in colors:
    john.color(pen_color)
    john.forward(50)
    john.left(90)

window.exitonclick()                    # 等待使用者關閉視窗
