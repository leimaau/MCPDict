#!/usr/bin/env python3

from tables._表 import 表

class 字表(表):
	key = "wuu_oj_wz"
	_file = "温州方言同音字表*.tsv"
	toneValues = {'阳入':8,'阴上':3,'阳平':2,'阴入':7,'阳去':6,'阴平':1,'阴去':5,'阳上':4}

	def parse(self, fs):
		_,hz,_,yb,_,_,sd,js = fs[:8]
		if not yb: return
		sd = str(self.toneValues[sd])
		yb += sd
		return hz, yb, js
