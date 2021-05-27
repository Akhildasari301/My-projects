
# import matplotlib
import matplotlib.pyplot as plt

# import random module

import random

class Randomwalk:
	"""Random walk class"""
	def __init__(self, num_points):
		self.num_points = num_points

		# walk starts at (0, 0)
		# x_values
		self.x_vals = [0]

		# y values 
		self.y_vals = [0]

	def get_step(self): # this method will calculte the next step
		direction = [-1, 1]
		steps = [1, 2, 3, 4]

		x_step = random.choice(direction) * random.choice(steps)
		y_step = random.choice(direction) * random.choice(steps)

		return x_step, y_step

	def get_points(self): # method to generate all the points

		while len(self.x_vals) < self.num_points:

			x_dist, y_dist = self.get_step()

			if x_dist == 0 and y_dist == 0:
				continue

			next_x = self.x_vals[-1] + x_dist
			next_y = self.y_vals[-1] + y_dist

			self.x_vals.append(next_x)
			self.y_vals.append(next_y)


	def plot_walk(self): # method to plot the data
		plt.plot(self.x_vals, self.y_vals, c="blue")
		plt.title("Randomwalk Simulation", fontsize=24)
		plt.xlabel("x values", fontsize=14)
		plt.ylabel("y values", fontsize=14)
		plt.tick_params(axis="both", labelsize=14)
		plt.show()


<<<<<<< HEAD
=======
rw = Randomwalk(1000)
rw.get_points()

rw.plot_walk()
>>>>>>> 03df627aa79f2e7fea470d19bde617ea73bb1609
