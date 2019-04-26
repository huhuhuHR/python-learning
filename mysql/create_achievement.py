import pymysql

drop = '''
    drop table  if exists achievement
'''
createAchievement = '''
    create table achievement_source(
        id bigint(20) NOT NULL AUTO_INCREMENT,
        idcard varchar(255)  DEFAULT NULL,
        name varchar(255)  DEFAULT NULL,
        chinese varchar(255)  DEFAULT NULL,
        math varchar(255)  DEFAULT NULL,
        english varchar(255)  DEFAULT NULL,
        multiple varchar(255)  DEFAULT NULL,
        total varchar(255)  DEFAULT NULL,
        creat_time datetime(0) DEFAULT now(),
        update_time datetime(0) DEFAULT NULL,
        PRIMARY KEY (`id`) USING BTREE
    )ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic
'''

createAchievementCopy = '''
    create table achievement_target(
        id bigint(20) NOT NULL AUTO_INCREMENT,
        idcard varchar(255)  DEFAULT NULL,
        name varchar(255)  DEFAULT NULL,
        chinese varchar(255)  DEFAULT NULL,
        math varchar(255)  DEFAULT NULL,
        english varchar(255)  DEFAULT NULL,
        multiple varchar(255)  DEFAULT NULL,
        total varchar(255)  DEFAULT NULL,
        creat_time datetime(0) DEFAULT now(),
        update_time datetime(0) DEFAULT NULL,
        PRIMARY KEY (`id`) USING BTREE
    )ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic
'''

config = {
    "host": "10.0.53.154",
    "user": "root",
    "password": "Unidc@2018",
    "database": "datax"
}


def query():
    db = pymysql.connect("localhost", "root", "Niejing", "datax")
    ursor = db.cursor()
    # 使用execute()方法执行SQL语句
    ursor.execute("select * from test")
    # 使用fetall()获取全部数据
    data = ursor.fetchall()
    # 打印获取到的数据
    for item in data:
        print(item)
    # 关闭游标和数据库的连接
    ursor.close()
    db.close()


def createTable(tableNameSql):
    db = pymysql.connect(**config)
    cursor = db.cursor()
    for sql in tableNameSql:
        cursor.execute(sql)
    # 提交数据
    db.commit()
    cursor.close()
    db.close()


def dropTable(tableName):
    db = pymysql.connect(**config)
    cursor = db.cursor()
    cursor.execute(tableName)
    # 提交数据
    db.commit()
    cursor.close()
    db.close()


if __name__ == '__main__':
    tableNameSql = []
    tableNameSql.append(createAchievement)
    tableNameSql.append(createAchievementCopy)
    for sql in tableNameSql:
        print(sql)
    createTable(tableNameSql)
