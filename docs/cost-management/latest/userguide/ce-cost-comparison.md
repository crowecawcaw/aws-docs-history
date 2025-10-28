# Comparing your costs between time periods

Cost Comparison is a feature in Cost Explorer that helps you quickly identify and understand
changes in your AWS spending. It automatically analyzes cost variations between two
selected months, highlighting the largest cost drivers and explaining the reasons behind
these changes. The feature provides both console and API access to help you analyze cost
changes across your AWS spending.

Key benefits:

- Quickly identifies top cost changes across services, accounts, and Regions.
- Provides detailed breakdowns of cost drivers, including usage and discount
  changes.
- Reduces manual cost analysis time from hours to seconds.
- Available in Cost Explorer at no additional cost.

## Permissions

To access data in the Cost Comparison feature, you need the following IAM
permissions:

- `ce:GetCostAndUsageComparisons`
- `ce:GetCostComparisonDrivers`

These permissions enable you to retrieve cost and usage comparisons and cost drivers.

## Accessing the console

To analyze your cost changes in the console, you can use either the **Top
trends** widget or Cost Explorer.

###### To access the console

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. Do either of the following:
   - On the console home page, view the **Top trends**
     widget, which shows the top 10 cost variations between the previous two
     months.
   - In the navigation pane, choose **Cost Explorer**, and
     then choose **Compare** in the **Report
     parameters** panel.

Review the **Top Trends** widget regularly to identify significant
cost changes early. For more information about this widget, see [Top trends](view-billing-dashboard.md#top-trends-widget "view-billing-dashboard.md#top-trends-widget").
