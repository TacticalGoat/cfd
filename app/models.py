import stackexchange

class StackExchange():
	so = stackexchange.Site(stackexchange.StackOverflow,'Q690mZMepgGQKkys7JNuUQ((')

	def search(self,term):
		self.qs = so.search(q=term)
