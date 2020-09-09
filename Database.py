import pymysql


def tableExists(cursor, name):  # 判断tablename表是否存在
    sql = "SHOW TABLES LIKE '" + name + "'"
    cursor.execute(sql)
    return cursor.fetchone()


def creaTable(cursor, tablename):  # 创建tablename表
    sql = f'CREATE TABLE {tablename}(request_datetime DATETIME, request_timespent FLOAT, \
                                    request_type VARCHAR(30), request_result VARCHAR(20), \
                                    request_ip VARCHAR(200), request_proxy VARCHAR(200), \
                                    request_domain VARCHAR(100), request_url VARCHAR(3000), \
                                    request_method VARCHAR(30), request_referer VARCHAR(3000), \
                                    request_cache VARCHAR(10), request_statuscode INT, \
                                    request_pagesize INT, request_useragent varchar(3000))'
    if tableExists(cursor, tablename):
        print(f'表{tablename}已存在!')
    else:
        cursor.execute(sql)
        print(f'表{tablename}创建成功!')


def delTable(cursor, tablename):  # 删除tablename表
    sql = f'DROP TABLE {tablename}'
    if tableExists(cursor, tablename):
        cursor.execute(sql)
        print(f'表{tablename}删除成功!')
    else:
        print(f'表{tablename}不存在!')


def clearTable(cursor, tablename):  # 清除tablename的数据
    sql = f'TRUNCATE TABLE {tablename}'
    if tableExists(cursor, tablename):
        cursor.execute(sql)
        print(f'表{tablename}数据清除成功!')
    else:
        print(f'表{tablename}不存在!')


def dbInsert(cursor, tablename, data):  # 插入数据
    x = 0
    y = 0
    try:
        sql = "insert into {} values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(tablename)
        cursor.execute(sql, (
        data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11],
        data[12], data[13]))
    except BaseException as e:
        with open('/CYD/log/error.log', mode='a') as f3:
            f3.write(str(e))
            f3.write('\n')
            f3.close()


if __name__ == '__main__':
    conn = pymysql.connect(user='root', password='Wunai1995', database='cyd')
    cursor = conn.cursor()
    print(11111111111111111111111)
    cursor.close()
    conn.close()
