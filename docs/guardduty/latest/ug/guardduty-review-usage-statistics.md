# Reviewing GuardDuty estimated usage

cost

The GuardDuty usage provides cost estimates based on the your usage over the last 30 days
per AWS Region. The estimated usage is different than your billing usage. For
information about how GuardDuty estimates the usage cost, see [Understanding how GuardDuty calculates usage
costs](monitoring_costs.md#usage-calculations "monitoring_costs.md#usage-calculations"). If you're a GuardDuty
administrator account, you can view the cost estimates for each member account, broken down by data
sources and accounts.

Choose your preferred access method to review the usage cost for your GuardDuty
account.

**To review estimated GuardDuty usage cost**

Console

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").

Make sure to use the GuardDuty administrator account. 2. In the navigation pane, choose **Usage**. 3. On the **Usage** page, a GuardDuty administrator
account with member accounts can view the **Estimated
organization cost** for the last 30 days. This is an
estimated total usage cost for your organization. 4. GuardDuty administrator accounts can either view the usage cost breakdown by data
source, or by accounts. Individual or standalone accounts can view
the breakdown by data source.

If you have member accounts – Select the **By
accounts** tab to view the statistics for each member
account.

Under the **By data sources** tab, when you
select a data source that has a usage cost associated with it, the
corresponding sum of the cost breakdown at the accounts level may
not always be the same.

API/CLI
Run the [GetUsageStatistics](../APIReference/API_GetUsageStatistics.md "../APIReference/API_GetUsageStatistics.md") API operation using the
credentials of GuardDuty administrator account account. Provide the following information to
run the command:

- (Required) provide the Regional GuardDuty detector ID of the account
  for which you want to retrieve the statistics.
- (Required) provide one of the types of statistics to retrieve:
  `SUM_BY_ACCOUNT | SUM_BY_DATA_SOURCE | SUM_BY_RESOURCE |
SUM_BY_FEATURE | TOP_ACCOUNTS_BY_FEATURE`.

Currently, `TOP_ACCOUNTS_BY_FEATURE` does not support
retrieving usage statistics for
`RDS_LOGIN_EVENTS`.

- (Required) provide one or more data sources or features to query
  your usage statistics.
- (Optional) provide a list of account IDs for which you want to
  retrieve usage statistics.

You can also use the AWS Command Line Interface. The following command is an example about
retrieving the usage statistics for all the data sources and features,
calculated by accounts. Make sure to replace the `detector-id`
with your own valid detector ID. For standalone accounts, this command
returns the usage cost over the past 30 days for your account only. If you
are a GuardDuty administrator account with member accounts, you see costs listed by account
for all members.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

Replace `SUM_BY_ACCOUNT` by the type with which you want to
calculate the usage statistics.

**To monitor cost for data sources
only**

```
aws guardduty get-usage-statistics --detector-id `12abc34d567e8fa901bc2d34e56789f0` --usage-statistic-type `SUM_BY_ACCOUNT` --usage-criteria '{"DataSources":["FLOW_LOGS", "CLOUD_TRAIL", "DNS_LOGS", "S3_LOGS", "KUBERNETES_AUDIT_LOGS", "EC2_MALWARE_SCAN"]}'
```

**To monitor cost for features**

```
aws guardduty get-usage-statistics --detector-id `12abc34d567e8fa901bc2d34e56789f0` --usage-statistic-type `SUM_BY_ACCOUNT` --usage-criteria '{"Features":["FLOW_LOGS", "CLOUD_TRAIL", "DNS_LOGS", "S3_DATA_EVENTS", "EKS_AUDIT_LOGS", "EBS_MALWARE_PROTECTION", "RDS_LOGIN_EVENTS", "LAMBDA_NETWORK_LOGS", "EKS_RUNTIME_MONITORING", "FARGATE_RUNTIME_MONITORING", "EC2_RUNTIME_MONITORING"]}'
```
