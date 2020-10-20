import json
import pytest
import requests
from config.api.api_variables import success_code


@pytest.mark.usefixtures("suite_setup", "api_suite_setup")
class TestAPI1:
    '''
    Test API1- Test suite
    '''

    @pytest.mark.regression
    def test_api_1_1(self):
        '''
        Test api 1-1
        :return:
        '''
        print("API-1-1")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_api_1_2(self):
        '''
        Test api 1-2
        :return:
        '''
        print("API-1-2")

    @pytest.mark.regression
    def test_api_1_3(self, setup_test_api_1_3):
        '''
        Test api 1-3
        :param setup_test_api_1_3: it is setup  for this testcase
        :return:
        '''
        print("API-1-3")
        assert 1==2

    @pytest.fixture()
    def setup_test_api_1_3(self):
        '''
        This is setup method for test api 1_3
        :return:
        '''
        print("Setup for API-Test-1_3")
        yield
        print("Teardown for API-Test-1_3")