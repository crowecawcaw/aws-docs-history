# Reviewing estimated usage costs for

Macie

To review your current estimated usage costs for Amazon Macie, you can use the Amazon Macie
console or the Amazon Macie API. Both the console and the API provide estimated costs for
Macie pricing dimensions. If you’re currently participating in a 30-day free trial, you
can use this data to estimate your costs for using Macie after your free trial ends. For
information about Macie pricing dimensions and considerations, see [Understanding estimated
usage costs](account-mgmt-costs-calculations.md "account-mgmt-costs-calculations.md"). For detailed information
and examples of usage costs, see [Amazon Macie
pricing](https://aws.amazon.com/macie/pricing/ "https://aws.amazon.com/macie/pricing/").

In Macie, estimated usage costs are reported in US dollars (USD) and apply only to the
current AWS Region. If you use the console to review the data, the cost estimates are
for the current calendar month to date (inclusively). If you query the data
programmatically with the Amazon Macie API, you can specify an inclusive time range for the
estimates, either a rolling time range of the preceding 30 days or the current calendar
month to date.

###### Topics

- [Reviewing estimated
  usage costs on the console](#account-mgmt-costs-review-console "#account-mgmt-costs-review-console")
- [Querying estimated usage
  costs with the API](#account-mgmt-costs-review-api "#account-mgmt-costs-review-api")

## Reviewing estimated usage costs on

the Amazon Macie console

On the Amazon Macie console, cost estimates are organized as follows:

- **Preventative control monitoring** – This is the estimated cost
  of maintaining an inventory of your Amazon Simple Storage Service (Amazon S3) general purpose buckets,
  and evaluating and monitoring the buckets for security and access
  control.
- **Sensitive data discovery jobs** – This is the
  estimated cost of the sensitive data discovery jobs that you ran.
- **Automated sensitive data discovery** – These are the estimated costs of
  performing automated sensitive data discovery. This includes monitoring and evaluating your S3
  bucket inventory to identify S3 objects that are eligible for analysis. It
  also includes analyzing eligible objects and reporting sensitive data
  statistics, findings, and other types of results.

To review estimates for automated sensitive data discovery by using the console, you must be the Macie administrator for an
organization or have a standalone Macie account.

###### To review your estimated usage costs on the console

Follow these steps to review your estimated usage costs by using the Amazon Macie
console.

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to review your estimated costs.
3. In the navigation pane, choose **Usage**.

If you have a standalone Macie account or a member account in an organization, the
**Usage** page displays a breakdown of the estimated usage
costs for your account.

If you’re the Macie administrator for an organization, the **Usage** page lists
accounts in your organization. In the table:

- **Service quota – Jobs** – This is the current
  monthly quota for running sensitive data discovery jobs to analyze S3 objects in
  buckets that an account owns.
- **Free trial** – These fields indicate whether an
  account is currently participating in the free trial for preventative control
  monitoring or automated sensitive data discovery. A **Free trial** field is empty if
  the applicable free trial has ended for an account.
- **Total** – This is the total estimated cost for an
  account.

The **Estimated costs** section shows the total estimated cost for your
organization and a breakdown of those costs. To review the breakdown of estimated
costs for a specific account in your organization, choose the account in the table.
The **Estimated costs** section then shows this breakdown. To show
this data for another account, choose the account in the table. To clear your
account selection, choose **X** next to the account ID.

## Querying estimated usage costs with the

Amazon Macie API

To query your estimated usage costs programmatically, you can use the following
operations of the Amazon Macie API:

- **GetUsageTotals** – This operation returns total estimated usage
  costs for your account, grouped by usage metric. If you’re the Macie administrator
  for an organization, this operation returns aggregated cost estimates for
  all the accounts in your organization. To learn more about this operation,
  see [Usage Totals](../APIReference/usage.md "../APIReference/usage.md") in the _Amazon Macie API
  Reference_.
- **GetUsageStatistics** – This operation returns usage statistics
  and related data for your account, grouped by account and then by usage
  metric. The data includes total estimated usage costs and current account
  quotas. As applicable, it also indicates when your 30-day free trial started
  for Macie and for automated sensitive data discovery. If you’re the Macie administrator for an organization,
  this operation returns a breakdown of the data for all the accounts in your
  organization. You can customize your query by sorting and filtering the
  query results. To learn more about this operation, see [Usage
  Statistics](../APIReference/usage-statistics.md "../APIReference/usage-statistics.md") in the _Amazon Macie API
  Reference_.

When you use either operation, you can optionally specify an inclusive time range for
the data. This time range can be a rolling time range of the preceding 30 days
(`PAST_30_DAYS`) or the current calendar month to date
(`MONTH_TO_DATE`). If you don’t specify a time range, Macie returns the
data for the preceding 30 days.

The following examples show how to query estimated usage costs and statistics by using the
[AWS Command Line Interface (AWS CLI)](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md"). You can also query the data by using a current version of another AWS command line tool or an AWS
SDK, or by sending HTTPS requests directly to Macie. For information about AWS tools and SDKs,
see [Tools to Build on AWS](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/").

###### Examples

- [Querying total
  estimated usage costs](#account-mgmt-costs-review-api-totals "#account-mgmt-costs-review-api-totals")
- [Querying
  usage statistics](#account-mgmt-costs-review-api-statistics "#account-mgmt-costs-review-api-statistics")

### Example 1: Querying total

estimated usage costs

To query total estimated usage costs by using the AWS CLI, run the [get-usage-totals](../../../cli/latest/reference/macie2/get-usage-totals.md "../../../cli/latest/reference/macie2/get-usage-totals.md") command and optionally specify a time range for the
data. For example:

```
`C:\>` `aws macie2 get-usage-totals --time-range `MONTH_TO_DATE``
```

Where `MONTH_TO_DATE` specifies the current calendar
month to date as the time range for the data.

If the command runs successfully, you receive output similar to the
following.

```
`{
 "timeRange": "MONTH_TO_DATE",
 "usageTotals": [
 {
 "currency": "USD",
 "estimatedCost": "153.45",
 "type": "SENSITIVE_DATA_DISCOVERY"
 },
 {
 "currency": "USD",
 "estimatedCost": "65.18",
 "type": "AUTOMATED_SENSITIVE_DATA_DISCOVERY"
 },
 {
 "currency": "USD",
 "estimatedCost": "1.51",
 "type": "DATA_INVENTORY_EVALUATION"
 },
 {
 "currency": "USD",
 "estimatedCost": "0.98",
 "type": "AUTOMATED_OBJECT_MONITORING"
 }
 ]
}`
```

Where `estimatedCost` is the total estimated usage cost for the associated
usage metric (`type`):

- `SENSITIVE_DATA_DISCOVERY`, for analyzing S3 objects with
  sensitive data discovery jobs.
- `AUTOMATED_SENSITIVE_DATA_DISCOVERY`, for analyzing S3 objects with
  automated sensitive data discovery.
- `DATA_INVENTORY_EVALUATION`, for monitoring and evaluating S3 general purpose
  buckets for security and access control.
- `AUTOMATED_OBJECT_MONITORING`, for evaluating and monitoring your S3 bucket
  inventory to identify S3 objects that are eligible for analysis by
  automated sensitive data discovery.

### Example 2: Querying

usage statistics

To query usage statistics by using the AWS CLI, run the [get-usage-statistics](../../../cli/latest/reference/macie2/get-usage-statistics.md "../../../cli/latest/reference/macie2/get-usage-statistics.md") command. You can optionally sort, filter, and
specify a time range for the query results. The following example retrieves
usage statistics for a Macie administrator account for the preceding 30 days. The results
are sorted in ascending order by AWS account ID.

For Linux, macOS, or Unix, using the backslash (\) line-continuation character to improve readability:

```
`$` `aws macie2 get-usage-statistics \
--sort-by '{"key":"`accountId`","orderBy":"`ASC`"}' \
--time-range `PAST_30_DAYS``
```

For Microsoft Windows, using the caret (^) line-continuation character to improve readability:

```
`C:\>` `aws macie2 get-usage-statistics ^
--sort-by={\"key\":\"`accountId`\",\"orderBy\":\"`ASC`\"} ^
--time-range `PAST_30_DAYS``
```

Where:

- `accountId` specifies the field to use to
  sort the results.
- `ASC` is the sort order to apply to the
  results, based on the value for the specified field
  (`accountId`).
- `PAST_30_DAYS` specifies the
  preceding 30 days as the time range for the data.

If the command runs successfully, Macie returns a `records` array.
The array contains an object for each account that’s included in the query
results. For example:

```
`{
 "records": [
 {
 "accountId": "111122223333",
 "automatedDiscoveryFreeTrialStartDate": "2024-01-28T16:00:00+00:00",
 "freeTrialStartDate": "2020-05-20T12:26:36.917000+00:00",
 "usage": [
 {
 "currency": "USD",
 "estimatedCost": "1.51",
 "type": "DATA_INVENTORY_EVALUATION"
 },
 {
 "currency": "USD",
 "estimatedCost": "65.18",
 "type": "AUTOMATED_SENSITIVE_DATA_DISCOVERY"
 },
 {
 "currency": "USD",
 "estimatedCost": "153.45",
 "serviceLimit": {
 "isServiceLimited": false,
 "unit": "TERABYTES",
 "value": 50
 },
 "type": "SENSITIVE_DATA_DISCOVERY"
 },
 {
 "currency": "USD",
 "estimatedCost": "0.98",
 "type": "AUTOMATED_OBJECT_MONITORING"
 }
 ]
 },
 {
 "accountId": "444455556666",
 "automatedDiscoveryFreeTrialStartDate": "2024-01-28T16:00:00+00:00",
 "freeTrialStartDate": "2020-05-18T16:26:36.917000+00:00",
 "usage": [
 {
 "currency": "USD",
 "estimatedCost": "1.58",
 "type": "DATA_INVENTORY_EVALUATION"
 },
 {
 "currency": "USD",
 "estimatedCost": "63.13",
 "type": "AUTOMATED_SENSITIVE_DATA_DISCOVERY"
 },
 {
 "currency": "USD",
 "estimatedCost": "145.12",
 "serviceLimit": {
 "isServiceLimited": false,
 "unit": "TERABYTES",
 "value": 50
 },
 "type": "SENSITIVE_DATA_DISCOVERY"
 },
 {
 "currency": "USD",
 "estimatedCost": "1.02",
 "type": "AUTOMATED_OBJECT_MONITORING"
 }
 ]
 }
 ],
 "timeRange": "PAST_30_DAYS"
}`
```

Where `estimatedCost` is the total estimated usage cost for the
associated usage metric (`type`) for an account:

- `DATA_INVENTORY_EVALUATION`, for monitoring and evaluating S3 general purpose
  buckets for security and access control.
- `AUTOMATED_SENSITIVE_DATA_DISCOVERY`, for analyzing S3
  objects with automated sensitive data discovery.
- `SENSITIVE_DATA_DISCOVERY`, for analyzing S3 objects with
  sensitive data discovery jobs.
- `AUTOMATED_OBJECT_MONITORING`, for evaluating and
  monitoring the account's S3 bucket inventory to identify S3 objects that
  are eligible for analysis by automated sensitive data discovery.
