import sys, os, time
from pathlib import Path
from playwright.sync_api import sync_playwright

_THIS = Path(__file__).resolve()
_SRC_ROOT = _THIS.parents[1]
if str(_SRC_ROOT) not in sys.path: sys.path.insert(0, str(_SRC_ROOT))
from pages.auto_stubs import *
try:
    from pages.base_page import *
except Exception:
    pass
try:
    from pages.customer1_page import *
except Exception:
    pass
try:
    from pages.customer2_page import *
except Exception:
    pass
try:
    from pages.dashboard_page import *
except Exception:
    pass
def run_positive_add_new_customer():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=(os.getenv("UI_RUNNER_HEADLESS","false").lower()=="true"),
                                    slow_mo=int(os.getenv("UI_RUNNER_SLOWMO","0") or "0"))
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://preview--bank-buddy-crm-react.lovable.app/")
        click_customer(page)
        click_new_customer(page)
        enter_full_name(page, "John Doe")
        enter_email(page, "johhn.doe@example.com")
        enter_address(page, "123 Main ST, Anytown, ZUZSA")
        enter_occupation(page, "Software Engineer")
        enter_annual_income(page, "75000")
        enter_initial_deposit(page, "1000")
        click_add_new_customer(page)
        linger_after_success(page)
        if os.getenv("UI_RUNNER_AUTOCLOSE","1") == "1":
            context.close(); browser.close()

def run_negative_add_new_customer():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=(os.getenv("UI_RUNNER_HEADLESS","false").lower()=="true"),
                                    slow_mo=int(os.getenv("UI_RUNNER_SLOWMO","0") or "0"))
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://preview--bank-buddy-crm-react.lovable.app/")
        click_customer(page)
        click_new_customer(page)
        enter_full_name(page, "John Doe")
        enter_email(page, "johhn.doeexample.com")
        enter_address(page, "123 Main ST, Anytown, ZUZSA")
        enter_occupation(page, "Software Engineer")
        enter_annual_income(page, "75000")
        enter_initial_deposit(page, "1000")
        click_add_new_customer(page)
        linger_after_success(page)
        if os.getenv("UI_RUNNER_AUTOCLOSE","1") == "1":
            context.close(); browser.close()

def run_edge_add_new_customer():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=(os.getenv("UI_RUNNER_HEADLESS","false").lower()=="true"),
                                    slow_mo=int(os.getenv("UI_RUNNER_SLOWMO","0") or "0"))
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://preview--bank-buddy-crm-react.lovable.app/")
        click_customer(page)
        click_new_customer(page)
        enter_full_name(page, "")
        enter_email(page, "")
        enter_address(page, "")
        enter_occupation(page, "")
        enter_annual_income(page, "")
        enter_initial_deposit(page, "")
        click_add_new_customer(page)
        linger_after_success(page)
        if os.getenv("UI_RUNNER_AUTOCLOSE","1") == "1":
            context.close(); browser.close()

if __name__ == '__main__':
    run_positive_add_new_customer()
    run_negative_add_new_customer()
    run_edge_add_new_customer()
