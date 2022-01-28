#!/usr/bin/env python3

from tables._縣志 import 字表 as 表

class 字表(表):
	key = "cjy_ll_fz_ls"
	_file = "离石话同音字表*.tsv"
	note = "來源：李小平 2004《山西離石方言音系》；安靜先生 整理錄入"
	tones = "24 1 1a 陰平 ꜀,44 2 1b 陽平 ꜁,312 3 2 上 ꜂,,52 5 3 去 ꜄,,4 7 4a 陰入 ꜆,23 8 4b 陽入 ꜇"
	simplified = 2
