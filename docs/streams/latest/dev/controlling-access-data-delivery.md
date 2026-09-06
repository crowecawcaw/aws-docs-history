

# Access control for streaming tables and Amazon S3 delivery
<a name="controlling-access-data-delivery"></a>

 Streaming tables and Amazon S3 delivery use an IAM service execution role that Amazon Kinesis Data Streams assumes to write data to your destination. Follow these access control practices: 
+ **Least privilege** – Grant only the minimum permissions the service execution role needs. Scope Amazon S3 permissions to specific buckets and prefixes rather than using wildcards.
+ **Scope to specific resources** – Restrict permissions to the specific bucket, table bucket, or table that the delivery writes to. Avoid using `Resource: "*"`.
+ **Confused deputy prevention** – Include `aws:SourceArn` and `aws:SourceAccount` conditions in the service execution role trust policy so that only your delivery resources can assume the role.
+ **Source stream encryption** – If your stream is encrypted with an AWS managed key (the `aws/kinesis` alias), you cannot create a delivery. Use a customer managed key for stream encryption instead.

 For the complete service execution role policies, see [IAM permissions for data delivery](data-delivery-iam.md). For encryption details and audit logging, see [Security for data delivery](data-delivery-security.md). 