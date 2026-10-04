

# IAM and networking recommendations
<a name="aurora-analytics-iam-networking"></a>

The following recommendations apply to the IAM role and VPC networking that you configure when you set up Aurora PostgreSQL analytics.
+ **Least-privilege IAM**: Grant only `s3:ListBucket` and `s3:GetObject`. Scope these to specific Amazon S3 prefixes using `Condition` blocks. For AWS Glue, grant `glue:GetTable` on specific catalog, database, and table ARNs only.
+ **Same-Region Amazon S3 bucket placement**: Place your Amazon S3 data bucket in the same AWS Region as your Aurora DB cluster. Cross-Region reads add latency and data transfer costs.
+ **VPC endpoints**: When your DB cluster runs in a private subnet, it can reach Amazon S3 and AWS Glue through either VPC endpoints or a NAT gateway. We recommend VPC endpoints (an Amazon S3 gateway endpoint, plus an AWS Glue interface endpoint for Iceberg) because they keep traffic on the AWS network and the Amazon S3 gateway endpoint adds no hourly charge.