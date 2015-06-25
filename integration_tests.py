__author__ = 'Dimitrii'

import unittest
from operations import create, read, read_all, update, delete


class IntegrationTests(unittest.TestCase):
    def test_create(self):
        self.assertEqual(create('nam1', 'surnam1'), "new doc created")

    def test_read_all(self):
        self.assertEqual(read_all(), [
            "<Document u'92ced8f9b1ad927a138414862d000487'@u'1-eb4055c4818429e8b4c4829d845e4d9e' {u'surname': u'h', u'name': u'D'}>",
            "<Document u'92ced8f9b1ad927a138414862d0020e6'@u'1-f74b26f6c09af40d585e365d0e552b08' {u'surname': u'jkl56', u'name': u'ASS124'}>",
            "<Document u'92ced8f9b1ad927a138414862d0030ba'@u'1-6bfead417512ef01d2a176c7a34101cd' {u'surname': u'tEST', u'name': u'Test'}>"])

    def test_read(self):
        self.assertEqual(read(2),
                         "<Document u'92ced8f9b1ad927a138414862d0030ba'@u'1-6bfead417512ef01d2a176c7a34101cd' {u'surname': u'tEST', u'name': u'Test'}>")

    def test_update(self):
        self.assertEqual(update(1, 'newdata1', 'newdata2'), "updated")

    def test_delete(self):
        self.assertEqual(delete(1), "Deleted")


if __name__ == "__main__":
    unittest.main()