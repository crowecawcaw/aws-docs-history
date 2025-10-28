# Troubleshooting Amazon S3

Check the following if data is not delivered to your Amazon Simple Storage Service (Amazon S3) bucket.

- Check the Firehose `IncomingBytes` and `IncomingRecords`
  metrics to make sure that data is sent to your Firehose stream successfully. For more
  information, see [Monitor Amazon Data Firehose with
  CloudWatch metrics](monitoring-with-cloudwatch-metrics.md "monitoring-with-cloudwatch-metrics.md").
- If data transformation with Lambda is enabled, check the Firehose
  `ExecuteProcessingSuccess` metric to make sure that Firehose has
  tried to invoke your Lambda function. For more information, see [Monitor Amazon Data Firehose with
  CloudWatch metrics](monitoring-with-cloudwatch-metrics.md "monitoring-with-cloudwatch-metrics.md").
- Check the Firehose `DeliveryToS3.Success` metric to make sure that
  Firehose has tried putting data to your Amazon S3 bucket. For more information, see
  [Monitor Amazon Data Firehose with
  CloudWatch metrics](monitoring-with-cloudwatch-metrics.md "monitoring-with-cloudwatch-metrics.md").
- Enable error logging if it is not already enabled, and check error logs for
  delivery failure. For more information, see [Monitor Amazon Data Firehose Using
  CloudWatch Logs](monitoring-with-cloudwatch-logs.md "monitoring-with-cloudwatch-logs.md").
- If you see an error message in the log saying _“Firehose encountered InternalServerError when calling Amazon S3 service. The operation
  will be retried; if the error persists, please contact S3 for resolution.”_, it could be due to the significant increase in request
  rates on a single partition in S3. You can optimize S3 prefix design patterns to mitigate the issue. For more information, see
  [Best practices design patterns: optimizing Amazon S3 performance](../../../AmazonS3/latest/userguide/optimizing-performance.md "../../../AmazonS3/latest/userguide/optimizing-performance.md").
  If this does not resolve the issue, contact AWS Support for further assistance.
- Make sure that the Amazon S3 bucket that is specified in your Firehose stream still
  exists.
- If data transformation with Lambda is enabled, make sure that the Lambda
  function that is specified in your Firehose stream still exists.
- Make sure that the IAM role that is specified in your Firehose stream has access
  to your S3 bucket and your Lambda function (if data transformation is enabled). Also, make sure that the IAM role has access to CloudWatch log group and log streams to check error logs. For more information, see [Grant Firehose access to an Amazon S3 destination](controlling-access.md#using-iam-s3 "controlling-access.md#using-iam-s3").
- If you're using data transformation, make sure that your Lambda function never
  returns responses whose payload size exceeds 6 MB. For more information, see
  [Amazon Data FirehoseData Transformation](data-transformation.md "data-transformation.md").
