# Understanding your cost efficiency metric

Cost efficiency is a metric that measures how effectively you're optimizing your AWS cloud resources. It is automatically generated everyday by considering resource optimization, resource utilization, and commitment savings and is applicable across multiple scopes—from individual regions to entire organizations.

It provides a simple, yet comprehensive measure of your cloud spend efficiency using the following formula:

Cost efficiency = 1 - (Potential Savings / Total Optimizable Spend) × 100%

For example, if your total monthly AWS spend that can be optimized is $100,000 and Cost Optimization Hub identifies $10,000 in potential savings, your cost efficiency is 90%.

You can track your cost efficiency over-time across your organization to understand and benchmark your cost efficiency. With daily refreshes, the metric provides insights into optimization progress, showing score improvements when you implement cost-saving recommendations, and score decreases when inefficient resources are provisioned.

The cost efficiency metric is based on a rolling 30-day spend and today’s savings opportunity. For example, the metric on November 30 will use the optimizable spend from October 31st to November 29th and the potential savings on November 30th.

## Potential Savings

Potential savings represent deduplicated, estimated total cost reductions you could achieve by implementing recommended actions across your AWS environment. These actions may include rightsizing resources, selecting optimal instance types, removing idle resources, and utilizing commitment-based pricing models such as Reserved Instances and Savings Plans.

Cost Optimization Hub prevents duplicate savings calculations by filtering and ranking overlapping opportunities to eliminate redundant savings and highlight those with the highest savings potential. For example, stopping an idle EC2 instance reduces the amount you can save through purchasing Savings Plans. Cost Optimization Hub proportionally reduces the estimated savings for Savings Plans recommendations based on the costs of idle EC2 instances that can be stopped.

## Total Optimizable Spend

Total Optimizable Spend represents your AWS spending on services where Cost Optimization Hub provides recommendations such as Amazon EC2 instances, Amazon RDS databases, and Amazon OpenSearch. It uses your **Net amortized costs** after removing any credits and refunds you might have. For more information, see [Your net amortized costs](ce-exploring-data.md#net-amortized-costs "ce-exploring-data.md#net-amortized-costs").

###### Note

For supported services, the entire service spend is included in Total Optimizable Spend.

### Supported Services

Optimizable spend in the cost efficiency metric is all spend under these included services:

- Amazon Elastic Compute Cloud (EC2) instances
- Amazon Elastic Container Service (ECS)
- Amazon Elastic Kubernetes Service (EKS)
- Amazon Elastic Block Store (EBS) volumes
- Amazon RDS databases
- Amazon SageMaker
- Amazon Redshift
- AWS Lambda functions
- OpenSearch
- MemoryDB
- DynamoDB
- ElastiCache

For a list of supported resources for these services, see [Supported resources](cost-optimization-hub.md#coh-supported-resources "cost-optimization-hub.md#coh-supported-resources")

## Viewing your Cost Efficiency

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost Optimization Hub**.
3. Your current Cost efficiency appears at the top of the page.
4. By default, you will see the **Overall** scores for your account on the Cost efficiency card on the right. You can perform the following actions on this card:
   - To view the 5 most efficient accounts, under “View efficiency by”, choose **Most efficient accounts**
   - To view the 5 least efficient accounts, under “View efficiency by”, choose **Least efficient accounts**
   - To view the 5 most efficient regions, under “View efficiency by”, choose **Most efficient regions**

To view cost efficiency across all your accounts and regions, use the table view under **Optimization details** . You can search for specific accounts or Regions, and sort by cost efficiency by clicking the column header.

## Frequently Asked Questions

1. **Why am I not able to view the cost efficiency?**

Please check that you've enrolled into Compute Optimizer. For more information, see [Getting
started with AWS Compute Optimizer](../../../compute-optimizer/latest/ug/getting-started.md "../../../compute-optimizer/latest/ug/getting-started.md"). If you are enrolled into Compute Optimizer but do not see the efficiency metric, it could be due to high variance in your AWS usage. We will generate the metric automatically once your usage becomes more stable. 2. **Why don't I see history in cost efficiency?**

You will not see history if you are a new customer of Cost Optimization Hub and Compute Optimizer. If you are an existing customer but do not see the history, it could be because of lack of historical data. You should start seeing the history with continued usage.
