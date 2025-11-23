# Estimating cost for Cost Explorer hourly

granularity

Cost Explorer offers hourly granularity data at a daily charge of $0.00000033 per
usage record, which translates to $0.01 per 1,000 usage records monthly. A usage
record corresponds to a line item with a specific resource and usage type.

Cost Explorer bills you daily based on the total hourly usage records hosted in
Cost Explorer for the past 14 days. For example, if you run one EC2 instance all
day every day for the past month, and you have hourly granularity enabled,
Cost Explorer will host 336 records per day (24 hours x 14 days) and charge you
$0.0001 daily ($0.00000033 per record x 336 records), resulting in a monthly bill of
$0.003 ($0.0001 daily cost x 30).

For the provided estimated usage records count, you can calculate the cost
yourself using the provided formula, or you can use AWS Pricing Calculator.

###### Note

Granular data visibility is only available for billing views that show chargeable data. When you use Billing Conductor as an account in a standard billing group or billing transfer billing group, you can't view granular data in Cost Explorer.
