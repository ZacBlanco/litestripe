import env
import mock
from litestripe.core.lite import Color

def test_color_init():
	r = Color(255, 0, 16)
	assert r.red == 255
	assert r.green == 0
	assert r.blue == 16
	r = Color(255, 256, 256)
	assert r.red == 255
	assert r.green == 0
	assert r.blue == 0

def test_color_calc():
	r = Color(0, 0, 0)
	assert r.calc_val(-212) == 212
	assert r.calc_val(212) == 212
	assert r.calc_val(-256) == 0
	assert r.calc_val(256) == 0
	

def test_color_floats():
	r = Color(0, 0, 0)
	assert r.calc_val(-212) == 212
	assert r.calc_val(212) == 212
	assert r.calc_val(-256) == 0
	assert r.calc_val(256) == 0
	
	
	