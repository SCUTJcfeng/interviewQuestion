# !/usr/bin/python3.6
# -*- coding:utf-8 -*-
'''
Project: interviewTest
Author: jc feng (jcfeng2013@gmail.com)
File Created: 2019-06-05 20:14:11
Last Modified: 2019-06-05 20:54:58
'''

'''
有 36 辆车和 6 条跑道，没有计时器的前提下，最少用几次比赛可以筛选出最快的三辆？
'''

'''answer 1
每次保留3辆最快的, 再增加3辆下一次比赛, 11次
'''

'''answer 2
36辆分6组跑, 6组保留前3辆, 剩18辆
18辆分3组跑, 3组保留前3辆, 剩9辆
9辆分1组跑, 1组保留前3辆, 剩6辆
最后一次, 得出前3辆
6+3+1+1=11
'''

'''answer 3(best)
36辆分6组跑, 6组第一名, 假设共ABCDEF6组
这6辆比赛1次, 得出前3名, 第一名同时为36辆得第一名, 假设前3名分别在ABC组, 分别为A1, B1, C1
剩下2, 3名
A1 B1 C1
A2 B2 C2
A3 B3 C3
C2, B3, C3 可以淘汰, 因为他们前面有至少3辆车比他们快
最后一次, B1 C1 A2 B2 A3 再比赛一次 得出前两名
6+1+1=8
'''


def fastest_car(car_list, tracks):
    pass


print(fastest_car(36, 6))
