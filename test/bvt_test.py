from appium import webdriver
import unittest
import time
from pytest_testconfig import config

timeout = 30
poll = 2


class IAppBVT(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        appium_server_url = config['appium_server_url']
        desired_caps['platformName'] = config['desired_caps']['platformName']
        desired_caps['udid'] = config['desired_caps']['udid']
        desired_caps['deviceName'] = config['desired_caps']['deviceName']
        desired_caps['appPackage'] = config['desired_caps']['appPackage']
        desired_caps['appActivity'] = config['desired_caps']['appActivity']
        desired_caps['automationName'] = config['desired_caps']['automationName']
        desired_caps['noReset'] = config['desired_caps']['noReset']

        self.driver = webdriver.Remote(appium_server_url, desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_bvt(self):
        print('BVT test is started!')
        status = self.is_record_event_btn_exist()
        print(f'The record event button is exist - {status}')
        self.assertTrue(status, f'Check record_button result is {status}')
        print('Test finished!')

    def is_record_event_btn_exist(self):
        elem = self._find_elem_by_xpath('//android.widget.Button[contains(@resource-id,"id/trackEventButton")]')
        return elem is not None

    def _find_elem_by_xpath(self, elem_xpath, time_out=timeout, raise_exception=True):
        start = time.time()
        elem = None
        while time.time() - start < time_out and elem is None:
            time.sleep(poll)
            try:
                elem = self.driver.find_element_by_xpath(elem_xpath)
            except Exception:
                print('by pass the element not found')

        if elem is None and raise_exception:
            raise LookupError(f'The element which xpath is {elem_xpath} could not be found')

        return elem
