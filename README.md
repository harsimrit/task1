# Problem Description:
Write the code to implement a Least-Recently Used (LRU) Cache. A correctly constructed
LRU Cache will have its maximum capacity set at the time of the construction, and when adding
new keys that cause the capacity to be exceeded, the least recently used item needs to be
identified and discarded. You can use any language to implement this.

# Assumptions
1. Any operation (get/put/del/reset) must be done on a valid cache. If cache is not defined and operation is requested, it will raise an exception
2. Calling put for an existing key will update the value and mark it as most recently used
3. Calling del for an existing key will mark it as accessed and then delete it
4. Calling del for a non existant key will do nothing

# Techinical Details:
1. This code uses Python 3.7.6 
2. The cache is implemented using OrderedDict as the base structure 
3. The individual methods are implemted in the encapsulating class 
4. The cache supports both numeric and strings keys and values 
5. The unit tests are implemeted as python unittest class
6. To get detailed print messages, set the cache with verbose as True

# Code Setup:
There are two files in the submission
1. cacheLRU.py - This is the file with the cache implemented as an OrderedDict
2. unit_tests.py - Unit tests implemented as unittest which cover edge cases as well as the functionality
3. main.py - Driver script for using the cache and its functions

# Getting Started
To run the project
1. Clone the repository to your local machine
2. run python unit_tests.py to run all the testcases
3. run python main.py to run custom driver script