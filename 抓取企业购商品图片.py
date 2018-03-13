import urllib.request
import urllib.parse
import json

#获取用户token
def get_logintoken(userid):
    url = r"http://10.0.66.93/wchat/wap/tokenCreate"
    data = {"userId":userid}
    datas = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url,data=datas)
    try:
        response = urllib.request.urlopen(req)
    except:
        print(response.status)
    else:
        response = json.load(response)
        return response["message"]


def get_class(token):
    url = r"http://10.0.66.93/wchat/wap/buyer/topClass"
    headers = {"login-token":token}
    req = urllib.request.Request(url,headers=headers)
    try:
        response = urllib.request.urlopen(req)
    except:
        print(response.status)
    else:
        response = json.load(response)
        print(response)
        for i in response["data"]:
            print("%s:%s"%(i,response["data"][i]))


userid = input("输入用户id：")
token = get_logintoken(userid)
get_class(token)