# !/usr/bin/python3.6
# -*- coding:utf-8 -*-
'''
Project: interviewTest
Author: jc feng (jcfeng2013@gmail.com)
File Created: 2019-06-05 17:32:21
Last Modified: 2019-06-05 18:47:26
'''

'''
春节期间小明使用微信收到很多个红包，非常开心。在查看领取红包记录时发现，
某个红包金额出现的次数超过了红包总数的一半。请帮小明找到该红包金额。
写出具体算法思路和代码实现，要求算法尽可能高效。
'''

array = [1, 3, 2, 2, 4, 2]
array_2 = [4, 4, 4, 4, 3, 3, 3, 2, 2, 1]
array_3 = [4, 4, 4, 4, 3, 3, 3, 2]


def count_array_complex(array):
    count = {}
    for num in array:
        try:
            count[num] += 1
            if count[num] > len(array) / 2:
                return num
        except KeyError:
            count[num] = 1
    return None


def count_array(array):
    key = array[0]
    count = 1
    for num in array[1:]:
        if num == key:
            count += 1
        else:
            count -= 1
            if count == 0:
                key = num
                count = 1
    count_key = 0
    for num in array:
        if num == key:
            count_key += 1
    if count_key > len(array) / 2:
        return key
    return None


print(count_array(array_3))
