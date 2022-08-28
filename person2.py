import pymysql
import json

str = """
{
    "message": "获取成功",
    "code": 200,
    "info": {
        "list": [
            {
                "uid": 76679,
                "type": 2,
                "stage": 1,
                "name": "19900012",
                "phone": "",
                "short_phone": "",
                "office_phone": "",
                "abbr": "1",
                "faculty_name": "东莞理工学院",
                "class_name": null,
                "avatar": "http://113.105.128.165:10001/uploads/cas_encrypt_head/default.jpg"
            },
        ],
        "total": 1,
        "self": {
            
        }
    }
}
"""
# 打开数据库连接
db = pymysql.connect(host='127.0.0.1',
                     user='root', password='luoyuhang123.', database='dgut')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

people = json.loads(str)['info']['list']

for person in people:
    if (person == []):
        continue
    print(person['uid'])
    sql1 = f"insert into person values ('{person['uid']}','{person['type']}','{person['stage']}',null,'{person['name']}',null,'{person['phone']}','{person['short_phone']}','{person['office_phone']}',null,null,null,'{person['faculty_name']}',null,'{person['class_name']}',null,null,null)"
    try:
        cursor.execute(sql1)
        # 执行sql语句
        db.commit()
    except:
        print('omg')
cursor.close()
db.close()