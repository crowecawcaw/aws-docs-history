

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# AWS managed policy: AWSApplicationMigrationMGHAccess
<a name="security-iam-awsmanpol-AWSApplicationMigrationMGHAccess"></a>

 

This policy allows AWS Transform MGN to send metadata about the progress of servers being migrated using MGN to AWS Migration Hub (MGH). MGN automatically creates an IAM role with this policy attached and assumes this role. We do not recommend that you attach this policy to your users or roles. Migration-progress data is only sent after the AWS "home region” is set in AWS MGH. If the Home AWS Region is different than the AWS Region into which a server is being migrated, this data will be sent cross-region. To stop MGN from sending this metadata to AWS MGH, detach it from your users or roles. 

 

 

 **Permissions details** 

To view the policy permission details see [AWSApplicationMigrationMGHAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSApplicationMigrationMGHAccess.html) in the AWS Managed Policy Reference Guide.