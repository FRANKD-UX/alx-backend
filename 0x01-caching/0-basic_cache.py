#!/usr/bin/env python3
"""
BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching.
    A caching system with no limit.
    """

    def put(self, key, item):
        """
        Add an item in the cache.
        
        Args:
            key: Key to add to the cache
            item: Value to associate with the key
            
        Returns:
            None
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key.
        
        Args:
            key: Key to look up in the cache
            
        Returns:
            The value associated with the key, or None if key doesn't exist
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
