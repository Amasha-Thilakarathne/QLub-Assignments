import pytest
from pages.payment_page import PaymentPage
from utils.config_loader import load_config


@pytest.mark.usefixtures("driver")
def test_full_payment_flow(driver):
    config = load_config()
    payment_page = PaymentPage(driver)

    # Navigate to the payment page
    driver.get(config["base_url"])
    print("Navigated to payment page.")

    # Verify and click 'Pay Now'
    assert payment_page.is_pay_now_button_visible(), "Pay Now button not visible"
    payment_page.click_pay_now()
    print("Clicked 'Pay Now'.")

    # Verify order table is displayed
    assert payment_page.is_order_table_visible(), "Order table not visible"

    # Capture and verify payable amount
    amount = payment_page.get_you_pay_amount()
    assert amount > 0, "Payable amount should be greater than 0"
    print(f"Payable amount: AED {amount}")

    # Split the bill
    payment_page.click_split_bill()
    payment_page.click_custom_split()
    payment_page.enter_custom_amount(config["custom_amount_value"])
    payment_page.click_confirm_split()
    print("Custom split applied.")

    # Select tip percentage (second button)
    payment_page.click_tip_by_index(2)
    print("Selected tip option #2.")

    # Enter card details and submit payment
    payment_page.enter_card_details(
        card_number="4242424242424242",
        expiry="12/26",
        cvv="123"
    )
    print("Entered card details.")
    payment_page.click_pay()
    print("Clicked 'Pay'.")

    # Assert payment success
    assert payment_page.is_payment_successful(), "Payment was not successful"
    print("Payment successful.")
