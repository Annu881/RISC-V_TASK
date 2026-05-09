import unittest
from src.analyzer import normalize_extension, cross_reference

class TestAnalyzer(unittest.TestCase):
    def test_normalize_extension(self):
        self.assertEqual(normalize_extension("zba"), "zba")
        self.assertEqual(normalize_extension("rv64_i"), "i")
        self.assertEqual(normalize_extension("RV32I"), "i")
        self.assertEqual(normalize_extension("zicsr"), "zicsr")
        self.assertEqual(normalize_extension("i"), "i")

    def test_cross_reference(self):
        # mock json 
        json_exts = {
            "i": ["add", "sub"],
            "m": ["mul"],
            "zba": ["sh1add"]
        }
        
        # mock manual
        manual_exts = {"I", "Zba", "zicsr"}
        
        result = cross_reference(json_exts, manual_exts)
        
        # 'm' is in JSON only
        self.assertIn("m", result["json_only"])
        # 'zicsr' is in manual only (normalized to what? cross_ref returns the original from manual_exts)
        self.assertIn("zicsr", result["manual_only"])
        # 'i' and 'zba' are in both (returns JSON original)
        self.assertIn("i", result["both"])
        self.assertIn("zba", result["both"])

if __name__ == "__main__":
    unittest.main()
