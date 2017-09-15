#-*- coding: UTF-8 -*-
import re
rime = open ('Data/rime.txt')
text = rime.read()

a = re.sub('(T.*PARTS)\.', '<title>\g<1></title>', text)


f = open("demo.html",'w')
f.write(a)
f.close()