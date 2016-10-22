from app import app
from flask import request,redirect,url_for,current_app
import unirest
import urllib
import httplib

@app.route('/error/<error>')
def error_handle(error):
	headers = {
		'Ocp-Apim-Subscription-Key':'cc0b7c5d4a6c4a4babb880a94c30a7dd',#current_app.config['MICROSOFT_KPE_KEY'],
		'Content-Type':'application/json',
		'Accept':'application/json'
	}
	params = urllib.urlencode({})
	body = {
		'documents':[
			{
				'language':'en',
				'id':'1',
				'text': str(error)
			}
		]
	}
	try:
		print "Connecting"
		conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
		conn.request("POST", "/text/analytics/v2.0/keyPhrases?%s" % params, str(body), headers)
		response = conn.getresponse()
		data = response.read()
		print "DONE"
		return data
	except Exception as e:
		return str(e)

@app.route('/error/',methods=['POST'])
def error_post():
	headers = {
		'Ocp-Apim-Subscription-Key':'cc0b7c5d4a6c4a4babb880a94c30a7dd',#current_app.config['MICROSOFT_KPE_KEY'],
		'Content-Type':'application/json',
		'Accept':'application/json'
	}
	params = urllib.urlencode({})
	body = str(request.form['body'])
	data = None
	try:
		print "Connecting"
		conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
		conn.request("POST", "/text/analytics/v2.0/keyPhrases?%s" % params, str(body), headers)
		response = conn.getresponse()
		data = response.read()
		print "DONE"
	except Exception as e:
		return str(e)