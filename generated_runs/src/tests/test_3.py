from pages.auto_stubs import *

from pages.base_page import *  # optional

from pages.customer1_page import *  # optional

from pages.customer2_page import *  # optional

from pages.dashboard_page import *  # optional

def test_positive_add_customer(page):
    page.goto("https://preview--bank-buddy-crm-react.lovable.app/")
    click_customers(page)
    click_add_customer(page)
    enter_full_name(page, "John Doe")
    enter_email(page, "john.doe@example.com")
    enter_phone_number(page, "1234567890")
    select_account_type(page, "Standard")
    enter_address(page, "123 Main St, Anytown, USA")
    enter_occupation(page, "Software Engineer")
    enter_annual_income(page, "75000")
    enter_initial_deposit(page, "1000")
    click_add_customer(page)

def test_negative_add_customer(page):
    page.goto("https://preview--bank-buddy-crm-react.lovable.app/")
    click_customers(page)
    click_add_customer(page)
    enter_full_name(page, "John Doe")
    enter_email(page, "john.doeexample.com")
    enter_phone_number(page, "1234567890")
    select_account_type(page, "Standard")
    enter_address(page, "123 Main St, Anytown, USA")
    enter_occupation(page, "Software Engineer")
    enter_annual_income(page, "75000")
    enter_initial_deposit(page, "1000")
    click_add_customer(page)

def test_edge_add_customer(page):
    page.goto("https://preview--bank-buddy-crm-react.lovable.app/")
    click_customers(page)
    click_add_customer(page)
    enter_full_name(page, "")
    enter_email(page, "")
    enter_phone_number(page, "")
    select_account_type(page, "Standard")
    enter_address(page, "")
    enter_occupation(page, "")
    enter_annual_income(page, "")
    enter_initial_deposit(page, "")
    click_add_customer(page)
