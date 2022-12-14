""" 
Created on : 13/11/22 5:57 AM
@author : ds  
"""

import unittest
from Nov_13_count_instance import Composer


class TestComposer(unittest.TestCase):

    def test_count_zero(self):
        self.assertEqual(0, Composer.count)

    def test_count_one(self):
        c = Composer("Ludvig van Beethoven", 1770, "Germany")
        self.assertEqual(1, Composer.count)

    def test_count_five(self):
        c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
        c2 = Composer("Ludvig van Beethoven", 1770, "Germany")
        c3 = Composer("Ludvig van Beethoven", 1770, "Germany")
        c4 = Composer("Ludvig van Beethoven", 1770, "Germany")
        c5 = Composer("Ludvig van Beethoven", 1770, "Germany")
        self.assertEqual(5, Composer.count)
