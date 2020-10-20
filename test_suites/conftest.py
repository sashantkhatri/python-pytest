import pytest
from selenium import webdriver
from utilities.common_utilities import load_system_config_to_json, load_user_file_to_json

driver = None
browser = None
sut = None
system_config = None
user_dict = None

def pytest_addoption(parser):
    '''
    command line argument addoptions
    :param parser:
    :return:
    '''
    parser.addoption(
        "--browser", action="store", default="headlesschrome",
        help="Default browser_name is 'chrome', it supports firefox, headlessfirefox, headlesschrome and chrome"
    )
    parser.addoption(
        "--sut", action="store", default="https://www.google.com/",
        help="Default sut url is 'https://www.google.com/'"
    )

@pytest.fixture()
def suite_setup(request):
    '''
    Suite Setup
    :param request:
    :return:
    '''
    # browser = None
    global sut
    global system_config
    global user_dict
    sut = request.config.getoption("--sut")
    # if sut == '':
    #     sut = get_sut_url()
    system_config = load_system_config_to_json()
    user_dict = load_user_file_to_json()
    request.cls.system_config = system_config
    request.cls.user_dict = user_dict
    yield
    print("tear-down")

# INTENTIONALLY ADD BELOW HOOK AND IT WILL EXECUTE AFTER EXECUTION OF ALL TEST SUTIE
# def pytest_sessionfinish(session, exitstatus):
#     print("Total : "+ str(session.testscollected) +", failed : "+str(session.testsfailed)+
#           ", Passed: "+str(session.testscollected - session.testsfailed))
