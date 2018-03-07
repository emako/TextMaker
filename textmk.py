import sys
import os
#where=1 -> Position (Right to left) Parm:pos, r2l
#where=2 -> Before Text Parm:before_text
#where=3 -> After Text Parm:after_text
def Insert(str1, str2, where=1, pos=0, right2left=False, before_text=None, after_text=None):
	def StrCombind(str1, str2, pos):
		return '{str_front}{str_insert}{str_behind}'.format(str_front=str1[0:pos], str_insert=str2, str_behind=str1[pos:])
	funcName = 'Insert'
	if where == 1:
		if right2left == True:
			pos = len(str1) - pos
		str_ret = StrCombind(str1, str2, pos)
	elif where == 2:
		if before_text == None:
			raise ValueError(funcName+': before_text is none.')
		pos = str1.find(before_text)
		if pos != -1:
			str_ret = StrCombind(str1, str2, pos)
		else:
			str_ret = str1
	elif where == 3:
		if after_text == None:
			raise ValueError(funcName+': after_text is none.')
		pos = str1.find(after_text)
		if pos != -1:
			pos += len(after_text)
			str_ret = StrCombind(str1, str2, pos)
		else:
			str_ret = str1
	return str_ret

def Delete(str, pos=0, count=1, right2left=False):
	funcName = 'Delete'
	if right2left == True:
		pos = len(str) - pos - count
	str_ret = '{str_front}{str_behind}'.format(str_front=str[0:pos], str_behind=str[pos+count:])
	return str_ret

def Remove(str1, str2, place='all'):
	funcName = 'Remove'
	place = place.lower()
	if place == 'all':
		str_ret = str1.replace(str2, '')
	elif place == 'first':
		pos = str1.find(str2)
		if pos != -1:
			count = len(str2)
			str_ret = Delete(str1, pos=pos, count=count, right2left=False)
		else:
			str_ret = str1
	elif place == 'last':
		pos = str1.find(str2)
		if pos != -1:
			count = len(str2)
			str_ret = Delete(str1, pos=pos, count=count, right2left=True)
		else:
			str_ret = str1
	else:
		raise ValueError(funcName+': palce.')
	return str_ret

def Replace(str1, str2=''):
	funcName = 'Replace'
	return str1.replace(str2)
	
def Split(str1, split, join=''):
	str_rets = str1.split(split)
	str_ret = join.join(str_rets)
	return str_ret

miru = Insert('123456789', 'abc', where=1, pos=100, right2left=False)
miru = Insert('123456789', 'abc', where=2, before_text='456')
#miru = Insert('123456789', 'abc', where=3, after_text='456')
miru = Delete('123456789', pos=3, count=3, right2left=True)
miru = Remove('123456789.123456789', '456', place='last')
miru = Split('123,123,123,123,', ',')
print("+"+miru+"+")