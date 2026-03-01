# Diagnosing throttling

When your application experiences throttling, DynamoDB provides detailed exception
information and targeted CloudWatch metrics to help you diagnose these events.

This section presents a systematic approach to understanding throttling events in your DynamoDB
applications. It shows how to interpret throttling exceptions, correlate them with CloudWatch
metrics for deeper insights, and understand what changes would reduce throttling in your
DynamoDB applications.

## Understanding throttling exceptions

When DynamoDB throttles a request, it returns specific exceptions with
detailed diagnostic information. For example, in Java,
these include `ProvisionedThroughputExceededException`,
`RequestLimitExceeded`, or `ThrottlingException`.

Each exception includes `ThrottlingReasons`, a collection of individual
`ThrottlingReason` containing two key fields to help you identify and
understand the throttling:

- **A reason** - A concatenated field following the
  format
  `<ResourceType><OperationType><LimitType>`
- **A resource ARN** - The Amazon Resource Name
  (ARN) of the affected table or index

The reason field follows a consistent patern that helps you understand exactly
what's happening:

- **ResourceType** (What is being throttled):
  `Table` or `Index`
- **OperationType** (What kind of operation):
  `Read` or `Write`
- **LimitType** (Why the throttling
  occurred):
  - `KeyRangeThroughputExceeded`: This occurs when a specific
    partition backing your table or index has consumed read or write
    capacity exceeding the internal per-partition throughput limits.
  - `ProvisionedThroughputExceeded`: This happens on a
    provisioned table or global secondary index when the read or write
    consumption rate has exceeded the provisioned amount.
  - `AccountLimitExceeded`: This happens on an on-demand table
    or index when the read or write consumption rate has exceeded the
    maximum consumption rate for a table and its indexes as set at the
    account level. You can request a raise in this quota.
  - `MaxOnDemandThroughputExceeded`: This happens on an on-demand table or index when
    the read or write consumption rate has exceeded the user-provided maximum consumption rate configured
    for the table or index. You can raise this value yourself to any value up to the account limit or set to -1 to
    indicate no user-provided limit.

The resource ARN identifies exactly which table or index is being throttled:

- For tables:
  `arn:aws:dynamodb:[region]:[account-id]:table/[table-name]`
- For indexes:
  `arn:aws:dynamodb:[region]:[account-id]:table/[table-name]/index/[index-name]`

Examples of complete throttling reasons:

- `TableReadProvisionedThroughputExceeded`
- `IndexWriteAccountLimitExceeded`

This helps identify exactly what resource is being throttled, what type of operation
caused it, and why the throttling occurred.

### Example exceptions

#### Example 1: Provisioned capacity exceeded on a GSI

```
{
    "ThrottlingReasons": [
        {
            "reason": "IndexWriteProvisionedThroughputExceeded",
            "resource": "arn:aws:dynamodb:us-west-2:123456789012:table/CustomerOrders/index/OrderDateIndex"
        }
    ],
    "awsErrorDetails": {
        "errorCode": "ProvisionedThroughputExceeded",
        "errorMessage": "The level of configured provisioned throughput for the index was exceeded",
        "serviceName": "DynamoDB",
        "sdkHttpResponse": {
            "statusText": "Bad Request",
            "statusCode": 400
        }
    }
}
```

In this example, the application receives a
`ProvisionedThroughputExceededException` with the reason
`IndexWriteProvisionedThroughputExceeded`. Writes to the
`OrderDateIndex` are being throttled because the write
consumption has exceeded the GSI's configured provisioned write capacity.

#### Example 2: On-demand maximum throughput exceeded

```
{
    "ThrottlingReasons": [
        {
            "reason": "TableReadMaxOnDemandThroughputExceeded",
            "resource": "arn:aws:dynamodb:us-east-1:123456789012:table/UserSessions"
        }
    ],
    "awsErrorDetails": {
        "errorMessage": "Throughput exceeds the maximum OnDemandThroughput configured on table or index",
        "errorCode": "ThrottlingException",
        "serviceName": "DynamoDB",
        "sdkHttpResponse": {
            "statusText": "Bad Request",
            "statusCode": 400
        }
    }
}
```

In this example, reads from the `UserSessions` table are being
throttled because they exceed the configured maximum on-demand throughput limit
on the table.

## DynamoDB throttling diagnosis framework

When your application encounters throttling, follow these steps to diagnose and
resolve the issue.

### Step 1 - Analyze the `ThrottlingReason` details

1. Check the **reason** field to
   identify the specific reason for throttling.
   The reason details the type of resource throttled (table or index),
   the type of operation causing the throttling event (read or write),
   and the limit type that was exceeded (partition, provisioned throughput, account limit).
2. Check the **resourceArn** field to identify
   which resource (table or GSI) is being throttled.
3. Use this combined information to understand the full context of the
   throttling issue.

For example, consider this scenario where you receive the following
exception `ProvisionedThroughputExceededException` with a
throttling reason `TableWriteKeyRangeThroughputExceeded`. The
impacted resourceARN is
`arn:aws:dynamodb:us-west-2:123456789012:table/CustomerOrders`.

This combination informs you that write operations to your
`CustomerOrders` table are being throttled. The throttling is
occurring at the partition level (not the table level, which would show as
`TableWriteProvisionedThroughputExceeded`). The root cause is
that you've exceeded the maximum throughput capacity for a specific
partition key value or range, indicating a hot partition issue.

Understanding this relationship between the exception elements helps you
implement the appropriate mitigation strategy - in this case, addressing the
hot partition rather than increasing the table's overall provisioned
capacity.

### Step 2 - Identify and analyze the related CloudWatch metrics

1. **Identify your metrics:** Each throttling
   reason in DynamoDB directly corresponds to specific CloudWatch metrics that you can
   monitor to track and analyze throttling events. You can systematically
   derive the appropriate CloudWatch metric names from the throttling reason.
2. Match your throttling reason to the corresponding CloudWatch metrics using
   this reference table:

| Complete throttling reasons and CloudWatch metrics reference | Category                                       | Throttling reason                       | Primary CloudWatch metrics |
| ------------------------------------------------------------ | ---------------------------------------------- | --------------------------------------- | -------------------------- |
| Provisioned capacity exceeded                                | TableReadProvisionedThroughputExceeded         | ReadProvisionedThroughputThrottleEvents |
| TableWriteProvisionedThroughputExceeded                      | WriteProvisionedThroughputThrottleEvents       |
| IndexReadProvisionedThroughputExceeded                       | ReadProvisionedThroughputThrottleEvents (GSI)  |
| IndexWriteProvisionedThroughputExceeded                      | WriteProvisionedThroughputThrottleEvents (GSI) |
| Partition limits exceeded                                    | TableReadKeyRangeThroughputExceeded            | ReadKeyRangeThroughputThrottleEvents    |
| TableWriteKeyRangeThroughputExceeded                         | WriteKeyRangeThroughputThrottleEvents          |
| IndexReadKeyRangeThroughputExceeded                          | ReadKeyRangeThroughputThrottleEvents (GSI)     |
| IndexWriteKeyRangeThroughputExceeded                         | WriteKeyRangeThroughputThrottleEvents (GSI)    |
| On-demand maximum exceeded                                   | TableReadMaxOnDemandThroughputExceeded         | ReadMaxOnDemandThroughputThrottleEvents |
| TableWriteMaxOnDemandThroughputExceeded                      | WriteMaxOnDemandThroughputThrottleEvents       |
| IndexReadMaxOnDemandThroughputExceeded                       | ReadMaxOnDemandThroughputThrottleEvents (GSI)  |
| IndexWriteMaxOnDemandThroughputExceeded                      | WriteMaxOnDemandThroughputThrottleEvents (GSI) |
| Account limits exceeded                                      | TableReadAccountLimitExceeded                  | ReadAccountLimitThrottleEvents          |
| TableWriteAccountLimitExceeded                               | WriteAccountLimitThrottleEvents                |
| IndexReadAccountLimitExceeded                                | ReadAccountLimitThrottleEvents (GSIs)          |
| IndexWriteAccountLimitExceeded                               | WriteAccountLimitThrottleEvents (GSIs)         |

For example, if you received
`IndexWriteProvisionedThroughputExceeded`, at a minimum, you
should monitor the `WriteProvisionedThroughputThrottleEvents`
CloudWatch metric for the specific index identified in the
`ResourceArn`. 3. Monitor these metrics in CloudWatch to understand the frequency and timing of
the throttling events, differentiate between read and write throttling,
identify time patterns when throttling increases, and track your capacity
utilization trends.

DynamoDB publishes detailed metrics for each table and global secondary
index. The metrics (`ReadThrottleEvents`,
`WriteThrottleEvents`, and `ThrottledRequests`)
aggregate all throttling events across your table and its indexes.

### Step 3 - Identify your throttled keys and high access rates using CloudWatch Contributor Insights (for partition-related throttling)

If you identified partition-related issues in Step 1 (such as
`KeyRangeThroughputExceeded` errors), CloudWatch Contributor Insights for
DynamoDB can help you diagnose which specific keys are driving your traffic and
experiencing throttling events in your table or index.

1. Enable CloudWatch Contributor Insights for your throttled table or index based
   on your `ResourceARN`.

You can choose the _Throttled keys_ mode
to focus exclusively on the most throttled keys. This mode is ideal for
continuous monitoring as it only processes events when throttling occurs.
Alternatively, the _Accessed and throttled
keys_ mode helps you look for patterns in your most accessed
keys. 2. Analyze the reports to identify problematic patterns. Look for keys with
disproportionately high access or throttling rates, correlate throttling and
traffic patterns. You can create integrated dashboards combining Contributor
Insights graphs and DynamoDB CloudWatch metrics.

For detailed information about enabling and using CloudWatch Contributor Insights, see
[Using CloudWatch Contributor Insights for
DynamoDB](contributorinsights.md "contributorinsights.md").

### Step 4 - Determine the appropriate solution

After diagnosing the specific cause of throttling, implement recommended solution
based on your specific context. The appropriate solution depends on multiple
factors, including your throttling scenario, table's capacity mode, table and key
design decisions, access patterns and query efficiency, global and secondary index
configuration, and overall system architecture and integration points.

For detailed solutions to address your specific throttling scenarios, see the
[DynamoDB throttling resolution guide](troubleshooting-throttling-diagnostics.md "troubleshooting-throttling-diagnostics.md") section. This resource
provides targeted remediation strategies customized to your particular throttling
reason and capacity mode configuration.

### Step 5 - Monitor your progress

1. Track your CloudWatch metrics that correspond to your throttling
   scenario.
2. Validate that your mitigation strategies are effective by observing a
   decrease in throttling events.
