import datetime
import re

import pymysql

import Database

netUrl = {
    'lcer':'lceryuan.net',
    'zzyy':'zz-zxyy.com',
    'tsyy':'taishanyy.com'
}

def DataHandler(filestr):
    data = []    
    regex_str = '\s(\S*)'
    result = re.findall(regex_str, filestr)    
    data.append(datetime.datetime.strptime(re.sub('<SP>', ' ', result[0]), '%Y-%m-%d %H:%M:%S'))   #请求时间:{re.sub(r'<SP>', ' ', result[0])}
    data.append(float(result[1]))   #请求耗时:{result[1]}
    data.append(result[2]) #攻击类型:{result[2]}
    data.append(result[3]) #是否拦截:{result[3]}
    data.append(result[4]) #客户端IP:{result[4]}
    data.append(re.sub('<SP>', '', result[5])) #代理IP:{result[5]}
    data.append(result[7]) #域名:{result[7]}
    data.append(result[8]) #URL:{result[8]}
    data.append(result[9]) #请求方法:{result[9]}
    data.append(result[10]) #Referer{result[10]}
    data.append(result[11]) #缓存命中情况:{result[11]}
    data.append(int(result[13])) #状态码:{result[13]}
    data.append(int(result[14])) #页面大小:{result[14]}
    data.append(re.sub('<SP>', ' ', result[16])) #User-Agent:{re.sub(r'<SP>', ' ', result[16])}
    return(data)

def DateGenerator(Stime, Ftime):
    date = []
    if Stime>=Ftime:
        t1 = Ftime
        t2 = Stime
    else:
        t1 = Stime
        t2 = Ftime
    
    t1 = datetime.datetime.strptime(Stime, '%Y-%m-%d')
    t2 = datetime.datetime.strptime(Ftime, '%Y-%m-%d')
    while(t1 <= t2):
        date.append(t1.strftime('%Y%m%d'))
        t1 += datetime.timedelta(days=1)                                                                                                                                                                                                                                                                                                                                                    
    return(date)

if __name__ == '__main__':
    conn = pymysql.connect(user='root', password='Wunai1995', database='cyd')
    cursor = conn.cursor()
    Stime = '2020-06-24'
    Ftime = '2020-06-26'
    x = 0
    y = 0
    Project = ['lcer', 'tsyy', 'zzyy']
    date = DateGenerator(Stime, Ftime)
    for p in Project:
        for d in date:
            filename1 = 'D:/2020-云天/DataHandler/CYD/log/'+ p +'/access/' + netUrl[p] + '-access-' + d +'.log'
            filename2 = 'D:/2020-云天/DataHandler/CYD/log/'+ p +'/attack/' + netUrl[p] + '-attack-' + d +'.log'
            tableNmae = p + d
            Database.creaTable(cursor, tableNmae)  
            with open(filename1, 'r', encoding='utf-8') as f1:
                for line in f1.readlines():
                    result = DataHandler(line)
                    Database.dbInsert(cursor, tableNmae, result)
                    x += 1
                    print(f'\r已处理{x}条\t', end='')
                f1.close()
            with open(filename2, 'r', encoding='utf-8') as f2: 
                for line in f2.readlines():
                    result = DataHandler(line)
                    x += 1
                    print(f'\r已处理{x}条\t', end='')                    
                f2.close()              
           
        conn.commit()    
    cursor.close()
    conn.close()
    print('处理结束!')
