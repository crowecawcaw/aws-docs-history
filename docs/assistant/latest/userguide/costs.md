

# Chatting about your AWS costs
<a name="costs"></a>

The AWS assistant helps you manage AWS costs through natural conversation. It can analyze historical and forecasted costs from AWS Cost Explorer and find recommendations from Cost Optimization Hub and AWS Compute Optimizer. It can also explain AWS Savings Plans and reservation opportunities, check invoices and balances, and answer AWS pricing questions.

You can ask a specific question or request an open-ended analysis. For example:
+ What were my EC2 costs last month?
+ What were the biggest drivers of last week's cost decrease?

Responses can show the APIs and parameters used and link to matching console views.

You can chat about costs in the AWS Management Console.

## Cost capabilities
<a name="cost-capabilities"></a>

**Cost analysis**  
Analyze spending patterns, trends, forecasts, and major changes.

**Optimization**  
Find idle or over-provisioned resources and review Cost Optimization Hub, AWS Compute Optimizer, AWS Savings Plans, and reservation recommendations.

**Pricing**  
Estimate AWS service and architecture costs.

**Payments**  
List recent invoices and check outstanding balances.

**Visualizations**  
Generate custom charts of costs, usage, forecasts, budgets, pricing, and optimization data.

The AWS assistant maintains context so that you can ask follow-up questions and refine an analysis.

## How cost analysis works
<a name="cost-how-it-works"></a>

The AWS assistant retrieves data from AWS Cost Explorer, Cost Optimization Hub, AWS Compute Optimizer, AWS Budgets, AWS Free Tier, AWS Pricing, and AWS Savings Plans and reservation recommendation APIs. It performs calculations and analyzes patterns using your actual usage and spending data.

## Prerequisites
<a name="cost-prerequisites"></a>
+ Your IAM identity must have permission to use the AWS assistant and access the billing and cost-management data required for your question. For an example policy, see [Allow the AWS assistant to access cost data](security-iam-examples.md#iam-example-cost-chat).
+ Enable AWS Cost Explorer in the account. For instructions on enabling it, see [Enabling AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html).
+ Enable optional services such as Cost Optimization Hub and AWS Budgets to use their related capabilities.

## Example cost questions
<a name="cost-examples"></a>

### Analysis and forecasting
<a name="cost-analysis-examples"></a>
+ What were my costs last month?
+ Show my EC2 spending trends for the past six months.
+ Why did my costs increase last week?
+ Analyze last month's spending and give me the most important insights.

### Optimization and monitoring
<a name="cost-optimization-examples"></a>
+ What are my top cost optimization opportunities?
+ Which EC2 instances are over-provisioned?
+ Do I have idle resources?
+ Which AWS Savings Plans should I purchase?
+ Have any teams exceeded their budgets?
+ Do I have any cost anomalies?

### Pricing
<a name="cost-pricing-examples"></a>
+ How much does a c8g.2xlarge instance cost in `us-east-1`?
+ What would it cost to store 1 PB in Amazon Simple Storage Service (Amazon S3) in Dublin?
+ Estimate a basic three-tier web application with Amazon Elastic Compute Cloud (Amazon EC2), Amazon API Gateway, a small SQL database, and a frontend hosted through Amazon CloudFront.

### Visualizations
<a name="cost-visualization-examples"></a>
+ Graph my support charges by month for the last 12 months.
+ Show an area chart of EC2 costs by instance type by day this month.
+ Create a chart of S3 storage pricing by tier in `us-east-1`.
+ Graph AWS Savings Plans coverage and utilization for the last three months.
+ Graph EC2 cost per vCPU hour over the last three weeks.

For more information about cost analysis, see [Overview of cost management capabilities in Amazon Q Developer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-q-overview.html) in the *AWS Cost Management User Guide*.