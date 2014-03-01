# -*- coding: utf-8 -*-
import urllib
import cookielib, urllib2
import re						#
import string
import time
import httplib2

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))


def getcook(set_cookie):
	strlist = set_cookie.split('path=/,')
	cookie = ''
	for value in strlist:
		cookie += value[:value.find('exp')]
	f = open('cookie','w')
	f.write(cookie)
	f.close()
	return cookie


http = httplib2.Http('.cache')

username = raw_input('username:')
password = raw_input('password:')

url = 'http://www.nexushd.org/takelogin.php'   
body = {
	'username': username, 
	'password': password
}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
response, content = http.request(url, 'POST', headers=headers, body=urllib.urlencode(body))

#begin to saythanks
headers['Cookie'] = getcook(response['set-cookie'])

begins = raw_input('begins:')
ends = raw_input('ends:')

for i in xrange(int(begins),int(ends)+1):
	body = {'id': i}
	url = 'http://www.nexushd.org/thanks.php'
	response, content = http.request(url, 'POST', headers=headers,body=urllib.urlencode(body))
	print '%d done' % i