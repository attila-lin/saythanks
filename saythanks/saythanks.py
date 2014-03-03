# -*- coding: utf-8 -*-
#!/usr/bin/env python
import urllib
import cookielib, urllib2
import string
import time
import httplib2

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

# 添加多线程
import threading
mylock = threading.RLock()

#
thread_num = 30

loginurl = 'http://www.nexushd.org/takelogin.php'
posturl = 'http://www.nexushd.org/thanks.php'

class myThread(threading.Thread):  
	def __init__(self, begin, end):  
		threading.Thread.__init__(self)
		self.begin = begin
		self.end = end
		  
	def run(self): 
		now = self.begin
		while True:  
			mylock.acquire()
			if now > self.end: 
				mylock.release()
				break
			body = {'id': now}
			response, content = http.request(posturl, 'POST', headers=headers, body=urllib.urlencode(body))
			print 'No.%d\thas done' % now
			now += 1
			mylock.release()  


def getcook(set_cookie):
	strlist = set_cookie.split('path=/,')
	cookie = ''
	for value in strlist:
		cookie += value[:value.find('exp')]
	f = open('.cookie','w')
	f.write(cookie)
	f.close()
	return cookie

http = httplib2.Http('.cache')

headers = {'Content-Type': 'application/x-www-form-urlencoded'}	


def getPasswd():
	username = raw_input('Enter username: ')
	import getpass
	password = getpass.getpass('Enter password: ')
	return username, password


def ifLogin(username, password):
	body = {
		'username': username, 
		'password': password
	}
	global headers
	response, content = http.request(loginurl, 'POST', headers=headers, body=urllib.urlencode(body))
	if response['set-cookie']:
		headers['Cookie'] = getcook(response['set-cookie'])
		return True
	else:
		print "Error username or Error password!"
		return False

def getRange():
	begin = raw_input('Enter begin with: ')
	end   = raw_input('Enter end with  : ')
	begin = int(begin)
	end = int(end)
	if begin <= 0:
		begin = 0
	if end < begin:
		end = begin
	return begin, end

def sayThx(begin, end):
	global thread_num
	avg = int( (end - begin) / thread_num )
	for x in xrange(1, thread_num):
		myThread(begin, begin + avg).start()
		begin += avg

def main():
	username, password = getPasswd()
	if ifLogin(username, password):
		begin, end = getRange()
		sayThx(begin, end)

if __name__ == '__main__':
	main()