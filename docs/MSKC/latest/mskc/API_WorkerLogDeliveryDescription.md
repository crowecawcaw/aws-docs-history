# WorkerLogDeliveryDescription

Workers can send worker logs to different destination types. This configuration
specifies the details of these destinations.

## Contents

**cloudWatchLogs**

Details about delivering logs to Amazon CloudWatch Logs.

Type: [CloudWatchLogsLogDeliveryDescription](API_CloudWatchLogsLogDeliveryDescription.md "API_CloudWatchLogsLogDeliveryDescription.md") object

Required: No

**firehose**

Details about delivering logs to Amazon Kinesis Data Firehose.

Type: [FirehoseLogDeliveryDescription](API_FirehoseLogDeliveryDescription.md "API_FirehoseLogDeliveryDescription.md") object

Required: No

**s3**

Details about delivering logs to Amazon S3.

Type: [S3LogDeliveryDescription](API_S3LogDeliveryDescription.md "API_S3LogDeliveryDescription.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kafkaconnect-2021-09-14/WorkerLogDeliveryDescription.md "../../../goto/SdkForCpp/kafkaconnect-2021-09-14/WorkerLogDeliveryDescription.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/WorkerLogDeliveryDescription.md "../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/WorkerLogDeliveryDescription.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/WorkerLogDeliveryDescription.md "../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/WorkerLogDeliveryDescription.md")
