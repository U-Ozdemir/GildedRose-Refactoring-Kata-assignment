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

    # Backstage passes
    def test_backstage_sell_in_11_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 0)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)
        
    def test_backstage_sell_in_10_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 0)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)

    def test_backstage_sell_in_9_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 9, 0)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)

    def test_backstage_sell_in_5_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 0)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].quality)

    def test_backstage_sell_in_0_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 0)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_backstage_sell_in_negative_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 0)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_backstage_max_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, 50)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_backstage_max_quality_1(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, 49)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_backstage_max_quality_2(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 49)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_backstage_max_quality_3(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 49)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_backstage_negative_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, -1)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)    

    def test_backstage_negative_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, -1)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)  

    def test_backstage_negative_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, -1)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    # Sulfuras
    def test_Sulfuras_before_sell_date(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 80)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_Sulfuras_on_sell_date(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_Sulfuras_after_sell_date(self):
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_Sulfuras_max_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 100)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_Sulfuras_min_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, -100)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    # Conjured
    def test_Sulfuras_before_sell_date(self):
        items = [Item("Conjured Mana Cake", 1, 10)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_Sulfuras_on_sell_date(self):
        items = [Item("Conjured Mana Cake", 0, 10)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(6, items[0].quality)

    def test_Sulfuras_after_sell_date(self):
        items = [Item("Conjured Mana Cake", -1, 10)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(6, items[0].quality)

    def test_Sulfuras_max_quality(self):
        items = [Item("Conjured Mana Cake", 1, 51)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_Sulfuras_min_quality(self):
        items = [Item("Conjured Mana Cake", 1, -1)]       
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()
