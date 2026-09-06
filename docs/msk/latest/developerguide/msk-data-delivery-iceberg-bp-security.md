

# Security
<a name="msk-data-delivery-iceberg-bp-security"></a>
+ Scope IAM permissions to the specific destination bucket and schema registry used by each Channel.
+ Use the `aws:SourceArn` condition in the trust policy to prevent other clusters or services from assuming the Channel role.
+ Enable CloudTrail logging to audit all Channel API calls.