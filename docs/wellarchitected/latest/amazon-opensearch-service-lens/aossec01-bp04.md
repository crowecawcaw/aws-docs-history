# AOSSEC01-BP04 Encrypt slow and error logs in Amazon CloudWatch

to protect sensitive information

Protect sensitive information in slow and error logs by encrypting
them, keeping them confidential even when stored in Amazon CloudWatch.

**Level of risk exposed if this best practice
is not established:** Medium

**Desired outcome:** Slow and error
logs are encrypted. This protects your logs from exposing
information such as document fields and queries.

**Benefits of establishing this best
practice:** Improved security and confidentiality of
sensitive information.

## Implementation guidance

If you're publishing slow and error logs to Amazon CloudWatch, you
can protect them with encryption by using an AWS KMS key to secure
your CloudWatch Logs log group. To achieve this, create an AWS KMS
key, set permissions on the key, associate it with a log group.
After this is completed, you can use the same AWS KMS key with your
OpenSearch Service domain.

For step-by-step instructions on implementing this encryption
process, see
[Encrypt
log data in CloudWatch Logs using AWS Key Management Service](../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md "../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md") and
[How
do I use AWS KMS to encrypt log data in CloudWatch Logs?](https://repost.aws/knowledge-center/cloudwatch-encrypt-log-data "https://repost.aws/knowledge-center/cloudwatch-encrypt-log-data")

## Resources

- [Encrypt
  log data in CloudWatch Logs using AWS Key Management Service](../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md "../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md")
