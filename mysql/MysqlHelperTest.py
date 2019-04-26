from mysql.MySqlHelper import MysqlHelper as help

if __name__ == '__main__':
    mh = help("127.0.0.1", "root", "Niejing", "localhost")
    mh.open()
    curs = mh.curs
    sql = "select count(*) from test"
    result = curs.execute(sql)
    print(result)
    mh.close()
