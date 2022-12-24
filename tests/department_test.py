import unittest 

from zipcode.department import Department, Endpoint

class TestComponent(unittest.TestCase):
    def test_enumeration(self):

        keys = [dep.value for dep in Endpoint]

        self.assertEqual(14,len(keys))

class TestIntegration(unittest.TestCase):
    pass

