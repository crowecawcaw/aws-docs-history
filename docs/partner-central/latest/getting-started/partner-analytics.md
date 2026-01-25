# Partner Analytics Dashboard

Partner Analytics includes 8 dashboards that let you filter, sort, and drill down on the data you need to manage your ACE Opportunities and Leads, Investments, AWS-led Marketing Campaigns, and Trainings and Certifications. To navigate across dashboards within the dashboard, simply click on the desired dashboard.

The 8 dashboards are:

- [At a Glance:](partner-analytics-at-a-glance.md "partner-analytics-at-a-glance.md") Comprehensive visualization of cross-functional KPIs and critical success metrics aggregated from core operational domains.
- [Opportunities:](partner-analytics-opportunity-pipeline.md "partner-analytics-opportunity-pipeline.md") Quantitative analysis of AWS and Partner-referred opportunity flows, featuring pipeline velocity metrics, revenue forecasting models, and statistical conversion analytics.
- [Leads:](partner-analytics-lead-pipeline.md "partner-analytics-lead-pipeline.md") Systematic tracking of lead acquisition and progression, with granular conversion rate analysis and source attribution metrics.
- [Investments:](partner-analytics-funding.md "partner-analytics-funding.md") Data-driven insights into funding utilization, including claim metrics and hierarchical analysis of funding source distribution.
- [Channel:](partner-analytics-resell.md "partner-analytics-resell.md") Multi-dimensional analysis of incentive programs across Solution Provider and Distribution frameworks, incorporating CEI benefit utilization and discount mechanism performance across public sector and growth segments.
- [Marketing Campaigns:](partner-analytics-marketing.md "partner-analytics-marketing.md") Granular examination of AWS marketing initiative efficacy, with integrated lead-to-opportunity conversion modeling and funnel progression metrics.
- [Training and Certifications:](partner-analytics-training-certifications.md "partner-analytics-training-certifications.md") Quantitative assessment of organizational capability development, tracking certifications, accreditation completion rates, and training program progression metrics.

## Navigating the Partner Insights dashboards

This section describes the controls, filters, and functions of the Partner Insights dashboard.

### Filter by Date – Preset Dropdowns

The Date Filter in Partner Analytics includes two mechanisms to drill down on specific time periods – preset dropdown options based on commonly used time periods, and custom filtering to specific date ranges. Date ranges selected in this filter are automatically applied to all the metrics and tables in the dashboard, as well as to all other dashboards, unless otherwise specified.

Because some metrics in Partner Analytics and Marketplace Insights refresh at different cadences, the preset Date Filter options vary by dashboard.

- Opportunities and Leads have preset dropdown options include Past 30 days, Past 60 days, Past 90 days, Trailing 12 months (TTM), and Year to date (YTD).
- For all other dashboards, preset dropdown options include Past available 1 month, Past available 2 months, Past available 3 months, Year over year (YoY), and Year to date (YTD). Because some metrics do not refresh daily, exact "past X days" filters cannot be applied to these metrics, unlike daily refreshed KPIs. Therefore, dashboard-wide date filters in some dashboards are limited to "Past X available month(s)" dropdown options. The dashboard logic automatically applies relevant date filters to each metric, aligned to the refresh cadences of those metrics. If data is not available for the current month, the dashboard will source the next most recent month available.

### Filter by Date – Custom

In addition to the preset date filters, or set a custom date range. Note that Discounts metrics will still be shown at a monthly level. To specify exact start and end dates:

- Choose 'Custom' in the date filter dropdown menu.
- Click on the 'Start Date' search bar to open a calendar pop-up. Then, choose the desired filter start date in the calendar.
- Repeat Step 2 with the 'End Date' search bar.

**Date values for filtering by date:**

- The Opportunity date defaults to partner accepted date for AWS Referred Opportunities and Opportunity submitted date for Partner Referred Opportunities
- The Lead date tagging defaults to the created date, regardless of when the Lead was last modified.
- The Investments date defaults to Issued Credit and Redeemed Credit – Promotion Creation Date (the date on which a credit code was generated). All Cash KPIs and Approved Credit – Pre-Approved Date. Discounts follow the billing period.
- The Marketing Campaigns date defaults to campaign-associated data, the Opportunity metrics leverage Opportunity date, the Pipeline reflects Opportunity created date for AO, approval date for PO, the revenue uses Opportunity launch date, and Campaign-associated Leads metrics use Lead date.
- Training and Certifications date defaults to Net New Certification is date of when Certification was awarded for first time (does not include re-certification), Net New Accreditation uses date of course completion, and Net New Training leverages the date of course completion.
