# -*- coding: utf-8 -*-

# need to be added to functions later on instead of hardcoding.
min_quality = 0
max_quality = 50
legendary_quality = 80
min_sell_in = 0

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality) 


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                return self.update_agedBrie_quality
            # elif item.name == "Conjured Mana Cake":
            #     return self.x
            # elif item.name == "Sulfuras, Hand of Ragnaros":
            #     return self.x
            # elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            #     return self.x

    def update_agedBrie_quality(self):
        if self.sell_in > 0:
            return self.sell_in - 1

            # if item.quality < 0:
            #     item.quality = 0
            # elif item.quality < 50:
            #     return self.quality + 1
            # else:
            #     item.quality = 50

        # else:
        #     item.sell_in -= 1
        #     if item.quality < 0:
        #         item.quality = 0
        #     elif item.quality < 50:
        #         item.quality += 2
        #     else:
        #             item.quality = 50



                    # """If the sellin date is more then 0 the following happens:
                    #     1. selling decrease by 1.
                    #     2. item quality changes:
                    #         - to 0 if the quality is below 0
                    #         - to 50 if the quality is over 50
                    #         - otherwise quality increases with 1 
                        
                    #     The same happens when selling date is below 0, except quality increas is +2 now."""

            # if item.name == "Aged Brie":
            #     if item.sell_in > 0:
            #         item.sell_in -= 1
            #         if item.quality < 0:
            #             item.quality = 0
            #         elif item.quality < 50:
            #             item.quality += 1
            #         else:
            #              item.quality = 50
            #     else:
            #         item.sell_in -= 1
            #         if item.quality < 0:
            #             item.quality = 0
            #         elif item.quality < 50:
            #             item.quality += 2
            #         else:
            #              item.quality = 50
          
          
            #             # """
            #             #     If sellin date is more then 0, then the item is update as following:
            #             #     1. Sellin decreases by 1.
            #             #     2. Item quality changes:
            #             #         - If quality is over 50, it becomes 50
            #             #         - If quality is over 0, decreases quality with 2.
            #             #         - Otherwise if quality is negative, it becomes 0.

            #             #     If selling date is less then 0, then the following happens:
            #             #     1. Sellin decreases by 1.
            #             #     2. Item quality changes:
            #             #         - If quality is over 50, it becomes 50
            #             #         - If quality is over 0, decreases quality with 4.
            #             #         - Otherwise if quality is negative, it becomes 0.
            #             # """

            # elif item.name == "Conjured Mana Cake":
            #     if item.sell_in > 0:
            #         item.sell_in -= 1
            #         if item.quality > 50: 
            #             item.quality = 50
            #         elif item.quality > 0: 
            #             item.quality -= 2
            #         else:
            #             item.quality = 0
                    
            #     elif item.sell_in < 0:
            #         item.sell_in -= 1
            #         if item.quality > 50: 
            #             item.quality = 50
            #         elif item.quality > 0: 
            #             item.quality -= 4
            #         else:
            #             item.quality = 0
                    
                   
            # # """ Sulfuras does not need to be selled or decreases in quality.
            # # """            
                    
            # elif item.name == "Sulfuras, Hand of Ragnaros":
            #     if item.quality < 80:
            #         item.quality = 80
            #     else: 
            #         item.quality = 80

            # # """ If the sellin date is more then 10, the item is updated as following:
            # #         1. Sellin decreases by 1.
            # #         2. If the quality is over 50, then quality changes to 50.
            # #         3. Otherwise the quality increases by 1.
            # #     If the sellin date is more then 5, the item is updated as following:
            # #         1. Sellin decreases by 1.
            # #         2. If the quality is over 50, then quality changes to 50.
            # #         3. Otherwise the quality increases by 2.
            # #      If the sellin date is more then 0, the item is updated as following:
            # #         1. Sellin decreases by 1.
            # #         2. If the quality is over 50, then quality changes to 50.
            # #         3. Otherwise the quality increases by 3.
            # # """
                
            # elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            #     if item.sell_in > 10:
            #         item.sell_in -= 1
            #         if item.quality > 50:
            #             item.quality = 50
            #         else:
            #             item.quality += 1
               
            #     elif item.sell_in > 5:
            #         item.sell_in -= 1
            #         if item.quality > 50:
            #             item.quality = 50
            #         elif item.quality >= 0:
            #             item.quality += 2
            #         else:
            #             item.quality = 0
               
            #     elif item.sell_in > 0:
            #         item.sell_in -= 1
            #         if item.quality > 50:
            #             item.quality = 50
            #         elif item.quality >= 0:
            #             item.quality += 3
            #         else:
            #             item.quality = 0
                    
            #     else:
            #         item.sell_in -=1
            #         item.quality = 0
                

           



