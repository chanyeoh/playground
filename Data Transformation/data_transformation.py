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

	def plot(self, plt):
		if self.classification == 1:
			plt.plot(self.x, self.y, 'ro')
		else:
			plt.plot(self.x, self.y, 'bx')

class DataPoint3D(DataPoint):
	def __init__(self, x, y, z, classification):
		super().__init__(x, y, classification)
		self.z = z

	def plot(self, plt):
		if self.classification == 1:
			plt.scatter(self.x, self.y, self.z, marker='o')
		else:
			plt.scatter(self.x, self.y, self.z, marker='x')

class ConeTransformation:
	C = 1
	def __init__(self, data_dp):
		self.data_dp = data_dp

	def transform_to_cone(self):
		cone_data = []
		for dp in self.data_dp:
			cone_dp = self.calculate_cone_data_point(dp)
			cone_data.append(cone_dp)
		return cone_data

	def calculate_cone_data_point(self, dp):
		z = math.sqrt(self.C * pow(dp.x, 2) + self.C * pow(dp.y, 2))
		return DataPoint3D(dp.x, dp.y, z, dp.classification)


	def get_x_y_point(self, cone_data):
		data = []
		for dp in cone_data:
			data.append(DataPoint(dp.x, dp.y, dp.classification))
		return data

	def get_x_z_point(self, cone_data):
		data = []
		for dp in cone_data:
			data.append(DataPoint(dp.x, dp.z, dp.classification))
		return data

	def get_y_z_point(self, cone_data):
		data = []
		for dp in cone_data:
			data.append(DataPoint(dp.y, dp.z, dp.classification))
		return data

	def get_x_point(self, cone_data):
		data = []
		for dp in cone_data:
			data.append(DataPoint(dp.x, 0, dp.classification))
		return data

	def get_y_point(self, cone_data):
		data = []
		for dp in cone_data:
			data.append(DataPoint(dp.y, 0, dp.classification))
		return data

	def get_z_point(self, cone_data):
		data = []
		for dp in cone_data:
			data.append(DataPoint(dp.z, 0, dp.classification))
		return data


RADIUS = 1
def generate_circle_data():
	data = []
	x_arr = np.arange(-2., 2., 0.2)
	y_arr = np.arange(-2., 2., 0.2)
	for x in x_arr:
		for y in y_arr:
			dp = calculate_and_label_radius(x, y)
			data.append(dp)
	return data

def calculate_and_label_radius(x, y):
	r = pow(x, 2) + pow(y, 2)
	return DataPoint(x, y, r < RADIUS)

def plot_data(data):
	plt.figure()
	plt.xlim([-4,4])
	plt.ylim([-4,4])
	for d in data:
		d.plot(plt)

	plt.show()

def plot_3d_data(data):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	for dp in data:
		dp.plot(ax)
	plt.show()


if __name__ == "__main__":
	# Data Transformation
	data = generate_circle_data()
	cone_transformation = ConeTransformation(data)
	cone_3d_dp = cone_transformation.transform_to_cone()

	# Plot the Data
	plot_data(data)
	plot_3d_data(cone_3d_dp)
	plot_data(cone_transformation.get_x_z_point(cone_3d_dp))
	plot_data(cone_transformation.get_z_point(cone_3d_dp))