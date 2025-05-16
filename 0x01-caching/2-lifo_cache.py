#!/usr/bin/env python3
"""
FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching.
    A caching system using FIFO (First-In-First-Out) algorithm.
    """

    def __init__(self):
        """
        Initialize the FIFOCache.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache.
        
        Args:
            key: Key to add to the cache
            item: Value to associate with the key
            
        Returns:
            None
        """
        if key is None or item is None:
            return
        
        # If key already exists, update its value and don't change order
        if key in self.cache_data:
            self.cache_data[key] = item
            return
        
        # Add new item to cache
        self.cache_data[key] = item
        self.order.append(key)
        
        # Check if cache is full
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove first item (FIFO)
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

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
