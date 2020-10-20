import pytest

from utilities.execl_utilities import ExcelUtilities



@pytest.mark.usefixtures("ui_suite_setup", "suite_setup")
class TestUI1:

    @pytest.mark.regression
    def test_ui_1_1(self, setup_ui_1_1):
        '''
        test_ui_1_1
        :param setup_ui_1_1: fixture for this testcase
        :return:
        '''
        print("test_ui_1_1")

    @pytest.fixture()
    def setup_ui_1_1(self):
        '''
        Fixture for test_ui_1_1, setup and teardowm for test_ui_1_1
        :return:
        '''
        print("In - setup 1_1")
        yield
        print("In - teardown 1_1")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_ui_1_2(self, setup_ui_1_2):
        '''
        test_ui_1_2
        :param setup_ui_1_2: fixture for this testcase
        :return:
        '''
        print("UI-1-2")

    @pytest.fixture()
    def setup_ui_1_2(self):
        '''
        Fixture for test_ui_1_2, setup and teardowm for test_ui_1_2
        :return:
        '''
        print("In Setup 1_2")
        yield
        print("In Teardown 1_2")

    @pytest.mark.sanity
    def test_ui_1_3(self):
        '''
        test_ui_1_3
        :return:
        '''
        print("UI-1-3")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_ui_1_4(self, get_login_test_data):
        '''
        Datadriven test with fixture
        :param get_login_test_data:
        :return:
        '''
        print("UI-1-4")
        print("Datadriven")
        print(get_login_test_data['is_valid_credentials'])
        print(get_login_test_data['email'])
        print(get_login_test_data['password'])

    @pytest.fixture(params=ExcelUtilities.get_test_data("Sheet1"))
    def get_login_test_data(self, request):
        '''
        fixture of data driven test
        :param request:
        :return:
        '''
        return request.param