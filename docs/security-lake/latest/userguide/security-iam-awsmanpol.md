# AWS managed policies for Security Lake

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

## AWS managed policy: AmazonSecurityLakeMetastoreManager

Amazon Security Lake uses an AWS Lambda function to manage metadata in your data lake. Through the use of this function, Security Lake can
index Amazon Simple Storage Service (Amazon S3) partitions that contain your data and data files into the AWS Glue Data Catalog tables. This managed policy
contains all of the permissions for the Lambda function to index the S3 partitions and data files into the AWS Glue tables.

**Permissions details**

This policy includes the following permissions:

- `logs` – Allows principals to log the output of the Lambda function to Amazon CloudWatch Logs.
- `glue` – Allows principals to perform specific write actions for AWS Glue Data Catalog tables. This also allows
  AWS Glue crawlers to identify partitions in your data.
- `sqs` – Allows principals to perform specific read and write actions for Amazon SQS queues that send event notifications when
  objects are added to or updated in your data lake.
- `s3` – Allows principals to perform specific read and write actions for the Amazon S3 bucket that
  contains your data.

To review the permissions for this policy, see [AmazonSecurityLakeMetastoreManager](../../../aws-managed-policy/latest/reference/AmazonSecurityLakeMetastoreManager.md "../../../aws-managed-policy/latest/reference/AmazonSecurityLakeMetastoreManager.md") in the _AWS Managed Policy
Reference Guide_.

## AWS managed policy: AmazonSecurityLakePermissionsBoundary

Amazon Security Lake creates IAM roles for third-party custom sources to write data to the data lake and for third-party
custom subscribers to consume data from the data lake, and uses this policy when creating these roles to define the boundary of their permissions. You don't need to take action to
use this policy. If the data lake is encrypted with a customer managed AWS KMS key, `kms:Decrypt` and `kms:GenerateDataKey`
permissions are added.

To review the permissions for this policy, see [AmazonSecurityLakePermissionsBoundary](../../../aws-managed-policy/latest/reference/AmazonSecurityLakePermissionsBoundary.md "../../../aws-managed-policy/latest/reference/AmazonSecurityLakePermissionsBoundary.md") in the _AWS Managed Policy
Reference Guide_.

## AWS managed policy: AmazonSecurityLakeAdministrator

You can attach the `AmazonSecurityLakeAdministrator` policy to a principal
before they enable Amazon Security Lake for their account. This policy grants administrative permissions that allow a principal full access to all Security Lake actions. The principal can then onboard to Security Lake and subsequently configure sources and subscribers in Security Lake.

This policy includes the actions that Security Lake administrators can perform on other AWS
services through Security Lake.

The `AmazonSecurityLakeAdministrator` policy does not support the creation of
utility roles required by Security Lake to manage Amazon S3 cross-region replication,
registration of new data partitions in AWS Glue, run a Glue crawler on data added to
custom sources, or notify HTTPS endpoint subscribers of new data. You can create these roles
ahead of time as described in [Getting started with Amazon Security Lake](getting-started.md "getting-started.md").

In addition to the `AmazonSecurityLakeAdministrator` managed policy,
Security Lake requires `lakeformation:PutDataLakeSettings` permissions for
onboarding and configuration functions. `PutDataLakeSettings` allows setting
an IAM principal as an administrator for all regional Lake Formation resources in the account.
This role has to have `iam:CreateRole permission` as well as
`AmazonSecurityLakeAdministrator` policy attached to it.

Lake Formation administrators have full access to the Lake Formation console, and control the initial data
configuration and access permissions. Security Lake assigns the principal that enables Security Lake and
the `AmazonSecurityLakeMetaStoreManager` role (or other specified role) as
Lake Formation administrators so that they can create tables, update table schema, register new
partitions, and configure permissions on tables. You must include the following
permissions in the policy for the Security Lake administrator user or role:

###### Note

To provide sufficient permissions to grant Lake Formation based subscriber access, Security Lake recommends
adding the following `glue:PutResourcePolicy` permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowPutLakeFormationSettings",
 "Effect": "Allow",
 "Action": "lakeformation:PutDatalakeSettings",
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": "securitylake.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AllowGlueActions",
 "Effect": "Allow",
 "Action": ["glue:PutResourcePolicy", "glue:DeleteResourcePolicy"],
 "Resource": [
 "arn:aws:glue:*:*:catalog",
 "arn:aws:glue:*:*:database/amazon_security_lake_glue_db*",
 "arn:aws:glue:*:*:table/amazon_security_lake_glue_db*/*"
 ],
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": "securitylake.amazonaws.com"
 }
 }
 }
 ]
}`

```

**Permissions details**

This policy includes the following permissions.

- `securitylake` – Allows principals full access to all Security Lake actions.
- `organizations` – Allows principals to retrieve information from AWS
  Organizations about the accounts in an organization. If an account belongs to an
  organization, then these permissions allow the Security Lake console to display account
  names and account numbers.
- `iam` – Allows principals to create service-linked roles for Security Lake,
  AWS Lake Formation, and Amazon EventBridge, as a required step when enabling those
  services. Also allows for creation and editing of policies for subscriber and custom
  source roles, with permissions of those roles limited to what is allowed by the
  `AmazonSecurityLakePermissionsBoundary` policy.
- `ram` – Allows principals to configure Lake Formation-based query access
  by subscribers to Security Lake sources.
- `s3`– Allows principals to create and manage Security Lake buckets, and read
  the contents of those buckets.
- `lambda` – Allows principals to manage the Lambda used to update AWS Glue
  table partitions following AWS source delivery and cross-region replication.
- `glue` – Allows principals to create and manage the Security Lake
  database and tables.
- `lakeformation` – Allows principals to manage Lake Formation permissions
  for Security Lake tables.
- `events` – Allows principals to manage rules used to notify subscribers
  of new data in Security Lake sources.
- `sqs` – Allows principals to create and manage Amazon SQS queues used to notify
  subscribers of new data in Security Lake sources.
- `kms` – Allows principals to grant access for Security Lake to write data
  using a customer-managed key.
- `secretsmanager` – Allows principals to manage secrets used for notifying
  subscribers of new data in Security Lake sources via HTTPS endpoints.

To review the permissions for this policy, see [AmazonSecurityLakeAdministrator](../../../aws-managed-policy/latest/reference/AmazonSecurityLakeAdministrator.md "../../../aws-managed-policy/latest/reference/AmazonSecurityLakeAdministrator.md") in the _AWS Managed Policy
Reference Guide_.

## AWS managed policy: SecurityLakeServiceLinkedRole

Security Lake uses the service-linked role named `AWSServiceRoleForSecurityLake` to
create and operate the security data lake.

You can't attach the `SecurityLakeServiceLinkedRole` managed policy to your IAM entities. This policy is
attached to a service-linked role that permits Security Lake to perform actions on your behalf. For more information, see
[Service-linked role permissions for Security Lake](slr-permissions.md "slr-permissions.md").

## AWS managed policy:

SecurityLakeResourceManagementServiceRolePolicy

Security Lake uses the service-linked role named
`AWSServiceRoleForSecurityLakeResourceManagement` to perform ongoing monitoring
and performance improvements, which can reduce latency and costs.

You can't attach the `SecurityLakeResourceManagementServiceRolePolicy` managed
policy to your IAM entities. This policy is attached to a service-linked role that permits
Security Lake to perform actions on your behalf. For more information, see [Service-linked role permissions for resource management](AWSServiceRoleForSecurityLakeResourceManagement.md "AWSServiceRoleForSecurityLakeResourceManagement.md").

## AWS managed policy: AWSGlueServiceRole

The `AWSGlueServiceRole` managed policy invokes the AWS Glue crawler and permits AWS Glue to crawl custom
source data and identify partition metadata. This metadata is necessary to create and update tables in the Data Catalog.

For more information, see [Collecting data from custom sources in Security Lake](custom-sources.md "custom-sources.md").

## Security Lake updates to AWS managed

policies

View details about updates to AWS managed policies for Security Lake since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the Security Lake Document history page.

| Change                                                                                                                                                                                                | Description                                                                                                                                                                                                                                          | Date               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [AWSServiceRoleForSecurityLakeResourceManagement](AWSServiceRoleForSecurityLakeResourceManagement.md "AWSServiceRoleForSecurityLakeResourceManagement.md") – Updated existing policy                  | This policy was updated to replace the `StringLike` operator with the `ArnLike` operator to evaluate the ARN-type keys for the `lambda:FunctionArn` in the `aws:ResourceAccount` condition block. This provides more secure enforcement.             | September 25, 2025 |
| [Service-linked role for Amazon Security Lake](AWSServiceRoleForSecurityLakeResourceManagement.md "AWSServiceRoleForSecurityLakeResourceManagement.md") – New service-linked role                     | We added a new service-linked role `AWSServiceRoleForSecurityLakeResourceManagement`. This service-linked role provides permissions to Security Lake to perform ongoing monitoring and performance improvements, which can reduce latency and costs. | November 14, 2024  |
| [Service-linked role for Amazon Security Lake](using-service-linked-roles.md "using-service-linked-roles.md") – Update to existing service-linked role permissions                                    | We added AWS WAF actions to the AWS managed policy for the `SecurityLakeServiceLinkedRole` policy. The additional actions allow Security Lake to collect AWS WAF logs, when it is enabled as a log source in Security Lake.                          | May 22, 2024       |
| [AmazonSecurityLakePermissionsBoundary](#security-iam-awsmanpol-AmazonSecurityLakePermissionsBoundary "#security-iam-awsmanpol-AmazonSecurityLakePermissionsBoundary") – Update to an existing policy | Security Lake added SID actions to the policy.                                                                                                                                                                                                       | May 13, 2024       |
| [AmazonSecurityLakeMetastoreManager](#security-iam-awsmanpol-AmazonSecurityLakeMetastoreManager "#security-iam-awsmanpol-AmazonSecurityLakeMetastoreManager") – Update to an existing policy          | Security Lake updated the policy to add metadata clean up action which lets you delete the metadata in your data lake.                                                                                                                               | March 27, 2024     |
| [AmazonSecurityLakeAdministrator](#security-iam-awsmanpol-AmazonSecurityLakeAdministrator "#security-iam-awsmanpol-AmazonSecurityLakeAdministrator") – Update to an existing policy                   | Security Lake updated the policy to allow `iam:PassRole` on the new `AmazonSecurityLakeMetastoreManagerV2` role and lets Security Lake deploy or update data lake components.                                                                        | February 23, 2024  |
| [AmazonSecurityLakeMetastoreManager](#security-iam-awsmanpol-AmazonSecurityLakeMetastoreManager "#security-iam-awsmanpol-AmazonSecurityLakeMetastoreManager") – New policy                            | Security Lake added a new managed policy that grants permissions for Security Lake to manage metadata in your data lake.                                                                                                                             | January 23, 2024   |
| [AmazonSecurityLakeAdministrator](#security-iam-awsmanpol-AmazonSecurityLakeAdministrator "#security-iam-awsmanpol-AmazonSecurityLakeAdministrator") – New policy                                     | Security Lake added a new managed policy that grants a principal full access to all Security Lake actions.                                                                                                                                           | May 30, 2023       |
| Security Lake started tracking changes                                                                                                                                                                | Security Lake started tracking changes for its AWS managed policies.                                                                                                                                                                                 | November 29, 2022  |
