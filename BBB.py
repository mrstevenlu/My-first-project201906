

# Filename : 04-random.py
# author by : Seven Lu

# 目的:
# 掌握随机的概念
# 掌握集中不同的产生随机数的方式

# 导入 random(随机数) 模块
import random


# 产生 0 到 1 之间的随机浮点数
print( "随机数 0-1 是：" )
x = random.random()
print(x)

# 产生 1 到 10 的一个整数型随机数
print("随机数 1-10 是：")
print(random.randint(1,10) )
