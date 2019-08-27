# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class Ai129HomeItem(scrapy.Item):

    possition=scrapy.Field()#职位         title
    monthly_pay=scrapy.Field()#月薪
    corporation=scrapy.Field()#公司
    experience=scrapy.Field()#经验
    educational=scrapy.Field()#学历
    corporation_address=scrapy.Field()#公司地址
    departmen=scrapy.Field()#部门
    responsibilities=scrapy.Field()#岗位描述
    Job_Requirement=scrapy.Field()#职位要求
    company_size=scrapy.Field()#公司规模
    official_website=scrapy.Field()#公司官网
    major_business=scrapy.Field()#公司主营业务
