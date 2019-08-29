import pymysql
import mysql.achievement_gen as gen


class MysqlHelper:
    '''
      初始化参数
      :param host: 主机
      :param user: 用户名
      :param password: 密码
      :param database: 数据库
      :param port: 端口号，默认是3306
      :param charset: 编码，默认是utf8
    '''

    def __init__(self, config):
        self.host = config['host']
        self.port = config['port']
        self.database = config['database']
        self.user = config['user']
        self.password = config['password']
        self.charset = config['charset']
        self.conn = None
        self.cur = None

    # 获取链接
    def connect(self):
        '''
        获取连接对象和执行对象
        :return:
        '''
        if self.conn is None:
            self.conn = pymysql.connect(host=self.host,
                                        user=self.user,
                                        password=self.password,
                                        database=self.database,
                                        port=self.port,
                                        charset=self.charset)
            self.cur = self.conn.cursor()

    # 获取一行数据
    def fetchone(self, sql, params=None):
        '''
        根据sql和参数获取一行数据
        :param sql: sql语句
        :param params: sql语句对象的参数元组，默认值为None
        :return: 查询的一行数据
        '''
        dataOne = None
        try:
            count = self.cur.execute(sql, params)
            if count != 0:
                dataOne = self.cur.fetchone()
        except Exception as ex:
            print(ex)
        finally:
            self.close()
        return dataOne

    def __item(self, sql, params=None):
        '''
        执行增删改
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 受影响的行数
        '''
        count = 0
        try:
            count = self.cur.execute(sql, params)
            self.conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            self.close()
        return count

    def update(self, sql, params=None):
        '''
        执行修改
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 受影响的行数
        '''
        return self.__item(sql, params)

    def insert(self, sql, params=None):
        '''
        执行新增
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 受影响的行数
        '''
        return self.__item(sql, params)

    def executemany(self, sql, args=None):
        '''
            insert into table values(%s,%s,...)
            args = []
        '''
        if not args:
            return
        rowcount = 0
        try:
            rowcount = self.cur.executemany(sql, args)
            self.conn.commit()
        except Exception as ex:
            self.conn.rollback()
            print(ex)
        return rowcount

    def delete(self, sql, params=None):
        '''
        执行删除
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 受影响的行数
        '''
        return self.__item(sql, params)

    def dropTable(self, table):
        try:
            self.cur.execute('drop table if exists %s' % table)
            self.conn.commit()
        except Exception as ex:
            print(ex)

    def close(self):
        '''
        关闭执行工具和连接对象
        '''
        try:
            if self.cur != None:
                self.cur.close()
            if self.conn != None:
                self.conn.close()
        except:
            pass

    def createTable(self):
        self.cur.execute(createAchievement)
        self.cur.execute(createAchievementCopy)
        self.conn.commit()

    def descColumnNames(self, tableName):
        mysql.cur.execute("select *  from %s where  id =1" % tableName)
        col_name_list = [tuple[0] for tuple in mysql.cur.description]
        return col_name_list;


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

if __name__ == '__main__':
    config = {
        'host': '127.0.0.1',
        'port': 3309,
        'database': 'etl',
        'user': 'root',
        'password': '123456',
        'charset': 'utf8'
    }
    mysql = MysqlHelper(config)
    mysql.connect()
    try:
        # mysql.dropTable('achievement_source')
        # mysql.dropTable('achievement_target')
        # mysql.createTable()
        values = []
        sql = "insert into achievement_source(idcard,name,chinese,math,english,multiple,total)values(%s,%s,%s,%s,%s,%s,%s) "
        for i in range(10000):
            id_num = gen.get_random_id()
            name = gen.get_random_name()
            Chinese = gen.get_random_score()
            Math = gen.get_random_score()
            English = gen.get_random_score()
            Zonghe = gen.get_random_score2()
            Total = Chinese + Math + English + Zonghe
            values.append((id_num, name, Chinese, Math, English, Zonghe, Total))
            if len(values) % 1000:
                mysql.cur.executemany(sql, values)
                mysql.conn.commit()
                values.clear()
        if len(values) > 0:
            mysql.cur.executemany(sql, values)
            mysql.conn.commit()
        # print(mysql.descColumnNames("achievement_source"))
    except Exception as ex:
        mysql.conn.rollback()
        print(ex)
    mysql.close()
