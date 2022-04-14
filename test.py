import unittest
from hello_world import say_hello


class TestHelloWorld(unittest.TestCase):
    def test_say_hello(self):
        """
        Test that it return a correct hello message
        """
        self.assertEqual(say_hello(name="John Doe"), "Hello, John Doe")


if __name__ == '__main__':
    unittest.main()
