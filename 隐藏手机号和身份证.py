import re
import os

def get_file(url):
    files = []
    file_name_list = os.listdir(url)
    for file in file_name_list:
        if file.endswith("txt"):
            files.append(file)
    return files

def encrypt(url,file_list):
    re_phone = re.compile(r"^1[3-8](\d{5}\d{4}$)")
    re_identity_card = re.compile(r"\d{4}(\d{10})\d{4}|\d{3}[Xx]")
    for file in file_list:
        try:
            with open(url + "\\" + file,"r",encoding="utf=8") as f:
                content = f.readlines()
                print(content)
                for index,line in enumerate(content):
                    print(index,line)

        except:
            print("cuowu")

        else:
            phone = re.search(r"^1[3-8]\d{10}",content,re.S).span()
            print(content[0],phone)

url = input("输入地址：")
files = get_file(url)
print(files)
encrypt(url,files)