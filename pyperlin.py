from math import *

class PerlinNoise():
	def __init__(self, persistance, frequency, octaves, amplitude = 1, seed = 0):
		self.persistance = persistance
		self.frequency = frequency
		self.octaves = octaves
		self.amplitude = amplitude
		self.seed = seed * seed + 15731

	def get_height(self, x, y):
		total = 0.0
		amplitude  = self.amplitude
		frequency = self.frequency
		max_value = 0.0

		for i in range(0, self.octaves):
			total += self.get_value(x * frequency + self.seed, y * frequency + self.seed) * amplitude
			max_value += amplitude
			amplitude *= self.persistance
			frequency *= 2

		total = (total + 1.0) / 2.0

		return total / max_value

	def get_value(self, x ,y):
		int_x = int(x)
		int_y = int(y)
		frac_x = x - int_x
		frac_y = y - int_y

		v1 = self.smooth_noise(int_x, int_y)
		v2 = self.smooth_noise(int_x+1, int_y)
		v3 = self.smooth_noise(int_x, int_y+1)
		v4 = self.smooth_noise(int_x+1, int_y+1)

		i1 = self.interpolate(v1, v2, frac_x)
		i2 = self.interpolate(v3, v4, frac_x)

		return self.interpolate(i1, i2, frac_y)

	def smooth_noise(self, x, y):
		corners = (self.noise(x - 1, y - 1) + self.noise(x + 1, y - 1) + self.noise(x - 1, y + 1) + self.noise(x + 1, y + 1)) / 16.0
		sides = (self.noise(x - 1, y) + self.noise(x + 1, y) + self.noise(x, y + 1) + self.noise(x, y - 1)) / 8.0
		center = self.noise(x, y) / 4.0

		return corners + sides + center

	def interpolate(self, x, y, a):
		ft = a * 3.1415927
		f = (1 - cos(ft)) * 0.5

		return (x * (1 - f) + y * f)

	def noise(self, x, y):
		n = int(x) + int(y) * 57
		n = (n << 13) ^ n
		t = (n * (n * n * 15731 + 789211) + 1376312589) & 0x7fffffff

		return 1.0 - float(t) * 0.931322574615478515625e-9
