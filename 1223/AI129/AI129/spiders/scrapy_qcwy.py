
import scrapy
from lxml import etree
class scrapy_qc(scrapy.Spider):
    name = 'qc'
    def start_requests(self):
        pass
        yield scrapy.Request(url='https://search.51job.com/list/010000,000000,0000,00,9,99,python%2520web,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=',callback=self.parse)
    def parse(self, response):
        # print(response.text)
        html=etree.HTML(response.text)
        url_list=html.xpath('//p[@class="t1 "]/span/a/@href')
        # for url in url_list:
        yield scrapy.Request(url=url_list[0],callback=self.parse1)
    def parse1(self,response):
        # print(response.text)
        html=etree.HTML(response.text)
        zhiwei=html.xpath('//h1/@title')[0]#职位
        # print(zhiwei)
        salary=html.xpath('//div[@class="cn"]/strong/text()')[0]#工资
        # print(salary)
        gs=html.xpath('//a[@class="com_name himg"]/p/@title')[0]#公司
        # print(gs)
        jingyan=html.xpath('//p[@class="msg ltype"]/text()')[1]#经验
        # print(jingyan)
        xueli=html.xpath('//p[@class="msg ltype"]/text()')[2]#学历
        # print(xueli)

        guanwang=html.xpath('//p[@class="cname"]/a/@href')[0]
        print(guanwang)
