from helloworld.helloworld import *

import unittest


class TestHelloWorld(unittest.TestCase):

    def test__helloworld__normal_condition_should_return_helloworld(self):
        hw = HelloWorld()
        result = hw.return_message()
        expected_result = "hello world"
        self.assertEqual(result, expected_result)
