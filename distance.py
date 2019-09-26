import csv
import geopy.distance
import csv

input = open('../DATA/test.csv', 'r')
output = open('../DATA/results3.csv', 'w')
writer = csv.writer(output)

input.readline()
coords = []
classes = []
precincts = []
p = 1
count = 5

for row in csv.reader(input):
	if row[0] != "":
		coords.append((float(row[3]), float(row[4])))
	else:
		classes.append((count, coords))
		coords = []
		count = count - 1
		if count == -1:
			precincts.append((p, classes))
			classes = []	
			count = 5
			p = p + 1

rt = 0
count = 0
for precinct, classes in precincts:
	print("Precinct: " + str(precinct))
	for n, c in classes:
		while len(c) != 0:
			t = c.pop()
			for x in c:
				count = count + 1
				d = geopy.distance.vincenty(t,x).feet
				rt = rt + d
		writer.writerow([precinct, n, rt/count, rt, count])
		rt = 0
		count = 0