import scrapy
from scrapy.selector import Selector
from xoso.items import XosoItem, GiaiItem
from bs4 import BeautifulSoup
from lxml import etree
import requests

class xoso_spider(scrapy.Spider):
    name = 'xs'
    allowed_domains = ['minhngoc.net.vn']
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    start_urls = ['https://www.minhngoc.net.vn/ket-qua-xo-so/mien-nam.html']

    # def start_requests(self):
    #     return scrapy.Request('https://www.minhngoc.net.vn/ket-qua-xo-so/mien-nam.html', self.parse)
    def parse(self, response):
        print("========")
        with open(f'html.html', 'wb') as f:
            f.write(response.body)
        Tinhs = Selector(response).xpath('//*[@id="noidung"]/div[2]/div[2]/div[2]/table[1]/tbody/tr/td[2]/table')
        #'//*[@id="noidung"]/div[2]/div[2]/div[2]/table[1]/tbody/tr/td[2]/table/tbody/tr'
        #'//*[@id="noidung"]/div[2]/div[2]/div[2]/table[1]/tbody/tr/td[2]/table/tbody/tr/td[1]'
        #tinh2 = Tinhs.xpath('//tbody/tr/td[2]/table/tbody/tr/td[1]')
        # req = requests.get('https://www.minhngoc.net.vn/ket-qua-xo-so/mien-nam.html')

        # with open("html.html") as fp:
        #     soup = BeautifulSoup(fp, features="lxml")
        tinh2 = Selector(response).xpath('//*[@id="noidung"]/div[2]/div[2]/div[2]/table[1]/tbody/tr/td[2]/table').getall()[0]
        # print(tinh2)
        #test = Selector(response).xpath('//*[@id="noidung"]/div[3]/div[2]')

        soup = BeautifulSoup(tinh2, "html.parser")
        print(type(soup))
        with open("out_table.html","w",encoding='utf-8') as file:
            file.writelines(str(soup))

        # dom = etree.HTML(str(soup))
        self.logger.info(soup.find_all("table")[0].find_all("table")[1].find_all(class_="giai8")[0].text)
        print("===dcm=====")
        #self.logger.info(test)
        print("===dcm2=====")

        #for tinh in Tinhs:
        self.logger.info("-----------")
        item = XosoItem()

        # item['Tây_Ninh'] = self.parse2(Tinhs.xpath('td[1]/table/tbody'))
        # item['An_Giang'] = self.parse2(Tinhs.xpath('td[2]/table/tbody'))
        # item['Bình_Thuận'] = self.parse2(Tinhs.xpath('td[3]/table/tbody'))
        item['Tây_Ninh'] = {self.parse2(soup.find_all("table")[0].find_all("table")[0])}
        item['An_Giang'] = {self.parse2(soup.find_all("table")[0].find_all("table")[1])}
        item['Bình_Thuận'] = {self.parse2(soup.find_all("table")[0].find_all("table")[2])}
        yield item

    def parse2(self, path:BeautifulSoup):
        self.logger.info(path.find_all(class_="giai6"))
        item2 = GiaiItem()
        item2['Tên_Tỉnh'] = self.remove_space(path.find_all(class_="tinh")[0].text)
        item2['Mã_Tỉnh'] = self.remove_space(path.find_all(class_="matinh")[0].text)
        item2['Giải_Tám'] = self.remove_space(path.find_all(class_="giai8")[0].text)
        item2['Giải_Bảy'] = self.remove_space(path.find_all(class_="giai7")[0].text)
        print("===================================")
        for x in path.find_all(class_="giai6")[0].find_all('div'):
            print("*************************8")
            print(x.text)
        item2['Giải_Sáu'] = {self.remove_space(x.text).replace('\n','') for x in path.find_all(class_="giai6")[0].find_all('div')}
        item2['Giải_Năm'] = self.remove_space(path.find_all(class_="giai5")[0].text)
        item2['Giải_Tư'] = {self.remove_space(x.text) for x in path.find_all(class_="giai4")[0].find_all('div')}
        item2['Giải_Ba'] = {self.remove_space(x.text) for x in path.find_all(class_="giai3")[0].find_all('div')}
        item2['Giải_Nhì'] = self.remove_space(path.find_all(class_="giai2")[0].text)
        item2['Giải_Nhất'] = self.remove_space(path.find_all(class_="giai1")[0].text)
        item2['Giải_Đặc_Biệt'] = self.remove_space(path.find_all(class_="giaidb")[0].text)
        return item2

    def remove_space(self, x):
        return x.replace('\n','').replace('\r','').replace('\t','')








