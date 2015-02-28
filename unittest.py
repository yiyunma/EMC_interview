import os
import flaskr
import unittest
import request

class FlaskrTestCase(unittest.TestCase):
	def fibTest(self):
		assert request.method == 'GET'

if __name__ == '__main__':
    unittest.main()
