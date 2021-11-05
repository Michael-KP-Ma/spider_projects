# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class XiamaiPipeline:
    def open_spider(self, spider):
        self.db = pymysql.connect(host='localhost', port=3306, user='root', password='301932', db='xiamai', charset='utf8')
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        data = dict(item)
        keys = ', '.join(data.keys())
        values = ', '.join(["%s"]*len(data))
        sql = 'INSERT INTO %s (%s) values (%s)' % (item.table, keys, values)
        print(sql)
        try:
            self.cursor.execute(sql, tuple(data.values()))
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
        return item

    def close_spider(self, spider):
        self.db.close()
