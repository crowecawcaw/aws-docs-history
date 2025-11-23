# Knowing the differences

between Billing and Cost Explorer data

## Billing data

Your billing data appears on the **Bills** and
**Payments** pages of the AWS Billing and Cost Management console, and in the invoice
that AWS issues to you. Billing data helps you understand the actual invoiced
charges for previous billing periods, and the estimated charges that you've accrued
for the current billing period, based on your month-to-date service usage. Your
invoice represents the amount that you owe to AWS.

## Cost Explorer data

Your Cost Explorer data appears in the following places:

- The Billing and Cost Management home page
- The pages for Cost Explorer, Budgets, and Cost Anomaly Detection
- Your reports for coverage and usage

Cost Explorer supports deep-dive analysis so that you can identify savings opportunities.
Cost Explorer data provides more granular dimensions (such as Availability Zone or operating
system) and includes features that might show differences when compared to billing
data. On the **Cost Management** preferences page, you can manage
your preferences for Cost Explorer data, including linked account access and historical and
granular data settings. For more information, see [Controlling access to Cost Explorer](ce-access.md "ce-access.md").

## Amortized costs

Billing data is always presented on a _cash_ basis. It
represents the amount that AWS charges you each month. For example, if you
purchase a one-year, all-upfront Savings Plan in September, AWS will charge you
the full cost for that Savings Plan in the September billing period. Your billing
data will then include the full cost of that Savings Plan in September. This helps
you understand, validate, and pay your AWS invoices on time.

In contrast, you can use Cost Explorer data to view amortized costs. When costs are
amortized, an upfront charge is spread, or _amortized_ over the
life of that agreement. In the previous example, you can use Cost Explorer for an amortized
view of your Savings Plan. A one-year, all-upfront Savings Plan purchase will be
spread evenly across the 12 months of the commitment term. Use amortized costs to
gain insight into the effective daily costs associated with your portfolio of
reservations or Savings Plans.

## AWS service grouping

With billing data, your AWS charges are grouped into AWS services on your
invoice. To help with deep-dive analysis, Cost Explorer will group some costs differently.

For example, let's say that you want to understand compute costs for Amazon Elastic Compute Cloud
compared to ancillary cost, such as Amazon Elastic Block Store volumes or NAT gateways. Instead of a
single group for Amazon EC2 costs, Cost Explorer will group costs into **EC2 -
Instances** and **EC2 - Other**.

In another example, to help analyze data transfer costs, Cost Explorer groups your transfer
costs by service. In billing data, data transfer costs are grouped into a single
service named **Data Transfer**.

## Estimated charges for the

current month

Your billing data and Cost Explorer data are refreshed at least once per day. The cadence
when they're refreshed might differ. This can result in differences for your
month-to-date estimated charges.

## Rounding

Your billing data and Cost Explorer data are processed at different granularities. For
example, Cost Explorer data is available with hourly and resource-level granularity. Billing
data is monthly and doesn't offer resource-level details. As a result, your billing
data and Cost Explorer data might vary due to rounding. When these data sources are
different, the amount on your invoice is the final amount that you owe to
AWS.

## Presentation of

discounts, credits, refunds, and taxes

The billing data on the **Bills** page (for example, in the
**Charges by service** tab) excludes refunds, while Cost Explorer data
includes refunds. When a refund is issued, this might cause differences in other
charge types.

For example, let's say that a portion of your taxes was refunded. On the
**Bills** page, the **Taxes by service** tab
will continue to show the full tax amount. The Cost Explorer data will show the post-refund
tax amount.

If you use billing transfer and sign in to the Billing and Cost Management console with a bill source account, you can't view credits, refunds, or taxes in the **Bills** page, Cost Explorer, or AWS Cost and Usage Report."
