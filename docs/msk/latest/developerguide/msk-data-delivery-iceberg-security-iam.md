

# IAM and access control
<a name="msk-data-delivery-iceberg-security-iam"></a>

A Channel uses IAM roles for authorization. Follow least privilege:
+ Scope S3 Tables permissions to the specific bucket used by the Channel.
+ Scope Glue Schema Registry permissions to the specific registry used by the Channel.
+ Use `aws:SourceArn` and `aws:SourceAccount` in the trust policy to prevent confused deputy attacks.