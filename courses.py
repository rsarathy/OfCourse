class Course:
	def __init__(self, ident, name, descr, credit):
		self.ident = ident
		self.name = name
		self.descr = descr
		self.credit = int(credit)
		self.opacity = float(credit)/4.0

	def get_id(self):
		return self.ident

	def get_department(self):
		id = self.get_id()
		dept = id.split(" ")
		return dept[0]

	def get_name(self):
		return self.name

	def get_descr(self):
		return self.descr

	def get_credit(self):
		return self.credit

	def to_print(self):
		print "%s - %s (%s credit hours):\n%s" % (self.get_id(), self.get_name(), self.get_credit(), self.get_descr())


class Catalog:
	def __init__(self, filename):
		self.courses = {}
		with open(filename) as f:
			for line in f:
				data = line.strip().split("|")
				_id = data[0]
				_name = data[1]
				_descr = data[2]
				_credit = data[3]

				c = Course(_id, _name, _descr, _credit)
				self.courses[_id] = c

	def show(self):
		for c in sorted(self.courses.keys()):
			self.courses[c].to_print()

	def get_courses(self):
		return self.courses

# for testing purposes only, run with "python courses.py"
if __name__ == '__main__':
	catalog = Catalog("courses.txt")
	catalog.show()
