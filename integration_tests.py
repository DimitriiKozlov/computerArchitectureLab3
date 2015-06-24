__author__ = 'Dimitrii'

import unittest
from operations import create, read, read_all, update, delete


class IntegrationTests(unittest.TestCase):
    """@mock.patch("mypackage.func")
    def test_createdb(self, mock_func):
        create_db('4')
        assert mock_func.call_args == [call('a')]"""


    def test_create(self):
        self.assertEqual(create('nam1', 'surnam1'), "new doc created")

    def test_read_all(self):
        self.assertEqual(read_all(), [
            "<Document u'16f98a5c35dcb61ce73f486390005be5'@u'2-314ae555d881c79e88a21d4df5230f72' {u'surname': u'fg', u'name': u'gf'}>",
            "<Document u'16f98a5c35dcb61ce73f486390006990'@u'1-138b49b469c90bc3a5c734c06461ede3' {u'surname': u'text', u'name': u'text'}>",
            "<Document u'16f98a5c35dcb61ce73f486390006dc9'@u'1-61c91e79536b7c0562503ca084c912b8' {u'surname': u'we', u'name': u'we'}>]"])

    def test_read(self):
        self.assertEqual(read(0),
                         "<Document u'16f98a5c35dcb61ce73f486390005be5'@u'2-314ae555d881c79e88a21d4df5230f72' {u'surname': u'fg', u'name': u'gf'}>")

    def test_update(self):
        self.assertEqual(update(1, 'newdata1', 'newdata2'), "updated")

    def test_delete(self):
        self.assertEqual(delete(1), "Deleted")


if __name__ == "__main__":
    unittest.main()