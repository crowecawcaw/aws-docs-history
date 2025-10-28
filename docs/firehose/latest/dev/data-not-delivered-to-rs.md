# Troubleshooting Amazon Redshift

Check the following if data is not delivered to your Amazon Redshift provisioned cluster or Amazon Redshift
Serverless workgroup.

Data is delivered to your S3 bucket before loading into Amazon Redshift. If the data was not
delivered to your S3 bucket, see [Troubleshooting Amazon S3](data-not-delivered-to-s3.md "data-not-delivered-to-s3.md").

- Check the Firehose `DeliveryToRedshift.Success` metric to make sure
  that Firehose has tried to copy data from your S3 bucket to the Amazon Redshift provisioned
  cluster or Amazon Redshift Serverless workgroup. For more information, see [Monitor Amazon Data Firehose with
  CloudWatch metrics](monitoring-with-cloudwatch-metrics.md "monitoring-with-cloudwatch-metrics.md").
- Enable error logging if it is not already enabled, and check error logs for
  delivery failure. For more information, see [Monitor Amazon Data Firehose Using
  CloudWatch Logs](monitoring-with-cloudwatch-logs.md "monitoring-with-cloudwatch-logs.md").
- Check the Amazon Redshift `STL_CONNECTION_LOG` table to see if Firehose can
  make successful connections. In this table, you should be able to see
  connections and their status based on a user name. For more information, see
  [`STL_CONNECTION_LOG`](../../../redshift/latest/dg/r_STL_CONNECTION_LOG.md "../../../redshift/latest/dg/r_STL_CONNECTION_LOG.md") in the
  _Amazon Redshift Database Developer Guide_.
- If the previous check shows that connections are being established, check the
  Amazon Redshift `STL_LOAD_ERRORS` table to verify the reason for the COPY
  failure. For more information, see [`STL_LOAD_ERRORS`](../../../redshift/latest/dg/r_STL_LOAD_ERRORS.md "../../../redshift/latest/dg/r_STL_LOAD_ERRORS.md") in the
  _Amazon Redshift Database Developer Guide_.
- Make sure that the Amazon Redshift configuration in your Firehose stream is accurate and
  valid.
- Make sure that the IAM role that is specified in your Firehose stream can access
  the S3 bucket that Amazon Redshift copies data from, and also the Lambda function for data
  transformation (if data transformation is enabled). Also, make sure that the IAM role has access to CloudWatch log group and log streams to check error logs. For more information, see
  [Grant Firehose access to an Amazon Redshift destination](controlling-access.md#using-iam-rs "controlling-access.md#using-iam-rs") .
- If your Amazon Redshift provisioned cluster or Amazon Redshift Serverless workgroup is in a virtual
  private cloud (VPC), make sure that the cluster allows access from Firehose IP
  addresses. For more information, see [Grant Firehose access to an Amazon Redshift destination](controlling-access.md#using-iam-rs "controlling-access.md#using-iam-rs") .
- Make sure that the Amazon Redshift provisioned cluster or Amazon Redshift Serverless workgroup is
  publicly available.
- If you're using data transformation, make sure that your Lambda function never
  returns responses whose payload size exceeds 6 MB. For more information, see
  [Amazon Data FirehoseData Transformation](data-transformation.md "data-transformation.md").
