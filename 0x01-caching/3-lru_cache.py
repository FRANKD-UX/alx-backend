#!/usr/bin/env python3
"""
LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching.
    A caching system using LRU (Least Recently Used) algorithm.
    """

    def __init__(self):
        """
        Initialize the LRUCache.
        """
        super().__init__()
        self.usage_order = []  # Track the usage order of keys

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
        
        # If key already exists, update its value and move to most recently used
        if key in self.cache_data:
            self.cache_data[key] = item
            # Update key position in usage order (remove and re-add to make it most recently used)
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return
        
        # Check if cache is full before adding new item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove least recently used item (first item in usage_order)
            lru_key = self.usage_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")
        
        # Add new item to cache
        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """
        Get an item by key.
        Updates the usage order to mark the key as most recently used.
        
        Args:
            key: Key to look up in the cache
            
        Returns:
            The value associated with the key, or None if key doesn't exist
        """
        if key is None or key not in self.cache_data:
            return None
        
        # Update usage order (move the accessed key to the end as most recently used)
        self.usage_order.remove(key)
        self.usage_order.append(key)
        
        return self.cache_data[key]
