import sys, time

class Color(object):
	
	def __init__(self, red=0, green=0, blue=0):
		self.set_red(red)
		self.set_green(green)
		self.set_blue(blue)
		
	def set_red(self, r):
		self.red = self.calc_val(r)
	def set_green(self, g):
		self.green = self.calc_val(g)
	def set_blue(self, b):
		self.blue = self.calc_val(b)
		
	def get_red(self):
		return self.red
	def get_green(self):
		return self.green
	def get_blue(self):
		return self.blue
	
	
	def calc_val(self, val):
		return abs(val) % 256
	
	def get_rgb(self):
		return self.__str__();
	
	def __str__(self):
		return ('rgb(' + ', '.join([str(self.red), str(self.green), str(self.blue)]) + ')')
	


class Litestripe(object):
	
	# We are only allowing the 'general' GPIO pins 
	ALLOWED_PINS = [4, 17, 27, 22, 5, 6, 13, 19, 26, 18, 23, 24, 25, 12, 16, 20, 21]
	#red green and blue 
	def __init__(self, red_pin, green_pin, blue_pin, brightness=100):
		import pigpio
#		Disallow same pin for two colors
#		if red == green or red == blue or green == blue:
#			raise ValueError('The pin values cannot be the same')
		self.gpio = pigpio.pi()
		if red_pin in self.ALLOWED_PINS:
			self.red_pin = red_pin
		else:
			raise ValueError('Red pin must be one of: ' + str(self.ALLOWED_PINS))
		
		if green_pin in self.ALLOWED_PINS:
			self.green_pin = green_pin
		else:
			raise ValueError('Green pin must be one of: ' + str(self.ALLOWED_PINS))
		
		if blue_pin in self.ALLOWED_PINS:
			self.blue_pin = blue_pin
		else:
			raise ValueError('Blue pin must be one of: ' + str(self.ALLOWED_PINS))
			
		self.red_val = 0
		self.green_val = 0
		self.blue_val = 0
		self.set_brightness(brightness)
		
	def set_brightness(self, level):
		
		if level > 0:
			self.brightness = (level % 101)
		else:
			self.brightness = 1
		self.set_rgb()
	
	# Mod the value with 256 to make sure we don't get values which are too high
	def set_rgb(self, red=None, green=None, blue=None):
		
		if red == None:
			red = self.red_val
		if green == None:
			green = self.green_val
		if blue == None:
			blue = self.blue_val
		
		brightness_level = float(self.brightness)/100
		
		self.red_val = abs(red) % (256 * brightness_level)
		self.gpio.set_PWM_dutycycle(self.red_pin, self.red_val)
		
		self.green_val = abs(green) % (256 * brightness_level)
		self.gpio.set_PWM_dutycycle(self.green_pin, self.green_val)
		
		self.blue_val = abs(blue) % (256 * brightness_level)
		self.gpio.set_PWM_dutycycle(self.blue_pin, self.blue_val)
		return self
	
	def set_red(self, value):
		return self.set_rgb(red=value)
		
	def set_green(self, value):
		return self.set_rgb(green=value)
		
	def set_blue(self, value):
		return self.set_rgb(blue=value)
	
	def add_to_color(self, red, green, blue):
		return self.set_rgb(self.red_val + red, self.green_val + green, self.blue_val + blue)
	
	def set_color(self, color):
		return self.set_rgb(color.get_red(), color.get_green(), color.get_blue())

	def get_color(self):
		return Color(self.red_val, self.green_val, self.blue_val)
	
	# time in seconds
	def transition_to(self, color, duration, sleep_time=0.05):
		if duration == 0:
			return self.set_color(color)
			
		iterations = float(duration)/sleep_time
		dr = float((color.red - self.red_val))/iterations
		dg = float((color.green - self.green_val))/iterations
		db = float((color.blue - self.blue_val))/iterations
		
		for i in range(int(iterations)):
			self.add_to_color(dr, dg, db)
			time.sleep(sleep_time)						 
		
		self.set_color(color)
		
		return self

	def fade_out(self, duration, sleep_time=0.05):
		return self.transition_to(Color(0, 0, 0), duration, sleep_time)
	
	def __del__(self):
		self.gpio.stop()
		
		
	def __str__(self):
		b = "brightness: " + 	str(self.brightness)
		rp = 'Red Pin: ' + 	str(self.red_pin)
		gp = 'Green Pin: ' + 	str(self.green_pin)
		bp = 'Blue Pin: ' + 	str(self.blue_pin)
		rv = 'Red Value: ' + 	str(self.red_val)
		gv = 'Green Value: ' + 	str(self.green_val)
		bv = 'Blue Value: ' + 	str(self.blue_val)
		return '[' + ', '.join([b, rp, gp, bp, rv, gv, bv]) + ']'
	

					 
					 
					 
