#!/usr/bin/env python3
"""
LFUCache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching.
    A caching system using LFU (Least Frequently Used) algorithm.
    If multiple items have the same frequency, use LRU (Least Recently Used).
    """

    def __init__(self):
        """
        Initialize the LFUCache.
        """
        super().__init__()
        self.frequencies = {}  # Track frequency of each key
        self.usage_order = []  # Track usage order for LRU tiebreaker

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
        
        # If key already exists, update its value and don't discard anything
        if key in self.cache_data:
            self.cache_data[key] = item
            # Update key position in usage order (remove and re-add to make it most recently used)
            self.usage_order.remove(key)
            self.usage_order.append(key)
            # Increment frequency count
            self.frequencies[key] += 1
            return
        
        # Check if cache is full before adding new item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self._discard_least_frequent()
        
        # Add new item to cache
        self.cache_data[key] = item
        self.usage_order.append(key)
        self.frequencies[key] = 1  # Initialize frequency count

    def get(self, key):
        """
        Get an item by key.
        Updates the usage order and frequency count.
        
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
        
        # Increment frequency count
        self.frequencies[key] += 1
        
        return self.cache_data[key]

    def _discard_least_frequent(self):
        """
        Discard the least frequently used item.
        If multiple items have the same frequency, use LRU.
        """
        if not self.cache_data:
            return
        
        # Find the minimum frequency
        min_freq = min(self.frequencies.values())
        
        # Get all keys with minimum frequency
        min_freq_keys = [k for k, v in self.frequencies.items() if v == min_freq]
        
        # If multiple keys have the same minimum frequency, use LRU
        if len(min_freq_keys) > 1:
            # Find the least recently used key among min_freq_keys
            for key in self.usage_order:
                if key in min_freq_keys:
                    lfu_key = key
                    break
        else:
            lfu_key = min_freq_keys[0]
        
        # Remove the selected key
        del self.cache_data[lfu_key]
        del self.frequencies[lfu_key]
        self.usage_order.remove(lfu_key)
        print(f"DISCARD: {lfu_key}")
