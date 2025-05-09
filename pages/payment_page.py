from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from utils.reader import LocatorReader


class PaymentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        cfg = LocatorReader()

        # iframe locators
        self.card_iframe   = cfg.get("payment_page", "card_number_iframe")
        self.expiry_iframe = cfg.get("payment_page", "expiry_date_iframe")
        self.cvv_iframe    = cfg.get("payment_page", "cvv_iframe")

        # real inputs inside each frame
        self.card_input   = cfg.get("payment_page", "card_number_input")
        self.expiry_input = cfg.get("payment_page", "expiry_date_input")
        self.cvv_input    = cfg.get("payment_page", "cvv_input")

        # page elements
        self.pay_now_button        = cfg.get("payment_page", "pay_now_button")
        self.order_table_section   = cfg.get("payment_page", "order_table_section")
        self.total_pay_amount      = cfg.get("payment_page", "total_pay_amount")
        self.split_bill_button     = cfg.get("payment_page", "split_bill_button")
        self.custom_split_button   = cfg.get("payment_page", "custom_split_button")
        self.custom_amount_input   = cfg.get("payment_page", "custom_amount_input")
        self.confirm_split_button  = cfg.get("payment_page", "confirm_split_button")
        self.pay_button            = cfg.get("payment_page", "pay_button")
        self.success_message_xpath = cfg.get("payment_page", "payment_success_message")

    def is_pay_now_button_visible(self) -> bool:
        return self.is_visible(self.pay_now_button)

    def click_pay_now(self) -> None:
        self.click(self.pay_now_button)

    def is_order_table_visible(self) -> bool:
        return self.is_visible(self.order_table_section)

    def get_you_pay_amount(self) -> float:
        text = self.get_text(self.total_pay_amount).replace("AED", "").strip()
        return float(text)

    def click_split_bill(self) -> None:
        self.click(self.split_bill_button)

    def click_custom_split(self) -> None:
        self.click(self.custom_split_button)

    def enter_custom_amount(self, amount: str) -> None:
        self.send_keys(self.custom_amount_input, amount)

    def click_confirm_split(self) -> None:
        self.click(self.confirm_split_button)

    def click_tip_by_index(self, index: int) -> None:
        xpath = f"(//div[contains(@class,'inputs_tipItem__')])[{index}]"
        self.click(xpath)

    def enter_card_details(self, card_number: str, expiry: str, cvv: str) -> None:
        def _enter(frame_xpath, input_xpath, value):
            self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, frame_xpath)))
            elem = self.wait.until(EC.visibility_of_element_located((By.XPATH, input_xpath)))
            elem.clear()
            elem.send_keys(value)
            self.driver.switch_to.default_content()

        _enter(self.card_iframe,   self.card_input,   card_number)
        _enter(self.expiry_iframe, self.expiry_input, expiry)
        _enter(self.cvv_iframe,    self.cvv_input,    cvv)

    def click_pay(self) -> None:
        self.click(self.pay_button)

    def is_payment_successful(self) -> bool:
        return self.is_visible(self.success_message_xpath)
