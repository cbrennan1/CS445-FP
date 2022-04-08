import unittest
import Accounts

class TestAccounts(unittest.TestCase):

    def test_httpStatus(self):
        httpStatusCheck = Accounts(httpStatus)
        self.assertEqual(httpStatusCheck, 200)
