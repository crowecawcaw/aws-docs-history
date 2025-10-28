# Troubleshooting Amazon OpenSearch

Service

Check the following if data is not delivered to your OpenSearch Service domain.

Data can be backed up to your Amazon S3 bucket concurrently. If data was not delivered to
your S3 bucket, see [Troubleshooting Amazon S3](data-not-delivered-to-s3.md "data-not-delivered-to-s3.md").

- Check the Firehose `IncomingBytes` and `IncomingRecords`
  metrics to make sure that data is sent to your Firehose stream successfully. For more
  information, see [Monitor Amazon Data Firehose with
  CloudWatch metrics](monitoring-with-cloudwatch-metrics.md "monitoring-with-cloudwatch-metrics.md").
- If data transformation with Lambda is enabled, check the Firehose
  `ExecuteProcessingSuccess` metric to make sure that Firehose has
  tried to invoke your Lambda function. For more information, see [Monitor Amazon Data Firehose with
  CloudWatch metrics](monitoring-with-cloudwatch-metrics.md "monitoring-with-cloudwatch-metrics.md").
- Check the Firehose `DeliveryToAmazonOpenSearchService.Success` metric
  to make sure that Firehose has tried to index data to the OpenSearch Service
  cluster. For more information, see [Monitor Amazon Data Firehose with
  CloudWatch metrics](monitoring-with-cloudwatch-metrics.md "monitoring-with-cloudwatch-metrics.md").
- Enable error logging if it is not already enabled, and check error logs for
  delivery failure. For more information, see [Monitor Amazon Data Firehose Using
  CloudWatch Logs](monitoring-with-cloudwatch-logs.md "monitoring-with-cloudwatch-logs.md").
- Make sure that the OpenSearch Service configuration in your Firehose stream is
  accurate and valid.
- If data transformation with Lambda is enabled, make sure that the Lambda
  function that is specified in your Firehose stream still exists. Also, make sure that the IAM role has access to CloudWatch log group and log streams to check error logs.
  For more information, see [Grant FirehoseAccess to a Public OpenSearch Service Destination](controlling-access.md#using-iam-es "controlling-access.md#using-iam-es").
- Make sure that the IAM role that is specified in your Firehose stream can
  access your OpenSearch Service cluster, S3 backup bucket, and Lambda function (if data
  transformation is enabled). Also, make sure that the IAM role has access to CloudWatch log group and log streams to check error logs. For more information, see [Grant Firehose access to a public OpenSearch Service destination](controlling-access.md#using-iam-es "controlling-access.md#using-iam-es").
- If you're using data transformation, make sure that your Lambda function never
  returns responses whose payload size exceeds 6 MB. For more information, see
  [Amazon Data FirehoseData Transformation](data-transformation.md "data-transformation.md").
- Amazon Data Firehosecurrently does not support the delivery of CloudWatch Logs to Amazon OpenSearch Service destination because
  Amazon CloudWatch combines multiple log events into one Firehose record and Amazon OpenSearch Service cannot accept multiple log events in one record.
  As an alternative, you can consider [Using subscription filter for Amazon OpenSearch Service in CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/CWL_OpenSearch_Stream.md "../../../AmazonCloudWatch/latest/logs/CWL_OpenSearch_Stream.md").
