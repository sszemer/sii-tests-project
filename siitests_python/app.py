from utils import browser_utils


class TestRunner:
    def __init__(self):
        self.driver = browser_utils.setup_driver()


if __name__ == "__main__":
    test_runner = TestRunner()

    test_runner.driver.get("https://www.kayak.pl/")

    el = test_runner.driver.find_element_by_xpath("//*[contains(@id, 'soundsGood')]")
    el.click()
    if test_runner.driver.find_elements_by_xpath("//*[@title = 'Akceptuj']"):
        el = test_runner.driver.find_element_by_xpath("//*[@title = 'Akceptuj']")
        el.click()

    print(el.id)
