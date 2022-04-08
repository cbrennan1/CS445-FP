import unittest
import Accounts

class TestAccounts(unittest.TestCase):

    def test_httpStatus(self):
        httpStatusCheck = Accounts(httpStatus)
        self.assertEqual(httpStatusCheck, 200)

    def test_uidcheck(self):
        zerouid = Accounts.uidcheck[0]
        oneuid = Accounts.uidcheck[1]
        twouid = Accounts.uidcheck[2]
        self.assertEqual(zerouid, '<uid0>')
        self.assertEqual(oneuid, '<uid1>')
        self.assertEqual(twouid, '<uid2>')

if __name__ == '__main__':
    unittest.main()