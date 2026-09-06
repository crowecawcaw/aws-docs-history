

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# AWS managed policy: AWSApplicationMigrationReplicationServerPolicy
<a name="security-iam-awsmanpol-AWSApplicationMigrationReplicationServerPolicy"></a>

 

This policy is attached to the AWS Transform MGN replication server’s instance role. 

 

This policy allows the AWS Transform MGN Replication Servers, which are EC2 instances launched by AWS Transform MGN - to communicate with the AWS MGN service, and to create EBS snapshots in your AWS account. An IAM role with this policy is attached (as an EC2 Instance Profile) by AWS Transform MGN to the MGN replication servers which are automatically launched and terminated by MGN, as needed. MGN Replication Servers are used to help data replication from your external servers to AWS, as part of the migration process managed using MGN. We do not recommend that you attach this policy to your users or roles. 

 **Permissions details** 

To view the policy permission details see [AWSApplicationMigrationReplicationServerPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSApplicationMigrationReplicationServerPolicy.html) in the AWS Managed Policy Reference Guide.