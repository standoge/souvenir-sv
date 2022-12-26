import unittest

from zipcode.department import Department, Endpoint


class TestComponent(unittest.TestCase):
    def setUp(self):
        """Generate instance of Department to test it."""
        self.my_dep = Endpoint.san_vicente.value
        self.my_object = Department(self.my_dep)

    def test_enumeration(self):
        """Test if Enum has 14 values regarded to 14 departments."""
        keys = [dep.value for dep in Endpoint]
        self.assertEqual(14, len(keys))

    def test_summary(self):
        """
        Test if method returns None type, it mean that filter argument
        is wrong and bs4 doesn't find any match.
        """
        self.assertNotEqual(self.my_object.summary, None)

    def test_zipcodes(self):
        """
        Test if method returns None type, it mean that array with
        HTML labels match doesn't exist in filter argument used.
        """
        self.assertNotEqual(self.my_object.zip_codes, None)
