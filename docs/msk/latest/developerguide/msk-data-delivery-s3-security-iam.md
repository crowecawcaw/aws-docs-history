

# IAM and access control
<a name="msk-data-delivery-s3-security-iam"></a>

A Channel uses IAM roles for authorization. Follow least privilege:
+ Scope S3 permissions to the specific bucket and prefix used by the Channel.
+ Use `aws:SourceArn` and `aws:SourceAccount` in the trust policy to prevent confused deputy attacks.