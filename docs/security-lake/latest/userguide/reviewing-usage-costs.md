# Reviewing Security Lake usage and estimated costs

The **Usage** page of the Amazon Security Lake console lets you review your current Security Lake usage, as well as
future usage and cost estimates. If you’re currently participating in a 15-day free trial, your
usage during the trial can help you estimate your costs for using Security Lake after your free trial ends. For
an overview of Security Lake pricing, see [How Security Lake pricing is determined](estimating-costs.md "estimating-costs.md"). For detailed information
and cost examples, see [Amazon Security Lake Pricing](https://aws.amazon.com/security-lake/pricing/ "https://aws.amazon.com/security-lake/pricing/").

In Security Lake, estimated usage costs are reported in US Dollars and apply only to the current
AWS Region. The costs cover Security Lake usage by all accounts in your organization and include conversion to the
Open Cybersecurity Schema Framework (OCSF) and Apache Parquet format. However, the predicted costs don't
include costs for other services that Security Lake works with, such as Amazon Simple Storage Service (Amazon S3) and AWS Glue.

On the **Usage** page, you choose a time period for which to view usage and cost data. The default time period
is the last 1 calendar day. You must have at least 1 day of Security Lake usage to see cost projections.

The top of the page shows the **Projected cost for all accounts**. This is your predicted Security Lake cost
in the current AWS Region for the next 30 calendar days based on your actual usage during the selected time frame. The actual usage and predicted cost reflects all accounts
in your organization.

On the remainder of the page, the usage and cost data is divided into two tables as follows:

- **Usage and cost by source** – This is your current Security Lake usage broken down by
  data source, as well as estimated usage and costs for the next 30 calendar days based on your actual usage during the
  selected time frame. The actual usage, predicted usage, and predicted cost reflect all accounts in
  your organization. If you select a source, a split panel opens which shows which accounts generated logs and events from that
  source. For each account, the split panel includes both actual usage from that source and predicted usage and costs.
- **Usage and cost by account** – This is your current Security Lake usage broken down by
  account, as well as estimated usage and costs for the next 30 calendar days based on your actual usage during the
  selected time frame. If you select an account, a split panel opens which shows the sources that contributed to that account's
  usage. For each contributing source, the split panel includes both actual usage and predicted usage and costs.
  All supported AWS data sources appear in the preceding tables, even if you haven't added a particular source in
  Security Lake. We recommend adding all AWS sources if you're participating in the free trial to get cost
  estimates for your full set of logs and events. For instructions on adding an AWS source, see [Collecting data from AWS services in Security Lake](internal-sources.md "internal-sources.md"). Custom sources aren't included in usage or cost calculations.

Follow these steps to review your usage and cost data in the Security Lake console.

###### To review Security Lake usage and predicted costs (console)

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/").
2. By using the AWS Region selector in the upper-right corner of the page, select the
   Region in which you want to review your usage and costs.
3. In the navigation pane, choose **Settings** and then **Usage**.
4. Select the time period for which you want to see usage and cost data. The default is the last 1 day.
5. Select the **By data source** or **By accounts** tab to review usage and costs
   in detail.
