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
    re_phone = re.compile(r"1[3-8]\d{5}\d{4}")
    re_identity_card = re.compile(r"\d{4}\d{10}\d{4}|\d{3}[Xx]")
    def encrypt_phone(matched):
        phone = matched.group("phone")
        encrpt_phone = phone[:3]+"*****"+phone[8:]
        return encrpt_phone

    def encrypt_identify_card(matched):
        indentify_card = matched.group("identify_card")
        encrypt_identify_card = indentify_card[:5] + "********" + indentify_card[11:]

    for file in file_list:
        try:
            with open(url + "\\" + file,"r",encoding="utf=8") as f:
                content = f.readlines()
                content = "".join(content)
                print(content)
        except:
            print("cuowu")

        else:
           if (re_phone.search(content)):
               content = re.sub(r"(?P<phone>1[3-8]\d{5}\d{4})",encrypt_phone,content)
               is_change = True
           elif (re_identity_card.search(content)):
               content = re.sub((r"(?P<identify_card>\d{4}\d{10}\d{4}|\d{3}[Xx])",encrypt_identify_card,content)
           else:





url = input("输入地址：")
files = get_file(url)
print(files)
encrypt(url,files)