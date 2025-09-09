import asyncio
from services.page_enricher import enrich_page
from utils.enrichment_status import is_enriched




from .base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page, page_name="dashboard"):
        super().__init__(page, page_name)
        self._enriched = False

    async def _enrich_if_needed(self, force=False):
        if force or not is_enriched(self.page_name):
            await enrich_page(self.page, self.page_name)
            self._enriched = True
    async def verify_navigation_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_label_navigation_e89cbf2f').is_visible()

    async def click_dashboard(self):
        await self._enrich_if_needed()
        await self.page.smartAI('dashboard_dashboard_button_navigation_83914516').click()

    async def click_customers(self):
        await self._enrich_if_needed()
        await self.page.smartAI('dashboard_customers_button_navigation_bb4303b6').click()

    async def click_loans(self):
        await self._enrich_if_needed()
        await self.page.smartAI('dashboard_loans_button_navigation_42436e2a').click()

    async def click_transactions(self):
        await self._enrich_if_needed()
        await self.page.smartAI('dashboard_transactions_button_navigation_f0479a72').click()

    async def click_tasks(self):
        await self._enrich_if_needed()
        await self.page.smartAI('dashboard_tasks_button_navigation_cde2a4d6').click()

    async def click_reports(self):
        await self._enrich_if_needed()
        await self.page.smartAI('dashboard_reports_button_navigation_578fb659').click()

    async def click_analytics(self):
        await self._enrich_if_needed()
        await self.page.smartAI('dashboard_analytics_button_navigation_49884ab5').click()

    async def click_settings(self):
        await self._enrich_if_needed()
        await self.page.smartAI('dashboard_settings_button_navigation_7a36fd5d').click()

    async def enter_search_customers_loans_transactions(self, value):
        await self._enrich_if_needed()
        await self.page.smartAI('dashboard_search_customers,_loans,_transactions..._textbox_search_3310a968').fill(value)

    async def verify_dashboard_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_dashboard_label_page_title_a353b4f0').is_visible()

    async def verify_welcome_back_here_s_your_banking_overview_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_welcome_back!_heres_your_banking_overview._label_welcome_message_479a4097').is_visible()

    async def verify_total_customers_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_total_customers_label_total_customers_228048fb').is_visible()

    async def verify_2_847_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_2,847_label_total_customers_value_6d9c1e09').is_visible()

    async def verify_12_5_from_last_month_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_+12.5%_from_last_month_label_total_customers_change_3fa8cc36').is_visible()

    async def verify_active_loans_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_active_loans_label_active_loans_3dfc1d95').is_visible()

    async def verify_45_2m_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_$45.2m_label_active_loans_value_e93e7652').is_visible()

    async def verify_8_2_from_last_month_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_+8.2%_from_last_month_label_active_loans_change_60884863').is_visible()

    async def verify_monthly_transactions_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_monthly_transactions_label_monthly_transactions_914c549d').is_visible()

    async def verify_18_394_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_18,394_label_monthly_transactions_value_fc666ffb').is_visible()

    async def verify_15_3_from_last_month_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_+15.3%_from_last_month_label_monthly_transactions_change_4afb9cb3').is_visible()

    async def verify_revenue_growth_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_revenue_growth_label_revenue_growth_bfb3b4b4').is_visible()

    async def verify_4_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_4%_label_revenue_growth_value_de36ce03').is_visible()

    async def verify_2_1_from_last_month_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_+2.1%_from_last_month_label_revenue_growth_change_fa8c15eb').is_visible()

    async def click_export_report(self):
        await self._enrich_if_needed()
        await self.page.smartAI('dashboard_export_report_button_export_ed26f6d4').click()

    async def verify_loan_portfolio_trend_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_loan_portfolio_trend_label_loan_portfolio_trend_16637d4f').is_visible()

    async def verify_monthly_loan_disbursements_over_the_last_6_months_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_monthly_loan_disbursements_over_the_last_6_months_label_loan_portfolio_info_f2592b48').is_visible()

    async def verify_customer_distribution_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_customer_distribution_label_customer_distribution_28babd8d').is_visible()

    async def verify_customer_segments_by_account_type_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_customer_segments_by_account_type_label_customer_distribution_info_737296be').is_visible()

    async def verify_premium_35_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_premium_35%_label_premium_segment_a6240e39').is_visible()

    async def verify_standard_45_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_standard_45%_label_standard_segment_ddbf0b0b').is_visible()

    async def verify_basic_20_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_basic_20%_label_basic_segment_6072a081').is_visible()

    async def verify_edit_with_visible(self):
        await self._enrich_if_needed()
        assert await self.page.smartAI('dashboard_edit_with_label_edit_info_ab3b756e').is_visible()

    async def click_lovable(self):
        await self._enrich_if_needed()
        await self.page.smartAI('dashboard_lovable_button_edit_tool_2de51406').click()