# AWS managed policies for AWS Supply Chain

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

## AWS managed policy: AWSSupplyChainFederationAdminAccess

AWSSupplyChainFederationAdminAccess provides AWS Supply Chain federated users access to the
AWS Supply Chain application, including the required permissions to perform actions within the
AWS Supply Chain application. The policy provides administrative permissions over IAM Identity Center users and
groups and is attached to a role created by AWS Supply Chain for you. You shouldn't attach the
AWSSupplyChainFederationAdminAccess policy to any other IAM entities.

Although this policy provides all access to AWS Supply Chain through the scn:\* permissions,
the AWS Supply Chain role determines your permissions. The AWS Supply Chain role only includes the
required permissions, and don't have permissions to the admin APIs.

**Permissions details**

This policy includes the following permissions:

- `Chime` – Provides access to create or delete users under an
  Amazon Chime AppInstance; Provides access to manage channel, channel members, and
  moderators; Provides access to send messages to channel. Chime operations are scoped
  to app instances tagged with "SCNInstanceId".
- `AWS IAM Identity Center (AWS SSO)` – Provides permissions
  required to associate and disassociate user profiles, list profiles association, list application assignments,
  describe application, describe instance, and get application assignment configuration in IAM Identity Center.
- `AppFlow` – Provides access to create, update, and delete
  connection profiles; Provides access to create, update, delete, start, and stop
  flows; Provides access to tag and untag flows and describe flow records.
- `Amazon S3` – Provides access to list all buckets. Provides GetBucketLocation, GetBucketPolicy, PutObject, GetObject, and ListBucket access to buckets with resource
  arn arn:aws:s3:::aws-supply-chain-data-\*.
- `SecretsManager` – Provides access to creating secrets and updating secret policy.
- `KMS` – Provides Amazon AppFlow service the access to list keys and
  key alias. Provides DescribeKey, CreateGrant and ListGrants permissions to KMS keys
  tagged with key-value aws-suply-chain-access : true; Provides access to create
  secrets and update secret policy.

The permissions (_kms:ListKeys_, _kms:ListAliases_, _kms:GenerateDataKey_, and _kms:Decrypt)_ are not restricted to Amazon AppFlow and these permissions can be granted to any AWS KMS Key in your account.

To view the permissions of this policy, see [AWSSupplyChainFederationAdminAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSSupplyChainFederationAdminAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSSupplyChainFederationAdminAccess") in the AWS Management Console.

## AWS Supply Chain updates to AWS managed

policies

The following table lists details about updates to AWS managed policies for AWS Supply Chain
since this service began to track these changes. For automatic alerts about changes to this
page, subscribe to the RSS feed on the AWS Supply Chain Document history page.

| Change                                                                                                                                                                               | Description                                                                                                                                                                                                                                  | Date               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [AWSSupplyChainFederationAdminAccess](#security-iam-awsmanpol-AWSSupplyChainFederationAdminAccess "#security-iam-awsmanpol-AWSSupplyChainFederationAdminAccess") –<br>Updated policy | AWS Supply Chain updated the managed policy to allow federated users access<br>to data in IAM Identity Center that is encrypted with customer managed KMS keys (CMKs).                                                                       | October 30, 2025   |
| [AWSSupplyChainFederationAdminAccess](#security-iam-awsmanpol-AWSSupplyChainFederationAdminAccess "#security-iam-awsmanpol-AWSSupplyChainFederationAdminAccess") – Updated<br>policy | AWS Supply Chain updated the managed policy to allow federated users<br>access to `ListApplicationAssignments`, `DescribeApplication`, `DescribeInstance`,<br>and `GetApplicationAssignmentConfiguration` operations in IAM Identity Center. | December 10, 2024  |
| [AWSSupplyChainFederationAdminAccess](#security-iam-awsmanpol-AWSSupplyChainFederationAdminAccess "#security-iam-awsmanpol-AWSSupplyChainFederationAdminAccess") –<br>Updated policy | AWS Supply Chain updated the managed policy to allow federated users access to ListProfileAssociations operations in IAM Identity Center.                                                                                                    | November 01, 2023  |
| [AWSSupplyChainFederationAdminAccess](#security-iam-awsmanpol-AWSSupplyChainFederationAdminAccess "#security-iam-awsmanpol-AWSSupplyChainFederationAdminAccess") –<br>Updated policy | AWS Supply Chain updated the managed policy to allow federated users access to the PutObject and GetObject operations on the dedicated S3 bucket<br>with resource arn arn:aws:s3:::aws-supply<br>• chain-data-\*.                            | September 21, 2023 |
| [AWSSupplyChainFederationAdminAccess](#security-iam-awsmanpol-AWSSupplyChainFederationAdminAccess "#security-iam-awsmanpol-AWSSupplyChainFederationAdminAccess") –<br>New policy     | AWS Supply Chain added a new policy to allow federated users to access the<br>AWS Supply Chain application. This includes permissions necessary to perform<br>actions within the AWS Supply Chain application.                               | March 01, 2023     |
| AWS Supply Chain started tracking changes                                                                                                                                            | AWS Supply Chain started tracking changes for its AWS managed policies.                                                                                                                                                                      | March 01, 2023     |
