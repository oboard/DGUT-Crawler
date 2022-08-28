import requests
import pymysql
import json
import time
import _thread


# 打开数据库连接
db = pymysql.connect(host='127.0.0.1',
                     user='root', password='luoyuhang123.', database='dgut')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

token = ''  # 填写Bearer Token

def get(i):
    kw = {'uid': i+149638}
    # 设置请求头
    headers = {
        "User-Agent": "Chrome/54.0.2840.99 Safari/537.36",
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": token
    }
    try:
        # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
        response = requests.get(
            "http://lgapp.dgut.edu.cn/api/home/getPersonDetail", params=kw, headers=headers)
        person = json.loads(response.text)['info']
        if (person == []):
            print('空', end='')
            return
        print(person['uid'])
        sql1 = f"insert into person values ('{person['uid']}','{person['type']}','{person['stage']}','{person['sex']}','{person['name']}','{person['username']}','{person['phone']}','{person['short_phone']}','{person['office_phone']}','{person['qq']}','{person['wechat']}','{person['email']}','{person['faculty_name']}','{person['faculty_id']}','{person['class_name']}','{person['class_id']}','{person['address']}','{person['avatar']}')"
        cursor.execute(sql1)
        # 执行sql语句
        db.commit()
    except:
        print('重复')


for i in range(100000):
    get(i)

cursor.close()
db.close()
