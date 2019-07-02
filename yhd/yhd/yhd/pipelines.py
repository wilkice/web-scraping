# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql


class YhdPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoPipeline(object):

    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB'),
            mongo_collection=crawler.settings.get('MONGO_COLLECTION'),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        self.db[self.mongo_collection].insert_one(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()


class MysqlPipeline(object):
    def __init__(self, host, user, password, database, table, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.table = table
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            table=crawler.settings.get('MYSQL_TABLE'),
            port=crawler.settings.get('MYSQL_PORT'),
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(
            self.host, self.user, self.password, self.database, port=self.port, charset='utf8')
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        name = item['name']
        price = item['price']
        info = item['info']
        sql = "insert into {} values ('{}', {}, '{}')".format(
            self.table, name, price, info)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
        return item

    def close_spider(self, spider):
        self.db.close()
