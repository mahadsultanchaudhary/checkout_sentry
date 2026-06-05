import pytest
import os
from utils.slack_helper import send_slack_alert

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # This executes the test and gets the result
    outcome = yield
    report = outcome.get_result()

    # We only care about the 'call' phase (the actual test execution) 
    # and only if the status is 'failed'
    if report.when == "call" and report.failed:
        # Get the 'page' fixture from the test
        page = item.funcargs.get("page")
        
        if page:
            # Ensure a screenshots directory exists
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            
            screenshot_path = f"screenshots/failure_{item.name}.png"
            page.screenshot(path=screenshot_path)
            
            # Trigger the Slack alert
            try:
                send_slack_alert(item.name, screenshot_path)
                print(f"\n[Sentry] Failure detected in {item.name}. Slack notification sent.")
            except Exception as e:
                print(f"\n[Sentry] Failed to send Slack alert: {e}")