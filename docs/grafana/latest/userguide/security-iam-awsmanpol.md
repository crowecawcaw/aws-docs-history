# AWS managed policies for Amazon Managed Grafana

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

## AWS managed

policy: AWSGrafanaAccountAdministrator

AWSGrafanaAccountAdministrator policy provides access within Amazon Managed Grafana to create and
manage accounts and workspaces for the entire organization.

You can attach AWSGrafanaAccountAdministrator to your IAM entities.

**Permissions details**

This policy includes the following permissions.

- `iam` – Allows principals to list and get IAM roles so
  that the administrator can associate a role with a workspace as well as pass
  roles to the Amazon Managed Grafana service.
- `Amazon Managed Grafana` – Allows principals read and write access to all
  Amazon Managed Grafana APIs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AWSGrafanaOrganizationAdmin",
 "Effect": "Allow",
 "Action": [
 "iam:ListRoles"
 ],
 "Resource": "*"
 },
 {
 "Sid": "GrafanaIAMGetRolePermission",
 "Effect": "Allow",
 "Action": "iam:GetRole",
 "Resource": "arn:aws:iam::*:role/*"
 },
 {
 "Sid": "AWSGrafanaPermissions",
 "Effect": "Allow",
 "Action": [
 "grafana:*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "GrafanaIAMPassRolePermission",
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::*:role/*",
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "grafana.amazonaws.com"
 }
 }
 }
 ]
}`

```

## AWS

managed policy: AWSGrafanaWorkspacePermissionManagement (obsolete)

This policy is obsolete. This policy should not be attached to any new users,
groups, or roles.

Amazon Managed Grafana added a new policy,
[AWSGrafanaWorkspacePermissionManagementV2](#security-iam-awsmanpol-AWSGrafanaWorkspacePermissionManagementV2 "#security-iam-awsmanpol-AWSGrafanaWorkspacePermissionManagementV2")
to replace this policy. This new managed policy improves security for your workspace
by providing a more restrictive set of permissions.

## AWS

managed policy: AWSGrafanaWorkspacePermissionManagementV2

AWSGrafanaWorkspacePermissionManagementV2 policy provides only the ability to update
user and group permissions for Amazon Managed Grafana workspaces.

You can attach AWSGrafanaWorkspacePermissionManagementV2 to your IAM entities.

**Permissions details**

This policy includes the following permissions.

- `Amazon Managed Grafana` – Allows principals to read and update user and
  group permissions for Amazon Managed Grafana workspaces.
- `IAM Identity Center` – Allows principals to read IAM Identity Center entities. This is
  a necessary part of associating principals with Amazon Managed Grafana applications, but that
  also requires an additional step, described after the policy listing that
  follows.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "AWSGrafanaPermissions",
 "Effect": "Allow",
 "Action": [
 "grafana:DescribeWorkspace",
 "grafana:DescribeWorkspaceAuthentication",
 "grafana:UpdatePermissions",
 "grafana:ListPermissions",
 "grafana:ListWorkspaces"
 ],
 "Resource": "arn:aws:grafana:*:*:/workspaces*"
 },
 {
 "Sid": "IAMIdentityCenterPermissions",
 "Effect": "Allow",
 "Action": [
 "sso:DescribeRegisteredRegions",
 "sso:GetSharedSsoConfiguration",
 "sso:ListDirectoryAssociations",
 "sso:GetManagedApplicationInstance",
 "sso:ListProfiles",
 "sso:GetProfile",
 "sso:ListProfileAssociations",
 "sso-directory:DescribeUser",
 "sso-directory:DescribeGroup"
 ],
 "Resource": "*"
 }
 ]
}`

```

**Additional policy needed**

To fully allow a user to assign permissions, in addition to the
`AWSGrafanaWorkspacePermissionManagementV2` policy, you must also assign
a policy to provide access to Application assignment in IAM Identity Center.

To create this policy, you must first collect the **Grafana
application ARN** for your workspace

1. Open the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Applications** from the left menu.
3. Under the **AWS managed** tab, find the application called
   **Amazon Grafana-_workspace-name_**,
   where `workspace-name` is the name of your workspace. Select the
   application name.
4. The IAM Identity Center application managed by Amazon Managed Grafana for the workspace is shown. This
   application's ARN is shown in the details page. It will be in the form:
   `arn:aws:sso::`owner-account-id`:application/ssoins-`unique-id`/apl-`unique-id``.

The policy you create should look like the following. Replace
`grafana-application-arn` with the ARN that you found in the
previous step:

For information about how to create and apply policy to your roles or users, see
[Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the
_AWS Identity and Access Management User Guide_.

## AWS managed

policy: AWSGrafanaConsoleReadOnlyAccess

AWSGrafanaConsoleReadOnlyAccess policy grants access to read-only operations in
Amazon Managed Grafana.

You can attach AWSGrafanaConsoleReadOnlyAccess to your IAM entities.

**Permissions details**

This policy includes the following permission.

- `Amazon Managed Grafana` – Allows principals read-only access to
  Amazon Managed Grafana APIs

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AWSGrafanaConsoleReadOnlyAccess",
 "Effect": "Allow",
 "Action": ["grafana:Describe*", "grafana:List*"],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed

policy: AmazonGrafanaRedshiftAccess

This policy grants scoped access to Amazon Redshift and the dependencies needed to use the Amazon Redshift
plugin in Amazon Managed Grafana. AmazonGrafanaRedshiftAccess policy allows a user or an IAM role
to use the Amazon Redshift data source plugin in Grafana. Temporary credentials for Amazon Redshift databases
are scoped to the database user `redshift_data_api_user` and credentials from
Secrets Manager can be retrieved if the secret is tagged with the key
`RedshiftQueryOwner`. This policy allows access to Amazon Redshift clusters tagged
with `GrafanaDataSource`. When creating a customer managed policy, the
tag-based authentication is optional.

You can attach AmazonGrafanaRedshiftAccess to your IAM entities. Amazon Managed Grafana also
attaches this policy to a service role that allows Amazon Managed Grafana to perform actions on your
behalf.

**Permissions details**

This policy includes the following permission.

- `Amazon Redshift` – Allows principals to describe clusters and obtain
  temporary credentials for a database user named
  `redshift_data_api_user`.
- `Amazon Redshift–data` – Allows principals to execute queries on
  clusters tagged as `GrafanaDataSource`.
- `Secrets Manager` – Allows principals to list secrets and read secret
  values for secrets tagged as `RedshiftQueryOwner`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "redshift:DescribeClusters",
 "redshift-data:GetStatementResult",
 "redshift-data:DescribeStatement",
 "secretsmanager:ListSecrets"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "redshift-data:DescribeTable",
 "redshift-data:ExecuteStatement",
 "redshift-data:ListTables",
 "redshift-data:ListSchemas"
 ],
 "Resource": "*",
 "Condition": {
 "Null": {
 "aws:ResourceTag/GrafanaDataSource": "false"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "redshift:GetClusterCredentials",
 "Resource": [
 "arn:aws:redshift:*:*:dbname:*/*",
 "arn:aws:redshift:*:*:dbuser:*/redshift_data_api_user"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": "*",
 "Condition": {
 "Null": {
 "secretsmanager:ResourceTag/RedshiftQueryOwner": "false"
 }
 }
 }
 ]
}`

```

## AWS managed policy:

AmazonGrafanaAthenaAccess

This policy grants access to Athena and the dependencies needed to enable querying and
writing results to Amazon S3 from the Athena plugin in Amazon Managed Grafana. AmazonGrafanaAthenaAccess
policy allows a user or an IAM role to use the Athena data source plugin in Grafana.
Athena workgroups must be tagged with `GrafanaDataSource` to be accessible.
This policy contains permissions for writing query results in an Amazon S3 bucket with a name
prefixed with `grafana-athena-query-results-`. Amazon S3 permissions for accessing
the underlying data source of an Athena query are not included in this policy.

You can attach AWSGrafanaAthenaAccess policy to your IAM entities. Amazon Managed Grafana also
attaches this policy to a service role that allows Amazon Managed Grafana to perform actions on your
behalf.

**Permissions details**

This policy includes the following permission.

- `Athena` – Allows principals to run queries on Athena
  resources in workgroups tagged as `GrafanaDataSource`.
- `Amazon S3` – Allows principals to read and write query results
  to a bucket prefixed with `grafana-athena-query-results-`.
- `AWS Glue` – Allows principals access to AWS Glue databases,
  tables, and partitions. This is required so that the principal can use the AWS
  Glue Data Catalog with Athena.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "athena:GetDatabase",
 "athena:GetDataCatalog",
 "athena:GetTableMetadata",
 "athena:ListDatabases",
 "athena:ListDataCatalogs",
 "athena:ListTableMetadata",
 "athena:ListWorkGroups"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "athena:GetQueryExecution",
 "athena:GetQueryResults",
 "athena:GetWorkGroup",
 "athena:StartQueryExecution",
 "athena:StopQueryExecution"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "Null": {
 "aws:ResourceTag/GrafanaDataSource": "false"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "glue:GetDatabase",
 "glue:GetDatabases",
 "glue:GetTable",
 "glue:GetTables",
 "glue:GetPartition",
 "glue:GetPartitions",
 "glue:BatchGetPartition"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:ListBucketMultipartUploads",
 "s3:ListMultipartUploadParts",
 "s3:AbortMultipartUpload",
 "s3:CreateBucket",
 "s3:PutObject",
 "s3:PutBucketPublicAccessBlock"
 ],
 "Resource": [
 "arn:aws:s3:::grafana-athena-query-results-*"
 ]
 }
 ]
}`

```

## AWS managed

policy: AmazonGrafanaCloudWatchAccess

This policy grants access to Amazon CloudWatch and the dependencies needed to use CloudWatch as a
datasource within Amazon Managed Grafana.

You can attach AWSGrafanaCloudWatchAccess policy to your IAM entities. Amazon Managed Grafana
also attaches this policy to a service role that allows Amazon Managed Grafana to perform actions on
your behalf.

**Permissions details**

This policy includes the following permissions.

- `CloudWatch` – Allows principals to list and get metric data and
  logs from Amazon CloudWatch. It also allows viewing data shared from source accounts in
  CloudWatch cross-account observability.
- `Amazon EC2` – Allows principals to get details regarding
  resources that are being monitored.
- `Tags` – Allows principals to access tags on resources, to
  allow filtering the CloudWatch metric queries.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:DescribeAlarmsForMetric",
 "cloudwatch:DescribeAlarmHistory",
 "cloudwatch:DescribeAlarms",
 "cloudwatch:ListMetrics",
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:GetMetricData",
 "cloudwatch:GetInsightRuleReport"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups",
 "logs:GetLogGroupFields",
 "logs:StartQuery",
 "logs:StopQuery",
 "logs:GetQueryResults",
 "logs:GetLogEvents"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeTags",
 "ec2:DescribeInstances",
 "ec2:DescribeRegions"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "tag:GetResources",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "oam:ListSinks",
 "oam:ListAttachedLinks"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Amazon Managed Grafana updates to AWS managed

policies

View details about updates to AWS managed policies for Amazon Managed Grafana since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the [Amazon Managed Grafana document history](doc-history.md "doc-history.md")
page.

| Change                                                                                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Date               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| [AWSGrafanaWorkspacePermissionManagement](#security-iam-awsmanpol-AWSGrafanaWorkspacePermissionManagement "#security-iam-awsmanpol-AWSGrafanaWorkspacePermissionManagement") – obsolete                                                                                                                 | This policy has been replaced by<br>**AWSGrafanaWorkspacePermissionManagementV2**.<br>This policy is considered obsolete, and will no longer be updated. The<br>new policy improves security for your workspace by providing a more<br>restrictive set of permissions.                                                                                                                                                                                                                                                               | January 5, 2024    |
| [AWSGrafanaWorkspacePermissionManagementV2](#security-iam-awsmanpol-AWSGrafanaWorkspacePermissionManagementV2 "#security-iam-awsmanpol-AWSGrafanaWorkspacePermissionManagementV2") – New policy                                                                                                         | Amazon Managed Grafana added a new policy,<br>**AWSGrafanaWorkspacePermissionManagementV2**<br>to replace the obsolete<br>**AWSGrafanaWorkspacePermissionManagement**<br>policy. This new managed policy improves security for your workspace by<br>providing a more restrictive set of permissions.                                                                                                                                                                                                                                 | January 5, 2024    |
| [AmazonGrafanaCloudWatchAccess](#security-iam-awsmanpol-AmazonGrafanaCloudWatchAccess "#security-iam-awsmanpol-AmazonGrafanaCloudWatchAccess") – New policy                                                                                                                                             | Amazon Managed Grafana added a new policy<br>**AmazonGrafanaCloudWatchAccess**.                                                                                                                                                                                                                                                                                                                                                                                                                                                      | March 24, 2023     |
| [AWSGrafanaWorkspacePermissionManagement](#security-iam-awsmanpol-AWSGrafanaWorkspacePermissionManagement "#security-iam-awsmanpol-AWSGrafanaWorkspacePermissionManagement") – Update<br>to an existing policy                                                                                          | Amazon Managed Grafana added new permissions to<br>**AWSGrafanaWorkspacePermissionManagement**<br>so that IAM Identity Center users and groups in Active Directory can be associated<br>with Grafana workspaces.<br>The following permissions were added:<br>`sso-directory:DescribeUser`, and<br>`sso-directory:DescribeGroup`                                                                                                                                                                                                      | March 14, 2023     |
| [AWSGrafanaWorkspacePermissionManagement](#security-iam-awsmanpol-AWSGrafanaWorkspacePermissionManagement "#security-iam-awsmanpol-AWSGrafanaWorkspacePermissionManagement") – Update<br>to an existing policy                                                                                          | Amazon Managed Grafana added new permissions to<br>**AWSGrafanaWorkspacePermissionManagement**<br>so that IAM Identity Center users and groups can be associated with Grafana<br>workspaces.<br>The following permissions were added:<br>`sso:DescribeRegisteredRegions`,<br>`sso:GetSharedSsoConfiguration`,<br>`sso:ListDirectoryAssociations`,<br>`sso:GetManagedApplicationInstance`,<br>`sso:ListProfiles`,<br>`sso:AssociateProfile`,<br>`sso:DisassociateProfile`,<br>`sso:GetProfile`, and<br>`sso:ListProfileAssociations`. | December 20, 2022  |
| [AmazonGrafanaServiceLinkedRolePolicy](using-service-linked-roles.md "using-service-linked-roles.md") – New SLR<br>policy                                                                                                                                                                               | Amazon Managed Grafana added a new policy for the Grafana service-linked role,<br>**AmazonGrafanaServiceLinkedRolePolicy**.                                                                                                                                                                                                                                                                                                                                                                                                          | November 18, 2022  |
| [AWSGrafanaAccountAdministrator](#security-iam-awsmanpol-AWSGrafanaAccountAdministrator "#security-iam-awsmanpol-AWSGrafanaAccountAdministrator"), [AWSGrafanaConsoleReadOnlyAccess](#security-iam-awsmanpol-AWSGrafanaConsoleReadOnlyAccess "#security-iam-awsmanpol-AWSGrafanaConsoleReadOnlyAccess") | Allow access to all Amazon Managed Grafana resources                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | February 17, 2022  |
| [AmazonGrafanaRedshiftAccess](#security-iam-awsmanpol-AmazonGrafanaRedshiftAccess "#security-iam-awsmanpol-AmazonGrafanaRedshiftAccess") – New policy                                                                                                                                                   | Amazon Managed Grafana added a new policy<br>**AmazonGrafanaRedshiftAccess**.                                                                                                                                                                                                                                                                                                                                                                                                                                                        | November 26, 2021  |
| [AmazonGrafanaAthenaAccess](#security-iam-awsmanpol-AmazonGrafanaAthenaAccess "#security-iam-awsmanpol-AmazonGrafanaAthenaAccess") – New policy                                                                                                                                                         | Amazon Managed Grafana added a new policy<br>**AmazonGrafanaAthenaAccess**.                                                                                                                                                                                                                                                                                                                                                                                                                                                          | November 22, 2021  |
| [AWSGrafanaAccountAdministrator](#security-iam-awsmanpol-AWSGrafanaAccountAdministrator "#security-iam-awsmanpol-AWSGrafanaAccountAdministrator")<br>– Update to an existing policy                                                                                                                     | Amazon Managed Grafana removed permissions from<br>**AWSGrafanaAccountAdministrator**.<br>The `iam:CreateServiceLinkedRole` permission scoped to<br>the `sso.amazonaws.com` service was removed, and instead<br>we recommend that you attach the<br>\*_AWSSSOMasterAccountAdministrator_<br>• policy to<br>grant this permission to a user.                                                                                                                                                                                          | October 13, 2021   |
| [AWSGrafanaWorkspacePermissionManagement](#security-iam-awsmanpol-AWSGrafanaWorkspacePermissionManagement "#security-iam-awsmanpol-AWSGrafanaWorkspacePermissionManagement")<br>– Update to an existing policy                                                                                          | Amazon Managed Grafana added new permissions to<br>**AWSGrafanaWorkspacePermissionManagement**<br>so that users with this policy can see the authentication methods<br>associated with workspaces.<br>The `grafana:DescribeWorkspaceAuthentication`<br>permission was added.                                                                                                                                                                                                                                                         | September 21, 2021 |
| [AWSGrafanaConsoleReadOnlyAccess](#security-iam-awsmanpol-AWSGrafanaConsoleReadOnlyAccess "#security-iam-awsmanpol-AWSGrafanaConsoleReadOnlyAccess")<br>– Update to an existing policy                                                                                                                  | Amazon Managed Grafana added new permissions to<br>**AWSGrafanaConsoleReadOnlyAccess**<br>so that users with this policy can see the authentication methods<br>associated with workspaces.<br>The `grafana:Describe*` and `grafana:List*`<br>permissions were added to the policy, and they replace the previous<br>narrower permissions `grafana:DescribeWorkspace`,<br>`grafana:ListPermissions`, and<br>`grafana:ListWorkspaces`.                                                                                                 | September 21, 2021 |
| Amazon Managed Grafana started tracking changes                                                                                                                                                                                                                                                         | Amazon Managed Grafana started tracking changes for its AWS managed<br>policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                     | September 9, 2021  |
