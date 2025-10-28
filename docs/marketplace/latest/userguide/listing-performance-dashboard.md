# Listing performance dashboard

The listing performance dashboard provides an overview of, and detailed data about, your
AWS Marketplace listings. The dashboard provides data about traffic volumes and the steps that
your customers take to subscribe to your products. The dashboard also provides a detailed
breakdown of traffic by marketing channels.

###### Note

- To unlock this dashboard, you must enroll the [AWS Marketplace Seller Prime](https://pages.awscloud.com/aws-marketplace-seller-prime.html "https://pages.awscloud.com/aws-marketplace-seller-prime.html") program.
- To open this dashboard, sign in to the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/ "https://aws.amazon.com/marketplace/management/"), choose **Insights**, **Marketing**,
  and then choose the **Listing performance** tab.
  For more information about using the AWS Marketplace dashboards, see [Seller dashboards](dashboards.md "dashboards.md"), earlier in this section.

###### Topics

- [Section 1: Filters](#listing-section-1-filters "#listing-section-1-filters")
- [Section 2: Date filter deep dive](#date-filter-deep-dive "#date-filter-deep-dive")
- [Section 3:  Summary metrics](#listing-summary-metrics "#listing-summary-metrics")
- [Section 4:  Monthly trend and funnel conversion](#monthly-trend-funnel "#monthly-trend-funnel")
- [Section 5: Traffic trend by channel](#traffic-trend-by-channel "#traffic-trend-by-channel")
- [Section 6: Monthly traffic and agreement
  metrics](#monthly-traffic-agreement "#monthly-traffic-agreement")
- [Section 7: Web traffic sources for unique
  visitors](#traffic-sources-unique-visitors "#traffic-sources-unique-visitors")
- [Section 8: Web traffic source breakdown](#traffic-source-breakdown "#traffic-source-breakdown")

## Section 1: Filters

You can use the following filters to refine your data.

| Control name
| Description
|
| --- | --- |
| **Product title** | The title of the product. |
| **Date** | Includes the past 30, 60, and 90 days, the trailing 12 months (TTM), and year to date (YTD). You can choose custom to define a specific start and end date. | For more information about filtering, see [Filtering data on Quick Suite](../../../quicksight/latest/user/adding-a-filter.md "../../../quicksight/latest/user/adding-a-filter.md") in the _Quick Suite User Guide_. ## Section 2: Date filter deep dive This date filter applies to all the metrics on the listing performance dashboards. For example, when you use the default year-to-date filter value, the following metrics appear:
| Metric | Description |
| --- | --- |
| **Unqiue visitors** | Number of unique individuals who have visited AWS Marketplace listing pages in YTD. |
| **New public offer agreements** | Number of agreements with public offer as offer visibility that have at least 1 active day within YTD. |
| **New unique visitors** | Number of unique individuals who have visited AWS Marketplace listing pages for the first time in YTD. |
| **Return unique visitors** | Number of unique individuals who have visited AWS Marketplace listing pages who had previously visited before the beginning of the selected year and visited again in YTD. | ## Section 3:  Summary metrics This section of the dashboard displays a summary visualization of your traffic and public offer agreements. Key peformance indicatrs (KPIs) include the number of unique visitors, the number of new public offer agreements, the number of new unique visitors, and the number of return unique visitors. You can see the year-over-year or period-over-period changes in volume and percentage. You can update the date range by updating the date criteria in the date field in the filter section.
| Metrics | Description |
| --- | --- |
| **Unique visitors** | Number of unique individuals who have visited AWS Marketplace listing pages. |
| **Agreement** | A contract signed between a proposer (product or service owner) and an accepter (customer) to start using a product. |
| **New public offer agreements** | Number of agreements with public offer as offer visibility that have acceptance date within the selected date range. include status being active, expired, cancelled, and terminated. |
| **Status** | **Active** - Some or all of the terms of the agreement are in-force. **Expired** - The agreement ended on its pre-agreed end date. **Canceled** - The acceptor chooses to end the agreement prior to its end date. **Terminated** - The agreement ended before its pre-agreed end date due to an AWS-initiated termination event, such as a payment failure. **Renewed** - The agreement was renewed into a new agreement using functionality such as auto-renewal. **Replaced** - The agreement was replaced using a replacement offer. | ## Section 4:  Monthly trend and funnel conversion This section of the dashboard provides traffic and agreement trends for a specified date range. Key performance indicators include the number of unique visitors and the number of new agreements, referring to the new public offer agreements. **Unique visitor by month -** provides the monthly view for the number of unique visitors. The total of monthly unique visitors can be more than the total unique visitors in the summary metric section as one unique visitor can visit multiple months. **New agreements by month -** provides the monthly view for the number of new public offer agreements. **Funnel conversion -** provides the step-by-step conversion view. It includes listing page, procurement page, configuration page and fulfillment page. You can select unique visitors, page views and unique accounts as what the bars show as. When you hover over each bar, you can see the conversion percentage defined as the current bar’s value as a percentage of previous bar.
| Metrics | Description |
| --- | --- |
| **Unique visitors** | Number of unique individuals who have visited AWS Marketplace listing pages. |
| **Page views** | Number of visits to a AWS Marketplace listing page. |
| **Unique accounts** | Number of unique AWS account ID associated with a visitor. This metric is only applicable after a visitor authenticates. | ## Section 5: Traffic trend by channel This section of the dashboard provides a deep dive into monthly traffic trend. You can select unique visitors and page views as what the bars show as. You can select a single channel or multiple ones in the channel filter to see the monthly trend for the selected channel(s). ## Section 6: Monthly traffic and agreement metrics This section of the dashboard provides a monthly view for unique visitors, new agreements, conversion rate and total agreements. Conversion rate is defined as new agreements divided by unique visitors for each month. The data in the table represents an entire month, even if you select date range for a partial month. For example, if you filter the data to display the period from January 15, 2024 to March 15, 2024, the table will still include the complete monthly data for January 1, 2024 through March 31, 2024. The data in the table is sorted by **Month**, with the most recent month displayed first. You can choose to sort the table by any of the available columns by clicking on the corresponding column header with the option to sort the data in either ascending or descending order. ## Section 7: Web traffic sources for unique visitors This section of the dashboard provides deep dives into unique visitors by marketing sources. The categories include seller organic discovery, seller-led marketing campaigns, AWS organic discovery, and AWS-led campaigns. Those categories are identified by the tracking codes associated with the visitor or visit.
| Traffic source | Description |
| --- | --- |
| Seller organic discovery | Unique visitors who arrive at your listings through calls to action and points of discovery on your website or in-app notifications. |
| Seller-led marketing campaigns | Unique visitors who arrive at your listings through your paid advertising or promotional channels. |
| AWS organic discovery | Unique visitors who arrive at your listings through AWS channels, such as organic AWS website traffic, AWS console(s) search, and AWS Marketplace search. |
| AWS marketing campaigns | Unique visitors who arrive at your listings through AWS-led campaigns and paid promotions. | ## Section 8: Web traffic source breakdown Web traffic source breakdown table provides the granular breakdown of marketing activities that drive the traffic. <br>• **Traffic source** - Includes AWS-led and seller-led as two main categories. <br>• **Traffic type** - Includes seller organic discovery, seller-led marketing campaigns, AWS organic discovery and AWS-led marketing campaigns. <br>• **Channel** - Includes the various marketing tactics, which are paid display, paid search, paid social media, email, organic, internal site traffic external links and other. <br>• **Publisher** - Refers to the entity where the campaign is published, including Facebook, Google, LinkedIn, AWS, Seller-led. and others. <br>• **Promotion** - Refers to the specific campaign for which a dedicated tracking code has been generated. An example can be `psm_linked_post_free-trial-global-ver-a`.
| Metrics | Description |
| --- | --- |
| Attributed agreements | Total agreements contributed by the visits for each promotion. |
| Conversion rate | Attributed agreements divided by unique visitors for each promotion. |
