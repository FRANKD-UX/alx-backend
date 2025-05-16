class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching.
    A caching system using LFU (Least Frequently Used) algorithm.
    If multiple items have the same frequency, uses LRU algorithm.
    """

    def __init__(self):
        """Initialize the LFUCache"""
        super().__init__()
        self.frequencies = {}  # Key: frequency count
        self.usage_order = []  # For LRU tiebreaker

    def put(self, key, item):
        """
        Add an item in the cache using LFU algorithm
        
        Args:
            key: Key to add to the cache
            item: Value to associate with the key
        """
        if key is None or item is None:
            return

        # Update existing key
        if key in self.cache_data:
            self.cache_data[key] = item
            # Update usage order
            self.usage_order.remove(key)
            self.usage_order.append(key)
            # Increment frequency
            self.frequencies[key] += 1
            return

        # Add new key
        if len(self.cache_data) >= self.MAX_ITEMS:
            self._discard_lfu()
        
        self.cache_data[key] = item
        self.usage_order.append(key)
        self.frequencies[key] = 1

    def get(self, key):
        """
        Get an item by key and update frequency and usage order
        
        Args:
            key: Key to look up in the cache
            
        Returns:
            The value associated with the key, or None if key doesn't exist
        """
        if key is None or key not in self.cache_data:
            return None
        
        # Update usage order
        self.usage_order.remove(key)
        self.usage_order.append(key)
        
        # Increment frequency
        self.frequencies[key] += 1
        
        return self.cache_data[key]

    def _discard_lfu(self):
        """Helper method to discard least frequently used item"""
        if not self.cache_data:
            return
        
        # Find minimum frequency
        min_freq = min(self.frequencies.values())
        
        # Get all keys with minimum frequency
        min_freq_keys = [k for k, f in self.frequencies.items() if f == min_freq]
        
        # If multiple keys have the same min frequency, use LRU to break tie
        lfu_key = None
        for key in self.usage_order:
            if key in min_freq_keys:
                lfu_key = key
                break
        
        # Remove the key
        del self.cache_data[lfu_key]
        del self.frequencies[lfu_key]
        self.usage_order.remove(lfu_key)
        print("DISCARD: {}".format(lfu_key))
