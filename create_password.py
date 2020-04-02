# -*- coding=utf-8 -*-

from random import choice, sample, shuffle
from os import system

#设置各种字符
chars = '`~!@#$%^&*(){}[]_+-=/,.|:;<>?\\\'\"'
capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
number = '0123456789'

string = ''
print('1.字符		2.大写字母	3.小写字母	4.数字')
options = input('Please choose the options that your password would contain:')

#去除无效输入
index = []
_index = []
for i in list(options):
	if i not in index:
		index.extend(i)
for j in index:
	if j in ['1', '2', '3', '4']:
		_index.extend(j)

#集合所需字符
for option in list(_index):
	if option == '1':
		string += chars
	elif option == '2':
		string += capital
	elif option == '3':
		string += lowercase
	elif option == '4':
		string += number

#输入密码长度并生成
length = int(input('Please input the length of the password you want to get:'))

#至少包含一种字符的方式
count = 0
temp = []
while count < length-len(list(_index)):
	count += 1
	temp.extend(sample(string, 1))
for option in list(_index):
	if option == '1':
		temp.extend(sample(chars, 1))
	elif option == '2':
		temp.extend(sample(capital, 1))
	elif option == '3':
		temp.extend(sample(lowercase, 1))
	elif option == '4':
		temp.extend(sample(number, 1))

shuffle(temp)
temp = ''.join(temp)
print(temp)
#print(len(temp))

system('pause')

