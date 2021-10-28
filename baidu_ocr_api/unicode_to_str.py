# -*- coding:utf-8 -*-

import json
from docx import Document
from docx.shared import Pt
f = open('/Users/aqumik/Desktop/Github/chineseocr/data.json','r')
content = f.read()
a = json.loads(content)
# a = content

print(type(a))
print(a)
f.close()

document = Document()


b = a['words_result']
print(type(b))
for item in b:
    print(item['words'])
    doc = item['words']
    document.add_paragraph(doc)

style = document.styles['Normal']
font = style.font
font.size = Pt(10)

document.save('test1.docx')