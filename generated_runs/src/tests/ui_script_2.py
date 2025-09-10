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
def run_positive_add_customer():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=(os.getenv("UI_RUNNER_HEADLESS","false").lower()=="true"),
                                    slow_mo=int(os.getenv("UI_RUNNER_SLOWMO","0") or "0"))
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://preview--bank-buddy-crm-react.lovable.app/")
        click_add_customer(page)
        linger_after_success(page)
        if os.getenv("UI_RUNNER_AUTOCLOSE","1") == "1":
            context.close(); browser.close()

def run_negative_add_customer():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=(os.getenv("UI_RUNNER_HEADLESS","false").lower()=="true"),
                                    slow_mo=int(os.getenv("UI_RUNNER_SLOWMO","0") or "0"))
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://preview--bank-buddy-crm-react.lovable.app/")
        click_add_customer(page)
        linger_after_success(page)
        if os.getenv("UI_RUNNER_AUTOCLOSE","1") == "1":
            context.close(); browser.close()

def run_edge_add_customer():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=(os.getenv("UI_RUNNER_HEADLESS","false").lower()=="true"),
                                    slow_mo=int(os.getenv("UI_RUNNER_SLOWMO","0") or "0"))
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://preview--bank-buddy-crm-react.lovable.app/")
        click_add_customer(page)
        linger_after_success(page)
        if os.getenv("UI_RUNNER_AUTOCLOSE","1") == "1":
            context.close(); browser.close()

if __name__ == '__main__':
    run_positive_add_customer()
    run_negative_add_customer()
    run_edge_add_customer()
