# -*- coding: gbk -*-
import scrapy
from PM.items import PmItem

class PmSpider(scrapy.Spider):
    name = 'pm'
    allowed_domains = ['www.tianqihoubao.com']
    start_urls = []
    base_url = 'http://www.tianqihoubao.com/aqi/'
    city = ['shanghai','nanjing','wuxi','changzhou','suzhou','nantong','yancheng','yangzhou','zhenjiang','jstaizhou','hangzhou',
            'ningbo','jiaxing','huzhou','shaoxing','jinhua','zhoushan','taizhou','hefei','wuhu','maanshan','tongling','anqing',
            'chuzhou','chizhou','xuancheng']
    years = range(2013,2019)
    month = ['01','02','03','04','05','06','07','08','09','10','11','12']
    for k in city:
        for i in years:
            for j in month:
                if (int(i) == 2013 and int(j) < 10) or (int(i) == 2018 and int(j) > 4):
                    continue
                start_urls.append(base_url + str(k) + '-' + str(i) + str(j) + '.html')
    # print(start_urls)
    # start_urls = ['http://www.tianqihoubao.com/']

    def parse(self, response):
        # print(response.body.decode('gbk'))
        # response.body = response.body.decode('gbk')
        city = response.xpath('//h1/text()').extract()[0].strip()[-21:-19]
        # print(city)
        item_list = response.xpath('//table/tr')
        # print(item_list)
        count = 1
        for item in item_list:
            if count == 1:
                count += 1
                continue
            data = PmItem()
            data['city'] = city
            data['date'] = item.xpath('./td[1]/text()').extract()[0].strip()
            data['quality_level'] = item.xpath('./td[2]/text()').extract()[0].strip()
            data['AQI'] = item.xpath('./td[3]/text()').extract()[0].strip()
            data['AQI_level'] = item.xpath('./td[4]/text()').extract()[0].strip()
            data['PM2_5'] = item.xpath('./td[5]/text()').extract()[0].strip()
            data['PM10'] = item.xpath('./td[6]/text()').extract()[0].strip()
            data['So2'] = item.xpath('./td[7]/text()').extract()[0].strip()
            data['No2'] = item.xpath('./td[8]/text()').extract()[0].strip()
            data['Co'] = item.xpath('./td[9]/text()').extract()[0].strip()
            data['O3'] = item.xpath('./td[10]/text()').extract()[0].strip()
            yield data