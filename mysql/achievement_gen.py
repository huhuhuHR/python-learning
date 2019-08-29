from faker import Faker
import random
import numpy as np

import pymysql

import sys
import time


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


config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "Niejing",
    "database": "compateall"
}


# 200 13
# 500 35.46814322471619 数据量5000,总共耗时：351.85799074172974
# 1000 69.13909006118774 数据量9000,总共耗时：615.8100788593292
def wayOne(g, s):
    start = time.time()
    sql = "insert into achievement_source(idcard,name,chinese,math,english,multiple,total)values(%s,%s,%s,%s,%s,%s,%s) "
    db = pymysql.connect(**config)
    cursor = db.cursor()
    group = g
    size = s
    id_num = get_random_id()
    name = get_random_name()
    Chinese = get_random_score()
    Math = get_random_score()
    English = get_random_score()
    Zonghe = get_random_score2()
    Total = Chinese + Math + English + Zonghe
    for j in range(group):
        gStart = time.time()
        usersvalues = []
        for i in range(size):  # 这里以生成60条数据为测试
            key = str(j) + str(i)
            usersvalues.append(
                (str(id_num) + key, str(name) + key, Chinese, Math, English, Zonghe, Total))
        cursor.executemany(sql, usersvalues)
        db.commit()
        print("第%s批结束,耗时%s" % (str(j + 1), str(time.time() - gStart)))
    cursor.close()
    db.close()
    print("数据量%s,总共耗时：%s" % (str(group * size), str(time.time() - start)))


def wayTwo():
    start = time.time()
    g = 5
    db = pymysql.connect(**config)
    cursor = db.cursor()
    for g in range(1):
        sql = "insert into achievement_source(idcard,name,chinese,math,english,multiple,total)values"
        gStart = time.time()
        for i in range(989):
            id_num = get_random_id()
            name = get_random_name()
            Chinese = get_random_score()
            Math = get_random_score()
            English = get_random_score()
            Zonghe = get_random_score2()
            Total = Chinese + Math + English + Zonghe
            sql += "(" + str(id_num) + ",'" + str(name) + "'," + str(Chinese) + "," + str(Math) + "," + str(
                English) + "," + str(Zonghe) + "," + str(Total) + "),"
        id_num = get_random_id()
        name = get_random_name()
        Chinese = get_random_score()
        Math = get_random_score()
        English = get_random_score()
        Zonghe = get_random_score2()
        Total = Chinese + Math + English + Zonghe
        sql += "(" + str(id_num) + ",'" + str(name) + "'," + str(Chinese) + "," + str(Math) + "," + str(
            English) + "," + str(Zonghe) + "," + str(Total) + ")"
        cursor.execute(sql)
        # print(sql)
        sql = ""
        db.commit()
        print("第%s批结束,耗时%s" % (str(10000), str(time.time() - gStart)))
    cursor.close()
    db.close()
    print("数据量%s,总共耗时：%s" % (str(g * 10000), str(time.time() - start)))


def theadInsert(size, j):
    print("runing" + str(j))
    db = pymysql.connect(**config)
    cursor = db.cursor()
    gStart = time.time()
    usersvalues = []
    sql = "insert into achievement_source(idcard,name,chinese,math,english,multiple,total)values(%s,%s,%s,%s,%s,%s,%s) "
    for i in range(size):  # 这里以生成60条数据为测试
        id_num = get_random_id()
        name = get_random_name()
        Chinese = get_random_score()
        Math = get_random_score()
        English = get_random_score()
        Zonghe = get_random_score2()
        Total = Chinese + Math + English + Zonghe
        usersvalues.append((id_num, name, Chinese, Math, English, Zonghe, Total))
    cursor.executemany(sql, usersvalues)
    db.commit()
    cursor.close()
    db.close()
    print("第%s批结束,耗时%s" % (str(j + 1), str(time.time() - gStart)))


if __name__ == '__main__':
    wayOne(1, 100)
    # for j in range(group):
    #     t = threading.Thread(target=theadInsert, args=(size, j))
    #     t.start()
    # # print("数据量%s,总共耗时：%s" % (str(group * size), str(time.time() - start)))
