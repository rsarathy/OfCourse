class Course:
	def __init__(self, ident, name, descr, credit):
		self.ident = ident
		self.name = name
		self.descr = descr
		self.credit = credit

	def get_id(self):
		return self.ident

	def get_name(self):
		return self.name

	def get_descr(self):
		return self.descr

	def get_credit(self):
		return self.credit

	def to_print(self):
		print "%s - %s (%s credit hours):\n%s" % (self.get_id(), self.get_name(), self.get_credit(), self.get_descr())

if __name__ == '__main__':
	courses = []
	with open("courses.txt") as f:
		for line in f:
			data = line.strip().split("|")

			_id = data[0]
			_name = data[1]
			_descr = data[2]
			_credit = data[3]

			c = Course(_id, _name, _descr, _credit)
			c.to_print()
			courses.append(c)