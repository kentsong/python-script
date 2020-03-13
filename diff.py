#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import difflib

try:
	tfile1=sys.argv[1]
	tfile2=sys.argv[2]
except Exception as e:
	print ("错误："+str(e))
	print ("请准确输入参数，例如：python diff.py file1 file2")
	sys.exit()
def readfile(filename):
	try:
		fileHandle=open(filename,'rb')
		lines=fileHandle.read().splitlines()
		fileHandle.close()
		return lines
	except IOError as error:
		print('读取文件错误：'+str(error))
		sys.exit()
if tfile1=="" or tfile2=="":
	print ("请准确输入参数，例如：python diff.py file1 file2")
	sys.exit()

with open(tfile1, 'r') as mem:
    mems = mem.readlines()
    mem.close()

with open(tfile2, 'r') as mem2:
    mems2 = mem2.readlines()
    mem2.close()



#d=difflib.HtmlDiff()
#print s.make_file(tfile1_lines,tfile2_lines)

#为了生成html能识别中文，可用下面代码 #修改diff.html的编码，将ISO-8859-1改为UTF-8
#====================================
#方法1：
d=difflib.HtmlDiff()
q=d.make_file(mems,mems2)
old_str='charset=ISO-8859-1'
new_str='charset=UTF-8'
data=q.replace(old_str,new_str)
fo=open('diff.html','w')
fo.write(data)
fo.close()
#====================================
#方法2：
#d=difflib.HtmlDiff()
#q=d.make_file(tfile1_lines,tfile2_lines)
#old_str='charset=ISO-8859-1'
#new_str='charset=UTF-8'
#fo=open('diff.html','w')
#fo.write(q)
#fo.close()
#with open('diff.html','r') as f:
#        lines=f.readlines()
#with open('diff.html','w') as f_new:
#        for line in lines:
#                f_new.write(line.replace(old_str,new_str))
#=====================================
#方法3：
# old_str='charset=ISO-8859-1'
# new_str='charset=UTF-8'
# d=difflib.HtmlDiff()
# q=d.make_file(tfile1_lines,tfile2_lines)
# with open('diff.html','w') as f_new:
# 	f_new.write(q.replace(old_str,new_str))