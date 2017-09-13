# -*- coding: UTF-8 -*-
import re

rime = open('Data/rime-intro.txt')
text = rime.read()
print "Regular Expressions with rime-intro.txt"
print text

##def h1(matched):
##	  m = int (matched.group())
##	  return ('<h1>'+matched+'<\h1>')

#regex = re.compile('(.*$)')
#a = regex.sub('<h1>\g<1><\h1>', text)

a = re.sub('(.*$)', '<h1>\g<1><\h1>', text)

print a