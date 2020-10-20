import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from utilities.common_utilities import get_home_directory, \
    load_system_config_to_json

driver = None
browser = None
sut = None


@pytest.fixture(scope="class")
def ui_suite_setup(request):
    '''
    UI suite setup : Initialize and launch browser
    :param request:
    :return:
    '''
    global driver
    global browser_name
    global sut
    browser_name = request.config.getoption("--browser")
    print(browser_name)
    sut = request.config.getoption("--sut")
    system_config = load_system_config_to_json()
    # if sut == '':
    #     sut = get_sut_url()
    if browser_name == "chrome" or browser_name == "headlesschrome":
        chrome_options = webdriver.ChromeOptions()
        options = \
            system_config['ui']['browser'][0]['chrome']['chromeOptions']['args']
        for option in options:
            chrome_options.add_argument(option)
        if browser_name == "headlesschrome":
            chrome_options.add_argument('headless')
            # executable_path = "/usr/bin/chromedriver",
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox" or browser_name == "headlessfirefox":
        desired_capabilities = system_config['ui']['browser'][1]['firefox']
        desired_capabilities['marionette'] = True
        options = Options()
        if browser_name =='headlessfirefox':
            options.headless = True
            # executable_path = "/usr/bin/geckodriver",
        driver = webdriver.Firefox(desired_capabilities=desired_capabilities,
                                   options=options)
    driver.get(sut)
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    '''
    It is a hook which adds screenshot of failure testcase in report
    :param item:
    :return:
    '''
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    home_dir = get_home_directory()
    if report.when == 'call' or report.when == "suite_setup":
        xfail = hasattr(report, 'wasxfail')
        if(report.skipped and xfail) or (report.failed and not xfail):
            file_name = str(report.nodeid.replace("::", "_") + ".png").split("/")[2]
            file_name = "screenshots/" + file_name
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:288px;" '\
                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    '''
    Capture screenshot
    :param name:
    :return:
    '''
    driver.get_screenshot_as_file(name)
