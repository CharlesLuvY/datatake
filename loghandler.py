import requests
import json
import datetime
import gzip

projects = ["lcer", "tsyy", "zzyy"]
logType = ["attack", "access"]

netUrl = {
    "lcer": "lceryuan.net",
    "tsyy": "taishanyy.com",
    "zzyy": "zz-zxyy.com"
}


def GetDownloadLink(payload):
    url = 'https://cloudskysec.365cyd.com/log_download/make_download_link'

    headers = {
        'Cookie': 'csrftoken=aBWO4YyJRh9L1dKxBAjqR5S3R4anVnrA; 365cyd_com_sid=zaljj9uxarislk5y7fagdczll8r9xlcu',
        'Host': 'cloudskysec.365cyd.com',
        'Referer': 'https://cloudskysec.365cyd.com/log_download/list/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'X-CSRFToken': 'aBWO4YyJRh9L1dKxBAjqR5S3R4anVnrA'
    }

    response = requests.post(url, payload, headers=headers)
    print(f'正在获取{filename}下载链接...', end='')
    try:
        download_link = json.loads(response.text)['data']['download_link']
        print('成功！')
        return download_link
    except BaseException as e:
        print(response.text)
        print(e)
        return 0


def Download(download_link):
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    }

    response = requests.get(download_link, headers=headers)
    print(f'正在下载{filename}...', end='')
    log = gzip.decompress(response.content)
    with open(filename, 'wb') as f:
        f.write(log)
        f.close()
        print('成功！')


for p in projects:
    for l in logType:
        payload = {
            'log_type': l,
            'date_index': '20200907',
            'domain': netUrl[p],
            'action_type': 'day'
        }
        filename = 'D:/2020-云天/DataHandler/CYD/log/' + p + '/' + payload['log_type'] + '/' + payload['domain'] + '-' + payload['log_type'] + "-" + payload['date_index'] + '.log'
        try:
            DL = GetDownloadLink(payload)
            Download(DL)
        except BaseException as e:
            with open('D:/2020-云天/DataHandler/CYD/log/error.log', mode='a') as f3:
                print('失败！')
                f3.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\t{filename}下载失败，失败原因：")
                f3.write(str(e))
                f3.write('\n')
                f3.close()
