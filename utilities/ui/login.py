from pytest import fail
from page_locators.login_page import *
from utilities.common_utilities import getLogger, get_totp
from .base_class import UIBaseClass

class Login(UIBaseClass):

    def __init__(self, driver):
        self.driver = driver
        self.log = getLogger()

    def perform_login(self, username, password, secret, valid_credentials=True):
        '''
        Perform login
        :param username: username
        :param password: password
        :param secret: secret to generate totp
        :param valid_credentials: are credentials valid
        :return:
        '''
        log = self.log
        log.info("Perform login")
