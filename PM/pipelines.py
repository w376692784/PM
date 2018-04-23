# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import xlwt

class PmPipeline(object):
    cities = ['上海','南京','无锡','常州','苏州','南通','盐城','扬州','镇江','泰州','杭州','宁波','嘉兴','湖州','绍兴','金华',
            '舟山','台州','合肥','芜湖','马鞍山','铜陵','安庆','滁州','池州','宣城']
    cities_en = ['shanghai','nanjing','wuxi','changzhou','suzhou','nantong','yancheng','yangzhou','zhenjiang','jstaizhou','hangzhou',
            'ningbo','jiaxing','huzhou','shaoxing','jinhua','zhoushan','taizhou','hefei','wuhu','maanshan','tongling','anqing',
            'chuzhou','chizhou','xuancheng']
    city = dict.fromkeys(cities,1)
    # num = range(26)
    city_count = dict(zip(cities,range(26)))
    titles = ['日期', '质量等级', 'AQI指数', '当天AQI排名', 'PM2.5', 'PM10', 'So2', 'No2', 'Co', 'O3']

    def __init__(self):
        if os.path.exists('/home/sephiroth/桌面/PM/Summary.xlsx'):
            os.remove('/home/sephiroth/桌面/PM/Summary.xlsx')
        self.sheet = dict.fromkeys(range(26),' ')
        self.f = xlwt.Workbook()
        for i in self.cities:
            # print(self.city_count[i])
            self.sheet[self.city_count[i]] = self.f.add_sheet(i,cell_overwrite_ok=True)
            # print(self.sheet[self.city_count[i]])
            for j in range(0, len(self.titles)):
                self.sheet[self.city_count[i]].write(0, j, self.titles[j])

    def process_item(self, item, spider):
        self.sheet[self.city_count[item['city']]].write(self.city[item['city']], 0, item['date'])
        self.sheet[self.city_count[item['city']]].write(self.city[item['city']], 1, item['quality_level'])
        self.sheet[self.city_count[item['city']]].write(self.city[item['city']], 2, item['AQI'])
        self.sheet[self.city_count[item['city']]].write(self.city[item['city']], 3, item['AQI_level'])
        self.sheet[self.city_count[item['city']]].write(self.city[item['city']], 4, item['PM2_5'])
        self.sheet[self.city_count[item['city']]].write(self.city[item['city']], 5, item['PM10'])
        self.sheet[self.city_count[item['city']]].write(self.city[item['city']], 6, item['So2'])
        self.sheet[self.city_count[item['city']]].write(self.city[item['city']], 7, item['No2'])
        self.sheet[self.city_count[item['city']]].write(self.city[item['city']], 8, item['Co'])
        self.sheet[self.city_count[item['city']]].write(self.city[item['city']], 9, item['O3'])
        self.city[item['city']] += 1
        # self.data.append(item_list)
        # return item
    def close_spider(self,spider):
        self.f.save('/home/sephiroth/桌面/PM/Summary.xlsx')
