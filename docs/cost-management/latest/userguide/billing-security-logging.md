

# Logging and monitoring in AWS Cost Management
<a name="billing-security-logging"></a>

Monitoring is an important part of maintaining the reliability, availability, and performance of your AWS account. There are several tools available to monitor your Billing and Cost Management usage.

## AWS Cost and Usage Reports
<a name="billing-security-logging-cur"></a>

AWS Cost and Usage Reports tracks your AWS usage and provides estimated charges associated with your account. Each report contains line items for each unique combination of AWS products, usage type, and operation that you use in your AWS account. You can customize the AWS Cost and Usage Reports to aggregate the information either by the hour or by the day.

For more information about AWS Cost and Usage Reports, see the [*Cost and Usage Report Guide*](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html).

## AWS Cost Explorer
<a name="billing-security-logging-ce"></a>

Cost Explorer enables you to view and analyze your costs and usage. You can monitor data for up to the last 13 months, forecast how much you're likely to spend for the next three months, and get recommendations for what Reserved Instances to purchase. You can use Cost Explorer to identify areas that need further inquiry and see trends that you can use to understand your costs.

For more information about Cost Explorer, see the [Analyzing your costs and usage with AWS Cost Explorer](ce-what-is.md).

## AWS Budgets
<a name="billing-security-logging-budget"></a>

Budgets enables you to track your AWS cost and usage by using the cost visualization provided by Cost Explorer. Budgets shows the status of your budgets, provides forecasts of your estimated costs, and tracks your AWS usage, including Free Tier. You can also receive notifications when your estimated costs exceed your budgets.

For more information about Budgets, see the [Managing your costs with AWS Budgets](budgets-managing-costs.md).

## AWS CloudTrail
<a name="billing-security-logging-cloudtrail"></a>

Billing and Cost Management is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Billing and Cost Management. CloudTrail captures all write and modify API calls for Billing and Cost Management as events, including calls from the Billing and Cost Management console and from code calls to the Billing and Cost Management APIs.

For more information about AWS CloudTrail, see the [Logging AWS Cost Management API calls with AWS CloudTrail](https://docs.aws.amazon.com/cost-management/latest/userguide/logging-with-cloudtrail.html).

## AWS Pricing Calculator
<a name="billing-security-logging-pc"></a>

The in-console AWS Pricing Calculator is an AWS Billing and Cost Management feature that enables you to estimate your planned cloud costs using your discount and purchase commitments. You can use Pricing Calculator to assess the cost impact for migrating workloads, planning new or growth of existing workloads, and plan for commitment purchases.

For more information about the in-console Pricing Calculator, see the [Generating estimates with Pricing Calculator](pricing-calculator.md).