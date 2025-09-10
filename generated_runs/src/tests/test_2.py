from pages.auto_stubs import *

from pages.base_page import *  # optional

from pages.customer1_page import *  # optional

from pages.customer2_page import *  # optional

from pages.dashboard_page import *  # optional

def test_positive_add_customer(page):
    page.goto("https://preview--bank-buddy-crm-react.lovable.app/")
    click_add_customer(page)

def test_negative_add_customer(page):
    page.goto("https://preview--bank-buddy-crm-react.lovable.app/")
    click_add_customer(page)

def test_edge_add_customer(page):
    page.goto("https://preview--bank-buddy-crm-react.lovable.app/")
    click_add_customer(page)
