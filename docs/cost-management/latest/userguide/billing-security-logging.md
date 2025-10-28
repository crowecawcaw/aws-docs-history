# Logging and monitoring in AWS Cost Management

Monitoring is an important part of maintaining the reliability, availability, and
performance of your AWS account. There are several tools available to monitor your Billing and Cost Management
usage.

## AWS Cost and Usage Reports

AWS Cost and Usage Reports tracks your AWS usage and provides estimated charges associated with
your account. Each report contains line items for each unique combination of AWS
products, usage type, and operation that you use in your AWS account. You can
customize the AWS Cost and Usage Reports to aggregate the information either by the hour or by the
day.

For more information about AWS Cost and Usage Reports, see the [_Cost and Usage Report
Guide_](../../../cur/latest/userguide/what-is-cur.md "../../../cur/latest/userguide/what-is-cur.md").

## AWS Cost Explorer

Cost Explorer enables you to view and analyze your costs and usage. You can monitor
data for up to the last 13 months, forecast how much you're likely to spend for the next
three months, and get recommendations for what Reserved Instances to purchase. You can
use Cost Explorer to identify areas that need further inquiry and see trends that you
can use to understand your costs.

For more information about Cost Explorer, see the [Analyzing your costs and usage with AWS Cost Explorer](ce-what-is.md "ce-what-is.md").

## AWS Budgets

Budgets enables you to track your AWS cost and usage by using the cost
visualization provided by Cost Explorer. Budgets shows the status of your budgets,
provides forecasts of your estimated costs, and tracks your AWS usage, including Free
Tier. You can also receive notifications when your estimated costs exceed your
budgets.

For more information about Budgets, see the [Managing your costs with AWS Budgets](budgets-managing-costs.md "budgets-managing-costs.md").

## AWS CloudTrail

Billing and Cost Management is integrated with AWS CloudTrail, a service that provides a record of actions taken by
a user, role, or an AWS service in Billing and Cost Management. CloudTrail captures all write and modify API calls
for Billing and Cost Management as events, including calls from the Billing and Cost Management console and from code calls to the
Billing and Cost Management APIs.

For more information about AWS CloudTrail, see the
[Logging AWS Cost Management
API calls with AWS CloudTrail](logging-with-cloudtrail.md "logging-with-cloudtrail.md").

## AWS Pricing Calculator

The in-console AWS Pricing Calculator is an AWS Billing and Cost Management feature that enables you to estimate your planned
cloud costs using your discount and purchase commitments. You can use Pricing Calculator to
assess the cost impact for migrating workloads, planning new or growth of existing workloads,
and plan for commitment purchases.

For more information about the in-console Pricing Calculator, see the [Generating estimates with Pricing Calculator](pricing-calculator.md "pricing-calculator.md").
