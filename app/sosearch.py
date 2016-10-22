import stackexchange
site = stackexchange.Site(stackexchange.StackOverflow, app_key='Q690mZMepgGQKkys7JNuUQ((')
site.be_inclusive()

def get_answers(qid):
	answers = ""
	try:
		question = site.question(int(qid))
		for answer in question.answers:
			#print answer.body
			answers += answer.body
			return answers
	except:
			return answers