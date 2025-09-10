import asyncio
from services.page_enricher import enrich_page
from utils.enrichment_status import is_enriched




from .base_page import BasePage

class Customer1Page(BasePage):
    def __init__(self, page, page_name="customer1"):
        super().__init__(page, page_name)
        self._enriched = False

    async def _enrich_if_needed(self, force=False):
        if force or not is_enriched(self.page_name):
            await enrich_page(self.page, self.page_name)
            self._enriched = True
    async def click_dashboard(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer1_dashboard_button_navigation_82dbfff5').click()

    async def click_customers(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer1_customers_button_navigation_2ff369e0').click()

    async def click_loans(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer1_loans_button_navigation_5a9a4dac').click()

    async def click_transactions(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer1_transactions_button_navigation_ccd4781d').click()

    async def click_tasks(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer1_tasks_button_navigation_ae9b969a').click()

    async def click_reports(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer1_reports_button_navigation_c61e04cf').click()

    async def click_analytics(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer1_analytics_button_navigation_d6270176').click()

    async def click_settings(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer1_settings_button_navigation_0688b7c5').click()

    async def enter_search_customers_loans_transactions(self, value):
        await self._enrich_if_needed()
        await self.page.smartAI('customer1_search_customers,_loans,_transactions..._textbox_search_cc811d8f').fill(value)

    async def enter_search_customers(self, value):
        await self._enrich_if_needed()
        await self.page.smartAI('customer1_search_customers..._textbox_search_0ce074e6').fill(value)

    async def click_filters(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer1_filters_button_filter_098e0703').click()

    async def verify_customers_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_customers_label_section_title_f56ded30').is_visible()

    async def verify_manage_your_customer_relationships_and_accounts_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_manage_your_customer_relationships_and_accounts_label_section_info_c0244772').is_visible()

    async def click_export(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer1_export_button_export_00f1dc0b').click()

    async def click_add_customer(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer1_add_customer_button_add_customer_f1b20083').click()

    async def verify_customer_list_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_customer_list_label_section_title_194ada63').is_visible()

    async def verify_3_customers_found_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_3_customers_found_label_info_5a0b87ef').is_visible()

    async def verify_customer_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_customer_label_column_title_cd55415b').is_visible()

    async def verify_account_type_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_account_type_label_column_title_03904455').is_visible()

    async def verify_balance_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_balance_label_column_title_66a19f46').is_visible()

    async def verify_status_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_status_label_column_title_a924671a').is_visible()

    async def verify_join_date_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_join_date_label_column_title_24492d13').is_visible()

    async def verify_actions_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_actions_label_column_title_7a76e079').is_visible()

    async def verify_sarah_johnson_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_sarah_johnson_label_customer_name_da4b3002').is_visible()

    async def verify_sarah_johnson_email_com_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_sarah.johnson@email.com_label_customer_email_53ef345e').is_visible()

    async def verify_premium_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_premium_label_account_type_b5143443').is_visible()

    async def verify_1_45_000_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_$1,45,000_label_balance_b240e584').is_visible()

    async def verify_active_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_active_label_status_08668054').is_visible()

    async def verify_2023_01_15_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_2023-01-15_label_join_date_493fe85d').is_visible()

    async def verify_michael_chen_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_michael_chen_label_customer_name_026b1392').is_visible()

    async def verify_michael_chen_email_com_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_michael.chen@email.com_label_customer_email_098ef835').is_visible()

    async def verify_standard_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_standard_label_account_type_8be36523').is_visible()

    async def verify_52_000_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_$52,000_label_balance_12f41cbc').is_visible()

    async def verify_2023_03_22_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_2023-03-22_label_join_date_f22573a4').is_visible()

    async def verify_emma_davis_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_emma_davis_label_customer_name_90873718').is_visible()

    async def verify_emma_davis_email_com_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_emma.davis@email.com_label_customer_email_2a2a78a7').is_visible()

    async def verify_89_000_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_$89,000_label_balance_db9a0a52').is_visible()

    async def verify_2022_11_08_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_2022-11-08_label_join_date_6963bb97').is_visible()

    async def verify_john_doe_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('customer1_john_doe_label_user_info_fe8e3db3').is_visible()

    async def click_edit_with_lovable(self):
        await self._enrich_if_needed()
        await self.page.smartAI('customer1_edit_with_lovable_button_edit_tool_b6e313c0').click()