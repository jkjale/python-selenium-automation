from selenium.webdriver.common.by import By
from pages.base_page import Page


class HelpPage(Page):
    ASK_SECTION = (By.CSS_SELECTOR, ".section > div:nth-child(3)")
    BROWSE_ALL_HEADER = (By.XPATH, "//*[text()='Browse all Help pages']")
    CONTACT_LINKS = (By.CSS_SELECTOR, ".section > div:nth-child(4)")
    HELP_HEADER = (By.XPATH, "//*[contains(text(), 'Target Help')]")
    TOPIC_SELECTION_DD = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")
    HEADER = (By.XPATH, "//h1[text()=' {SUBSTRING}']")
    SEARCH_ICON = (By.CSS_SELECTOR, ".social-column > div > input:nth-child(2)")
    SEARCH_INPUT = (By.CSS_SELECTOR, ".social-column > div > input:nth-child(1)")

    # Dynamic locator
    def _get_header_locator(self, header):
        return (self.HEADER[0], self.HEADER[1].replace('{SUBSTRING}', header))

    def open_help_page(self):
        self.open_url('https://help.target.com/help')

    def open_help_returns(self):
        self.open_url(
            'https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def select_help_topic(self, dropdown_option):
        self.select_from_dropdown(dropdown_option, *self.TOPIC_SELECTION_DD)

    def verify_help_topic_page(self, header):
        locator = self._get_header_locator(header)
        self.wait_until_visible(locator)

    def verify_target_help_header(self):
        self.wait_until_visible(self.HELP_HEADER)
        self.verify_text('Target Help', *self.HELP_HEADER)

    def verify_search_input(self):
        self.find_element(*self.SEARCH_INPUT)

    def verify_search_icon(self):
        self.find_element(*self.SEARCH_ICON)

    def verify_ask_section(self):
        self.find_element(*self.ASK_SECTION)

    def verify_contact_us_links(self):
        self.find_element(*self.CONTACT_LINKS)

    def verify_browse_all_header(self):
        self.find_element(*self.BROWSE_ALL_HEADER)
        self.verify_text('browse all help pages', *self.BROWSE_ALL_HEADER)
