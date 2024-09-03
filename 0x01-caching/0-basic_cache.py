#!/usr/bin/env python3
""" BasicCaching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Caching without limit
    """

    def __init__(self):
        """ Class initialization
        """
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item in the cache
        """
        return self.cache_data.get(key)
