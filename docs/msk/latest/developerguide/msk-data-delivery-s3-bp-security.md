

# Security
<a name="msk-data-delivery-s3-bp-security"></a>
+ Scope IAM permissions to the specific destination bucket used by each Channel.
+ Use the `aws:SourceArn` condition in the trust policy to prevent other clusters or services from assuming the Channel role.
+ Enable CloudTrail logging to audit all Channel API calls.