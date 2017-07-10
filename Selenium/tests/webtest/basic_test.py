import pytest
import unittest


@pytest.mark.usefixtures("one_time_setup")
class BasicTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, one_time_setup):
        self.driver = one_time_setup
        print("In setup")

    def test_twitter(self):
        self.driver.get("http://www.twitter.com")
        assert "Twitter" in self.driver.title

    def test_facebook(self):
        self.driver.get("http://www.facebook.com")
        assert "Facebook" in self.driver.title