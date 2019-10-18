from .utils import browser_utils


class TestRunner:
    def __init__(self):
        self.driver = browser_utils.setup_driver()


if __name__ == "__main__":
    test_runner = TestRunner()

    test_runner.driver.get("https://www.skyscanner.pl/")

    el = test_runner.driver.find_element_by_id("footer-flags-root")

    print(el.text)
