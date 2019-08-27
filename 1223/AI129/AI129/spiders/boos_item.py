#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/19 15:36
# @Author  : Ryu
# @Site    :
# @File    : boos_item.py
# @Software: PyCharm
import scrapy,json
from lxml import etree
from ..items import Ai129HomeItem
import time
class boos_spider(scrapy.Spider):
    name = 'boos'
    def start_requests(self):
        # url='https://www.zhipin.com/job_detail/?query=web&scity=101010100&industry=&position='
        time.sleep(3)
        scity = ['c101010100', 'job_detail', 'c101280100', 'c101280600']
        query_list = ['Python+web', '%E7%88%AC%E8%99%AB', 'AI', '%E5%A4%A7%E6%95%B0%E6%8D%AE']
        for city in scity:
            for job in query_list:
                url = 'https://www.zhipin.com/' + city + '/?query=' + job
                yield scrapy.Request(url,callback=self.parse1)
    def parse1(self, response):
        text=etree.HTML(response.text)
        po=text.xpath('//div[@class="info-primary"]/h3/a/@href')
        for i in po:
            url_new='https://www.zhipin.com'+i
            yield scrapy.Request(url_new,callback=self.parse)
    def parse(self, response):
        possition = ''  # 职位
        monthly_pay = ''  # 月薪
        corporation = ''  # 公司
        experience = ''  # 经验
        educational = ''  # 学历
        corporation_address = ''  # 公司地址
        departmen = ''  # 部门
        responsibilities = ''  # 岗位描述
        Job_Requirement = ''  # 职位要求
        company_size = ''  # 公司规模
        official_website = ''  # 公司官网
        major_business = ''  # 公司主营业务
        html=etree.HTML(response.text)
        try:
            possition=html.xpath('//div[@class="info-primary"]/div[@class="name"]/h1/text()')[0]#职位
        except Exception:
            pass
        try:
            monthly_pay=html.xpath('//div[@class="info-primary"]/div[@class="name"]/span[@class="badge"]/text()')#月薪
            monthly_pay=(''.join(monthly_pay)).strip()
        except Exception:
            pass
        try:
            company_size=(html.xpath('//div[@class="info-company"]/p/text()'))[1]#公司规模
        except Exception:
            pass
        try:
            corporation=html.xpath('//div[@class="info-company"]/h3/a/text()')[0]#公司名
        except Exception:
            pass
        try:
            experience=html.xpath('//div[@class="info-primary"]/p/text()')[1] # 经验
        except Exception:
            pass
        try:
            educational=html.xpath('//div[@class="info-primary"]/p/text()')[2] # 学历
        except Exception:
            pass
        try:
            corporation_address=(html.xpath('//div[@class="location-address"]/text()'))[0]# 公司地址
        except Exception:
            pass
        try:
            lists=html.xpath('//div[@class="job-sec"]/div[@class="text"]/text()')# 岗位描述
            Job_Requirement = ''.join(lists)
            responsibilities=lists[-1]
        except Exception:
            pass
        try:
            official_website=(html.xpath('//div[@class="info-company"]/p/text()'))[2]# 公司官网
        # major_business=html.xpath()# 公司主营业务
            print(company_size)
        except Exception:
            pass
        item=Ai129HomeItem()
        item['possition'] =possition   # 职位
        item['monthly_pay'] = monthly_pay  # 月薪
        item['corporation'] = corporation  # 公司
        item['experience'] = experience  # 经验
        item['educational'] = educational  # 学历
        item['corporation_address'] = corporation_address  # 公司地址
        item['departmen'] = departmen  # 部门
        item['responsibilities'] = responsibilities  # 岗位描述
        item['Job_Requirement'] = Job_Requirement  # 职位要求
        item['company_size'] = company_size  # 公司规模
        item['official_website'] = official_website  # 公司官网
        item['major_business'] = major_business  # 公司主营业务
        yield item
