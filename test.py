#!/usr/bin/env python
import unittest
import ruuvi

class TestRuuvi(unittest.TestCase):
 """
       This test part depends on what you want to test its functions.
       Above are incompleted codes
 """
    """ def setUp(self):
        ruuvi.ruuvi.testing = True
        self.ruuvi = ruuvi.ruuvi.test_client()
    def test_Temp(self):
        test = 
        self.assertEqual(test,) """

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
