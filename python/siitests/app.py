from .utils import browser_utils


class TestRunner:
    def __init__(self):
        self.driver = browser_utils.setup_driver()


if __name__ == "__main__":
    test_runner = TestRunner()
