import unittest
from app.models import Comments

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_comment =Comments( comment_name = 'lol')


if __name__ =='__main__':
    unittest.main()