import stackexchange

class StackExchange():
	so = stackexchange.Site(stackexchange.StackOverflow,'Q690mZMepgGQKkys7JNuUQ((')

	def search(self,term):
		self.qs = so.search(q=term)

	def fetch_answers(self,term):
		self.search(term)
		return self.qs