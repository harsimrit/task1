from cacheLRU import Cache

if __name__ == '__main__':

    #to define the cache
    cache = Cache(size=3,verbose=True)

    #to enter key/value to the cache
    cache.put('a',1)
    cache.put('b',2)
    cache.put('c',3)
    cache.put('d',4)
    
    #to get value of a particular key in the cache
    val = cache.get('b')

    #to delete a particular key
    cache.delKey('c')

    #to dump the cache for visual inspection
    cache.dumpCache()

    #to reset the cache
    cache.reset()