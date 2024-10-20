import pytest
from utils.helpers.config_provider import settings_config


pytest_plugins = (
    "fixtures.base_driver_setup"
)


def pytest_addoption(parser):
    parser.addoption("--run", action="store_false", default=True)


def pytest_configure(config):
    if hasattr(config, '_metadata'):
        config._metadata['Nowina URL'] = settings_config.base_page_url
        config._metadata['Plugins'] = None
        config._metadata['Python'] = None
        config._metadata['Packages'] = None
        config._metadata['Platform'] = None


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)
    report.description = str(item.function.__doc__)


def pytest_runtest_setup(item):
    """
    Setup test_name_ global pytest variable
    """
    test_name = item.name.replace("test_", "")
    setattr(item, "test_name_", test_name)


def is_master(config):
    """True if the code running the given pytest.config object is running in a xdist master
    node or not running xdist at all.
    """
    return not hasattr(config, 'slaveinput')