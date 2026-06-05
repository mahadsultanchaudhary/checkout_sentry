from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from playwright.sync_api import expect

def test_successful_checkout(page):
    login = LoginPage(page)
    checkout = CheckoutPage(page)

    # Action
    login.navigate()
    login.login("standard_user", "secret_sauce")
    
    # Add item
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    
    # Complete Checkout
    checkout.complete_checkout("Mahad", "Sultan", "46000")

    # --- GOLDEN ASSERTIONS ---
    # 1. Check the Header Text
    expect(checkout._complete_header).to_have_text("Thank you for your order!")
    
    # 2. Check the URL (Proves we moved to the right page)
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    
    # 3. Check the Cart (Proves the state changed to 'Empty')
    # Use a generic locator for the badge; it should be hidden when count is 0
    expect(page.locator(".shopping_cart_badge")).to_have_count(0)