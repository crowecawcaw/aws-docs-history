# Using the AWS Billing and Cost Management home page

Use the Billing and Cost Management home page for an overview of your AWS cloud financial management data and
to help you make faster and more informed decisions. Understand high-level cost trends and
drivers, quickly identify anomalies or budget overruns which require your attention, review
recommended actions, understand cost allocation coverage, and identify savings
opportunities.

The data on this page comes from AWS Cost Explorer. If you haven’t used Cost Explorer before, it’s
_automatically_ enabled for you once you visit this page. It can take up to 24 hours
for your data to appear on this page. When available, your data will be refreshed at
least once every 24 hours. The Cost Explorer data on the home page is tailored for
analytical purposes. This means the data can differ from your invoices and the
**Bills** page due to differences in how data is grouped into
AWS services; how discounts, credits, refunds, and taxes are displayed; differences in
timing for the current month's estimated charges; and rounding.

For more information, see [Knowing the differences
between Billing and Cost Explorer data](differences-billing-data-cost-explorer-data.md "differences-billing-data-cost-explorer-data.md").

For more information about AWS Cloud Financial Management, see the [Getting started](https://console.aws.amazon.com/costmanagement/home?#/getting-started "https://console.aws.amazon.com/costmanagement/home?#/getting-started") page in the AWS Billing and Cost Management console. You can choose a topic and then follow the links to that specific console page or the documentation.

## Managing Billing and Cost Management widgets

You can customize how the widgets appear by moving or resizing the widgets.

###### To manage the Billing and Cost Management widgets

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement](https://console.aws.amazon.com/costmanagement/home "https://console.aws.amazon.com/costmanagement/home").
2. (Optional) To customize the Billing and Cost Management home page, drag and drop a widget to move it,
   or change the widget size.
3. To take action on each recommendation or to learn more, review the data in the
   widget and then follow the links in the widget.
4. To reset the layout, choose **Reset layout** and then choose
   **Reset**.

You can use the following widgets:

- [Cost summary](#cost-summary-widget "#cost-summary-widget")
- [Cost monitor](#cost-monitor-widget "#cost-monitor-widget")
- [Cost breakdown](#cost-breakdown-widget "#cost-breakdown-widget")
- [Recommended actions](#recommended-actions-widget "#recommended-actions-widget")
- [Savings opportunities](#savings-opportunities-widget "#savings-opportunities-widget")
- [Top trends](#top-trends-widget "#top-trends-widget")

## Cost summary

The cost summary widget provides a quick view of your current cost trends compared to
your spending in the last month.

To view your month-to-date estimated charges on the **Bills** page,
choose **View bill**.

All metrics shown in the cost summary widget exclude credits and refunds. This means
you might see different numbers on the home page compared to the
**Bills** page or your invoices. The widget shows the following
metrics that you can choose to view in Cost Explorer:

- **Month-to-date cost** – Your estimated costs for the
  current month. The trend indicator compares the current month's costs to last
  month's cost for the same time period.
- **Last month's cost for same time period** – Your
  costs for last month, for the same time period. For example, if today is
  February 15, the widget also shows last month's cost for January
  1–15.

###### Note

Trend calculations might be influenced by the number of days in each
month. For example, on July 31, the trend indicator will look at costs from
July 1–31 and compare it to costs for June 1–30.

- **Total forecasted cost for current month** – A
  forecast of your estimated total costs for the current month.
- **Last month's total cost** – The total costs for
  last month. For more information, choose each metric to view the costs in Cost Explorer,
  or choose **View bill** to view your month-to-date estimated
  charges on the **Bills** page.

###### Note

The metrics in this widget exclude credits and refunds. The costs here
might differ from the costs on the **Bills** page or your
invoices.

For more information about Cost Explorer, see [Forecasting with Cost Explorer](../../../cost-management/latest/userguide/ce-forecast.md "../../../cost-management/latest/userguide/ce-forecast.md").

## Cost monitor

This widget provides a quick view of your cost and usage budgets and any cost
anomalies that AWS detected, so that you can fix it.

- **Budgets status** – Alerts you if any of your cost and
  usage budgets were exceeded.

The status can be the following:

- **OK** – Cost and usage budgets haven't been
  exceeded.
- **Over budget** – A cost and usage budget has been
  exceeded. Your actual cost is greater than 100%. The number of exceeded
  budgets and a warning icon will appear.
- **Setup required** – You haven't created any cost
  and usage budgets.

Choose the status indicator to go to the **Budgets** page to review
details of each budget or to create one. The budgets status indicator only shows
information about cost and usage budgets. Budgets that you created to track the coverage
or utilization of your Savings Plans or reservations won't appear in this widget. Cost
anomalies status alerts you if AWS detected any anomalies with your costs since the
first day of the current month. The status can be the following:

- **OK** – Cost anomalies haven't been detected in
  the current month.
- **Anomalies detected** – A cost anomaly has been
  detected. The number of anomalies detected and a warning icon will appear.
- **Setup required** – You haven't created any
  anomaly detection monitors.

Choose the status indicator to go to the **Cost Anomaly Detection** page to review
details of each anomaly detected, or to create an anomaly detection monitor. The cost
anomalies status indicator only displays information about cost anomalies detected in
the current month. To view your full anomaly history, go to the
**Cost Anomaly Detection** page.

For more information about budgets, see [Managing your costs with AWS Budgets](../../../cost-management/latest/userguide/budgets-managing-costs.md "../../../cost-management/latest/userguide/budgets-managing-costs.md").

For more information about anomaly detection monitors, see [Detecting unusual spend with
AWS Cost Anomaly Detection](../../../cost-management/latest/userguide/manage-ad.md "../../../cost-management/latest/userguide/manage-ad.md").

## Cost breakdown

This widget provides a breakdown of your costs for the last six months, so you can
understand cost trends and drivers. To break down your costs, choose an option from the
dropdown list:

- Service
- AWS Region
- Member account (for AWS Organizations management accounts)
- Cost allocation tag
- Cost category

If you choose cost category or cost allocation tag key, hover over the chart to see
the values.

To dive deeper into your cost and usage, choose **Analyze your costs in
Cost Explorer**. Use Cost Explorer to visualize, group, and filter your costs and usage, with
additional dimensions, such as Availability Zone, instance type, and database engine.

For more information about Cost Explorer, see [Exploring your data
using Cost Explorer](../../../cost-management/latest/userguide/ce-exploring-data.md "../../../cost-management/latest/userguide/ce-exploring-data.md").

## Recommended actions

This widget helps you implement AWS cloud financial management best practices and
optimize your costs. It displays your recommended actions, ranked by priority.
Critical alerts appear at the top, followed by advisory warnings and informational recommended actions.

As a best practice, we recommend that you monitor any critical alerts daily, focusing on immediate actions
like payment issues or budget overruns. Review any advisory warnings on a weekly basis.

###### To use the recommended actions widget

1. For each recommendation, follow the link to take action on your account. By default, the widget shows up to four recommended actions.
2. To load additional recommended actions, choose **Load more
   actions**.
3. To dismiss a non-critical recommended action, choose the **X** icon
   on the top right corner. Critical alerts remain visible until addressed. Dismissed non-critical recommended actions will reappear after 7 days.

###### Note

You will need IAM permissions to the AWS service in order to see the recommended actions. For example, if you have access to all Billing and Cost Management actions except `budgets:DescribeBudgets`, you can view all recommendations on the page except for budgets. See the error message about adding the missing IAM action to your policy.

You will need the new IAM permission `bcm-recommended-actions:ListRecommendedActions` to view all recommended actions. For more information, see [Understanding recommended action types](../../../cost-management/latest/userguide/recommended-action-types.md "../../../cost-management/latest/userguide/recommended-action-types.md").

For a full list of the different recommended action types and the corresponding IAM policy permissions needed in order to see the recommended actions, refer to [Billing and Cost Management recommended actions policies](../../../cost-management/latest/userguide/billing-permissions-ref.md#allows-recommended-actions-access "../../../cost-management/latest/userguide/billing-permissions-ref.md#allows-recommended-actions-access").

For full details on the categorization of recommended actions, see [Understanding recommended action types](../../../cost-management/latest/userguide/recommended-action-types.md "../../../cost-management/latest/userguide/recommended-action-types.md").

## Cost allocation coverage

To create cost visibility and accountability in your organization, it's important to
allocate costs to teams, applications, environments, or other dimensions. This widget
shows unallocated costs for your cost categories and cost allocation tags, so that you
can identify where to take action to organize your costs.

Cost allocation coverage is defined as the percentage of your costs that don't have a
value assigned to the cost category or cost allocation tag keys that you've created.

###### Example

- Your month-to-date spend is $100, and you created a cost category (named
  _Teams_) to organize costs by individual teams.
- You have $40 in the _Team A_ cost category value, $35
  in the _Team B_ cost category value, and $25 that are
  unallocated.
- In this case, your cost allocation coverage is 25/100 = 25%.

A lower unallocated cost metric means that your costs are properly allocated along the
dimensions important to your organization. For more information, see [Building a cost allocation strategy](../../../whitepapers/latest/tagging-best-practices/building-a-cost-allocation-strategy.md "../../../whitepapers/latest/tagging-best-practices/building-a-cost-allocation-strategy.md") in the
_Best Practices for Tagging AWS Resources_ whitepaper.

This widget compares the month-to-date unallocated cost percentage to all of last
month's unallocated cost percentage. The widget shows up to five cost allocation tag
keys or five cost categories. If you have more than five of either cost allocation tag
keys or cost categories, use the widget preferences to specify the ones that you
want.

To analyze your unallocated costs in more detail by using Cost Explorer, choose the cost
category or cost allocation name.

To improve cost allocation coverage for your cost categories or cost allocation tags,
you can edit your cost category rules or improve resource tagging by using AWS Tag
Editor.

For more information, see the following topics:

- [Managing
  your costs with AWS cost categories](manage-cost-categories.md "manage-cost-categories.md")
- [Using AWS cost
  allocation tags](cost-alloc-tags.md "cost-alloc-tags.md")
- [Using Tag Editor](../../../tag-editor/latest/userguide/tag-editor.md "../../../tag-editor/latest/userguide/tag-editor.md")

## Savings opportunities

This widget shows recommendations from Cost Optimization Hub to help you save money and lower your
AWS bill. This can include:

- Deleting unused resources
- Rightsizing over-provisioned resources
- Purchasing Savings Plans or reservations

For each savings opportunity, the widget shows your estimated monthly savings. Your
estimated savings are _de-duplicated_ and
_automatically_ adjusted for each recommended savings
opportunity.

###### Example

- Let's say that you have two Amazon EC2 instances,
  `InstanceA` and
  `InstanceB`.
- If you purchased a Savings Plan, you could reduce the cost for
  `InstanceA` by $20 and the cost of
  `InstanceB` by $10, for a total of $30 savings.
- However, if `InstanceB` is idle, the widget might
  recommend that you terminate it instead of purchasing a Savings Plan. The
  savings opportunity would tell you how much you could save by terminating
  the idle `InstanceB`.

To view the savings opportunities in this widget, you can opt in by visiting the Cost Optimization Hub
page or using the [Cost
Management preferences](https://console.aws.amazon.com/cost-management/home?#/settings "https://console.aws.amazon.com/cost-management/home?#/settings") page.

## Top trends

This widget provides a quick overview of your most significant cost changes between the previous two months.

- Shows the top 10 cost variations, sorted by absolute dollar difference
- Displays both percentage and absolute value changes
- Highlights specific services, accounts, or Regions where changes occurred
- Allows you to choose any trend to analyze it further in Cost Explorer's Compare view

To dive deeper into your cost trends, choose **View your cost trends in Cost Explorer**.

For more information about comparing costs, see [Comparing your costs between time periods](../../../cost-management/latest/userguide/ce-cost-comparison.md "../../../cost-management/latest/userguide/ce-cost-comparison.md").

## Understanding the Billing dashboard

###### Note

You can access the previous version of the **Billing** home page
from the **Legacy Pages** section of the navigation pane.

You can use the dashboard page of the AWS Billing console to gain a general
view of your AWS spending. You can also use it to identify your highest cost
service or Region and view trends in your spending over the past few months. You
can use the dashboard page to see various breakdowns of your AWS usage. This
is especially useful if you're a Free Tier user. To view more details about your
AWS costs and invoices, choose **Billing details** in the
left navigation pane. You can customize your dashboard layout at any time by
choosing the gear icon at the top of the page to match your use case.

Viewing your AWS costs in the AWS Billing console dashboard doesn't
require turning on Cost Explorer. To turn on Cost Explorer to access
additional views of your cost and usage data, see [Enabling
AWS Cost Explorer](../../../cost-management/latest/userguide/ce-enable.md "../../../cost-management/latest/userguide/ce-enable.md").

###### To open the AWS Billing console and dashboard

- Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
  [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
  By default, the console shows the **AWS Billing Dashboard**
  page.

#### Understanding your dashboard

page

Your AWS Billing console dashboard contains the following sections. To
create your preferred layout, drag and drop sections of the**Dashboard** page. To customize the visible sections and layout,
choose the gear icon at the top of the page. These preferences are stored
for ongoing visits to the **Dashboard** page. To
temporarily remove sections from your view, choose the `x` icon
for each section. To make all sections visible, choose refresh at the top of
the page.

**AWS summary**

This section is an overview of your AWS costs across all
accounts, AWS Regions, service providers, and services, and
other KPIs. **Total compared to prior period**
displays your total AWS costs for the most recent closed
month. It also provides a comparison to your total forecasted
costs for the current month. Choose the gear icon on the card to
decide which KPIs you want to display.

**Highest cost and usage details**

This section shows your top service, account, or AWS Region
by estimated month-to-date (MTD) spend. To choose which to view,
choose the gear icon on the top right.

**Cost trend by top five services**

In this section, you can see the cost trend for your top five
services for the most recent three to six closed billing
periods.

You can choose between chart types and time periods on the top
of the section. You can adjust additional preferences using the
gear icon.

The columns provide the following information:

- **Average**: The average cost over
  the trailing three months.
- **Total**: The total for the most
  recent closed month.
- **Trend**: Compares the
  **Total** column with the
  **Average** column.

**Account cost trend**

This section shows the cost trend for your account for the
most recent three to six closed billing periods. If you're a
management account of AWS Organizations, the **cost trend by top
five section** shows your top five AWS accounts
for the most recent three to six closed billing periods. If
invoices weren't already issued, the data isn't visible in this
section.

You can choose between chart types and time periods on the top
of the section. Adjust additional preferences using the gear
icon.

The columns provide the following information:

- **Average**: The average cost over
  the trailing three months.
- **Total**: The total for the most
  recent closed month.
- **Trend**: Compares the
  **Total** column with the
  **Average** column.

On the dashboard, you can view the following graphs:

- **Spend Summary**
- **Month-to-Date Spend by Service**
- **Month-to-Date Top Services by Spend**

**Spend Summary**

The **Spend Summary** graph shows you how
much you spent last month, the estimated costs of your AWS
usage for the month-to-date, and a forecast for how much you are
likely to spend this month. The forecast is an estimate that's
based on your past AWS costs. Therefore, your actual monthly
costs might not match the forecast.

**Month-to-Date Spend by
Service**

The **Month-to-Date Spend by Service** graph
shows the top services that you use most and the proportion of
your costs that service contributed to. The
**Month-to-Date Spend by Service** graph
doesn't include forecasting.

**Month-to-Date Top Services by
Spend**

The **Month-to-Date Top Services by Spend**
graph shows the services that you use most, along with the costs
incurred for the month to date. The **Month-to-Date Top
Services by Spend** graph doesn't include
forecasting.

###### Note

The Billing and Cost Management console has a refresh time of approximately 24 hours to
reflect your billing data.
