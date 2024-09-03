#!/usr/bin/env python3
""" FifoCaching module
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Caching with limit
        uses  FIFO as replacement strategy
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]

    def get(self, key):
        """ Get an item in the cache
        """
        if key:
            return self.cache_data.get(key)
        return None
