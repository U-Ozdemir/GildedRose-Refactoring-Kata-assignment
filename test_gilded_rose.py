# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    # Aged brie
    def test_brie_before_sell_date_quality(self):
        items = [Item("Aged Brie", 1, 0)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in) 
        self.assertEqual(1, items[0].quality)
        
    def test_brie_on_sell_date_quality(self):
        items = [Item("Aged Brie", 0, 0)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in) 
        self.assertEqual(2, items[0].quality)

    def test_brie_negative_sell_date_quality(self):
        items = [Item("Aged Brie", -1, 0)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-2, items[0].sell_in) 
        self.assertEqual(2, items[0].quality)

    def test_brie_max_quality(self):
        items = [Item("Aged Brie", 0, 50)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in) 
        self.assertEqual(50, items[0].quality)

    def test_brie_max_quality_1(self):
        items = [Item("Aged Brie", 0, 49)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in) 
        self.assertEqual(50, items[0].quality)

    def test_brie_max_quality_2(self):
        items = [Item("Aged Brie", 1, 49)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in) 
        self.assertEqual(50, items[0].quality)

    def test_brie_max_quality_3(self):
        items = [Item("Aged Brie", 1, 51)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in) 
        self.assertEqual(50, items[0].quality)   

    def test_brie_negative_quality(self):
        items = [Item("Aged Brie", 1, -1)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in) 
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
