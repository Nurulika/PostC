# test_postcssprocessor.py
"""
Tests for PostCSSProcessor module.
"""

import unittest
from postcssprocessor import PostCSSProcessor

class TestPostCSSProcessor(unittest.TestCase):
    """Test cases for PostCSSProcessor class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PostCSSProcessor()
        self.assertIsInstance(instance, PostCSSProcessor)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PostCSSProcessor()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
