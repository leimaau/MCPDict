#!/usr/bin/env python3

from tables._表 import 表

class 字表(表):
	key = "och_ba"
	_file = "BaxterSagartOC2015-10-13.tsv"
	_city = "白-沙"
	_lang = "上古（白一平沙加爾2015）"
	note = "來源：<a href=http://ocbaxtersagart.lsait.lsa.umich.edu/>上古音白一平沙加爾2015年擬音</a>"
	isYb = False

	def parse(self, fs):
		return fs[0], fs[4]
