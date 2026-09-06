

# AWS managed policies for Amazon ElastiCache
<a name="security-iam-awsmanpol"></a>





An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.













## AWS managed policy: ElastiCacheServiceRolePolicy
<a name="security-iam-awsmanpol-ElastiCacheServiceRolePolicy"></a>

You can't attach ElastiCacheServiceRolePolicy to your IAM entities. This policy is attached to a service-linked role that allows ElastiCache to perform actions on your behalf.

This policy allows ElastiCache to manage AWS resources on your behalf as necessary for managing your cache:
+ `ec2` – Manage EC2 networking resources to attach to cache nodes, including VPC endpoints (for serverless caches), Elastic Network Interfaces (ENIs) (for node-based clusters), and security groups.
+ `cloudwatch` – Emit metric data from the service into CloudWatch.
+ `outposts` – Allow creation of cache nodes on AWS Outposts.

You can find the [ElastiCacheServiceRolePolicy](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/ElastiCacheServiceRolePolicy) policy on the IAM console and [ElastiCacheServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ElastiCacheServiceRolePolicy.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AmazonElastiCacheFullAccess
<a name="security-iam-awsmanpol-AmazonElastiCacheFullAccess"></a>

You can attach the `AmazonElastiCacheFullAccess` policy to your IAM identities.

This policy allows principals full access to ElastiCache using the AWS Management Console:
+ `elasticache` — Access all APIs.
+ `iam` — Create service-linked role necessary for service operation.
+ `ec2` — Describe dependent EC2 resources necessary for cache creation (VPC, subnet, security group) and allow creation of VPC endpoints (for serverless caches).
+ `kms` — Allow usage of customer-managed CMKs for encryption-at-rest.
+ `cloudwatch` — Allow access to metrics to display ElastiCache metrics in the console.
+ `application-autoscaling` — Allow access to describe autoscaling policies for caches.
+ `logs` — Used to populate log streams for log delivery functionality in the console.
+ `firehose` — Used to populate delivery streams for log delivery functionality in the console.
+ `s3` — Used to populate S3 buckets for snapshot restore functionality in the console.
+ `outposts` — Used to populate AWS Outposts for cache creation in the console.
+ `sns` — Used to populate SNS topics for notification functionality in the console.

You can find the [AmazonElastiCacheFullAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AmazonElastiCacheFullAccess) policy on the IAM console and [AmazonElastiCacheFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonElastiCacheFullAccess.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AmazonElastiCacheReadOnlyAccess
<a name="security-iam-awsmanpol-AmazonElastiCacheReadOnlyAccess"></a>

You can attach the `AmazonElastiCacheReadOnlyAccess` policy to your IAM identities.

This policy allows principals read-only access to ElastiCache using the AWS Management Console:
+ `elasticache` — Access read-only `Describe` APIs.

You can find the [AmazonElastiCacheReadOnlyAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AmazonElastiCacheReadOnlyAccess) policy on the IAM console and [AmazonElastiCacheReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonElastiCacheReadOnlyAccess.html) in the *AWS Managed Policy Reference Guide*.

## ElastiCache updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for ElastiCache since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the ElastiCache Document history page.




| Change | Description | Date | 
| --- | --- | --- | 
| [AmazonElastiCacheFullAccess](#security-iam-awsmanpol-AmazonElastiCacheFullAccess) – Update to an existing policy | ElastiCache added new permissions to allow vertical scaling for MemCached, for the action `elasticache:ModifyCacheCluster`. | March 27, 2025 | 
| [AmazonElastiCacheFullAccess](#security-iam-awsmanpol-AmazonElastiCacheFullAccess) – Update to an existing policy | ElastiCache added new permissions to allow management of serverless caches, and to enable usage of all service features via the console. | November 27, 2023 | 
| [ElastiCacheServiceRolePolicy](#security-iam-awsmanpol-ElastiCacheServiceRolePolicy) – Update to an existing policy | ElastiCache added new permissions to allow management of VPC endpoints for serverless cache resources. | November 27, 2023 | 
| ElastiCache started tracking changes | ElastiCache started tracking changes for its AWS managed policies. | February 07, 2020 | 