# -*- coding: UTF-8 -*-
import re

rime = open('Data/rime.txt')
text = rime.read()

a = re.findall('(?i)the', text)
#(?i)不区分大小写
print '共找到'+ str(len(a)) +'个结果'
print a

a = re.findall('[tT]h[eir]*', text)
print '共找到'+ str(len(a)) +'个结果'
print a