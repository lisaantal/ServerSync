# test_serversync.py
"""
Tests for ServerSync module.
"""

import unittest
from serversync import ServerSync

class TestServerSync(unittest.TestCase):
    """Test cases for ServerSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ServerSync()
        self.assertIsInstance(instance, ServerSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ServerSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
