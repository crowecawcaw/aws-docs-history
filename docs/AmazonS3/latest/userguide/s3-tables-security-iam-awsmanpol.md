

# AWS managed policies for S3 Tables
<a name="s3-tables-security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

## AWS managed policy: AmazonS3TablesFullAccess
<a name="s3-tables-security-iam-awsmanpol-amazons3tablesfullaccess"></a>

You can attach the `AmazonS3TablesFullAccess` policy to your IAM identities. This policy grants permissions that allow full access to Amazon S3 Tables. For more information about this policy, see [AmazonS3TablesFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonS3TablesFullAccess.html).

## AWS managed policy: AmazonS3TablesReadOnlyAccess
<a name="s3-tables-security-iam-awsmanpol-amazons3readonlyaccess"></a>

You can attach the `AmazonS3TablesReadOnlyAccess` policy to your IAM identities. This policy grants permissions that allow read-only access to Amazon S3 Tables. For more information about this policy, see [AmazonS3TablesReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonS3TablesReadOnlyAccess.html).

## AWS managed policy: AmazonS3TablesLakeFormationServiceRole
<a name="s3-tables-security-iam-awsmanpol-amazons3tableslakeformationservicerole"></a>

You can attach the `AmazonS3TablesLakeFormationServiceRole` policy to your IAM identities. This policy grants permissions that allow the AWS Lake Formation service role access to S3 Tables. AWS KMS permissions are used to allow Lake Formation to access encrypted tables. For more information about this policy, see [AmazonS3TablesLakeFormationServiceRole](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonS3TablesLakeFormationServiceRole.html).

## Amazon S3 Tables updates to AWS managed policies
<a name="s3-tables-security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Amazon S3 Tables since S3 Tables began tracking these changes.


| Change | Description | Date | 
| --- | --- | --- | 
| Amazon S3 Tables updated `AmazonS3TablesFullAccess`. | S3 Tables updated the AWS-managed policy called `AmazonS3TablesFullAccess`. This update grants permission to pass a role to the S3 Tables Replication service. | December 2, 2025 | 
| Amazon S3 Tables added `AmazonS3TablesLakeFormationServiceRole`. | S3 Tables added a new AWS-managed policy called `AmazonS3TablesLakeFormationServiceRole`. This policy grants permissions that allows the Lake Formation service role access to S3 Tables.  | May 19, 2025 | 
| Amazon S3 Tables added `AmazonS3TablesFullAccess`. | S3 Tables added a new AWS-managed policy called `AmazonS3TablesFullAccess`. This policy grants permissions that allow full access to Amazon S3 Tables.  | December 03, 2024 | 
| Amazon S3 Tables added `AmazonS3TablesReadOnlyAccess`. | S3 Tables added a new AWS-managed policy called `AmazonS3TablesReadOnlyAccess`. This policy grants permissions to allow read-only access to Amazon S3 Tables.  | December 03, 2024 | 
| Amazon S3 Tables started tracking changes. | Amazon S3 Tables started tracking changes for its AWS managed policies. | December 03, 2024 | 