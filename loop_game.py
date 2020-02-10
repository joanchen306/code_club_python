# -*- coding: utf-8 -*-
#上は日本語を使うためのコードです。

import random


y = random.randint(1,100)
x = input("1~100の中に一つの数字を選んでください: ")
x = int(x)
if x == y:
	print("ぴったりです! Nice Guess!")
elif x > y:
	print("惜しい、実際の数字は予想より小さい")
else:
	print("惜しい、実際の数字は予想より大きい")

print("y(予想) = " + str(y))