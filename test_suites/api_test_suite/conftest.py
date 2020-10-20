import pytest


sut = None


@pytest.fixture(scope="class")
def api_suite_setup(request):
    '''
    API Suite setup
    :param request: request parameter
    :return:
    '''
    global sut
    sut = request.config.getoption("--sut")
    request.cls.sut = sut
    yield
    print("api - teardown")