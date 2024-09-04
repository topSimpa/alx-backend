#!/usr/bin/env python3
""" FifoCaching module
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Caching with limit
        uses  LIFO as replacement strategy
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                last_key = self.cache_data.popitem()[0]
                print(f"DISCARD: {last_key}")
                del self.cache_data[last_key]
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item in the cache
        """
        return self.cache_data.get(key)
