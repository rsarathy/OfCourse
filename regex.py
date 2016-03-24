import re

c = str(raw_input("Enter a course:\n"))
cu = re.search('([a-zA-z]{2,4})( ?[0-5][0-9]{2})$', c)
while cu is None:
	c = str(raw_input("Invalid course. Enter a course in one of the following formats: SUBJ 123, SUBJ123, subj 123, subj123.\n"))
	cu = re.search('([a-zA-z]{2,4})( ?[0-5][0-9]{2})$', c)
course = cu.group(1).upper() + " " + cu.group(2).strip()
print "You are taking %s." % course