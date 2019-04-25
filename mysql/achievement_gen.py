from faker import Faker
import random
import numpy as np

import time

import sys


# 生成随机姓名
def get_random_name():
    return Faker().name()


golad_list = []


def get_random_id():
    id_list = []
    num_list = ""
    for i in range(15):
        id_list.append(random.randint(1, 9))
    for i in id_list:
        num_list += (str(i))
    return num_list


# 生成随机成绩
def get_random_score():
    random_score = np.random.normal(96, 6)  # 正态分布
    return int(random_score)


# 生成随机综合成绩
def get_random_score2():
    random_score2 = np.random.normal(250, 8)  # 正态分布
    return int(random_score2)


def get_fake_data():
    temp = sys.stdout  # 记录当前输出指向，默认是consle
    for i in range(60):  # 这里以生成60条数据为测试
        id_num = get_random_id()
        name = get_random_name()
        Chinese = get_random_score()
        Math = get_random_score()
        English = get_random_score()
        Zonghe = get_random_score2()
        Total = Chinese + Math + English + Zonghe
        with open("G:\python-learning\mysql\FakeData.txt", "a")as f:  # 两次输出重定向
            sys.stdout = f  # 输出指向txt文件
            print(id_num, name, Chinese, Math, English, Zonghe, Total)
    sys.stdout = temp  # 输出重定向回consle


if __name__ == '__main__':
    get_fake_data()
