"""
作者：Ma KaiPeng
日期：2021 年 11 月 02 日
"""


data = {
    'id': '123456',
    'age': 36,
    'name': 'michael'
}
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
sql = 'insert into products (%s) values (%s)' % (keys, values)

print(sql)
print(len(data))
print(len(data.keys()))
print(len(data.values()))
