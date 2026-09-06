

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# AWS managed policy: AWSApplicationMigrationFullAccess
<a name="security-iam-awsmanpol-AWSApplicationMigrationFullAccess"></a>

You can attach the `AWSApplicationMigrationFullAccess` policy to your IAM identities. 

This policy provides permissions to all public APIs of AWS Transform MGN, as well as permissions to read KMS key, License Manager, Resource Groups, Elastic Load Balancing, IAM, EC2, and Amazon FSx information. This policy should only be granted to an administrator or a power-user. 

**Important**  
You must attach the [AWSApplicationMigrationFullAccess](https://docs.aws.amazon.com/en_us/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationFullAccess.html) and the [AWSApplicationMigrationEC2Access](https://docs.aws.amazon.com/en_us/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationEC2Access.html) policies to your users and roles to enable them to launch test and cutover instances and to complete a full migration cycle with MGN.

 **Permissions details** 

To view the policy permission details see [AWSApplicationMigrationFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSApplicationMigrationFullAccess.html) in the AWS Managed Policy Reference Guide.