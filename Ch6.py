#-*- coding: UTF-8 -*-
import re
re.search('\351','''Qu’est-ce que la tolérance? c’est l’apanage de l’humanité. 
	Nous sommes tous pétris de faiblesses et d’erreurs; pardonnons-nous réciproquement nos sottises, 
	c’est la première loi de la nature.''')

asc = open('Data/ascii.txt')
a = asc.read()
re.search('\cG',a)
#查找控制字符，python可能不适用，待补充