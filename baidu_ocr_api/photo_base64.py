#-*-coding:utf-8 -*-
import json
import time
import requests
import base64
import urllib.parse
import json
from docx import Document
from docx.shared import Pt


'''
通用文字识别
'''
#25.ea11ec46f63173a157
request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
# 二进制方式打开图片文件


# png_path = '/Users/aqumik/Desktop/t1/192.png'
# f = open(png_path, 'rb')
# img = base64.b64encode(f.read())


document = Document()

for i in range(1,203):
    # print(i)
    png_path = '/Users/aqumik/Desktop/t1/' + str(i) + '.png'
    print(png_path)
    f = open(png_path,'rb')
    img = base64.b64encode(f.read())
    params = {"image":img}
    access_token = '24.9599d7c65d9f1093'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    time.sleep(3)
    if response:
        print (response.json())
        data = response.json()
        dataJson = json.dumps(data,ensure_ascii=False)
        fileObject = open('data.json', 'w')
        fileObject.write(dataJson)
        fileObject.close()


        f = open('/Users/aqumik/Desktop/Github/chineseocr/data.json', 'r')
        content = f.read()
        a = json.loads(content)
        # a = content
        print(type(a))
        print(a)
        f.close()

        b = a['words_result']
        print(type(b))
        for item in b:
            print(item['words'])
            doc = item['words']
            document.add_paragraph(doc)
        style = document.styles['Normal']
        font = style.font
        font.size = Pt(10)
document.save('test4.docx')



