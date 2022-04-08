#!/usr/bin/env python3

from tables._表 import 表

class 字表(表):
	key = "ko_okm"
	#https://github.com/nk2028/sino-korean-readings/blob/main/woosun-sin.csv
	_file = "woosun-sin.csv"
	isYb = False

	def parse(self, fs):
		hz = fs[0]
		py = "".join(fs[1:4])
		return hz, py
