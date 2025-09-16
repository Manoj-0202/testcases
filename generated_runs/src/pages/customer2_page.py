import asyncio
from services.page_enricher import enrich_page
from utils.enrichment_status import is_enriched




from .base_page import BasePage

class Customer2Page(BasePage):
    def __init__(self, page, page_name="customer2"):
        super().__init__(page, page_name)
        self._enriched = False

    async def _enrich_if_needed(self, force=False):
        if force or not is_enriched(self.page_name):
            await enrich_page(self.page, self.page_name)
            self._enriched = True
    async def click_close(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer2_button_close_bbd9cfda').click()

    async def verify_add_new_customer_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer2_add_new_customer_label_form_title_503bfefb').is_visible()

    async def verify_enter_the_customer_details_to_create_a_new_account_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer2_enter_the_customer_details_to_create_a_new_account._label_form_instructions_1d3264c5').is_visible()

    async def verify_full_name_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer2_full_name_label_full_name_label_0d6c9ba6').is_visible()

    async def enter_full_name_input(self, value):
        await self._enrich_if_needed()
        await self.page.smartAI('customer2_textbox_full_name_input_d1269eb5').fill(value)

    async def verify_email_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer2_email_label_email_label_14724efd').is_visible()

    async def enter_email_input(self, value):
        await self._enrich_if_needed()
        await self.page.smartAI('customer2_textbox_email_input_853239d7').fill(value)

    async def verify_phone_number_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer2_phone_number_label_phone_number_label_10af226f').is_visible()

    async def enter_phone_number_input(self, value):
        await self._enrich_if_needed()
        await self.page.smartAI('customer2_textbox_phone_number_input_55f64223').fill(value)

    async def verify_account_type_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer2_account_type_label_account_type_label_4f1b4cf7').is_visible()

    async def select_select_account_type(self, value):
        await self._enrich_if_needed()
        await self.page.smartAI('customer2_select_account_type_select_account_type_select_7191ef51').select_option(value)

    async def verify_address_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer2_address_label_address_label_bdeb8fc4').is_visible()

    async def enter_address_input(self, value):
        await self._enrich_if_needed()
        await self.page.smartAI('customer2_textbox_address_input_e960eb02').fill(value)

    async def verify_occupation_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer2_occupation_label_occupation_label_c0cb6dbb').is_visible()

    async def enter_occupation_input(self, value):
        await self._enrich_if_needed()
        await self.page.smartAI('customer2_textbox_occupation_input_856393e7').fill(value)

    async def verify_annual_income_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer2_annual_income_label_annual_income_label_a383096e').is_visible()

    async def enter_annual_income_input(self, value):
        await self._enrich_if_needed()
        await self.page.smartAI('customer2_textbox_annual_income_input_f7475565').fill(value)

    async def verify_initial_deposit_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer2_initial_deposit_label_initial_deposit_label_d47f310a').is_visible()

    async def enter_initial_deposit_input(self, value):
        await self._enrich_if_needed()
        await self.page.smartAI('customer2_textbox_initial_deposit_input_f453b59c').fill(value)

    async def click_cancel(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer2_cancel_button_cancel_0557d2eb').click()

    async def click_add_customer(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer2_add_customer_button_submit_a852831d').click()

    async def verify_navigation_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer2_navigation_label_navigation_7132ea8b').is_visible()

    async def click_dashboard(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer2_dashboard_button_navigation_e147550b').click()

    async def click_customers(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer2_customers_button_navigation_c7a70234').click()

    async def click_loans(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer2_loans_button_navigation_79c84a34').click()

    async def click_transactions(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer2_transactions_button_navigation_97d147f9').click()

    async def click_tasks(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer2_tasks_button_navigation_3d0433f8').click()

    async def click_reports(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer2_reports_button_navigation_a61bf922').click()

    async def click_analytics(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer2_analytics_button_navigation_458e43de').click()

    async def click_settings(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer2_settings_button_navigation_ae43bc74').click()