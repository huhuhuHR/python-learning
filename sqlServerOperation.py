import pymssql

# server    数据库服务器名称或IP
# user      用户名
# password  密码
# database  数据库名称

server = "10.0.53.158"
user = "sa"
password = "Unidc@2018"
database = "20180917_DI_one"
conn = pymssql.connect(server, user, password, database,'utf8')
cursor = conn.cursor()

# def insertData():
#     sql = "INSERT INTO sutdent_huhuhuhr(studentNo,studentname,class) VALUES (%s, %s,%s)"
#     data = [
#         ('1','霍荣','32班')
#     ]
#     cursor.executemany(sql, data)
#     conn.commit()

if __name__ == '__main__':
    rs = cursor.fetchone()
    print(rs)
