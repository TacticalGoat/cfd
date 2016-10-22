from app import app
from flask import request,redirect,url_for,current_app
import unirest
import urllib
import httplib
import duckduckgo
import json
import traceback
from .sosearch import get_answers

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

		links2 = duckduckgo.search(str(error),max_results=100)
		links2 = list(set(links2))
		print links2
		stackoverflow = []
	#	conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
	#	conn.request("POST", "/text/analytics/v2.0/keyPhrases?%s" % params, str(body), headers)
	#	response = conn.getresponse()
	#	data = response.read()
	#	print "DONE"
	#	print data
	#	result_dict = json.loads(data)
	#	key_phrase = str(result_dict['documents'][0]['keyPhrases'])
	#	links = duckduckgo.search(key_phrase,max_results=100)

		links2 = duckduckgo.search(str(error),max_results=100)
		links2 = list(set(links2))
		print links2
		stackoverflow = []

	#	for link in links:
	#		if 'stackoverflow.com' in link:
	#			stackoverflow.append(link)

		for link in links2:
			if 'stackoverflow.com' in link:
				stackoverflow.append(link)

		sqids = []
		for q in stackoverflow:
			q_list = q.split('/')
			if len(q_list) > 4:
				sqids.append(q_list[4])
		print sqids
		answers = ""
		for qid in sqids:
			answer = get_answers(qid)
			if answer is not None:
				answers += answer
		return json.dumps({'text':answers})
	except Exception as e:
		traceback.print_exc()
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
	print body
	data = None
	try:
		#print "Connecting"
		#conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
		#conn.request("POST", "/text/analytics/v2.0/keyPhrases?%s" % params, str(body), headers)
		#response = conn.getresponse()
		#data = response.read()
		#print "DONE"
		#print data
		#result_dict = json.loads(data)
		#key_phrase = str(result_dict['documents'][0]['keyPhrases'])
		#links = duckduckgo.search(key_phrase,max_results=100)
		links2 = duckduckgo.search(str(body),max_results=100)
		links2 = list(set(links2))
		#links = list(set(links))
		#print links

		#print links2


		#print links2
		stackoverflow = []

		for link in links2:
			if 'stackoverflow.com' in link:
				stackoverflow.append(link)

		sqids = []
		for q in stackoverflow:
			q_list = q.split('/')
			if len(q_list) > 4:
				sqids.append(q_list[4])
		#print sqids
		answers = ""
		for qid in sqids:
			answer = get_answers(qid)
			if answer is not None:
				answers += answer
		return json.dumps({'text':answers})
	except Exception as e:
		return str(e)

