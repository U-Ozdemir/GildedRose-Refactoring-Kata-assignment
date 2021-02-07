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

    def update_agedBrie_quality(self, item):
        """ 
        Checking for sell_in date before or after:
            - decrease sell_in by 1

        Quality increases with:
            - 1 before sell_in date
            - 2 after sell_in date
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
                if item.quality > 50: 
                    item.quality = 50
            else:
                item.quality = 50 

    def update_conjured_quality(self, item):
        """
        Checking for sell_in date before or after:
            - decrease sell_in by 1

        Quality decrease with:
            - 2 before sell_in date
            - 4 after sell_in date  
        """
        if item.sell_in > 0:
            item.sell_in -= 1
            if item.quality > 50: 
                item.quality = 50
            elif item.quality > 0: 
                item.quality -= 2
                if item.quality < 0: 
                    item.quality = 0
            else:
                item.quality = 0         
        else:
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
        """ 
        Sulfuras does not need to be sold, nor decreases in quality. 
        """   
        if item.sell_in > 0:
            item.sell_in -=1
            item.quality = 80     
        else: 
            item.sell_in -=1
            item.quality = 80

    def update_backstage_quality(self, item):
        """ 
        Checking for sell_in date as follows:
            - When sell date is more then 10, the quality increases with +1.
            - When sell date is 10 or less, the quality increases with +2
            - When sell date is 5 or less, the quality increase with +3.
            - When sell date is past, the quality is 0.
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
            else:
                item.quality = 0

    def update_item_category(self, item):
        """
        Checks for the items and applies its method.
        """
        name = item.name
        if "Aged Brie" == name:
            return self.update_agedBrie_quality(item)
        elif "Conjured Mana Cake" == name:
            return self.update_conjured_quality(item)
        elif "Sulfuras, Hand of Ragnaros" == name:
            return self.update_sulfuras_quality(item)
        else:
            return self.update_backstage_quality(item)
        
    def update_quality(self):
        for item in self.items:
            self.update_item_category(item)
