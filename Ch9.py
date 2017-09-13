#-*- coding: UTF-8 -*-
import re
html = open('Data/lorem.dita')
text = html.read()

a = re.findall('<[_a-zA-Z][^>]*>',text)
print a