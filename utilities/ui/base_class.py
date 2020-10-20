import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException

from config.common_variables import m_sleep
from utilities.common_utilities import getLogger


class UIBaseClass:

    def get_visible_element(self, locator):
        '''
        Get visible element else through an exception(TimeoutException)
        :param locator: locator of webelement
        :return: element - a webelement
        '''
        try:
            element = WebDriverWait(self.driver, m_sleep).until(
                EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            log = getLogger()
            log.info("Timeout occur and element is not visible " + locator[1])

    def verify_link_presence(self, text):
        '''
        Verify link presence on page
        :param text: text of link
        :return: element - a webelement
        '''
        element = WebDriverWait(self.driver, m_sleep).until(
            EC.presence_of_element_located((By.LINK_TEXT, text))
        )
        return element

    def wait_for_page_gets_load(self, *locators):
        '''
        Wait untill page gets load
        :param locators: locators of page in list
        :return:
        '''
        for locator in locators:
            WebDriverWait(self.driver, m_sleep).until(
                EC.visibility_of_element_located(locator)
            )

    def verify_title(self, expected_title):
        '''
        Verify Title of page
        :param expected_title: expected title
        :return:
        '''
        actual_title = self.driver.title
        assert actual_title==expected_title, \
            "Actual Title '"+ actual_title +"'is not matched with expected title '" \
            + expected_title + "'"

    def click_on_visible_element(self, locator: object) -> object:
        '''
        Click on web element
        :param locator: locator of web element
        :return:
        '''
        element = self.get_visible_element(locator)
        log = getLogger()
        try:
            WebDriverWait(self.driver, m_sleep).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            log.info("Timeout is occured and element is not clickable "+ locator[1])
        element.click()

    def input_text_to_element(self, locator, input_text):
        '''
        Input to visible element
        :param locator: locator of web element
        :param input_text: input text
        :return:
        '''
        element = self.get_visible_element(locator)
        element.send_keys(input_text)

    def select_option_by_text(self, locator, text):
        '''
        Select option by text
        :param locator: locator of web element
        :param text: text
        :return:
        '''
        sel = Select(locator)
        sel.select_by_visible_text(text)