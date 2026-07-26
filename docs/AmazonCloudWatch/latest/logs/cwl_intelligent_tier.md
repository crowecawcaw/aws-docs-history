# Optimize storage costs with Amazon CloudWatch Logs Intelligent Tiering

Amazon CloudWatch Logs Intelligent Tiering automatically classifies your log data across three
access tiers based on access patterns: Standard, Infrequent Access, and Archive Instant
Access. With Intelligent Tiering, you can retain high-volume, long-retention logs at
lower-cost tiers without any operational overhead. Instead of filtering logs or offloading them to separate
storage solutions, you can keep them natively in CloudWatch Logs and benefit from the same query
experience regardless of which tier your data resides in.

CloudWatch Logs monitors access patterns and automatically reclassifies data not accessed for
30 days to the Infrequent Access tier, and data not accessed for 90 days to the Archive
Instant Access tier. When you access older data, CloudWatch Logs automatically promotes it back to the
Standard tier for 30 days. By consolidating all your logs in CloudWatch Logs, you get full
visibility in one tool—eliminating the operational overhead of managing multiple
storage solutions and reducing your mean time to resolution (MTTR) by querying, analyzing,
and alerting on all your logs in a single place.

To start optimizing storage costs, enable Intelligent Tiering at the account level
within a Region by using the CloudWatch console or by calling
`PutStorageTierPolicy`. After you enable Intelligent Tiering, it applies to
all log groups in your account within that Region.

Amazon CloudWatch Logs Intelligent Tiering is available in all AWS commercial regions except the
Middle East (Bahrain) and Middle East (UAE) Regions.

## CloudWatch Logs Intelligent Tiering access tiers

Your query experience remains the same regardless of which access tier your log data resides in.

Standard (default)

This is the default tier. All newly ingested log data starts in the
Standard tier. Log data remains in this tier as long as it is being
accessed. The Standard tier provides low latency and high-throughput
performance for queries, exports, live tail, and log retrieval.

Infrequent Access

If log data is not accessed for 30 consecutive days, it moves to the
Infrequent Access tier. The Infrequent Access tier provides the same
query latency and throughput as the Standard tier, at a lower storage
cost.

Archive Instant Access

If log data is not accessed for 90 consecutive days, it moves to the
Archive Instant Access tier. The Archive Instant Access tier provides
the same millisecond query latency as other tiers, at the lowest
storage cost.

## Actions that constitute access

The following access patterns automatically promote log data from the Infrequent
Access tier or Archive Instant Access tier back to the Standard tier. When any of
these operations read log events in a lower-cost tier, those log events move back
to the Standard tier for 30 days. The timer resets on each subsequent access.

###### Tier classification for log centralization

Accessing replicated logs in a destination account through [cross-account
cross-Region log centralization](CloudWatchLogs_Centralization.md "CloudWatchLogs_Centralization.md") only promotes the log data in
destination account.

- **Egress with query or alarm configuration**
  – Use `StartQuery` or `CreateScheduledQuery`
  to query log data with CloudWatch Logs Insights or to configure alarms on logs
- **Filtering and retrieving log events**
  – Use `FilterLogEvents` or
  `GetLogEvents` to read log events
- **Export** – Export log data to
  Amazon S3 with `CreateExportTask`

## Enabling CloudWatch Logs Intelligent Tiering

### Required permissions

To manage the storage tier for your account, you need the following IAM
permissions:

- `logs:PutStorageTierPolicy` – Required to set or change
  the storage tier for your account.
- `logs:GetStorageTierPolicy` – Required to retrieve the
  storage tier that is currently configured. Also required to enable
  Intelligent Tiering from the console.

Users with the `CloudWatchLogsFullAccess` managed policy already have
both permissions. Users with the `CloudWatchLogsReadOnlyAccess` managed
policy have the `logs:GetStorageTierPolicy` permission.

The following example shows a policy statement that grants both permissions:

```
{
    "Effect": "Allow",
    "Action": [
        "logs:PutStorageTierPolicy",
        "logs:GetStorageTierPolicy"
    ],
    "Resource": "*"
}
```

### Enable using the console

To enable Intelligent Tiering using the CloudWatch console:

1. Open the CloudWatch console at
   https://console.aws.amazon.com/cloudwatch/.
2. In the navigation pane, choose **Settings**.
3. On the **Settings** page, choose the
   **Logs** tab.
4. In the **Intelligent Tiering** section,
   choose **Enable**.

### Enable using the AWS CLI

To enable Intelligent Tiering, use the `put-storage-tier-policy`
command:

```
aws logs put-storage-tier-policy --storage-tier INTELLIGENT_TIERING
```

The command returns the storage tier that was set and the time it was last
updated:

```
{
    "storageTier": "INTELLIGENT_TIERING",
    "lastUpdatedTime": 1751328000000
}
```

To disable Intelligent Tiering, set the storage tier back to
`STANDARD`:

```
aws logs put-storage-tier-policy --storage-tier STANDARD
```

When you set the storage tier back to `STANDARD`, all log groups
in your account are billed at the Standard storage rate.

### Viewing your current configuration

To view the current storage tier for your account, use the
`get-storage-tier-policy` command:

```
aws logs get-storage-tier-policy
```

The command returns the current storage tier and the time it was last
updated:

```
{
    "storageTier": "INTELLIGENT_TIERING",
    "lastUpdatedTime": 1751328000000
}
```

## Monitoring storage per tier

When Intelligent Tiering is enabled, CloudWatch Logs publishes a vended metric that shows
the amount of data stored in each tier for each log group:

- **Namespace:**
  `AWS/Logs`
- **Metric name:**
  `StoredBytes`
- **Dimensions:**
  `LogGroupName`, `StorageType` (values:
  `Standard`, `Infrequent_Access`,
  `Archival_Instant_Access`)

You can use this metric to create CloudWatch dashboards that show per-tier storage
breakdown, set alarms on tier sizes, or track cost optimization over time.

###### Note

This metric is published once per day and might not reflect tier transitions
in real time.

## Pricing for CloudWatch Logs Intelligent Tiering

With Intelligent Tiering, you pay different storage rates based on the tier where
your data resides. There is no additional charge for enabling Intelligent Tiering,
and no charge for tier transitions. You pay only for the storage consumed in each
tier.

For more information about pricing, see
[Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

To view per-tier storage costs, use Athena and filter by the
`TimedStorage-ByteHrs` (Standard),
`TimedStorage-IA-ByteHrs` (Infrequent Access), and
`TimedStorage-AIA-ByteHrs` (Archive Instant Access) usage types. For more
information about CloudWatch Logs usage types in your bill, see
[Analyzing,
optimizing, and reducing CloudWatch costs](../monitoring/cloudwatch_billing.md "../monitoring/cloudwatch_billing.md").
