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
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_kwy = self.cache_data.poitem()[0]
            print(f"DISCARD: {first_key}")
            del self.cache_data[first_key]

    def get(self, key):
        """ Get an item in the cache
        """
        return self.cache_data.get(key)
