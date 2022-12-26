import unittest 

from zipcode.department import Department, Endpoint

class TestComponent(unittest.TestCase):

    def setUp(self):
        self.my_dep = Endpoint.san_vicente.value
        self.my_object = Department(self.my_dep)

    def test_enumeration(self):

        keys = [dep.value for dep in Endpoint]

        self.assertEqual(14,len(keys))

    def test_summary(self):
        self.assertNotEqual(self.my_object.summary,None)

class TestIntegration(unittest.TestCase):
    pass

