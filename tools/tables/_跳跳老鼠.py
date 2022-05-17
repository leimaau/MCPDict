#!/usr/bin/env python3

from tables._表 import 表 as _表
import re

class 表(_表):
	disorder = True

	def parse(self, fs):
		name = str(self)
		if name in ("金堂竹篙","綏寧河口","綏寧梅坪","宜章栗源","岳陽君山"):
			yb, sd, _, hzs = fs[:4]
		elif len(fs) > 3 and fs[3]:
			_, yb, sd, hzs = fs[:4]
		else:
			yb, sd, hzs = fs[:3]
		if sd == "調號": return
		yb = yb + sd
		l = list()
		for hz, c, js in re.findall("(.)([-=]?)(\[[^[]]*?\[[^[]]*?\][^[]]*?\]|\[.*?\])?", hzs):
			if js: js = js[1:-1]
			if hz == "~": hz = "□"
			l.append((hz, yb + c, js))
		return l

