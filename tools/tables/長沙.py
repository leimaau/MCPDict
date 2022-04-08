#!/usr/bin/env python3

from tables._表 import 表

class 字表(表):
	key = "hsn_cs"
	_file = "長沙話字表 *.tsv"

	def parse(self, fs):
		#"拼音"	"寬式IPA"	"調號"	"字甲"	"字乙"	"釋義"
		_, yb, sd, hz, hzb, js = fs[:6]
		yb = yb + sd
		l = list()
		l.append((hz, yb, js))
		if hz != hzb and hzb:
			l.append((hzb, yb, js))
		return l


