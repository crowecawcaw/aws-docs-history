Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Monitoring with Amazon CloudWatch Logs

You can monitor Amazon Monitron live data export using Amazon CloudWatch Logs. When a measurement fails
to export, Amazon Monitron will send a log event to your CloudWatch Logs. You can also set up a metric
filter on the error log to generate metrics and set up alarms. An alarm can watch
for certain thresholds and send notifications or take actions when those thresholds
are met. For more information, see [the CloudWatch User
Guide](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md").

Amazon Monitron sends log events to the /aws/monitron/data-export/{HASH_ID} log
group.

The log event has the following JSON format:

```
{
    "assetDisplayName": "string",
    "destination": "string",
    "errorCode": "string",
    "errorMessage": "string",
    "eventId": "string",
    "positionDisplayName": "string",
    "projectDisplayName": "string",
    "projectName": "string",
    "sensorId": "string",
    "siteDisplayName": "string",
    "timestamp": "string"
}
```

assetDisplayName

- The asset name displayed in the App
- Type: String

destination

- The ARN of the Kinesis data stream
- Type: String
- Pattern:
  arn:aws:kinesis:{{REGION}}:{{AWS\_ACCOUNT\_ID}}:stream/{{STREAM\_NAME}}

errorCode

- The error code
- Type: String
- Valid Values: `INTERNAL_SEVER_ERROR |
 KINESIS_RESOURCE_NOT_FOUND |
 KINESIS_PROVISIONED_THROUGHPUT_EXCEEDED | KMS_ACCESS_DENIED
| KMS_NOT_FOUND | KMS_DISABLED | KMS_INVALID_STATE | KMS_THROTTLING` errorMessage <br>• The detailed error message <br>• Type: String eventId <br>• The unique event ID corresponding to each measurement export <br>• Type: String positionDisplayName <br>• The sensor position name displayed in the App <br>• Type: String sensorId <br>• The physical ID of the sensor from which the measurement is sent <br>• Type: String siteDisplayName <br>• The site name displayed in the App <br>• Type: String timestamp <br>• The timestamp when the measurement is received by Amazon Monitron service in UTC <br>• Type: String <br>• Pattern: yyyy-mm-dd hh:mm:ss.SSS
