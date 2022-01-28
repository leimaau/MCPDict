#!/usr/bin/env python3

from tables._表 import 表
import re

class 字表(表):
	key = "hsn_cayi_ct_xxjtp"
	note = "來源：孙益民.湖南湘阴方言同音字汇[J].湖南大眾傳媒職業技術學院學報<br>轉錄者：跳跳老鼠"
	tones = "33 1 1a 陰平 ꜀,13 2 1b 陽平 ꜁,42 3 2 上 ꜂,,45 5 3a 陰去 ꜄,21 6 3b 陽去 ꜅"
	_file = "湘陰界頭鋪*.tsv"
	disorder = True
	simplified = 2

	def parse(self, fs):
		_, yb, sd, hzs = fs[:4]
		yb = yb + sd
		l = list()
		for hz, c, js in re.findall("(.)([-=]?)(\[.*?\[.*?\].*?\]|\[.*?\])?", hzs):
			if js: js = js[1:-1]
			l.append((hz, yb + c, js))
		return l

