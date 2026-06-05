from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from playwright.sync_api import expect

def test_trigger_slack_on_failure(page):
    login = LoginPage(page)
    checkout = CheckoutPage(page)

    # 1. Standard Login
    login.navigate()
    login.login("standard_user", "secret_sauce")
    
    # 2. Add an item
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    
    # 3. Complete Checkout
    checkout.complete_checkout("Mahad", "Sultan", "46000")

    # 4. INTENTIONAL FAILURE
    # We expect the header to say 'Order Failed' (it actually says 'Thank you for your order!')
    # Playwright will wait 5 seconds, fail, and trigger the conftest hook.
    expect(checkout._complete_header).to_have_text("Order Failed", timeout=5000)