# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
class Ai129HomePipeline(object):#创建Mysql数据库的连接对象
    def __init__(self):
        self.conn = MySQLdb.Connect(
            host='localhost',
            port=3306,
            user='root',
            password="'123456'",
            db='test_2',
            charset='utf8'
        )
        self.cursor = self.conn.cursor()
    def process_item(self,item,pider):#从item中读取爬虫数据并调用存储中
        self.insert([item['possition'],item['monthly_pay'],item['corporation'],item['experience'],item['educational'],item['corporation_address'],item['departmen'],item['responsibilities'],item['Job_Requirement'],item['company_size'],item['official_website'],item['major_business']])
        return item
    def insert(self,datas):#添加数据到数据库scrapy_table
        sql = 'insert into scrapy_table(possition,monthly_pay,corporation,experience,educational,corporation_address,departmen,responsibilities,Job_Requirement,company_size,official_website,major_business) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        self.cursor.execute(sql,datas)
        self.conn.commit()


    # position = ''  # 职位
    # monthly_pay = ''  # 月薪
    # corporation = ''  # 公司
    # experience = ''  # 经验
    # educational = ''  # 学历
    # corporation_address = ''  # 公司地址
    # departmen = ''  # 部门
    # responsibilities = ''  # 岗位描述
    # Job_Requirement = ''  # 职位要求
    # company_size = ''  # 公司规模
    # official_website = ''  # 公司官网
    # major_business = ''  # 公司主营业务


