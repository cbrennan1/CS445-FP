import unittest
import Accounts

class TestAccounts(unittest.TestCase):

    def test_httpStatus(self):
        httpStatusCheck = Accounts.httpstatus('https://www.google.com/')
        self.assertEqual(httpStatusCheck, 200)

    def test_uidcheck0(self):
        uid0 = Accounts.list[0].uid
        self.assertEqual(uid0, '<uid0>')

    def test_uidcheck1(self):
        uid1 = Accounts.list[1].uid
        self.assertEqual(uid1, '<uid1>')

    def test_uidcheck2(self):
        uid2 = Accounts.list[2].uid
        self.assertEqual(uid2, '<uid2>')

if __name__ == '__main__':
    unittest.main()