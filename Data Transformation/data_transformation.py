import math 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class DataPoint:
	def __init__(self, x, y, classification):
		self.x = x
		self.y = y 
		if classification:
			self.classification = 1
		else:
			self.classification = 0

class DataPoint3D(DataPoint):
	def __init__(self, x, y, z, classification):
		super().__init__(x, y, classification)
		self.z = z

def circle_calculation(x_arr, y_arr):
	data = []
	RADIUS = 1
	for x in x_arr:
		for y in y_arr:
			r = pow(x, 2) + pow(y, 2)
			dp = DataPoint(x, y, r < RADIUS)
			data.append(dp)
	return data

def plot_data(data):
	plt.figure()
	for d in data:
		if d.classification == 1:
			plt.plot(d.x, d.y, 'ro')
		else:
			plt.plot(d.x, d.y, 'bx')
	plt.xlim([-4,4])
	plt.ylim([-4,4])
	plt.show()

def plot_3d_data(data):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	for dp in data:
		if dp.classification == 1:
			ax.scatter(dp.x, dp.y, dp.z, marker='o')
		else:
			ax.scatter(dp.x, dp.y, dp.z, marker='x')

	plt.show()

def cone_transformation(data):
	cone_data = []
	C = 1
	for dp in data:
		z = math.sqrt(C * pow(dp.x, 2) + C * pow(dp.y, 2))
		dp_z = DataPoint3D(dp.x, dp.y, z, dp.classification)
		cone_data.append(dp_z)
	return cone_data

def flatten_transformation(data):
	# Only get Z and X
	plt.figure()
	for d in data:
		if d.classification == 1:
			plt.plot(d.x, d.z, 'ro')
		else:
			plt.plot(d.x, d.z, 'bx')
	plt.xlim([-4,4])
	plt.ylim([-4,4])
	plt.show()
	# Only get Z and Y
	plt.figure()
	for d in data:
		if d.classification == 1:
			plt.plot(d.y, d.z, 'ro')
		else:
			plt.plot(d.y, d.z, 'bx')
	plt.xlim([-4,4])
	plt.ylim([-4,4])
	plt.show()
	# Only get X and Y
	plt.figure()
	for d in data:
		if d.classification == 1:
			plt.plot(d.x, d.y, 'ro')
		else:
			plt.plot(d.x, d.y, 'bx')
	plt.xlim([-4,4])
	plt.ylim([-4,4])
	plt.show()

def super_flat(data):
	# Only get Z and X
	plt.figure()
	for d in data:
		if d.classification == 1:
			plt.plot(0, d.z, 'ro')
		else:
			plt.plot(0, d.z, 'bx')
	plt.xlim([-4,4])
	plt.ylim([-4,4])
	plt.show()


x = np.arange(-2., 2., 0.2)
y = np.arange(-2., 2., 0.2)

data = circle_calculation(x, y)
plot_data(data)
cone_data = cone_transformation(data)
plot_3d_data(cone_data)
flatten_transformation(cone_data)
super_flat(cone_data)