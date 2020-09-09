from docx import Document
import json

projects = ["lcer", "tsyy", "zzyy"]



def diary_doc(date):
    for d in date:
        for project in projects:
            dataname = "D:/2020-云天/DataHandler/CYD/" + project + "/AttackDate/" + d + ".txt"
            docname = "D:/2020-云天/DataHandler/CYD/" + project + "/日常巡检/" + project + d + "巡检记录.docx"
            sum1 = 0
            sum2 = 0
            sum3 = 0
            sum4 = 0
            sum5 = 0
            sum6 = 0
            sum7 = 0
            sum8 = 0
            sum9 = 0
            sum10 = 0
            sum11 = 0
            sum12 = 0
            sum13 = 0
            with open(dataname, encoding="UTF-8") as f:
                content = json.loads(f.read())
                f.close()
                for a in content["data"]["details"]:
                    sum1 += a["base"]["恶意扫描"]
                    sum2 += a["base"]["远程命令"]
                    sum3 += a["base"]["XSS跨站"]
                    sum4 += a["base"]["SQL注入"]
                    sum5 += a["base"]["敏感文件访问"]
                    sum6 += a["base"]["webshell"]
                    sum7 += a["base"]["代码执行"]
                    sum8 += a["base"]["恶意采集"]
                    sum9 += a["base"]["文件包含"]
                    sum10 += a["base"]["特殊攻击"]
                    sum11 += a["base"]["CC攻击"]
                    sum12 += a["base"]["其它"]
                    sum13 += a["rule"]["动态阻断拦截"]
            document = Document("D:/2020-云天/DataHandler/CYD/日常巡检模板/temple1.docx")
            table = document.tables[0]
            for row in table.rows[1].cells:
                print(row.text)



if __name__ == '__main__':
    diary_doc(["2020-09-08"])