#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/21 17:28
# @Author  : Ryu
# @Site    :
# @File    : nt.py
# @Software: PyCharm
import scrapy
from lxml import etree
from ..items import Ai129HomeItem
class nt_spider(scrapy.Spider):
    name='nt'
    def start_requests(self):#列表页面url
        city = ['%E5%8C%97%E4%BA%AC', '%E4%B8%8A%E6%B5%B7', '%E5%B9%BF%E5%B7%9E', '%E6%B7%B1%E5%9C%B3']
        keyword = ['python+web', 'AI', '%E7%88%AC%E8%99%AB', '%E5%A4%A7%E6%95%B0%E6%8D%AE']
        for city in city:
            for job1 in keyword:
                url = 'http://www.neitui.me/?name=job&handle=lists&city=' + city + '&keyword=' + job1
                yield scrapy.Request(url,callback=self.parse1)
    def parse1(self,response):#详情页面url
        text=response.text
        html=etree.HTML(text)
        urls=html.xpath('//div[@class="mt5 clearfix"]/a/@href')
        for i in urls:
            url='http://www.neitui.me'+i
            yield scrapy.Request(url,callback=self.parse)
    def parse(self, response):
        text=response.text
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
            possition = (html.xpath('//div[@class="c333 font26"]/text()'))[0]  # 职位
        except Exception:
            pass
        try:
            monthly_pay = (html.xpath('//div[@class="font16 mt10 mb10"]/span/text()'))[0]  # 月薪
        except Exception:
            pass

        try:
            company_size = (html.xpath('//div[@class="form-control-static"]/span/text()'))[1]  # 公司规模
        except Exception:
            pass
        try:
            corporation = (html.xpath('//div[@class="col-xs-8"]/a/text()'))[0]  # 公司名
        except Exception:
            pass
        try:
            experience = (html.xpath('//div[@class="font16 mt10 mb10"]/span/text()'))[1]  # 经验
        except Exception:
            pass
        try:
            educational = (html.xpath('//div[@class="font16 mt10 mb10"]/span/text()'))[2]  # 学历
        except Exception:
            pass
        try:
            corporation_address = (html.xpath('//div[@class="font16 mt10 mb10"]/span/text()'))[3]  # 公司地址
        except Exception:
            pass
        try:
            datas = html.xpath('//div[@class="mb20 jobdetailcon"]/text()')  # 岗位描述
            Job_Requirement = ''.join(datas)
            responsibilities = datas[-5]
        except Exception:
            print('错误！Job_')

            # Job_Requirement = html.xpath()  # 职位要求
        try:
            official_website = (html.xpath('//div[@class="form-control-static"]/span/text()'))[2]  # 公司官网
        except Exception:
            pass
        try:
            major_business = (html.xpath('//div[@class="form-control-static mt20"]/span/text()'))[0]  # 公司主营业务
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
