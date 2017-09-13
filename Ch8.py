#-*- coding: UTF-8 -*-
import re
rime = open('Data/rime-intro.txt')
text = rime.read()

a = re.search('(?i)ancyent (?=marinere)', text)
print a.group()
#环视，正前瞻，要求紧随其后的单词时marinere

a = re.search('(?i)ancyent (?!marinere)', text)
if a:
	print a.group()
else:
	print 'No match'
#反前瞻，要求后面不跟随

a = re.search('(?i)(?<=ancyent) marinere', text)
print a.group()
#正后顾，要求前面的单词为ancyent

a = re.search('(?i)(?<!ancyent) marinere', text)
if a:
	print a.group()
else:
	print 'No match'
#反后顾，要求前面的单词不为ancyent