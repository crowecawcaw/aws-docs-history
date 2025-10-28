# Troubleshooting Cost and Usage Reports

###### Topics

- [Why does my Cost and Usage Report data not match the data shown
  in other Billing and Cost Management features?](#cur-data-differences "#cur-data-differences")
- [How can I backfill data after changing my report
  settings?](#cur-backfill-data "#cur-backfill-data")
- [Why is my report file folder in Amazon S3 stored in an unnamed
  folder?](#cur-unnamed-folder "#cur-unnamed-folder")
- [Why can’t I select the option to include resource
  IDs on my report?](#cur-activate-resource-ids "#cur-activate-resource-ids")
- [Why don't my Cost and Usage Report queries for Amazon Athena
  work on Amazon Redshift, or my Amazon Redshift queries on Amazon Athena?](#cur-athena-redshift-queries "#cur-athena-redshift-queries")
- [Why have the columns included in my report changed
  from a previous month](#cur-cur-columns-changed "#cur-cur-columns-changed")
- [Why don't my queries or tables work after
  the columns in my report changed?](#cur-cur-columns-changed-solutions "#cur-cur-columns-changed-solutions")
- [How do I query my report?](#cur-cur-query-help "#cur-cur-query-help")
- [Where can I find the billing data for my Amazon EC2
  Dedicated Host?](#cur-cur-dedicated-hosts "#cur-cur-dedicated-hosts")
- [How do I interpret the billing data for my Amazon EC2 Elastic
  IP addresses?](#cur-cur-elastic-ips "#cur-cur-elastic-ips")
- [How do unblended and blended rates
  or costs differ in consolidated billing?](#cur-consolidated-billing-unblended-blended "#cur-consolidated-billing-unblended-blended")
- [Why do some line items in my report have a blended rate
  or blended cost of 0?](#cur-blended-rate-zero "#cur-blended-rate-zero")
- [How are All Upfront Reserved Instances amortized in my
  report?](#cur-all-upfront-ri "#cur-all-upfront-ri")

## Why does my Cost and Usage Report data not match the data shown

in other Billing and Cost Management features?

Other Billing and Cost Management features (Cost Explorer, Detailed Billing Reports, Billing and Cost Management console) might present your costs
differently for the following reasons:

- The billing features round cost data in different ways.
- The billing features might have different data refresh settings. For example, you can
  choose whether or not your Cost and Usage Report automatically refreshes a previously closed bill
  with any refunds, credits, or Support fees applied after the bill is finalized. Cost Explorer
  automatically reflects the same items. In this scenario, if you don’t activate the automatic
  refresh on your Cost and Usage Report, then the Cost and Usage Report data won’t match the Cost Explorer data.
- The billing features can group charges differently. For example, the
  **Bills** page in the Billing and Cost Management console shows data transfer charges as a separate
  **Data Transfer** grouping within your **AWS Service
  Charges**. Meanwhile, Cost and Usage Reports and Cost Explorer show data transfer charges as a usage
  type for each service.

If after reviewing these reasons you still believe you're seeing discrepancies between your
Cost and Usage Report and other Billing and Cost Management features, open a support case to request a review of your cost
data. In your support case, make sure to provide the report name and the billing period that you
would like reviewed. For more information on opening a case, see [Getting help with your exports and reports](billing-get-answers.md "billing-get-answers.md").

## How can I backfill data after changing my report

settings?

Open a support case to request a backfill of your cost data. In your support case, make
sure to provide the report name and the billing period that you want backfilled. For more
information on opening a case, see [Getting help with your exports and reports](billing-get-answers.md "billing-get-answers.md").

Note that you can't get a backfill of cost data for the following scenarios:

- You can't get a backfill for cost data from before the date that you created the
  account.
- If you use AWS Organizations and the structure of your organization changed, such as which account
  is designated the management account, then you can't get a backfill of data with the previous
  organization structure.
- If you use AWS Organizations and you change organizations, then you can't get a backfill of data
  from prior to joining your current organization.

## Why is my report file folder in Amazon S3 stored in an unnamed

folder?

Any **/** character in the **Report path prefix** of your
report generates an unnamed folder in your Amazon S3 bucket. To remove the unnamed folder in your
next report update, edit your report settings and remove the **/** character
from the **Report path prefix**. For instructions, see [Editing your Cost and Usage Reports configuration](edit-cur.md "edit-cur.md").

## Why can’t I select the option to include resource

IDs on my report?

When you create your report, you can select the option to **Include resource
ID**. If you create your report with **Report versioning** set to
**Overwrite existing report**, then you can’t modify your **Include
resource ID** selection after you create your report. To include resource IDs, you
must create a new report and select the **Include resource ID** option.

## Why don't my Cost and Usage Report queries for Amazon Athena

work on Amazon Redshift, or my Amazon Redshift queries on Amazon Athena?

Amazon Athena and Amazon Redshift databases format Cost and Usage Report columns differently. Amazon Athena adds an
underscore between words in the column name (line_item_normalized_usage_amount). Amazon Redshift adds an
underscore between the column type and the attribute (lineitem_normalizedusageamount). Make sure
to modify your queries to match the column name format in Amazon Athena or Amazon Redshift.

## Why have the columns included in my report changed

from a previous month

The columns that AWS includes in your report depend on your AWS usage. Every report
includes columns with the **identity/**, **bill/**, and
**lineItem/** prefixes:

- identity/LineItemId
- identity/TimeInterval
- bill/InvoiceId
- bill/BillingEntity
- bill/BillType
- bill/PayerAccountId
- bill/BillingPeriodStartDate
- bill/BillingPeriodEndDate
- lineItem/UsageAccountId
- lineItem/LineItemType
- lineItem/UsageStartDate
- lineItem/UsageEndDate
- lineItem/ProductCode
- lineItem/UsageType
- lineItem/Operation
- lineItem/AvailabilityZone
- lineItem/ResourceId
- lineItem/UsageAmount
- lineItem/NormalizationFactor
- lineItem/NormalizedUsageAmount
- lineItem/CurrencyCode
- lineItem/UnblendedRate
- lineItem/UnblendedCost
- lineItem/BlendedRate
- lineItem/BlendedCost
- lineItem/LineItemDescription
- lineItem/TaxType
- lineItem/LegalEntity

All other columns are included only if your monthly AWS usage generates data to populate
those columns.

For example, your report includes **savingsPlan/** columns only if you
used Savings Plans during that month.

## Why don't my queries or tables work after

the columns in my report changed?

The columns that AWS includes in your report depend on your AWS usage for the month.
Because the columns included in your report can change, it’s a best practice to reference column
names instead of column numbers in any custom queries or tables based on your report.

## How do I query my report?

For detailed information about querying your Cost and Usage Report, see [CUR Query
Library Help](https://wellarchitectedlabs.com/cost/300_labs/300_cur_queries/query_help/ "https://wellarchitectedlabs.com/cost/300_labs/300_cur_queries/query_help/") in the AWS Well-Architected Labs website.

## Where can I find the billing data for my Amazon EC2

Dedicated Host?

In the **ResourceID** column, look for the Dedicated Host ID rather than
the instance ID. Because Dedicated Hosts are metered by Dedicated Host running hours, your
report shows Dedicated Host usage by metered hours associated with the host ID.

## How do I interpret the billing data for my Amazon EC2 Elastic

IP addresses?

Amazon EC2 Elastic IP addresses are metered in aggregate. This means that each line item in your
report doesn’t correspond with an individual Elastic IP address. Each line item represents the
total number of chargeable hours. You can have one Elastic IP address assigned to a running
instance at no charge. You’re charged per hour on a pro-rata basis for each additional Elastic
IP address that you assign to the instance. Additionally, AWS charges an hourly fee for
unassigned Elastic IP addresses.

## How do unblended and blended rates

or costs differ in consolidated billing?

With consolidated billing for AWS Organizations, unblended and blended rates or costs can help you
understand how much an account's usage would cost for a standalone account versus a linked
account in an organization. Some services offer pricing tiers that can lower unit costs as usage
increases. Because AWS aggregates all usage for a service in an organization, individual
accounts might access lower-priced tiers sooner when their usage is aggregated in an
organization's monthly usage.

Unblended rates are the rates associated with an individual account's service usage. For a
line item, the unblended cost is usage multiplied by the unblended rate. The unblended cost
would be the cost of the account's usage if it were a standalone account. Blended rates are the
rates associated with total usage in an organization averaged across accounts. For a line item,
the blended cost is usage multiplied by the blended rate. The blended cost is the cost
attributed to the account's usage as a linked account in an organization.

For more information and examples of calculating unblended and blended costs, see [Understanding Consolidated Bills](../../../awsaccountbilling/latest/aboutv2/con-bill-blended-rates.md "../../../awsaccountbilling/latest/aboutv2/con-bill-blended-rates.md") in the _AWS Billing User Guide_

## Why do some line items in my report have a blended rate

or blended cost of 0?

Amazon EC2 line items with a Reserved Instance discount have an blended rate of zero. For these
line items, the **LineItemType** is **Discounted
Usage**.

The blended cost is the usage multiplied by the blended rate. If the value for blended rate
or usage is zero, then the blended cost is also zero.

## How are All Upfront Reserved Instances amortized in my

report?

Because All Upfront Reserved Instances are paid in full upfront, the amortized costs are
reflected in your report as the upfront payment divided over the associated time period (one
year or three years).

**reservation/AmortizedUpfrontCostForUsage** and
**reservation/EffectiveCost** are the same rate for All Upfront Reserved
Instances. This is because both columns are an equal division of the upfront payment for the
Reserved Instance over the total hours of its term.

It's expected that your report has **RIFee** line items populated for All
Upfront Reserved Instances, even though the **RIFee** is $0.00. These line
items represent the recurring hourly costs for the month, and they have additional usage data in
other columns. All Reserved Instances generate **RIFee** line items.
