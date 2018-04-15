#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import urllib.request
import urllib.parse
import urllib.error
import requests
import os


class album:

    def save_douban_html(self,url):
        self.url = url
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
        except:
            print("cuowu")
        else:
            return response.text

    def dir_file(self,response):
        self.response = response
        self.head_pattern = re.compile(r"<head>.*?<title>(.*?)</title>",re.S)
        self.dir_name = self.head_pattern.findall(self.response)
        print(self.dir_name)
        self.path = "F:\\杂物\\豆瓣-图\\" + self.dir_name[0]
        try:
            os.mkdir(self.path)
        except:
            pass

    def get_photo(self,response):
        self.response = response
        self.photo_pattern = re.compile(r"<a.*?class=.photolst_photo.*?src=\"(.*?)\"",re.S)#正则匹配图片链接
        self.photo_name_pattern = re.compile(r".*?(p\d+\.jpg)")#正则匹配图片名称
        self.photo_page_pattern = re.compile(r"<span\sclass=.next.*?<a\shref=\"(.*?)\"\s>",re.S)#正则匹配图片下一页地址
        self.get_photo_url = self.photo_pattern.findall(self.response)
        self.next_page_url = self.photo_page_pattern.findall(self.response)
        for url in self.get_photo_url:
            self.get_photo_name =self.photo_name_pattern.findall(url)
            print(self.get_photo_name)
            urllib.request.urlretrieve(url,self.path + "\\" + self.get_photo_name[0])  # 把图片下载到对应文件夹
        return  self.next_page_url



album_num = input("输入图片专辑：")
url = r"https://www.douban.com/photos/album/"+album_num
a = album()
html = a.save_douban_html(url)
print(html)
a.dir_file(html)
next_page = a.get_photo(html)
print(next_page)
while next_page:
    html = a.save_douban_html(next_page[0])
    next_page = a.get_photo(html)
    print(next_page)


#https://www.douban.com/photos/album/1658059987/


'''
        try:
            response = urllib.request.urlopen(self.url)
        except urllib.error.HTTPError as e:
            print('Error code: ', e.code)
        else:
            print(response.geturl())#返回请求的链接地址
            return response.read().decode("utf-8")
'''
