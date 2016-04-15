import csv

print "===MapReduce data==="
wdat = {}
data = []
tmp = []
with open("semester_data.csv", "r") as sem_data:
    d = csv.reader(sem_data, delimiter=',')
    for row in d:
        R = ', '.join(row)
        tmp.append(R)

for i in range(1, len(tmp)):
    form_data = tmp[i].split(", ")
    semester = form_data[1]
    c = []
    for i in range(7):
        ident = form_data[(i+1)*2]
        diffc = form_data[(i+1)*2+1]
        if ident is not '':
            course = (ident, int(diffc))
        c.append(course)
        data.append(course)

for kv in data:
    C = kv[0]
    D = kv[1]
    if C not in wdat:
        wdat[C] = [D]
    else:
        wdat[C].append(D)

for course in sorted(wdat):
    diff = wdat[course]
    wdat[course] = float(float(sum(diff))/len(diff))
    print course, wdat[course]
