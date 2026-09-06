

# Understanding how a cost comparison works
<a name="ce-understand-cost-comparison"></a>

You can use Cost Comparison to quickly understand your cloud spending by automatically identifying and unfolding the largest cost drivers driving the cost variations between two selected months. Cost Comparison provides a detailed breakdown for these cost variances, from usage shifts to changes in commitment-based discounts like Savings Plans coverage and applied credits, eliminating hours of manual investigation.

The **Top trends** widget on the console home page automatically applies Cost Comparison to show the top cost changes across your services, accounts, and Regions. For more information about this widget, see [Top trends](https://docs.aws.amazon.com/cost-management/latest/userguide/view-billing-dashboard.html#top-trends-widget).

You can use Cost Comparison in two main ways:
+ Query for any two months (referred to as baseline and comparison months) across any Cost Explorer dimension and cost metric. Cost Comparison analyzes your costs by:
  + Calculating the total cost for each selected dimension in the baseline month.
  + Comparing these with costs in the comparison month.
  + Ranking each resulting dimension value by the absolute cost difference.
  + Returning the top 10 increases or decreases for each dimension.

  **Example:**

  In the following example, Cost Comparison identified four services that demonstrated the largest change when comparing costs from March 2025 (comparison month) with April 2025 (baseline month):    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/cost-management/latest/userguide/ce-understand-cost-comparison.html)
+ Request detailed cost drivers for the cost change associated with a specific service, account, Region, or other dimension value. Cost Comparison:
  + Identifies the specific usage type driving the largest change.
  + Calculates the total cost for each charge type in the baseline and comparison months.
  + Ranks the results by absolute cost difference.
  + Provides a breakdown of cost changes for each charge type, allowing for targeted cost savings opportunities.

  **Example:**

  In the following example, Cost Comparison identified two RDS instances in Frankfurt, Germany (Europe Region) that accounted for a $63,336.48 cost difference between the selected months. For each instance, Cost Comparison identified additional cost drivers and their impact. The first instance (EU-InstanceUsage:db.r6g.8xl) showed increased cost and usage alongside decreased reserved capacity coverage, suggesting an opportunity to purchase additional reservations if the higher usage is expected to continue. The second instance (EU-InstanceUsage:db.t4g.xl) showed increased cost and usage with a decrease in applied credits compared to the previous month. This instance requires investigation into both the usage increase to evaluate potential reserved capacity purchases and the unexpected reduction in credits.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/cost-management/latest/userguide/ce-understand-cost-comparison.html)

If you need to analyze cost changes for specific areas of your business, choose filters to focus on other dimensions like tags or cost categories. Cost Comparison supports all of the available cost metrics (unblended, net unblended, net amortized, etc.) options in Cost Explorer, giving you flexibility to view the data in the way that is most meaningful for your needs. Cost Comparison dynamically updates the drivers based on the specific cost metrics or dimensions you select.