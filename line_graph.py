import matplotlib.pyplot as plt


class LineGraph:
	def __init__(self, x_values, y_values, title, x_axis_label, y_axis_label):
		self.x_values = x_values
		self.y_values = y_values
		self.title = title
		self.x_axis_label = x_axis_label
		self.y_axis_label = y_axis_label
		
	def show(self):
		plt.scatter(self.x_values, self.y_values)
		plt.plot(self.x_values, self.y_values)
		plt.title(self.title)
		plt.xlabel(self.x_axis_label)
		plt.ylabel(self.y_axis_label)
		plt.show()
