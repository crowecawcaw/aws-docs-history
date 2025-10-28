# Required key policy for use with SSE-KMS

You can protect the data in your Amazon S3 bucket by enabling either Server-Side
Encryption with Amazon S3-Managed Keys (SSE-S3) or Server-Side Encryption with KMS Keys
(SSE-KMS) on your S3 bucket. For more information, see [Protecting data using
server-side encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md") in the _Amazon S3 User
Guide_.

If you choose SSE-S3, no additional configuration is required. Amazon S3 handles the encryption key.

If you choose SSE-KMS, you must use a customer managed key ARN. If you use a key ID, you can run into a [LogDestination undeliverable](flow-logs-troubleshooting.md#flow-logs-troubleshooting-kms-id "flow-logs-troubleshooting.md#flow-logs-troubleshooting-kms-id") error when creating a flow log. Also, you must update the key policy for your customer managed key so that the log delivery account can write to your S3 bucket.
For more information about the required key policy for use with SSE-KMS, see [Amazon S3 bucket server-side encryption](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-SSE-KMS-S3 "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-SSE-KMS-S3")
in the _Amazon CloudWatch Logs User Guide_.
