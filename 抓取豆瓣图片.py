import re
import urllib.request
import urllib.parse

class album:
    url = r"https://www.douban.com/photos/album/"
    lines = ""
    pattern = ""
    dir_name = []
    def __init__(self,album_num):
        self.album_num = album_num
        self.url = self.url + self.album_num

    def save_douban_html(self):
        try:
            response = urllib.request.urlopen(self.url)
        except:
            return self.url
        else:
            with open("douban.txt", 'w', encoding="utf-8") as f:
                f.write(response.read().decode("utf-8"))

    def dir_file(self):
        with open("douban.txt", 'r', encoding="utf-8") as f:
            self.lines = f.readlines()
        self.pattern = re.compile(r"<div\sclass=.info.>\s*?<h1>(.*?)</h1>\s*?",re.S)
        self.dir_name = self.pattern.findall(str(self.lines))
        print(self.dir_name)

album_num = input("输入图片专辑：")
a = album(album_num)
a.save_douban_html()
a.dir_file()


https://www.douban.com/photos/album/76894387

