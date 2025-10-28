# AWS managed

policy: AmazonDataZoneFullAccess

You can attach the `AmazonDataZoneFullAccess` policy to your IAM
identities.

This policy provides full access to Amazon DataZone via the AWS Management Console. This policy also
has permissions to AWS KMS for encrypted SSM parameters. The KMS key must be
tagged with EnableKeyForAmazonDataZone to allow decrypting the SSM
parameters.

**Permissions details**

This policy includes the following permissions:

- `datazone` – grants principals full access to Amazon DataZone
  via the AWS Management Console.
- `kms` – Allows principals to list aliases, describe
  keys, and decrypt keys.
- `s3` – Allows principals to choose existing or create
  new S3 buckets to store Amazon DataZone data.
- `ram` – Allows principals to share Amazon DataZone domains
  across AWS accounts.
- `iam` – Allows principals to list and pass roles and get
  policies.
- `sso` – Allows principals to obtain the regions where
  AWS IAM Identity Center is enabled.
- `secretsmanager` – Allows principals to create, tag, and
  list secrets with a specific prefix.
- `aoss` – Allows principals to create and retrieve
  information for OpenSearch Serverless security policies.
- `bedrock` – Allows principals to create, list, and
  retrieve information for inference profiles and foundation models.
- `codeconnections` – Allows principals to delete,
  retrieve information, list connections, and manage tags for
  connections.
- `codewhisperer` – Allows principals to list
  CodeWhisperer profiles.
- `ssm` – Allows principals to put, delete, and retrieve
  information for parameters.
- `redshift` – Allows principals to describe clusters and
  list serverless workgroups
- `glue` – Allows principals to get databases.
  To view the permissions for this policy, see [AmazonDataZoneFullAccess](../../../aws-managed-policy/latest/reference/AmazonDataZoneFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonDataZoneFullAccess.md") in the _AWS Managed
  Policy Reference_.

## Policy considerations and limitations

There are certain functionalities that the
`AmazonDataZoneFullAccess` policy doesn't cover.

- If you create an Amazon DataZone domain with your own AWS KMS key, you must
  have the permissions to `kms:CreateGrant` for domain creation
  to succeed, and to `kms:GenerateDataKey`,
  `kms:Decrypt` for that key to invoke other Amazon DataZone
  APIs such as `listDataSources` and
  `createDataSource`. And you must also have the
  permissions to `kms:CreateGrant`, `kms:Decrypt`,
  `kms:GenerateDataKey`, and `kms:DescribeKey`
  in the resource policy of that key.

If you use the default service-owned KMS key, then this isn't
required.

For more information, see [AWS Key Management Service](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md").

- If you want to use _create_ and
  _update_ role functionalities within the
  Amazon DataZone console, you must have administrator privileges or have the
  required IAM permissions to create IAM roles and create/update
  policies. The required permissions include `iam:CreateRole`,
  `iam:CreatePolicy`, `iam:CreatePolicyVersion`,
  `iam:DeletePolicyVersion`, and
  `iam:AttachRolePolicy` permissions.
- If you create a new domain in Amazon DataZone with AWS IAM Identity Center users login
  activated, or if you activate it for an existing domain in Amazon DataZone,
  you must have permissions to the following:
  - organizations:DescribeOrganization
  - organizations:ListDelegatedAdministrators
  - sso:CreateInstance
  - sso:ListInstances
  - sso:GetSharedSsoConfiguration
  - sso:PutApplicationGrant
  - sso:PutApplicationAssignmentConfiguration
  - sso:PutApplicationAuthenticationMethod
  - sso:PutApplicationAccessScope
  - sso:CreateApplication
  - sso:DeleteApplication
  - sso:CreateApplicationAssignment
  - sso:DeleteApplicationAssignment
  - sso-directory:CreateUser
  - sso-directory:SearchUsers
  - sso:ListApplications

- In order to accept an AWS account association request in Amazon DataZone,
  you must have the `ram:AcceptResourceShareInvitation`
  permission.
- If you want to create required resource for SageMaker Unified Studio
  network setup, you must have permissions to the following and attach
  AmazonVpcFullAccess policy:
  - iam:PassRole
  - cloudformation:CreateStack
