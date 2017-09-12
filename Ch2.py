# -*- coding: UTF-8 -*-
import re

rime = open('Data/rime-intro.txt')
text = rime.read()
print "Regular Expressions with rime-intro.txt"
print text

a = re.findall('\d', text)
print "using \d:", a

a = re.findall('[01]', text)
print "using [01]:", a

a = re.findall('\D', text)
print "using \D:", a

a = re.findall('[^0-9]', text)
print "using [^0-9]:", a

a = re.findall('\W', text)
print "using \W:", a

a = re.findall('\s', text)
print "using \s:", a
#匹配空白符，制表符（\t），换行符（\n），回车符（\r）

a = re.match ('.{8}', text)
print "using .{8}:", a.group()

a = re.search ('A.{5}T', text)
print "using A.{5}T:", a.group()
#使用search寻找整个字符串的第一个匹配

a = re.search ('\w{7}', text)
print "using \w{7}:", a.group()

a = re.search ('\\b\w{5}\\b', text)
print "using \w{7}:", a.group()
#\\b匹配单词边界，没有\\b匹配ANCYE，有\\b匹配SEVEN