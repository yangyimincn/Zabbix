#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import urllib
import urllib2

#zabbix_connect_info
server = ""
method = ""
zid = 1
auth = None
params = {}

header = {"Content-Type":"application/json"}
jsonrpc = "2.0"

def get_zabbix_info(server, method, zid, auth, params):
	"""
		Return code:0(success)   1(zabbix error)   2(other error) 
	"""
	#Create zabbix url
	zabbix_url = "http://{0}/zabbix/api_jsonrpc.php".format(server)
	#Create zabbix_params
	body = {}
	body["jsonrpc"] = jsonrpc
	body["method"] = method
	body["params"] = params
	body["id"] = id
	body["auth"] = auth
	try:
		encodebody = json.dumps(body)
		request = urllib2.Request(zabbix_url, encodebody, header)
		response = urllib2.urlopen(request)
		result = json.loads(response.read())
		if "error" in result.keys():
			return [1, str(result["error"])]
			#return "failed!{0}".format(str(result["error"]))
		else:
			return [0, str(result["result"])]
	except Exception as e:
		return [2, e]

def get_zabbix_key(server, username, passwd):
	method = "user.login"
	zid = 1
	auth = None
	params = {"user": username, "password": passwd}
	get_zabbix_info(server, method, zid, auth,params)


