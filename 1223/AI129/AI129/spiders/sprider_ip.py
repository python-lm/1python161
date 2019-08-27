# import scrapy
# from lxml import etree
# from ..items import Ai129Item
# class Ip_daili(scrapy.Spider):
#     name = 'ip1'
#     def start_requests(self):
#         i=1
#         while 1:
#             a='inha/'+str(i)+'/'
#             yield scrapy.Request(url='https://www.kuaidaili.com/free/'+a,callback=self.parse)
#             i+=1
#     def parse(self, response):
#         index=0
#         html=etree.HTML(response.text)
#         #xueli = html.xpath('//ul[@class="terminal-ul clearfix"]/li/strong/text()')[3]
#         ip=html.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr/td[@ data-title="IP"]/text()')
#         port=html.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr/td[@ data-title="PORT"]/text()')
#         type=html.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr/td[@ data-title="类型"]/text()')
#         # print(ip,type,port)
#         for i in ip:
#             print(type[index],ip[index],port[index])
#             item=Ai129Item()
#             item['type'] = type[index]
#             item['ip']=ip[index]
#             item['port']=port[index]
#             yield item
#             index+=1
#
#
#
#
#
#
#
#
