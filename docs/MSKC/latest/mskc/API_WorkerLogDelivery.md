

# WorkerLogDelivery
<a name="API_WorkerLogDelivery"></a>

Workers can send worker logs to different destination types. This configuration specifies the details of these destinations.

## Contents
<a name="API_WorkerLogDelivery_Contents"></a>

 ** cloudWatchLogs **   <a name="MSKC-Type-WorkerLogDelivery-cloudWatchLogs"></a>
Details about delivering logs to Amazon CloudWatch Logs.  
Type: [CloudWatchLogsLogDelivery](API_CloudWatchLogsLogDelivery.md) object  
Required: No

 ** firehose **   <a name="MSKC-Type-WorkerLogDelivery-firehose"></a>
Details about delivering logs to Amazon Kinesis Data Firehose.  
Type: [FirehoseLogDelivery](API_FirehoseLogDelivery.md) object  
Required: No

 ** s3 **   <a name="MSKC-Type-WorkerLogDelivery-s3"></a>
Details about delivering logs to Amazon S3.  
Type: [S3LogDelivery](API_S3LogDelivery.md) object  
Required: No

## See Also
<a name="API_WorkerLogDelivery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/WorkerLogDelivery) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/WorkerLogDelivery) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/WorkerLogDelivery) 