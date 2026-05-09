import unittest
from src.parser import parse_instructions

class TestParser(unittest.TestCase):
    def test_parse_instructions(self):
        mock_data = {
            "add": {"extension": ["rv_i"]},
            "mul": {"extension": ["rv_m"]},
            "fancy": {"extension": ["rv_i", "rv_m"]}
        }
        
        exts, shared = parse_instructions(mock_data)
        
        # Test grouping
        self.assertIn("rv_i", exts)
        self.assertIn("rv_m", exts)
        self.assertEqual(len(exts["rv_i"]), 2)
        self.assertEqual(len(exts["rv_m"]), 2)
        
        # Test shared
        self.assertIn("fancy", shared)
        self.assertEqual(len(shared), 1)
        self.assertEqual(shared["fancy"], ["rv_i", "rv_m"])

if __name__ == "__main__":
    unittest.main()
