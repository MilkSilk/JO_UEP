import unittest

from selenium.webdriver.android import webdriver
from selenium.webdriver.common.keys import Keys


class TestSelenium(unittest.TestCase):
    @unittest.skip("Nie pyknie na serwerze github, bo nie sciagamy sterownika")
    def test_selenium(self):
        driver = webdriver.Chrome(executable_path='/Users/jacja/Downloads/chromedriver')
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)
        driver.close()