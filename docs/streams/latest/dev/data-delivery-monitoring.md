

# Monitoring data delivery
<a name="data-delivery-monitoring"></a>

 Use this topic to learn how to monitor your delivery using Amazon CloudWatch metrics, CloudWatch Logs, and AWS CloudTrail. 

## CloudWatch metrics
<a name="data-delivery-monitoring-metrics"></a>

 Each delivery publishes metrics to CloudWatch in the `AWS/Kinesis` namespace. Metric names are prefixed by destination type: `DeliveryToS3` for general purpose Amazon S3 deliveries and `DeliveryToIceberg` for streaming table deliveries. Use these metrics to monitor the health and performance of your delivery. 


**Amazon S3 delivery metrics (DeliveryToS3)**  

| Metric name | Unit | Description | 
| --- | --- | --- | 
| DeliveryToS3.DataFreshness | Seconds | The age of the oldest record not yet delivered to the destination. Rising values indicate delivery is falling behind. | 
| DeliveryToS3.BytesIn | Bytes | The volume of data read into the delivery path from the stream. | 
| DeliveryToS3.BytesProcessed | Bytes | The volume of data processed by the delivery. | 
| DeliveryToS3.BytesOut | Bytes | The volume of data written to the destination. | 
| DeliveryToS3.RecordCount | Count | The total number of records read from the stream. | 
| DeliveryToS3.SuccessfulRecordCount | Count | The number of records successfully delivered to the destination. | 
| DeliveryToS3.FailedRecordCount | Count | The number of records that failed delivery. A non-zero value is the key error signal. | 
| DeliveryToS3.DeliverySuccess | Count | The number of successful delivery operations. | 
| DeliveryToS3.DLQDeliverySuccess | Count | The number of records successfully written to the dead-letter queue. | 


**Streaming table delivery metrics (DeliveryToIceberg)**  

| Metric name | Unit | Description | 
| --- | --- | --- | 
| DeliveryToIceberg.DataFreshness | Seconds | The age of the oldest record not yet delivered to the table. Rising values indicate delivery is falling behind. | 
| DeliveryToIceberg.BytesIn | Bytes | The volume of data read into the delivery path from the stream. | 
| DeliveryToIceberg.BytesProcessed | Bytes | The volume of data processed by the delivery. | 
| DeliveryToIceberg.BytesOut | Bytes | The volume of data written to the table. | 
| DeliveryToIceberg.TotalRowCount | Count | The total number of rows read from the stream. | 
| DeliveryToIceberg.SuccessfulRowCount | Count | The number of rows successfully delivered to the table. | 
| DeliveryToIceberg.FailedRowCount | Count | The number of rows that failed delivery. A non-zero value is the key error signal. | 
| DeliveryToIceberg.CommitSuccess | Count | The number of successful Iceberg commits. | 
| DeliveryToIceberg.DLQDeliverySuccess | Count | The number of records successfully written to the dead-letter queue. | 

### Dimensions
<a name="data-delivery-monitoring-dimensions"></a>

 Delivery metrics are published with the following dimensions: 
+ `ChannelName` – The delivery name.
+ `ChannelId` – The unique identifier of the delivery.
+ `StreamName` – The name of the source Kinesis Data Streams stream.

**Note**  
 To target a specific delivery in a CloudWatch alarm, specify all three dimensions. For browsing or querying with `GetMetricData` and `ListMetrics`, you can filter by a subset of dimensions, such as `ChannelName` alone. 

### Recommended alarms
<a name="data-delivery-monitoring-alarms"></a>


**Recommended CloudWatch alarms for deliveries**  

| Alarm | Metric | Condition | Description | 
| --- | --- | --- | --- | 
| High failure rate | DeliveryToS3.FailedRecordCount | > 0 for 5 minutes | Records are failing delivery. Investigate schema mismatches or destination issues. | 
| Data freshness degradation | DeliveryToS3.DataFreshness | > threshold | Data delivery is falling behind. Investigate delivery issues such as missing permissions on the service execution role or throttling at the destination. | 
| No data delivered | DeliveryToS3.SuccessfulRecordCount | = 0 for 15 minutes | No records have been delivered. Verify the stream has data and the delivery is active. | 
| DLQ delivery failures | DeliveryToS3.DLQDeliverySuccess | = 0 when FailedRecordCount > 0 | Failed records cannot be written to the dead-letter queue. Check DLQ bucket permissions. | 

**Note**  
 The preceding alarms use the `DeliveryToS3` metrics for an Amazon S3 delivery. For a streaming table delivery, use the equivalent `DeliveryToIceberg` metrics (`DeliveryToIceberg.FailedRowCount`, `DeliveryToIceberg.DataFreshness`, `DeliveryToIceberg.SuccessfulRowCount`, and `DeliveryToIceberg.DLQDeliverySuccess`). 

## CloudWatch Logs
<a name="data-delivery-monitoring-logs"></a>

 Each delivery can publish detailed logs to CloudWatch Logs for debugging and operational visibility. 
+ **Default log group** – `/aws/kinesis/{{channelName}}/{{channelId}}`
+ **Log stream** – `DestinationDelivery`

### Enabling CloudWatch Logs via CLI
<a name="data-delivery-monitoring-logs-enable"></a>

 Enable CloudWatch Logs when creating or updating a delivery using the AWS CLI: 

```
aws kinesis create-channel \
    --channel-name "my-channel" \
    --service-execution-role-arn "arn:aws:iam::123456789012:role/my-channel-role" \
    --stream-configuration-list '[
        {
            "StreamARN": "arn:aws:kinesis:us-east-1:123456789012:stream/my-stream",
            "RecordConfiguration": { "RecordFormatType": "JSON" }
        }
    ]' \
    --s3-destination-configuration '{
        "StorageConfiguration": {
            "BucketARN": "arn:aws:s3:::my-destination-bucket",
            "ExpectedBucketOwner": "123456789012",
            "CompressionType": "GZIP"
        }
    }' \
    --logging-configuration '{
        "CloudWatchLogs": {
            "Enabled": true
        }
    }'
```

 When you enable CloudWatch Logs without specifying a log group, the delivery uses the default log group `/aws/kinesis/{{channelName}}/{{channelId}}`. If you specify a custom `LogGroupName`, make sure the service execution role's CloudWatch Logs permissions are scoped to that same log group. For the required permissions, see [IAM permissions for data delivery](data-delivery-iam.md). 

 You can also enable or update CloudWatch Logs on an existing delivery with the `update-channel` command, passing the same `--logging-configuration` value. 

### Required permissions
<a name="data-delivery-monitoring-logs-permissions"></a>

 To enable CloudWatch Logs, the delivery's service execution role must have the following permissions: 
+ `logs:CreateLogGroup`
+ `logs:CreateLogStream`
+ `logs:PutLogEvents`

 Scope these permissions to the specific log group ARN. See [Optional CloudWatch Logs permissions](data-delivery-iam.md#data-delivery-iam-cloudwatch-logs) for the full policy example. 

## AWS CloudTrail logging
<a name="data-delivery-monitoring-cloudtrail"></a>

 All delivery API calls are recorded by AWS CloudTrail. The following is an example AWS CloudTrail event for a `CreateChannel` call: 

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROA1EXAMPLE:user-session",
        "arn": "arn:aws:sts::<account-id>:assumed-role/<role-name>/user-session",
        "accountId": "<account-id>"
    },
    "eventTime": "2026-07-20T20:00:00Z",
    "eventSource": "kinesis.amazonaws.com",
    "eventName": "CreateChannel",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.1",
    "userAgent": "aws-cli/2.x",
    "requestParameters": {
        "streamName": "my-stream",
        "channelName": "my-channel"
    },
    "responseElements": {
        "channelARN": "arn:aws:kinesis:us-east-1:<account-id>:channel/<channel-id>"
    },
    "requestID": "a1b2c3d4-example",
    "eventID": "e5f6g7h8-example",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "recipientAccountId": "<account-id>"
}
```