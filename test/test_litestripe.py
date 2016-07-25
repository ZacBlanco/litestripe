import env
import sys, mock, unittest
from mock import MagicMock, patch
pigs = MagicMock()
patch.dict("sys.modules", pigpio=pigs).start()	
from litestripe.core.lite import Litestripe, Color
	
class test_init(unittest.TestCase):

	def test_lite_init(self):
		l = Litestripe(17, 17, 17)
		assert l.brightness == 100, 'Default brightness should be 100. Value was ' + str(l.brightness)

		assert l.red_pin == 17
		assert l.green_pin == 17
		assert l.blue_pin == 17

		assert l.red_val == 0
		assert l.green_val == 0
		assert l.blue_val == 0

		try:
			l = Litestripe(99, 17, 17)
			self.fail('Should have failed on red pin = 99')
		except ValueError as e:
			pass
		
		try:
			l = Litestripe(17, 99, 17)
			self.fail('Should have failed on green pin = 99')
		except ValueError as e:
			pass
		
		try:
			l = Litestripe(17, 17, 99)
			self.fail('Should have failed on blue pin = 99')
		except ValueError as e:
			pass
	
	def test_lite_set_color(self):
		l = Litestripe(17, 27, 22)
		orange = Color(255, 40, 0)
		l.set_color(orange)
		assert l.red_val == 255
		assert l.green_val == 40
		assert l.blue_val == 0
		l.set_rgb()
		assert l.red_val == 255
		assert l.green_val == 40
		assert l.blue_val == 0
		
	def test_lite_transitions(self):
		l = Litestripe(17, 27, 22)
		white = Color(255.0, 255.0, 255.0)
		light_orange = Color(128.0, 20.0, 0.0)
		l.set_color(white)
		assert str(l.get_color()) == str(white)
		l.transition_to(light_orange, 0.1)
		assert str(l.get_color()) == str(light_orange)
		l.fade_out(0.1)
		assert str(l.get_color()) == "rgb(0.0, 0.0, 0.0)"
	
	
	def test_stop(self):
		l = Litestripe(17, 27, 22)
		del l
		try:
			print l
			self.fail('Should have deleted l')
		except UnboundLocalError as e:
			pass
		
	def test_print_lite(self):
		l = Litestripe(17, 27, 22)
		white = Color(255.0, 255.0, 255.0)
		l.set_color(white)
		item = """[brightness: 100, Red Pin: 17, Green Pin: 27, Blue Pin: 22, Red Value: 255.0, Green Value: 255.0, Blue Value: 255.0]"""
		assert str(l) == item
		
		
		