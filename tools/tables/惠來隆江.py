#!/usr/bin/env python3

from tables._表 import 表

class 字表(表):
	key = "nan_cs_hllj"
	_file = "惠来隆江字表*.tsv"
	toneNames = {'阳入':8,'阴上':3,'阳平':2,'阴入':7,'阴平':1,'去声':5,'阳上':4}

	def parse(self, fs):
		_,hz,_,yb,js = fs[:5]
		if not yb: return
		for i in self.toneNames:
			if i in yb:
				yb = yb.replace(i, str(self.toneNames[i]))
				break
		return hz, yb, js

