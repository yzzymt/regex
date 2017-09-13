# -*- coding: UTF-8 -*-
import re

#a = re.match('\Q$\E', '$')
a = re.match('[$]', '$')
#\Q\E中内容理解为纯字符，使用[]实现