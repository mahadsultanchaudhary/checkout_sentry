class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self._cart_btn = page.locator(".shopping_cart_link")
        self._checkout_btn = page.locator("[data-test='checkout']")
        self._first_name = page.locator("[data-test='firstName']")
        self._last_name = page.locator("[data-test='lastName']")
        self._zip = page.locator("[data-test='postalCode']")
        self._continue_btn = page.locator("[data-test='continue']")
        self._finish_btn = page.locator("[data-test='finish']")
        self._complete_header = page.locator(".complete-header")

    def complete_checkout(self, f_name, l_name, zip_code):
        self._cart_btn.click()
        self._checkout_btn.click()
        self._first_name.fill(f_name)
        self._last_name.fill(l_name)
        self._zip.fill(zip_code)
        self._continue_btn.click()
        self._finish_btn.click()