from collections import OrderedDict
 
class Cache:
    """
    A python class which used ordered dictionary (OrderedDict) to implement the LRU cache.
    Each entry of the dictinoary will be a key/value pair. The search would be 
    by key. LRU Cache will have its maximum size defined at initiation. When adding 
    new keys that cause the capacity to be exceed the size defined at initialtion, 
    the oldest items will be removed to make room. The newly added items/last accessed 
    items will be moved to the back of the dictonary (most recently used) and the elements 
    at the begining will correspond to lest recently used. The element at the begining of the 
    dictionary will be the one to discard when the cache if full (least recently used)
    
    Methods:
        get(key) - Get the value corresponding to key
        put(key,value) - Insert key/value into the cache
        delKey(key) - Delete the key
        reset() - Clear the cache
        dumpCache() - Print the cache contents
    """
    def __init__(self, size, verbose=False):
        """
        Initialize new cache object with the size passed.
        Args:
            size (int): The max size of the cache.
        """
        self.printDebug = verbose
        self.sizeOfCache = size
        self.cacheLRU = OrderedDict()
         
    def get(self, key):
        """
        Returns the value corresponding to the key provided. 
        If the key does not exit, it returns None else it moves
        the key to the end of the dictionary using move_to_end 
        (method of OrderedDict)
        Args:
            key (int): The key to lookup the value
        Returns:
            value (int): The value corresponding to the key if found else None
        """
        if self.sizeOfCache == 0:
            if self.printDebug:
                print("Zero capacity cache and get request. Raise exception.")
            raise Exception('Cache is not defined')
        else:
            if key not in self.cacheLRU:
                return None
            else:
                self.cacheLRU.move_to_end(key)
                return self.cacheLRU[key]
 
    def put(self, key, value):
        """
        Inserts the key/value pair to the cache. If the cache is 
        already full (max capacity), it will remove the element at
        the head of the dict (least recently used) using popitem and 
        insert the key/value pair at the end of the dict (most recently used).
        If the key already exists, it will not fail but mark the item 
        as recently used (move it to the back of the dict)
        Returns:
            Nothing or exception if cache capacity is 0
        """
        if key in self.cacheLRU:
            if self.printDebug:
                print("Key {} already exists in cache. Update this and mark as recently used".format(key))
            self.cacheLRU[key] = value
            self.cacheLRU.move_to_end(key)
        else:
            if self.sizeOfCache == 0:
                if self.printDebug:
                    print("Zero capacity cache and put request. Raise exception.")
                raise Exception('Cache is not defined')
            else:
                if len(self.cacheLRU) >= self.sizeOfCache:
                    outKey, outVal = self.cacheLRU.popitem(last = False)
                    if self.printDebug:
                        print("Cache at capacity of {}. Removing LRU key {}".format(self.sizeOfCache,outKey))
                self.cacheLRU[key] = value
                self.cacheLRU.move_to_end(key)
        
    def delKey(self, key):
        """
        Delete the key from the cache if it exists. If the key does not exist
        nothing happens. The delete is treated as a cache hit and the key is moved
        to the end (most recently used) and then removed. 
        Returns:
            Nothing or exception if cache capacity is 0
        """
        if self.sizeOfCache == 0:
            if self.printDebug:
                print("Zero capacity cache and del request. Raise exception.")
            raise Exception('Cache is not defined')
        else:
            if key in self.cacheLRU:
                self.cacheLRU.move_to_end(key)
                self.cacheLRU.popitem(last = True)
            else:
                if self.printDebug:
                    print("Key {} to delete does not exist in the cache. Doing nothing.\n".format(self.sizeOfCache))

    def reset(self):
        """
        Reset the cache
        Returns:
            Nothing or exception if cache capacity is 0
        """
        if self.sizeOfCache == 0:
            if self.printDebug:
                print("Zero capacity cache and reset request. Raise exception.")
            raise Exception('Cache is not defined')
        else:
            self.cacheLRU.clear()

    def dumpCache(self):
        """
        Print the contents of the cache
        Returns:
            Nothing
        """
        print(self.cacheLRU)

 