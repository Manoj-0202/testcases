from pages.auto_stubs import *

from pages.base_page import *  # optional

from pages.customer1_page import *  # optional

from pages.customer2_page import *  # optional

from pages.dashboard_page import *  # optional

def test_positive_add_new_customer(page):
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

def test_negative_add_new_customer(page):
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

def test_edge_add_new_customer(page):
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
