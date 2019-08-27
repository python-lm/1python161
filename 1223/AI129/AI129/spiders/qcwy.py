#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/20 14:58
# @Author  : Ryu
# @Site    :
# @File    : qcwy.py
# @Software: PyCharm
import scrapy
from ..items import Ai129HomeItem
from lxml import etree
class Qcwy_Spider(scrapy.Spider):
    name = 'qcwy'
    def start_requests(self):
        city = ['010000', '020000', '030200', '040000']
        query = ['python%2520web', 'ai', '%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE','%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD']
        i=1
        while i<10:
            for city in city:
                for job1 in query:
                    print(city,job1)
                    url='https://search.51job.com/list/'+str(city)+',000000,0000,00,9,99,'+job1+',2,'+str(i)+'.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=4&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
                    # url = 'https://search.51job.com/list/' + city + ',000000,0000,00,9,99,' + job1 + ',2,1.html'
                    yield scrapy.Request(url,callback=self.parse1)
            i+=1
    def parse1(self, response):
        text=response.text
        html=etree.HTML(text)
        url_list=html.xpath('//div[@class="el"]/p/span/a/@href')
        for i in url_list:
            yield scrapy.Request(i,callback=self.parse)
    def parse(self, response):
        text=response.text
        html = etree.HTML(text)
        position = ''  # 职位
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
            position = str((html.xpath('//div[@class="tHeader tHjob"]/div/div/h1/text()'))[0]).strip()  # 职位
        except Exception:
            pass
        try:
            monthly_pay = (html.xpath('//div[@class="tHeader tHjob"]/div/div/strong/text()'))[0]  # 月薪
        except Exception:
            pass

        try:
            company_size = (html.xpath('//div[@class="com_tag"]/p/text()'))[1]  # 公司规模
        except Exception:
            pass
        try:
            corporation = str((html.xpath('//div[@class="tHeader tHjob"]/div/div/p/a/text()'))[0]).strip() # 公司名
        except Exception:
            pass
        try:
            experience = str((html.xpath('//div[@class="tHeader tHjob"]/div/div/p[@class="msg ltype"]/text()'))[1]).strip()  # 经验
        except Exception:
            pass
        try:
            educational = str((html.xpath('//div[@class="tHeader tHjob"]/div/div/p[@class="msg ltype"]/text()'))[2]).strip()  # 学历
        except Exception:
            pass
        try:
            corporation_address = str((html.xpath('//div[@class="tHeader tHjob"]/div/div/p[@class="msg ltype"]/text()'))[0]).strip()  # 公司地址
        except Exception:
            pass
        try:
            datas = (html.xpath('//div[@class="bmsg job_msg inbox"]/p/text()'))  # 岗位描述
            Job_Requirement = ''.join(datas)
            responsibilities = datas[-5]
        # Job_Requirement = html.xpath()  # 职位要求
        except Exception:
            pass
        try:
            official_website = html.xpath('//p[@class="cname"]/a/@href')[0]  # 公司官网
        except Exception:
            pass
        try:
            major_business=(html.xpath('//div[@class="com_tag"]/p/text()'))[2]# 公司主营业务
        except Exception:
            pass
        item = Ai129HomeItem()
        item['possition'] = position  # 职位
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