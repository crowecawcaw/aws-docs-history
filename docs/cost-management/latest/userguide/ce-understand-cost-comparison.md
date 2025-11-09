# Understanding how a cost comparison

works

You can use Cost Comparison to quickly understand your cloud spending by automatically
identifying and unfolding the largest cost drivers driving the cost variations between
two selected months. Cost Comparison provides a detailed breakdown for these cost
variances, from usage shifts to changes in commitment-based discounts like Savings Plans
coverage and applied credits, eliminating hours of manual investigation.

The **Top trends** widget on the console home page automatically
applies Cost Comparison to show the top cost changes across your services, accounts, and
Regions. For more information about this widget, see [Top trends](view-billing-dashboard.md#top-trends-widget "view-billing-dashboard.md#top-trends-widget").

You can use Cost Comparison in two main ways:

- Query for any two months (referred to as baseline and comparison months)
  across any Cost Explorer dimension and cost metric. Cost Comparison analyzes
  your costs by:

      + Calculating the total cost for each selected dimension in the
       baseline month.
      + Comparing these with costs in the comparison month.
      + Ranking each resulting dimension value by the absolute cost
       difference.
      + Returning the top 10 increases or decreases for each
       dimension.

  **Example:**

In the following example, Cost Comparison identified four services that demonstrated the
largest change when comparing costs from March 2025 (comparison month) with
April 2025 (baseline month):

| Service        | March 2025 | April 2025 | Change      |
| -------------- | ---------- | ---------- | ----------- |
| Amazon RDS     | $8,787.98  | $72,124.46 | +$63,336.48 |
| SageMaker      | $16,523.00 | $31,890.00 | +$15,367.00 |
| Amazon Connect | $5,144.00  | $17,902.00 | +$12,758.00 |
| EC2            | $68,708.00 | $60,463.00 | -$8,245.00  |

- Request detailed cost drivers for the cost change associated with a specific
  service, account, Region, or other dimension value. Cost Comparison:

      + Identifies the specific usage type driving the largest
       change.
      + Calculates the total cost for each charge type in the baseline and
       comparison months.
      + Ranks the results by absolute cost difference.
      + Provides a breakdown of cost changes for each charge type, allowing for targeted cost
       savings opportunities.

  **Example:**

In the following example, Cost Comparison identified two RDS instances in Frankfurt,
Germany (Europe Region) that accounted for a $63,336.48 cost difference between
the selected months. For each instance, Cost Comparison identified additional
cost drivers and their impact. The first instance (EU-InstanceUsage:db.r6g.8xl)
showed increased cost and usage alongside decreased reserved capacity coverage,
suggesting an opportunity to purchase additional reservations if the higher
usage is expected to continue. The second instance (EU-InstanceUsage:db.t4g.xl)
showed increased cost and usage with a decrease in applied credits compared to
the previous month. This instance requires investigation into both the usage
increase to evaluate potential reserved capacity purchases and the unexpected
reduction in credits.

| Cost drivers |                                  |
| ------------ | -------------------------------- | ------------ | -------- | ---------- | ---------- | ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Service      | Usage type                       |              | Baseline | Comparison | Difference | Unit | Console only explanation of cost<br>drivers                                                                                                                                                                                        |
| Amazon RDS   | EU-InstanceUsage:db.r6g.8xl      | USAGE_CHANGE | 4,599.11 | 36,855.11  | 32,256.00  | USD  | +32,256.00 cost change for Amazon RDS: EU-InstanceUsage:db.r6g.8xl<br>+ On-Demand usage increased by 701.4%, leading to a $32,256.00 increase in<br>costs<br>+ The usage covered by Reserved Instances decreased<br>by 47.77%      |
| Amazon RDS   | USAGE_CHANGE                     | 995.01       | 8,034.73 | 7,039.72   | Hours      |
| Amazon RDS   | RESERVATION_APPLIED_USAGE_CHANGE | 1,236.99     | 646.04   | -590.95    | Hours      |
| Amazon RDS   | EU-InstanceUsage:db.t4g.8xl      | USAGE_CHANGE | 5,386.21 | 36,047.21  | 30,661.00  | USD  | +30,661.00 cost change for Amazon RDS: EU-InstanceUsage:db.t4g.8xl<br>+ On-Demand usage increased by 569.2%, leading to a<br>$30,661.00 increase in costs<br>+ Credits applied decreased from $1,157.34 to $737.86, a 36% decrease |
| Amazon RDS   | USAGE_CHANGE                     | 1,074.66     | 7,192.18 | 6,117.52   | Hours      |
| Amazon RDS   | CREDIT_USAGE_CHANGE              | 1,157.34     | 737.86   | -419.48    | USD        |

If you need to analyze cost changes for specific areas of your business, choose
filters to focus on other dimensions like tags or cost categories. Cost Comparison
supports all of the available cost metrics (unblended, net unblended, net amortized,
etc.) options in Cost Explorer, giving you flexibility to view the data in the way that
is most meaningful for your needs. Cost Comparison dynamically updates the drivers based
on the specific cost metrics or dimensions you select.
