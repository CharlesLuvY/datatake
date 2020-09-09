import datetime
import json
import requests

JSLcookie = "xd64w8ib2omca9tbq93wpnuke94va2cx"
csrfToken = "snAWPuKTCNAvp7EvEip29Ww98RLqtEZazNPOQNy814bpwsw4HaNwFMCyzCtnB7Ba"
Project = "zzyy"

netUrl = {
    "lcer": "lceryuan.net",
    "tsyy": "taishanyy.com",
    "zzyy": "zz-zxyy.com"
}
headers = {
    'Cookie': 'csrftoken=g5DYgICGHDyBACsTYRACri2IWeT1Py3jnvSQh1qV6U9vHXks1JY6X887nZBYX1Fj; jiasule_com_sid=' + JSLcookie,
    'Referer': 'https://report.365cyd.com/report/v3/waf/?filter_site=lceryuan.net&filter_host=&set_area=zh',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
}


def DownCountryData(date):
    url = "https://report.365cyd.com/report/v3/waf/data/location_country/"
    payload = {
        'csrfmiddlewaretoken': csrfToken,
        'filter_site': netUrl[Project],
        'filter_host': ''
    }
    for d in date:
        filename = "D:/2020-云天/DataHandler/CYD/" + Project + "/CountryDate/" + d + ".txt"
        payload['searchDate'] = d
        response = requests.post(url, payload, headers=headers) 
        data = json.loads(response.text)
        if data['status'] == "success":
            with open(filename, mode="w", encoding="UTF-8") as f:
                f.write(response.text)
                print(d + "境内攻击信息下载成功!")
                f.close()
        else:
            print(d + "境内攻击信息下载失败，错误信息:" + data["message"])


def DownAttackData(date):
    url = "https://report.365cyd.com/report/v3/waf/data/trend/"
    payload = {
        'csrfmiddlewaretoken': csrfToken,
        'filter_site': netUrl[Project],
        'filter_host': '',
        'ip_type': 'all',
    } 
    for d in date:
        filename = "D:/2020-云天/DataHandler/CYD/" + Project + "/AttackDate/" + d + ".txt"
        payload['searchDate'] = d + "~" + d
        response = requests.post(url, payload, headers=headers) 
        data = json.loads(response.text)
        if data['status'] == "success":
            with open(filename, mode="w", encoding="UTF-8") as f:
                f.write(response.text)
                print(d + "攻击类型信息下载成功!")
                f.close()
        else:
            print(d + "攻击类型信息下载失败，错误信息:" + data["message"])


def DownForeignData(date):
    url = "https://report.365cyd.com/report/v3/waf/data/location_foreign/"
    payload = {
        'csrfmiddlewaretoken': csrfToken,
        'filter_site': netUrl[Project],
        'filter_host': '',
    } 
    for d in date:
        filename = "D:/2020-云天/DataHandler/CYD/" + Project + "/ForeignDate/" + d + ".txt"
        payload['searchDate'] = d + "~" + d
        response = requests.post(url, payload, headers=headers) 
        data = json.loads(response.text)
        if data['status'] == "success":
            with open(filename, mode="w", encoding="UTF-8") as f:
                f.write(response.text)
                print(d + "境外攻击信息下载成功!")
                f.close()
        else:
            print(d + "境外攻击信息下载失败，错误信息:" + data["message"])


def DateGenerator(stime, ftime):
    date = []
    time_s = datetime.datetime.strptime(stime, "%Y-%m-%d")
    time_f = datetime.datetime.strptime(ftime, "%Y-%m-%d")
    while time_s <= time_f:
        date.append(time_s.strftime("%Y-%m-%d"))
        time_s += datetime.timedelta(days=1)
    return date
