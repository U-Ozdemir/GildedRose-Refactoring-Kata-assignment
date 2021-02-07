class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality) 
        

class GildedRose(object):
    
    # MIN_QUALITY = 0
    # MAX_QUALITY = 50
    # LEGENDARY_QUALITY = 80
    # MIN_SELL_IN = 0

    def __init__(self, items):
        self.items = items

    def update_agedBrie_quality(self, item):
        """
        If the sellin date is more then 0 the following happens:
            1. selling decrease by 1.
            2. item quality changes:
                - to 0 if the quality is below 0
                - to 50 if the quality is over 50
                - otherwise quality increases with 1 
            
        The same happens when selling date is below 0, except quality increas is +2 now.
        """
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
                if item.quality > 50: #bij 49 wordt het 51, dus niet goed, moet 50 worden
                    item.quality = 50
            else:
                item.quality = 50 #klopt niet


    def update_conjured_quality(self, item):
        """
            If sellin date is more then 0, then the item is update as following:
            1. Sellin decreases by 1.
            2. Item quality changes:
                - If quality is over 50, it becomes 50
                - If quality is over 0, decreases quality with 2.
                - Otherwise if quality is negative, it becomes 0.

            If selling date is less then 0, then the following happens:
            1. Sellin decreases by 1.
            2. Item quality changes:
                - If quality is over 50, it becomes 50
                - If quality is over 0, decreases quality with 4.
                - Otherwise if quality is negative, it becomes 0.
        """

        if item.sell_in > 0:
            item.sell_in -= 1
            if item.quality > 50: 
                item.quality = 50
            elif item.quality > 0: # bij 1 geeft het -1, mag niet nagtief zij 
                item.quality -= 2
                if item.quality < 0: # opgelost met deze, maar kan wss anders
                    item.quality = 0
            else:
                item.quality = 0
                    
        elif item.sell_in < 0:
            item.sell_in -= 1
            if item.quality > 50: 
                item.quality = 50
            elif item.quality > 0: 
                item.quality -= 4
                if item.quality < 0: 
                    item.quality = 0
            else:
                item.quality = 0


    def update_sulfuras_quality(self, item):
        """ Sulfuras does not need to be selled, nor decreases in quality. """   

        if item.quality < 80:
            item.quality = 80
        else: 
            item.quality = 80

    def update_backstage_quality(self, item):
        """ 
            If the sellin date is more then 10, the item is updated as following:
                1. Sellin decreases by 1.
                2. If the quality is over 50, then quality changes to 50.
                3. Otherwise the quality increases by 1.

            If the sellin date is more then 5, the item is updated as following:
                1. Sellin decreases by 1.
                2. If the quality is over 50, then quality changes to 50.
                3. Otherwise the quality increases by 2.
                If the sellin date is more then 0, the item is updated as following:
                1. Sellin decreases by 1.
                2. If the quality is over 50, then quality changes to 50.
                3. Otherwise the quality increases by 3.
        """
                
        if item.sell_in > 10:
            item.sell_in -= 1
            if item.quality < 0:
                item.quality = 0
            elif item.quality < 50:
                item.quality += 1
            else: 
                item.quality = 50
               
        elif item.sell_in > 5:
            item.sell_in -= 1
            if item.quality < 0:
                item.quality = 0
            elif item.quality < 50:
                item.quality += 2
                if item.quality > 50:
                    item.quality = 50
            else: 
                item.quality = 50
        
        elif item.sell_in > 0:
            item.sell_in -= 1
            if item.quality < 0:
                item.quality = 0
            elif item.quality < 50:
                item.quality += 3
                if item.quality > 50:
                    item.quality = 50
            else: 
                item.quality = 50
                
        else:
            item.sell_in -=1
            if item.quality > 50:
                item.quality = 50

    def update_item_category(self, item):
        name = item.name
        if "Aged Brie" == name:
            return self.update_agedBrie_quality(item)
        elif "Conjured Mana Cake" == name:
            return self.update_conjured_quality(item)
        elif "Sulfuras, Hand of Ragnaros" == name:
            return self.update_sulfuras_quality(item)
        elif "Backstage passes to a TAFKAL80ETC concert" == name:
            return self.update_backstage_quality(item)
        
    def update_quality(self):
        for item in self.items:
            self.update_item_category(item)
