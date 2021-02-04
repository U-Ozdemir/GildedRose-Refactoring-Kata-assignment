# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items


    def update_quality(self):
        for item in self.items:

            if item.name == "Aged Brie":
                if item.sell_in > 0:
                    item.sell_in -= 1
                    if item.quality < 0:
                        item.quality = 0
                    elif item.quality < 50:
                        item.quality += 1
                    else:
                         item.quality = 50
                else:
                    item.sell_in -= 1
                    if item.quality < 0:
                        item.quality = 0
                    elif item.quality < 50:
                        item.quality += 2
                    else:
                         item.quality = 50
          
          
            elif item.name == "Conjured Mana Cake":
                if item.sell_in > 0:
                    item.sell_in -= 1
                    if item.quality < 0:
                        item.quality = 0
                    elif item.quality < 50:
                        item.quality -= 2
                    else:
                         item.quality = 50
                elif item.sell_in < 0:   # sellin expired date
                    item.sell_in -= 1
                    if item.quality < 0:
                        item.quality = 0
                    elif item.quality > 0: 
                         item.quality -= 4
                    
                    
            elif item.name == "Sulfuras, Hand of Ragnaros":
                if item.quality < 80:
                    item.quality = 80
                else: 
                    item.quality = 80

                
            elif item.name == "Backstage passes to a TAFKAL80ETC concert": # deze klopt niet
                if item.sell_in > 10:
                    item.sell_in -= 1
                    if item.quality > 50:
                        item.quality = 50
                    else:
                        item.quality += 1
               
                elif item.sell_in > 5:
                    item.sell_in -= 1
                    if item.quality > 50:
                        item.quality = 50
                    elif item.quality >= 0:
                        item.quality += 2
                    else:
                        item.quality = 0
               
                elif item.sell_in > 0:
                    item.sell_in -= 1
                    if item.quality > 50:
                        item.quality = 50
                    elif item.quality >= 0:
                        item.quality += 3
                    else:
                        item.quality = 0
                    
                else:
                    item.sell_in -=1
                    item.quality = 0
                

           
           
            # if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
            #     if item.quality > 0:
            #         if item.name != "Sulfuras, Hand of Ragnaros":
            #             item.quality = item.quality - 1
            # else:
            #     if item.quality < 50:
            #         item.quality = item.quality + 1
            #         if item.name == "Backstage passes to a TAFKAL80ETC concert":
            #             if item.sell_in < 11:
            #                 if item.quality < 50:
            #                     item.quality = item.quality + 1
            #             if item.sell_in < 6:
            #                 if item.quality < 50:
            #                     item.quality = item.quality + 1
            # if item.name != "Sulfuras, Hand of Ragnaros":
            #     item.sell_in = item.sell_in - 1
            # if item.sell_in < 0:
            #     if item.name != "Aged Brie":
            #         if item.name != "Backstage passes to a TAFKAL80ETC concert":
            #             if item.quality > 0:
            #                 if item.name != "Sulfuras, Hand of Ragnaros":
            #                     item.quality = item.quality - 1
            #         else:
            #             item.quality = item.quality - item.quality
            #     else:
            #         if item.quality < 50:
            #             item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality) 


