class Litestripe(object):
	import pigpio
	gpio = pigpio.pi()
	
	# We are only allowing the 'general' GPIO pins 
	allowed_pins = [4, 17, 27, 22, 5, 6, 13, 19, 26, 18, 23, 24, 25, 12, 16, 20, 21]
	#red green and blue 
	def __init__(self, red_pin, green_pin, blue_pin):
#		Disallow same pin for two colors
#		if red == green or red == blue or green == blue:
#			raise ValueError('The pin values cannot be the same')
			
		if red_pin in allowed_pins:
			self.red_pin = red_pin
		else:
			raise ValueError('Red pin must be one of: ' + str(allowed_pins))
		
		if green_pin in allowed_pins:
			self.green_pin = green_pin
		else:
			raise ValueError('Green pin must be one of: ' + str(allowed_pins))
		
		if blue_pin in allowed_pins:
			self.blue_pin = blue_pin
		else:
			raise ValueError('Blue pin must be one of: ' + str(allowed_pins))
			
		self.red_val = 0
		self.green_val = 0
		self.blue_val = 0
		
	def set_color(self, color, value):
		if value < 0 or value >= 256
			throw ValueError("Color value must be in [0, 255]")
		
		if color == 'red':
			self.red_val = value
			gpio.set_PWM_dutycycle(self.red_pin, self.red_val)
		if color == 'green':
			self.green_val = value
			gpio.set_PWM_dutycycle(self.green_pin, self.green_val)
		if color == 'blue':
			self.blue_val = value
			gpio.set_PWM_dutycycle(self.blue_pin, self.blue_val)
			
	def set_red(self, value):
		self.set_color('red', value)
		
	def set_green(self, value):
		self.set_color('green', value)
		
	def set_blue(self, value):
		self.set_color('blue', value)
		
	def stop(self):
		gpio.stop()