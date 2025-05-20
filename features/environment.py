import os
import re
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from app.application import Application
from support.logger import logger


def before_all(context):
    context.config.setup_logging()
    load_dotenv()
    browser = context.config.userdata.get("browser", None)
    if browser:
        os.environ["BROWSER"] = browser
    else:
        browser = os.getenv("BROWSER", "chrome").lower()
        os.environ["BROWSER"] = browser
    print("Using browser:", browser)


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """

    # Get the browser type from the environment variable or use 'chrome' as default
    browser = os.getenv("BROWSER", "chrome").lower()

    if browser == "chrome":
        chrome_options = Options()
        context.is_mobile = os.getenv("ENABLE_MOBILE_EMULATION", "false").lower() == "true"
        device_name = os.getenv("MOBILE_EMULATION", None)
        if context.is_mobile and device_name:
            mobile_emulation = {
                "deviceName": device_name
            }
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        driver_path = ChromeDriverManager().install()
        service = Service(driver_path)
        context.driver = webdriver.Chrome(service=service, options=chrome_options)
        context.driver.maximize_window()

    elif browser == "firefox":
        driver_path = GeckoDriverManager().install()
        service = Service(driver_path)
        context.driver = webdriver.Firefox(service=service)
        context.driver.maximize_window()

    elif browser == "headless":
        options = Options()
        options.add_argument("headless")
        service = Service(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(options=options, service=service)

    elif browser == "browserstack":
        # Register for BrowserStack, then grab user and key from https://www.browserstack.com/accounts/settings
        # To change devices go to https://www.browserstack.com/docs/automate/capabilities and go to "Legacy" and choose device
        bs_user = os.getenv("BS_USERNAME")
        bs_key = os.getenv("BS_KEY")
        url = f"http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub"
        options = Options()
        device_name = "Google Pixel 9"
        bstack_options = {
            "osVersion": "15.0",
            "deviceName": device_name,
            "consoleLogs": "info",
            "sessionName": scenario_name,
        }
        # Use regex to check if the device name contains mobile-related keywords
        mobile_pattern = re.compile(r"(samsung|iphone|pixel|galaxy|android)", re.IGNORECASE)
        context.is_mobile = bool(mobile_pattern.search(device_name))
        options.set_capability("bstack:options", bstack_options)
        context.driver = webdriver.Remote(command_executor=url, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    print(f"Selected browser: {browser}")
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('Scenariooooo:', scenario)
    print('\nStarted scenario:', scenario.name)
    logger.info(f'Starting scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step:', step)
    logger.info(f'Starting step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed:', step.name)
        logger.warning(f'Step failed with status: {step.status}')


def after_scenario(context, feature):
    context.driver.quit()
