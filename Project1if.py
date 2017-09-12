# -*- coding: UTF-8 -*-
#输入电话号码查询归属地及运营商
import re

n = raw_input("请输入十一位完整手机号码或前七位数字：\n")
num = re.search('^(1\d{6})$|^(1\d{10})$', n)

if num:
	n = num.group(1)
else：
	print '输入错误，请重新输入。'
	exit()

data = open('Data/data.txt')
tel = data.read()

a = re.search(n + '.{5}(.{6}).{5}(.{6}).{5}(.{12})', tel)
if a:
	print '归属地:'+a.group(1)+a.group(2)+'\n运营商:'+a.group(3)
else:
	print '查无结果'