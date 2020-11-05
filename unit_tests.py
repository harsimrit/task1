import unittest
import random

from cacheLRU import Cache

class TestLRUCache(unittest.TestCase):
    """
        Test LRU Cache implementation
    """
    def setUp(self):
        """
        Set the verbose variable to print debug info
        """
        self.verbose = False

    def tearDown(self):
        pass

    def test_empty_cache_get(self):
        """
            Test the get function when cache capacity is 0
        """
        print('test_empty_cache_get')
        cache = Cache(size=0,verbose=self.verbose)
        with self.assertRaises(Exception) as context:
            val = cache.get(1)

        self.assertTrue('Cache is not defined' in str(context.exception))
        
    def test_empty_cache_del(self):
        """
            Test the del function when cache capacity is 0
        """
        print('test_empty_cache_del')
        cache = Cache(size=0,verbose=self.verbose)
        with self.assertRaises(Exception) as context:
            cache.delKey(1)

        self.assertTrue('Cache is not defined' in str(context.exception))

    def test_empty_cache_put(self):
        """
            Test the put function when cache capacity is 0
        """
        print('test_empty_cache_put')
        cache = Cache(size=0,verbose=self.verbose)
        with self.assertRaises(Exception) as context:
            cache.put(1,1)

        self.assertTrue('Cache is not defined' in str(context.exception))

    def test_empty_cache_reset(self):
        """
            Test the reset function when cache capacity is 0
        """
        print('test_empty_cache_reset')
        cache = Cache(size=0,verbose=self.verbose)
        with self.assertRaises(Exception) as context:
            cache.reset()

        self.assertTrue('Cache is not defined' in str(context.exception))

    def test_cache_reset(self):
        """
            Test the functionality of reseting the cache
        """
        print('test_cache_reset')
        cache = Cache(size=3,verbose=self.verbose)
        cache.put(1,3)
        cache.put(2,2)
        cache.put(3,1)
        cache.reset()

        self.assertEqual(0, len(cache.cacheLRU))
    
    def test_cache_get(self):
        """
            Test the functionality of get function
        """
        print('test_cache_get')
        cache = Cache(size=3,verbose=self.verbose)
        cache.put(1,4)
        cache.put(2,3)
        cache.put(3,3)
        cache.put(4,1)
        val = cache.get(2)

        self.assertEqual(3,val)
        self.assertEqual(2, next(reversed(cache.cacheLRU)))

    def test_cache_update_val(self):
        """
            Test the put function when value is updated for a key
        """
        print('test_cache_update_val')
        cache = Cache(size=3,verbose=self.verbose)
        cache.put(1,3)
        cache.put(2,2)
        cache.put(3,1)
        cache.put(1,5)

        self.assertEqual(5, cache.get(1))
        
    def test_cache_1(self):
        """
            Test the functionality of having the last item in 
            ordered dictionary as the most recent one 
        """
        print('test_cache_1')
        cache = Cache(size=3,verbose=self.verbose)
        cache.put(1,3)
        cache.put(2,2)
        cache.put(3,1)
        val = cache.get(1)

        self.assertEqual(1, next(reversed(cache.cacheLRU)))     
    
    def test_cache_2(self):
        """
            Test the functionality of having the last item in 
            ordered dictionary as the most recent one 
        """
        print('test_cache_2')
        cache = Cache(size=3,verbose=self.verbose)
        cache.put(1,3)
        cache.put(2,2)
        cache.put(3,1)
        val = cache.get(2)

        self.assertEqual(2, next(reversed(cache.cacheLRU)))

    def test_cache_3(self):
        """
            Test the functionality of having the last item in 
            ordered dictionary as the most recent one 
        """
        print('test_cache_3')
        cache = Cache(size=3,verbose=self.verbose)
        cache.put(1,3)
        cache.put(2,2)
        cache.put(3,1)
        val = cache.get(3)

        self.assertEqual(3, next(reversed(cache.cacheLRU)))
    
    def test_cache_4(self):
        """
            Test the functionality of deleting a key
        """
        print('test_cache_4')
        cache = Cache(size=3,verbose=self.verbose)
        cache.put(1,3)
        cache.put(2,2)
        cache.put(3,1)
        cache.delKey(1)

        self.assertEqual(3, next(reversed(cache.cacheLRU)))

    def test_cache_5(self):
        """
            Test the functionality of put when entries greater than size are added
        """
        print('test_cache_5')
        cache = Cache(size=3,verbose=self.verbose)
        cache.put(1,4)
        cache.put(2,3)
        cache.put(3,2)
        cache.put(4,1)

        self.assertEqual(4, next(reversed(cache.cacheLRU)))

if __name__ == '__main__':
    unittest.main()