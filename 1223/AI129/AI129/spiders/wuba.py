#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/20 12:50
# @Author  : Ryu
# @Site    :
# @File    : wuba.py
# @Software: PyCharm
import scrapy
from ..items import Ai129HomeItem
from lxml import etree
class Wubu_Spider(scrapy.Spider):
    name = 'wb'
    def start_requests(self):
        city = ['bj', 'sh', 'gz', 'sz']
        job = ['Python%20web', '%E7%88%AC%E8%99%AB', 'AI', '%E5%A4%A7%E6%95%B0%E6%8D%AE']
        for city in city:
            for job1 in job:
                url = 'https://' + city + '.58.com/job/?key=' + job1
                yield scrapy.Request(url,callback=self.parse1)
    def parse1(self, response):
        text=response.text
        html=etree.HTML(text)
        list_url=html.xpath('//div[@class="job_name clearfix"]/a/@href')
        for i in list_url:
            yield scrapy.Request(i,callback=self.parse)
    def parse(self, response):
        text=response.text
        print(text)
        html=etree.HTML(text)
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
        try:
            possition = html.xpath('//span[@class="pos_title"]/text()')  # 职位
        except Exception:
            pass
        try:
            monthly_pay = html.xpath('//span[@class="pos_salary"]/text()')  # 月薪
        except Exception:
            pass
        try:
            company_size = (html.xpath('//p[@class="comp_baseInfo_scale"]/text()'))  # 公司规模
        except Exception:
            pass
        try:
            corporation = html.xpath('//span[@class="daipei_name"]/text()')  # 公司名
        except Exception:
            pass
        try:
            experience = html.xpath('//span[@class="item_condition border_right_None"]/text()')  # 经验
        except Exception:
            pass
        try:
            educational = html.xpath('//span[@class="item_condition"]/text()')  # 学历
        except Exception:
            pass
        try:
            corporation_address = html.xpath('//span[@class="pos_area_span pos_address"]/span/text()')  # 公司地址
        except Exception:
            pass
        try:
            corporation_address=''.join(corporation_address)
        except Exception:
            pass
        try:
            responsibilities = html.xpath('//div[@class="jcourse-method"]/span/text()')  # 岗位描述
        except Exception:
            pass
        try:
            Job_Requirement = html.xpath('//div[@class="course-intro-cont"]/text()')  # 职位要求
        except Exception:
            pass
        # official_website = (html.xpath(''))  # 公司官网
        # major_business=html.xpath()# 公司主营业务
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
