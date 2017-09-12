# -*- coding: UTF-8 -*-
#输入电话号码查询归属地及运营商
import re

n = raw_input("What's your phone num?\n")
num = re.search('.{7}', n)
n = num.group()

data = open('Data/data.txt')
tel = data.read()

a = re.search(n + '.{5}(.{6}).{5}(.{6}).{5}(.{12})', tel)
print '归属地:'+a.group(1)+a.group(2)+'\n运营商:'+a.group(3)
