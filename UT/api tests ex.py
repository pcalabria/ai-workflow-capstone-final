#!/usr/bin/env python
"""
api tests
these tests use the requests package however similar requests can be made with curl
e.g.
data = '{"key":"value"}'
curl -X POST -H "Content-Type: application/json" -d "%s" http://localhost:8080/predict'%(data)
"""

import sys
import os
import unittest
import requests
import json
import re
from ast import literal_eval
import numpy as np

port = 4000

try:
    requests.post('http://127.0.0.1:{}/predict'.format(port))
    server_available = True
except:
    server_available = False
    
## test class for the main window function
class ApiTest(unittest.TestCase):
    """
    test the essential functionality
    """

    @unittest.skipUnless(server_available,"local server is not running")
    def test_01(self):
        """
        test the train functionality
        """
      
        r = requests.post('http://127.0.0.1:{}/train'.format(port),json={"mode":"test"})
        train_complete = re.sub("\W+","",r.text)
        self.assertEqual(train_complete,'true')
        
### Run the tests
if __name__ == '__main__':
    unittest.main()