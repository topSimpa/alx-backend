#!/usr/bin/env python3
""" LRUCaching module
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Caching with limit
        uses  Least Recently used as replacement strategy
    """

    def __init__(self):
        super().__init__()
        self.key_use = {}
        self.count_line = 0

    def put(self, key, item):
        """Add an item in the cache
        """
        if key and item:
            self.count_line += 1
            if self.cache_data.get(key):
                del_met = None
                for use_metric in self.key_use.keys():
                    if self.key_use[use_metric] == key:
                        del_met = use_metric
                        break
                if del_met:
                    del self.key_use[del_met]
            elif len(self.cache_data) == BaseCaching.MAX_ITEMS:
                min_use = min(self.key_use.keys())
                lru_key = self.key_use[min_use]
                print(f"DISCARD: {lru_key}")
                del self.cache_data[lru_key]
                del self.key_use[min_use]
            self.key_use[self.count_line] = key
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item in the cache
        """
        del_met = None
        val = self.cache_data.get(key)
        if val:
            for use_metric in self.key_use.keys():
                if self.key_use[use_metric] == key:
                    del_met = use_metric
                    self.count_line += 1
                    break
        if del_met:
            del self.key_use[del_met]
            self.key_use[self.count_line] = key
        return self.cache_data.get(key)
