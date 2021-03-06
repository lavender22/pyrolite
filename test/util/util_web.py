import unittest
from pyrolite.util.web import *


class TestUrlify(unittest.TestCase):
    """
    Tests the urlify utility function.
    """

    def test_strip(self):
        for s in ["A B", "A_B", "A  ", "A B C D"]:
            with self.subTest(s=s):
                self.assertFalse(" " in urlify(s))


class TestDownloadFile(unittest.TestCase):

    def test_non_existant(self):
        url = "http://www.notquitegoogle.com/"
        out = download_file(url, encoding=None)
        self.assertTrue(out is None)

    def test_image(self):
        url = "https://pyrolite.readthedocs.io/en/develop/_static/icon_small.png"
        out = download_file(url, encoding=None)
        self.assertTrue(out is not None)


if __name__ == "__main__":
    unittest.main()
