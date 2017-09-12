# -*- coding: UTF-8 -*-
import re

tel = '707-827-7019'
print 'Regular Expressions with tel number 707-827-7019'

a = re.match ('\d', tel)
print "using \d:", a.group()

a = re.match ('\d*', tel)
print "using \d*:", a.group()

a = re.match ('[0-9]', tel)
print "using [0-9]:", a.group()

a = re.match ('[012789]', tel)
print "using [012789]:", a.group()

a = re.match ('\d\d\d-\d\d\d-\d\d\d\d', tel)
print "using \d\d\d-\d\d\d-\d\d\d\d:", a.group()

a = re.match ('\d\d\d.\d\d\d.\d\d\d\d', tel)
print "using \d\d\d.\d\d\d.\d\d\d\d:", a.group()

a = re.match ('(\d)\d\\1', tel)
print "using (\d)\d\\1:", a.group()
#re包反向引用需要两个\

a = re.match ('\d{3}-?\d{3}-?\d{4}', tel)
print "using \d{3}-?\d{3}-?\d{4}:", a.group()

a = re.match ('(\d{3,4}[.-]?)+', tel)
print "using (\d{3,4}[.-]?)+:", a.group()

a = re.match ('(\d{3}[.-]?){2}\d{4}', tel)
print "using (\d{3}[.-]?){2}\d{4}:", a.group()

a = re.match ('^(\(\d{3}\)|\d{3}[.-]?)?\d{3}[.-]?\d{4}$', tel)
print "using ^(\(\d{3}\)|\d{3}[.-]?)?\d{3}[.-]?\d{4}$:", a.group()
#包含判断电话号码首三位是否有括号