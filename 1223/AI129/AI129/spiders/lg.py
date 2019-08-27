#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/21 9:58
# @Author  : Ryu
# @Site    :
# @File    : lg.py
# @Software: PyCharm
import scrapy
from ..items import Ai129HomeItem
from lxml import etree
import time
class lg_spider(scrapy.Spider):

    name='lg'
    def start_requests(self):
        city = ['%E5%8C%97%E4%BA%AC', '%E4%B8%8A%E6%B5%B7', '%E5%B9%BF%E5%B7%9E', '%E6%B7%B1%E5%9C%B3']
        list_job = ['python%20web', 'AI', '%E7%88%AC%E8%99%AB', '%E5%A4%A7%E6%95%B0%E6%8D%AE']
        for city in city:
            for job1 in list_job:
                time.sleep(3)
                url = 'https://www.lagou.com/jobs/list_' + job1 + '%20web?px=default&city=' + city
                'https://www.lagou.com/jobs/list_AI?city=%E5%B9%BF%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput='
                yield scrapy.Request(url,callback=self.parse1,cookies={'JSESSIONID':'ABAAABAAAIAACBIDF2D8A21A69435E1D94B9745CF8E6519'})
    def parse1(self,response):
        text=response.text
        html=etree.HTML(text)
        urls=html.xpath('//div[@class="p_top"]/a/@href')
        print(urls)
        for i in urls:
            print(i)
            yield scrapy.Request(i,callback=self.parse)
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
        text=response.text
        html=etree.HTML(text)
        try:
            possition = html.xpath('//div[@class="position-content-l"]/div/span/text()')[0]  # 职位
        except Exception:
            pass
        try:
            monthly_pay = (html.xpath('//dd[@class="job_request"]/p/span/text()'))[0]  # 月薪
            print(monthly_pay)
        except Exception:
            pass

        try:
            company_size = (html.xpath('//ul[@class="c_feature"]/li/text()'))[7]  # 公司规模
        except Exception:
            pass
        try:
            corporation = (html.xpath('//div[@class="company"]/text()'))[0]  # 公司名
        except Exception:
            pass
        try:
            experience = (html.xpath('//dd[@class="job_request"]/p/span/text()'))[2]  # 经验
        except Exception:
            pass
        try:
            educational = (html.xpath('//dd[@class="job_request"]/p/span/text()'))[3]  # 学历
        except Exception:
            pass
        try:
            corporation_address1 = html.xpath('//div[@class="work_addr"]/a/text()')
            corporation_address2 = (html.xpath('//div[@class="work_addr"]/text()'))
            corporation_address=corporation_address1[0]+corporation_address1[1]+corporation_address1[2]+str(corporation_address2[3]).strip()# 公司地址
        except Exception:
            pass
        try:
            lists = html.xpath('//dd[@class="job_bt"]/div/p/text()')  # 岗位描述
            Job_Requirement = ''.join(lists)
            responsibilities = lists[-3]
        except Exception:
            print('错误！Job_')
        try:
            official_website = ((html.xpath('//ul[@class="c_feature"]/li/a/@href')))[0]  # 公司官网
        except Exception:
            pass
        try:
            major_business = (html.xpath('//ul[@class="c_feature"]/li/text()'))[1]  # 公司主营业务
        except Exception:
            pass
        item = Ai129HomeItem()
        item['possition'] = possition  # 职位
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