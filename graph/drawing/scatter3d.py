from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from math import sqrt
import sys
import csv
from decimal import Decimal, ROUND_DOWN

def init_ax():
	fig = plt.figure()
	ax = Axes3D(fig)
	ax.set_xlabel('x-axis')
	ax.set_ylabel('y-axis')
	ax.set_zlabel('z-axis')
	return ax

def input_from_file(csvfilepath):
	li = []
	with open(csvfilepath) as f:
		reader = csv.reader(f)
		for row in reader:
			if len(row) != 3:
				break
			x = eval(row[0])
			y = eval(row[1])
			z = eval(row[2])
			li.append([x,y,z])
	return li

def input_from_stdin():
	li = []
	print('input coordinates:')
	while True:
		line = input()
		point = line.split(",")
		if len(point) != 3:
			break
		else:
			x = eval(point[0])
			y = eval(point[1])
			z = eval(point[2])
			li.append([x, y, z])
	return li

def plot(ax, li):
	for p in li:
		x = p[0]
		y = p[1]
		z = p[2]
		ax.scatter(x, y, z, c='r', marker='o')
		label = '(%s,%s,%s)' % (
			Decimal(x).quantize(Decimal('0.01'), rounding=ROUND_DOWN),
			Decimal(y).quantize(Decimal('0.01'), rounding=ROUND_DOWN),
			Decimal(z).quantize(Decimal('0.01'), rounding=ROUND_DOWN))
		ax.text(x, y, z, label)

def line(ax, li):
	src = li[0]
	for i in range(len(li)):
		ax.plot([src[0], li[i][0]], [src[1], li[i][1]], [src[2], li[i][2]])

ax = init_ax()

if len(sys.argv) > 1:
	li = input_from_file(sys.argv[1])
	print(li)
else:
	li = input_from_stdin()
	print(li)

plot(ax, li)
line(ax, li)

plt.show()
