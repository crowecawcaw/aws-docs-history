# Estimating monthly savings

Cost Optimization Hub analyzes specific pricing discounts to provide you with a measure of your cost
efficiency. This is done by dividing the aggregated estimated monthly savings of your cost
optimization opportunities by your amortized monthly AWS costs, exclusive of credits and
refunds.

For recommendations associated with a resource, estimated monthly cost impact is an
estimation of how much your AWS bill will change over a 730-hour period (365 \* 24 /12). This
estimate excludes the periods when the resources were not running and if you had implemented the
recommended action 730 hours ago. If the recommendation has a different lookback period, the
cost impact is normalized to a 730-hour period, which is the average number of hours per
month.

Note that your estimated monthly savings is a quick approximation of future savings. The
actual savings that you realize is dependent on your future AWS usage patterns.

## Aggregating estimated savings

Cost Optimization Hub aggregates AWS cost optimization recommendations for you across your AWS
accounts and AWS Regions. For example, it makes recommendations on resource rightsizing,
idle resource deletion, Savings Plans, and Reserved Instances.

You can aggregate estimated savings by the following categories:

- AWS account
- AWS Region
- Resource type
- Recommended action
- Implementation effort
- Is resource restart needed
- Is rollback possible
- Tag key

###### To aggregate your cost optimization recommendations

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost Optimization Hub**.
3. Choose to view your savings opportunities in **Chart view** or
   **Table view**.
4. Choose **Aggregate estimated savings by**, and then choose a
   category.
