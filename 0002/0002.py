"""
第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

"""

import pymysql
import uuid


def StoreInMysql(codelist):
    connection = pymysql.connect(host="localhost",
                                 user="root",
                                 passwd="",
                                 db="test")
    try:
        with connection.cursor() as cursor:
            cursor.execute('CREATE DATABASE IF NOT EXISTS activation_code')
            cursor.execute('USE activation_code')
            cursor.execute("CREATE TABLE IF NOT EXISTS code_table(id INT NOT NULL AUTO_INCREMENT, "
                           "code VARCHAR(100) NOT NULL, "
                           "PRIMARY KEY(id))")
            for code in codelist:
                cursor.execute('INSERT INTO code_table(code) VALUES (%s)', code)
                cursor.connection.commit()
    except BaseException as e:
        print(e)
    cursor.close()
    connection.close()


def getcode(count):
    codelist = []
    for i in range(count):
        code = str(uuid.uuid4())
        codelist.append(code)
    return codelist


if __name__ == '__main__':
    StoreInMysql(getcode(200))
    print("OK!")
