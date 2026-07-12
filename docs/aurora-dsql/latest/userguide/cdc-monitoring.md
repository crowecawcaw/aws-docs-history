# Monitoring streams

When Aurora DSQL encounters an error delivering a CDC record, the stream transitions to
`IMPAIRED` status. An impaired stream continues to process and deliver other
records—Aurora DSQL retries only the failing record. Aurora DSQL measures replication lag from the
oldest undelivered record, and the lag grows until you resolve the issue. Aurora DSQL retains
undelivered changes internally for one week.

If you resolve the underlying issue within this window, the next retry succeeds, the
error state clears, and the stream transitions back to `ACTIVE`. Fix the external
issue (IAM policy, AWS KMS key, Amazon Kinesis capacity, and so on) and Aurora DSQL retries
automatically.

If the replication lag exceeds the failure threshold, the stream transitions to
`FAILED`.

###### Important

A failed stream can't recover. You must delete the failed stream and create a
new one.

## Stream lifecycle

A stream transitions through the following statuses during its lifecycle:

- **`CREATING`** – Aurora DSQL is setting up
  the stream. Aurora DSQL doesn't deliver CDC records yet.
- **`ACTIVE`** – The stream is operational
  and delivering CDC records to the target.
- **`IMPAIRED`** – The stream has
  encountered an issue that requires your action. Aurora DSQL retries the failing record with
  exponential backoff, although other records can continue delivering. Aurora DSQL measures
  replication lag from the oldest undelivered record, and the lag grows until you resolve
  the issue. Aurora DSQL buffers undelivered changes internally for one week. See
  [Error code reference](#cdc-failure-reasons "#cdc-failure-reasons").
- **`FAILED`** – The stream has encountered
  a persistent error and is no longer delivering CDC records. A failed stream can't recover
  and you must delete it. See
  [Error code reference](#cdc-failure-reasons "#cdc-failure-reasons") for the conditions
  that cause a stream to enter this state.
- **`DELETING`** – Aurora DSQL is removing
  stream resources.
- **`DELETED`** – Aurora DSQL has deleted the
  stream. After deletion completes, `GetStream` returns a
  `ResourceNotFoundException`.

Call `GetStream` to view the stream status at any time. When the stream is
`IMPAIRED` or `FAILED`, the response includes a
`statusReason` object with the error code and timestamp. For more details
about the `GetStream` response fields, see
[GetStream](../APIReference/API_GetStream.md "../APIReference/API_GetStream.md") in the
Amazon Aurora DSQL API Reference.

## Troubleshooting an impaired or failed stream

Follow these steps when a CDC stream becomes impaired or fails. If the stream is
`FAILED`, you can't recover it—delete the stream, resolve the
underlying issue, and create a new one.

1. **Get the stream status.** Call `GetStream`
   and verify the `status` field. If the status is `ACTIVE`, the stream
   is healthy.

```
aws dsql get-stream \
  --cluster-identifier `cluster-id` \
  --stream-identifier `stream-id` \
  --region `region`
```

2. **Read the error code.** If the status is
   `IMPAIRED` or `FAILED`, the response includes a
   `statusReason` object. The `error` field contains the error
   code.

```
{
    "status": "IMPAIRED",
    "statusReason": {
        "error": "KINESIS_THROUGHPUT_EXCEEDED",
        "updatedAt": "2025-01-15T14:30:00Z"
    }
}
```

3. **Follow the remediation.** If the stream is
   `IMPAIRED`, look up the error code in the following table and apply the
   recommended fix. Aurora DSQL retries automatically after you resolve the underlying issue. If
   the stream is `FAILED`, delete it, resolve the issue, and create a new
   stream.

## Error code reference

The following table describes each error code, its cause, whether the stream can
recover, and the steps to resolve it.

| Error code                    | Cause                                                                                                                                                                        | Recoverable? | How to resolve                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `KINESIS_THROUGHPUT_EXCEEDED` | Your Kinesis data stream exceeded its throughput limit, or AWS KMS throttled<br>encryption operations on the Kinesis data stream, and the replication lag has<br>grown.      | Yes          | Increase the number of shards on your Kinesis data stream, or switch to on-demand<br>capacity mode. If the Kinesis data stream uses an AWS KMS customer managed key, verify<br>that the key's request quota is large enough. After you increase capacity, Aurora DSQL<br>retries automatically.                                                                                                                                                                                                          |
| `KINESIS_STREAM_NOT_FOUND`    | The target Kinesis data stream no longer exists.                                                                                                                             | No           | The stream transitions directly to `FAILED`. Delete the CDC stream<br>and create a new one pointing to a valid Kinesis data stream.                                                                                                                                                                                                                                                                                                                                                                      |
| `ROLE_ACCESS_DENIED`          | Aurora DSQL can't assume the IAM role specified in the target definition. The<br>AWS STS `AssumeRole` call returned `AccessDenied`.                                          | Yes          | Verify the role's trust policy allows the Aurora DSQL service principal<br>(`dsql.amazonaws.com`) to assume it. Verify the<br>`aws:SourceAccount` and `aws:SourceArn` conditions match your<br>cluster. For details, see<br>[Service role trust policy](cdc-iam.md#cdc-iam-trust-policy "cdc-iam.md#cdc-iam-trust-policy"). After you<br>fix the trust policy, Aurora DSQL retries automatically.                                                                                                        |
| `KINESIS_ACCESS_DENIED`       | The assumed role doesn't have permission to write to the Kinesis data stream.<br>Kinesis returned `AccessDeniedException`.                                                   | Yes          | Add `kinesis:PutRecord` and `kinesis:PutRecords` permissions<br>to the role's policy for the target Kinesis data stream Amazon Resource Name (ARN).<br>After you fix the policy, Aurora DSQL retries automatically.                                                                                                                                                                                                                                                                                      |
| `KINESIS_KMS_ACCESS_DENIED`   | The assumed role doesn't have permission to use the AWS KMS key that encrypts<br>the Kinesis data stream. This error covers AWS KMS access denial and invalid key<br>states. | Yes          | Verify the role has `kms:GenerateDataKey` permission on the AWS KMS<br>key that the Kinesis data stream uses. Also verify that the AWS KMS key is in an enabled<br>and valid state. This key is the encryption key on the Kinesis data stream, not the<br>cluster's AWS KMS key. For details, see<br>[Service role permissions policy](cdc-iam.md#cdc-iam-permissions-policy "cdc-iam.md#cdc-iam-permissions-policy"). After you fix the permissions or key<br>state, Aurora DSQL retries automatically. |
| `KINESIS_OVERSIZE_RECORD`     | A CDC record exceeded the maximum record size configured on the Kinesis data<br>stream.                                                                                      | Yes          | Increase `MaxRecordSizeInKiB` on the Kinesis data stream to<br>`10240` (10 MiB). You can update this setting on an existing Kinesis data<br>stream without deleting it. After you increase the limit, Aurora DSQL retries the oversized<br>record automatically and the stream transitions back to<br>`ACTIVE`.                                                                                                                                                                                          |
| `CLUSTER_CMK_INACCESSIBLE`    | The AWS KMS customer managed key that encrypts the Aurora DSQL cluster is<br>inaccessible.                                                                                   | Yes          | Verify the AWS KMS key policy and key state. Re-enable or restore access to the<br>key. After the key becomes accessible again, the stream transitions back to<br>`ACTIVE`.                                                                                                                                                                                                                                                                                                                              |

The preceding table lists every `StreamFailureErrorCode` value. For
details about the `statusReason` response field, see
[GetStream](../APIReference/API_GetStream.md "../APIReference/API_GetStream.md") in the
[Amazon Aurora DSQL API
Reference](CHAP_api_reference.md "CHAP_api_reference.md").

## Recovering an impaired stream

Most errors first transition the stream to `IMPAIRED`. An impaired stream
continues to process other records and retries the failing record automatically. A
`FAILED` stream isn't recoverable—you must delete it and create a new
one.

- **For recoverable errors:** fix the external issue
  (IAM policy, AWS KMS key, Kinesis capacity, or Kinesis record size limit). The next
  successful retry clears the error state and transitions the stream back to
  `ACTIVE`.
- **For `KINESIS_STREAM_NOT_FOUND`:** the
  stream transitions directly to `FAILED`. Delete the failed stream and create
  a new one pointing to a valid Kinesis data stream.

For all other error codes, if the replication lag exceeds the failure threshold before
you resolve the issue, the stream transitions from `IMPAIRED` to
`FAILED`. A failed stream can't transition back to `ACTIVE`.
Delete the failed stream, resolve the underlying issue, and create a new one.

## Monitoring stream health

Use CloudWatch metrics and the `GetStream` API to monitor stream health. CloudWatch
metrics provide continuous visibility into CDC pipeline performance, and
`GetStream` provides the specific error code when a stream is impaired or
failed.

For the full list of CDC metrics, including `IsImpaired`,
`BehindSourceLag`, `PublishedBytes`, and
`PublishedRecords`, see
[CloudWatch metrics for CDC streams](#cdc-cloudwatch-metrics "#cdc-cloudwatch-metrics"). For more
details about the `GetStream` response fields, see
[GetStream](../APIReference/API_GetStream.md "../APIReference/API_GetStream.md") in the
Amazon Aurora DSQL API Reference.

## CloudWatch metrics for CDC streams

Use the following CloudWatch metrics to monitor the health and throughput of each CDC
stream. Aurora DSQL publishes these metrics in the `AWS/AuroraDSQL` namespace with
the dimensions `ClusterId` and `StreamId`. The last metric is a
standard Amazon Kinesis metric in the `AWS/Kinesis` namespace that measures
downstream reading lag.

###### Note

Aurora DSQL also publishes the `BytesStreamed` and `StreamDPU`
metrics in the `AWS/AuroraDSQL` namespace for usage and billing tracking.
For descriptions, see
[CDC stream metrics](cloudwatch-monitoring.md#cdc-stream-metrics "cloudwatch-monitoring.md#cdc-stream-metrics").

| Metric name                                             | Useful statistic | Description                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `IsImpaired`                                            | Maximum          | Indicates whether the stream is impaired. The value is `1` when the<br>stream is in the `IMPAIRED` state, and `0` when the stream is<br>healthy. Aurora DSQL emits this metric continuously for each active or impaired stream.<br>Use this metric to create a CloudWatch alarm that notifies you when a stream becomes<br>impaired. |
| `BehindSourceLag`                                       | Average          | The delay, in milliseconds, between when a transaction commits in Aurora DSQL and when<br>the CDC system processes the resulting record. A rising value indicates that the CDC<br>pipeline is falling behind the write workload.                                                                                                     |
| `PublishedBytes`                                        | Sum              | The total bytes of CDC records that Aurora DSQL wrote to the target during the period.<br>Use this metric together with your Kinesis shard count to determine whether you've<br>provisioned enough write capacity.                                                                                                                   |
| `PublishedRecords`                                      | Sum              | The total number of CDC records that Aurora DSQL wrote to the target during the period.<br>Each committed row change produces one record.                                                                                                                                                                                            |
| `GetRecords.IteratorAgeMilliseconds`<br>(`AWS/Kinesis`) | Average          | A standard Kinesis metric that reports the age of the last record read from the<br>Kinesis data stream by your downstream app, in milliseconds. Use the<br>`StreamName` dimension. A rising value indicates that your downstream app<br>can't keep up with the rate at which Aurora DSQL writes CDC records to<br>Kinesis.           |

The Aurora DSQL console's **Monitoring** tab shows an
**Average end-to-end latency** value that combines
`BehindSourceLag` (CDC source latency) and
`GetRecords.IteratorAgeMilliseconds` (Kinesis reader lag). This combined value
represents the total delay from database commit to downstream read.

## Monitoring best practices

Use the following practices to detect and resolve CDC pipeline issues before they
affect your downstream systems.

###### Set alarms on `BehindSourceLag`

Create a CloudWatch alarm that fires when `BehindSourceLag` exceeds a
threshold that matters to your workload. For example, set 60 seconds for a
one-minute latency target. A sustained increase in this metric means the CDC pipeline is
falling behind. If the lag reaches the failure threshold, the stream transitions to FAILED.
Catching the trend gives you time to increase Kinesis capacity or investigate throughput
bottlenecks before the stream degrades.

###### Monitor `GetRecords.IteratorAgeMilliseconds` on the Kinesis side

Even when Aurora DSQL delivers records on time, your downstream app can fall behind.
Create a CloudWatch alarm on `GetRecords.IteratorAgeMilliseconds` (in the
`AWS/Kinesis` namespace, dimension `StreamName`) to detect
downstream lag independently. If this metric rises and `BehindSourceLag` stays
flat, the bottleneck is in your downstream app, not in Aurora DSQL.

###### Track `PublishedBytes` against Kinesis shard capacity

Each Kinesis shard supports up to 1 MiB per second for writes. Compare the
`PublishedBytes` Sum per minute against your total shard write capacity (number
of shards × 60 MiB per minute). If usage approaches 80 percent, add shards or
switch to on-demand capacity mode before throttling triggers
`KINESIS_THROUGHPUT_EXCEEDED`.

###### Alarm on `IsImpaired` for instant impairment detection

Create a CloudWatch alarm that fires when `IsImpaired` Maximum is greater than
or equal to `1` for one evaluation period. This gives you a direct signal when
a stream enters the `IMPAIRED` state, without polling the API. After the alarm
fires, call `GetStream` to read the `statusReason.error` field and
follow the remediation steps in
[Troubleshooting an impaired or failed stream](#cdc-troubleshooting "#cdc-troubleshooting").

###### Poll `GetStream` for detailed status

The `IsImpaired` metric tells you that a stream is impaired, but the
`GetStream` API provides the specific error code and timestamp. Poll
`GetStream` on a schedule (for example, every five minutes) or in response to
an `IsImpaired` alarm. The `statusReason.error` field tells you
what went wrong. Pair this with the troubleshooting steps in
[Troubleshooting an impaired or failed stream](#cdc-troubleshooting "#cdc-troubleshooting") for quick
resolution.

###### Use dashboards to correlate metrics

Create a CloudWatch dashboard that shows `IsImpaired`,
`BehindSourceLag`, `PublishedRecords`,
`PublishedBytes`, and `GetRecords.IteratorAgeMilliseconds` side by
side. Correlating these metrics helps you distinguish between a CDC pipeline issue (rising
`BehindSourceLag`) and a downstream reading issue (rising
`IteratorAge` with stable `BehindSourceLag`).
