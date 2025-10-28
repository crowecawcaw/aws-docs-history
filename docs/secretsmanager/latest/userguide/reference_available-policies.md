# AWS managed policy for AWS Secrets Manager

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWS managed policy: SecretsManagerReadWrite

This policy provides read/write access to AWS Secrets Manager, including permission to describe Amazon RDS, Amazon Redshift, and Amazon DocumentDB resources, and permission to use AWS KMS to encrypt and decrypt secrets. This policy also provides permission to create AWS CloudFormation change sets, get rotation templates from an Amazon S3 bucket that is managed by AWS, list AWS Lambda functions, and describe Amazon EC2 VPCs. These permissions are required by the console to set up rotation with existing rotation functions.

To create new rotation functions, you must also have permission to create AWS CloudFormation stacks and AWS Lambda execution roles. You can assign the [IAMFullAccess](../../../aws-managed-policy/latest/reference/IAMFullAccess.md "../../../aws-managed-policy/latest/reference/IAMFullAccess.md") managed
policy. See [Permissions for
rotation](rotating-secrets-required-permissions-function.md "rotating-secrets-required-permissions-function.md").

**Permissions details**

This policy includes the following permissions.

- `secretsmanager` – Allows principals to perform all Secrets Manager actions.
- `cloudformation` – Allows principals to create AWS CloudFormation stacks. This is
  required so that principals using the console to turn on rotation can create Lambda rotation functions through AWS CloudFormation stacks. For more information, see [How Secrets Manager uses AWS CloudFormation](cloudformation.md#how-asm-uses-cfn "cloudformation.md#how-asm-uses-cfn").
- `ec2` – Allows principals to describe Amazon EC2 VPCs. This is required so that principals using the console can create rotation functions in the same VPC as the database of the credentials they are storing in a secret.
- `kms` – Allows principals to use AWS KMS keys for cryptographic operations. This is required so that Secrets Manager can encrypt and decrypt secrets. For more information, see [Secret encryption and decryption in AWS Secrets Manager](security-encryption.md "security-encryption.md").
- `lambda` – Allows principals to list Lambda rotation functions. This is required so that principals using the console can choose existing rotation functions.
- `rds` – Allows principals to describe clusters and instances in
  Amazon RDS. This is required so that principals using the console can choose Amazon RDS clusters or instances.
- `redshift` – Allows principals to describe clusters in
  Amazon Redshift. This is required so that principals using the console can choose Amazon Redshift clusters.
- `redshift-serverless` – Allows principals to describe namespaces in
  Amazon Redshift Serverless. This is required so that principals using the console can choose Amazon Redshift Serverless namespaces.
- `docdb-elastic` – Allows principals to describe elastic clusters in Amazon DocumentDB. This is required so that principals using the console can choose Amazon DocumentDB elastic clusters.
- `tag` – Allows principals to get all resources in the account that are tagged.
- `serverlessrepo` – Allows principals to create AWS CloudFormation change sets. This is required so that principals using the console can create Lambda rotation functions. For more information, see [How Secrets Manager uses AWS CloudFormation](cloudformation.md#how-asm-uses-cfn "cloudformation.md#how-asm-uses-cfn").
- `s3` – Allows principals to get objects from an Amazon S3 bucket that is managed by AWS. This bucket contains Lambda [Rotation function
  templates](reference_available-rotation-templates.md "reference_available-rotation-templates.md"). This permission is required so that principals using the console can create Lambda rotation functions based on the templates in the bucket. For more information, see [How Secrets Manager uses AWS CloudFormation](cloudformation.md#how-asm-uses-cfn "cloudformation.md#how-asm-uses-cfn").

To view the policy, see [SecretsManagerReadWrite JSON policy document](../../../aws-managed-policy/latest/reference/SecretsManagerReadWrite.md#SecretsManagerReadWrite-json "../../../aws-managed-policy/latest/reference/SecretsManagerReadWrite.md#SecretsManagerReadWrite-json").

## Secrets Manager updates to AWS managed

policies

View details about updates to AWS managed policies for Secrets Manager.

| Change                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                     | Date               | Version |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------- |
| [SecretsManagerReadWrite](#security-iam-awsmanpol-SecretsManagerReadWrite "#security-iam-awsmanpol-SecretsManagerReadWrite") – Update to an existing policy | This policy was updated to allow describe access to Amazon Redshift Serverless so that console users can choose a Amazon Redshift Serverless namespace when they create an Amazon Redshift secret.                                                                                                                              | March 12, 2024     | v5      |
| [SecretsManagerReadWrite](#security-iam-awsmanpol-SecretsManagerReadWrite "#security-iam-awsmanpol-SecretsManagerReadWrite") – Update to an existing policy | This policy was updated to allow describe access to Amazon DocumentDB elastic clusters so that console users can choose an elastic cluster when they create an Amazon DocumentDB secret.                                                                                                                                        | September 12, 2023 | v4      |
| [SecretsManagerReadWrite](#security-iam-awsmanpol-SecretsManagerReadWrite "#security-iam-awsmanpol-SecretsManagerReadWrite") – Update to an existing policy | This policy was updated to allow describe access to Amazon Redshift so that console users can choose a Amazon Redshift cluster when they create an Amazon Redshift secret. The update also added new permissions to allow read access to an Amazon S3 bucket managed by AWS that stores the Lambda rotation function templates. | June 24, 2020      | v3      |
| [SecretsManagerReadWrite](#security-iam-awsmanpol-SecretsManagerReadWrite "#security-iam-awsmanpol-SecretsManagerReadWrite") – Update to an existing policy | This policy was updated to allow describe access to Amazon RDS clusters so that console users can choose a cluster when they create an Amazon RDS secret.                                                                                                                                                                       | May 3, 2018        | v2      |
| [SecretsManagerReadWrite](#security-iam-awsmanpol-SecretsManagerReadWrite "#security-iam-awsmanpol-SecretsManagerReadWrite") – New policy                   | Secrets Manager created a policy to grant permissions that are needed for using the console with all read/write access to Secrets Manager.                                                                                                                                                                                      | April 04, 2018     | v1      |
