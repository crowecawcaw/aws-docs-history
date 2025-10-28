# Performing a cost comparison

You can compare costs between any two months within the last 13 months to identify and
understand changes in your AWS spending. If you have enabled multi-year data at
monthly granularity, you can go back up to 38 months. For more information, see [Configuring multi-year and granular data](ce-configuring-data.md "ce-configuring-data.md").

###### Note

To access data in the Cost Comparison feature, you need IAM permissions. For more
information, see [Permissions](ce-cost-comparison.md#ce-cost-comparison-permissions "ce-cost-comparison.md#ce-cost-comparison-permissions").

###### To perform a detailed cost comparison

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost Explorer**.
3. In the **Report parameters** panel, choose
   **Compare**.
4. For **Date range**, choose between:
   - **Relative (Month over month)**: Compare current
     month to previous month.
   - **Absolute (Custom)**: Compare any two months within
     the last 13 months (or up to 38 months if you have enabled multi-year
     data at monthly granularity).

5. Under **Group by**, choose a **Dimension**
   (for example, Service, Linked account, Region, Tag).

###### Note

Group by resource is not available for cost comparisons. 6. Apply additional filters to narrow your analysis to specific services,
accounts, or other cost dimensions.

###### Note

Filter by resource is not available for cost comparisons. 7. View the detailed breakdown of cost changes:

    * Examine the graph and table displaying the cost comparison between the
     two selected periods.
    * Review the top 3 cost comparison drivers automatically highlighted by Cost Explorer.
     These show the most significant factors contributing to cost changes,
     whether increases or decreases.
    * Choose **View all** to see a comprehensive list of all cost comparison
     drivers.
    * For each cost comparison driver, Cost Explorer provides specific reasons for the change
     in costs, including usage changes, discount changes, and other charge
     types (for example, fees, credits).
    * Use the available Cost Explorer filters in **Report
     parameters** to analyze different aspects of your business.
     The graph and table are updated in real time, allowing you to analyze
     specific services, accounts, tags, or other dimensions to gain deeper
     insights into your cost changes.
