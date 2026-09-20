

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


<table>
<thead>
  <tr><th>Service</th><th>March 2025</th><th>April 2025</th><th>Change</th></tr>
</thead>
<tbody>
  <tr><td>Amazon RDS</td><td> $8,787.98</td><td>$72,124.46</td><td>+$63,336.48</td></tr>
  <tr><td>SageMaker</td><td>$16,523.00</td><td>$31,890.00</td><td>+$15,367.00</td></tr>
  <tr><td>Amazon Connect</td><td> $5,144.00</td><td>$17,902.00</td><td>+$12,758.00</td></tr>
  <tr><td>EC2</td><td>$68,708.00</td><td>$60,463.00</td><td> -$8,245.00</td></tr>
</tbody>
</table>

+ Request detailed cost drivers for the cost change associated with a specific service, account, Region, or other dimension value. Cost Comparison:
  + Identifies the specific usage type driving the largest change.
  + Calculates the total cost for each charge type in the baseline and comparison months.
  + Ranks the results by absolute cost difference.
  + Provides a breakdown of cost changes for each charge type, allowing for targeted cost savings opportunities.

  **Example:**

  In the following example, Cost Comparison identified two RDS instances in Frankfurt, Germany (Europe Region) that accounted for a $63,336.48 cost difference between the selected months. For each instance, Cost Comparison identified additional cost drivers and their impact. The first instance (EU-InstanceUsage:db.r6g.8xl) showed increased cost and usage alongside decreased reserved capacity coverage, suggesting an opportunity to purchase additional reservations if the higher usage is expected to continue. The second instance (EU-InstanceUsage:db.t4g.xl) showed increased cost and usage with a decrease in applied credits compared to the previous month. This instance requires investigation into both the usage increase to evaluate potential reserved capacity purchases and the unexpected reduction in credits.


<table>
<thead>
  <tr><th colspan="3">Cost drivers</th><th colspan="5"></th></tr>
  <tr><th>Service</th><th>Usage type</th><th></th><th>Baseline</th><th>Comparison</th><th>Difference</th><th>Unit</th><th>Console only explanation of cost drivers</th></tr>
</thead>
<tbody>
  <tr><td>Amazon RDS</td><td rowspan="3">EU-InstanceUsage:db.r6g.8xl</td><td>USAGE_CHANGE</td><td>4,599.11</td><td>36,855.11</td><td>32,256.00</td><td>USD</td><td rowspan="3">+32,256.00 cost change for Amazon RDS: EU-InstanceUsage:db.r6g.8xl<ul><li> On-Demand usage increased by 701.4%, leading to a $32,256.00 increase in costs </li><li> The usage covered by Reserved Instances decreased by 47.77% </li></ul></td></tr>
  <tr><td>Amazon RDS</td><td>USAGE_CHANGE</td><td>995.01</td><td>8,034.73</td><td>7,039.72</td><td>Hours</td></tr>
  <tr><td>Amazon RDS</td><td>RESERVATION_APPLIED_USAGE_CHANGE</td><td>1,236.99</td><td>646.04</td><td>-590.95</td><td>Hours</td></tr>
  <tr><td>Amazon RDS</td><td rowspan="3">EU-InstanceUsage:db.t4g.8xl</td><td>USAGE_CHANGE</td><td>5,386.21</td><td>36,047.21</td><td>30,661.00</td><td>USD</td><td rowspan="3">+30,661.00 cost change for Amazon RDS: EU-InstanceUsage:db.t4g.8xl<ul><li> On-Demand usage increased by 569.2%, leading to a $30,661.00 increase in costs </li><li> Credits applied decreased from $1,157.34 to $737.86, a 36% decrease </li></ul></td></tr>
  <tr><td>Amazon RDS</td><td>USAGE_CHANGE</td><td>1,074.66</td><td>7,192.18</td><td>6,117.52</td><td>Hours</td></tr>
  <tr><td>Amazon RDS</td><td>CREDIT_USAGE_CHANGE</td><td>1,157.34</td><td>737.86</td><td>-419.48</td><td>USD</td></tr>
</tbody>
</table>


If you need to analyze cost changes for specific areas of your business, choose filters to focus on other dimensions like tags or cost categories. Cost Comparison supports all of the available cost metrics (unblended, net unblended, net amortized, etc.) options in Cost Explorer, giving you flexibility to view the data in the way that is most meaningful for your needs. Cost Comparison dynamically updates the drivers based on the specific cost metrics or dimensions you select.