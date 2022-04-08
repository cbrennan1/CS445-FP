import unittest
import Accounts

class TestAccounts(unittest.TestCase):

    def test_httpStatus(self):
        httpStatusCheck = Accounts(httpStatus)
        self.assertEqual(httpStatusCheck, 200)

    def test_uidcheck(self):
        zerouid = Accounts(uid0)
        oneuid = Accounts(uid1)
        twouid = Accounts(uid2)
        self.assertEqual(zerouid, '<uid0>')
        self.assertEqual(oneuid, '<uid1>')
        self.assertEqual(twouid, '<uid2>')