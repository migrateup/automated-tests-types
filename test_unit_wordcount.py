import unittest
from wordcount import wordcount

class TestUnit(unittest.TestCase):
    def test_wordcount(self):
        self.assertDictEqual(
            {'foo' : 2, 'bar' : 1},
            wordcount('foo bar foo  '))
