# Use IAM Identity Center enabled Athena workgroups

[Trusted identity propagation](../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md") is an AWS IAM Identity Center feature that administrators of connected AWS services can use to grant and audit access to service data. Access to this data is based on user attributes such as group associations. Setting up trusted identity propagation requires collaboration between the administrators of connected AWS services and the IAM Identity Center administrators. For more information, see [Prerequisites and considerations](../../../singlesignon/latest/userguide/trustedidentitypropagation-overall-prerequisites.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overall-prerequisites.md").

With [IAM Identity Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md"),
you can manage sign-in security for your workforce identities, also known as
workforce users. IAM Identity Center provides one place where you can create or connect workforce users
and centrally manage their access across all their AWS accounts and applications. You can
use multi-account permissions to assign these users access to AWS accounts. You can use
application assignments to assign your users access to IAM Identity Center enabled applications, cloud
applications, and customer Security Assertion Markup Language (SAML 2.0) applications. For
more information, see [Trusted identity
propagation across applications](../../../singlesignon/latest/userguide/trustedidentitypropagation.md "../../../singlesignon/latest/userguide/trustedidentitypropagation.md") in the
_AWS IAM Identity Center User Guide_.

Athena SQL support for trusted identity propagation is available in both EMR Studio and
SageMaker Unified Studio. Each platform provides specific interfaces for using TIP with Athena.

When using Athena SQL in EMR Studio with IAM Identity Center identities, you have two workgroup
options:

- **Regular WorkGroups** – No user/group
  assignments needed.
- **IAM Identity Center enabled workgroups** –
  Requires assigning users/groups through IAM Identity Center console or API.
  For both options, you can run queries using the Athena SQL interface in EMR Studio with
  IAM Identity Center enabled.

## Considerations and limitations

When you use Trusted identity propagation with Amazon Athena, consider the following points:

- You cannot change the authentication method for the workgroup after the
  workgroup is created.
  - Existing Athena SQL workgroups cannot be modified to support IAM Identity Center
    enabled workgroups. Existing Athena SQL workgroups can propagate identity
    to downstream services.
  - IAM Identity Center enabled workgroups cannot be modified to support resource-level
    IAM permissions or identity based IAM policies.

- To access Trusted identity propagation enabled workgroups, IAM Identity Center users must be assigned to the
  `IdentityCenterApplicationArn` that is returned by the response
  of the Athena [GetWorkGroup](../APIReference/API_GetWorkGroup.md "../APIReference/API_GetWorkGroup.md")
  API action.
- Amazon S3 Access Grants must be configured to use Trusted identity propagation identities. For more
  information, see [S3 Access
  Grants and corporate directory identities](../../../AmazonS3/latest/userguide/access-grants-directory-ids.md "../../../AmazonS3/latest/userguide/access-grants-directory-ids.md") in the
  _Amazon S3 User Guide_.
- IAM Identity Center enabled Athena workgroups require Lake Formation to be configured to use IAM Identity Center
  identities. For configuration information, see [Integrating
  IAM Identity Center](../../../lake-formation/latest/dg/identity-center-integration.md "../../../lake-formation/latest/dg/identity-center-integration.md") in the _AWS Lake Formation Developer Guide_.
- By default, queries time out after 30 minutes in IAM Identity Center enabled workgroups. You
  can request a query timeout increase, but the maximum a query can run in Trusted identity propagation
  workgroups is one hour.
- User or group entitlement changes in Trusted identity propagation workgroups can require up to an
  hour to take effect.
- Queries in an Athena workgroup that uses Trusted identity propagation cannot be run directly from the
  Athena console. They must be run from the Athena interface in an EMR Studio
  that has IAM Identity Center enabled. For more information about using Athena in
  EMR Studio, see [Use the Amazon Athena
  SQL editor in EMR Studio](../../../emr/latest/ManagementGuide/emr-studio-athena.md "../../../emr/latest/ManagementGuide/emr-studio-athena.md") in the
  _Amazon EMR Management Guide_.
- Trusted identity propagation is not compatible with the following Athena features.
  - `aws:CalledVia` context keys for IAM Identity Center enabled
    workgroups.
  - Athena for Spark workgroups.
  - Federated access to the Athena API.
  - Federated access to Athena using Lake Formation and the Athena JDBC and ODBC
    drivers.

- You can use Trusted identity propagation with Athena only in the following AWS Regions:
  - `us-east-2` – US East (Ohio)
  - `us-east-1` – US East (N. Virginia)
  - `us-west-1` – US West (N. California)
  - `us-west-2` – US West (Oregon)
  - `af-south-1` – Africa (Cape Town)
  - `ap-east-1` – Asia Pacific (Hong Kong)
  - `ap-southeast-3` – Asia Pacific (Jakarta)
  - `ap-south-1` – Asia Pacific (Mumbai)
  - `ap-northeast-3` – Asia Pacific (Osaka)
  - `ap-northeast-2` – Asia Pacific (Seoul)
  - `ap-southeast-1` – Asia Pacific (Singapore)
  - `ap-southeast-2` – Asia Pacific (Sydney)
  - `ap-northeast-1` – Asia Pacific (Tokyo)
  - `ca-central-1` – Canada (Central)
  - `eu-central-1` – Europe (Frankfurt)
  - `eu-central-2` – Europe (Zurich)
  - `eu-west-1` – Europe (Ireland)
  - `eu-west-2` – Europe (London)
  - `eu-south-1` – Europe (Milan)
  - `eu-west-3` – Europe (Paris)
  - `eu-north-1` – Europe (Stockholm)
  - `me-south-1` – Middle East (Bahrain)
  - `sa-east-1` – South America (São Paulo)

The IAM user of the admin who creates the IAM Identity Center enabled workgroup in the Athena
console must have the following policies attached.

- The `AmazonAthenaFullAccess` managed policy. For details, see
  [AWS managed policy: AmazonAthenaFullAccess](managed-policies.md#amazonathenafullaccess-managed-policy "managed-policies.md#amazonathenafullaccess-managed-policy").
- The following inline policy that allows IAM and IAM Identity Center actions:

JSON

```
`{ "Version":"2012-10-17", "Statement": [ { "Action": [ "iam:createRole",
 "iam:CreatePolicy", "iam:AttachRolePolicy", "iam:ListRoles", "identitystore:ListUsers",
 "identitystore:ListGroups", "identitystore:CreateUser", "identitystore:CreateGroup",
 "sso:ListInstances", "sso:CreateInstance", "sso:DeleteInstance", "sso:ListTrustedTokenIssuers",
 "sso:DescribeTrustedTokenIssuer", "sso:ListApplicationAssignments",
 "sso:DescribeRegisteredRegions", "sso:GetManagedApplicationInstance",
 "sso:GetSharedSsoConfiguration", "sso:PutApplicationAssignmentConfiguration",
 "sso:CreateApplication", "sso:DeleteApplication", "sso:PutApplicationGrant",
 "sso:PutApplicationAuthenticationMethod", "sso:PutApplicationAccessScope",
 "sso:ListDirectoryAssociations", "sso:CreateApplicationAssignment",
 "sso:DeleteApplicationAssignment", "organizations:ListDelegatedAdministrators",
 "organizations:DescribeAccount", "organizations:DescribeOrganization",
 "organizations:CreateOrganization", "sso-directory:SearchUsers", "sso-directory:SearchGroups",
 "sso-directory:CreateUser" ], "Effect": "Allow", "Resource": [ "*" ] }, { "Action": [
 "iam:PassRole" ], "Effect": "Allow", "Resource": [
 "arn:aws:iam::`111122223333`:role/service-role/AWSAthenaSQLRole-*"
 ] } ] }`

```

## Creating an IAM Identity Center enabled Athena workgroup

The following procedure shows the steps and options related to creating an IAM Identity Center
enabled Athena workgroup. For a description of the other configuration options available
for Athena workgroups, see [Create a workgroup](creating-workgroups.md "creating-workgroups.md").

###### To create an SSO enabled workgroup in the Athena console

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. In the Athena console navigation pane, choose
   **Workgroups**.
3. On the **Workgroups** page, choose **Create
   workgroup**.
4. On the **Create workgroup** page, for **Workgroup
   name**, enter a name for the workgroup.
5. For **Analytics engine**, use the **Athena
   SQL** default.
6. For **Authentication**, choose
   **IAM Identity Center**.
7. For **Service role for IAM Identity Center access**, choose an existing
   service role, or create a new one.

Athena requires permissions to access IAM Identity Center for you. A service role is required
for Athena to do this. A service role is an IAM role that you manage that
authorizes an AWS service to access other AWS services on your behalf. To
query federated catalogs or run UDF, update service role with corresponding
Lambda permissions. For more information, see [Creating a role
to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
_IAM User Guide_. 8. Expand **Query result configuration**, and then enter or
choose an Amazon S3 path for **Location of query result**. 9. (Optional) Choose **Encrypt query results**. By default,
SSE-S3 is supported. To use SSE-KMS and CSE-KMS with query result location,
provide grants to the **Service role for IAM Identity Center** from Amazon S3
Access Grants. For more information, see [Sample role policy](#workgroups-identity-center-access-grant-location-sample-role-policy "#workgroups-identity-center-access-grant-location-sample-role-policy"). 10. (Optional) Choose **Create user identity based S3
prefix**.

When you create an IAM Identity Center enabled workgroup, the **Enable S3 Access
Grants** option is selected by default. You can use Amazon S3 Access
Grants to control access to Athena query results locations (prefixes) in Amazon S3.
For more information about Amazon S3 Access Grants, see [Managing access with Amazon S3
Access Grants](../../../AmazonS3/latest/userguide/access-grants.md "../../../AmazonS3/latest/userguide/access-grants.md").

In Athena workgroups that use IAM Identity Center authentication, you can enable the creation
of identity based query result locations that are governed by Amazon S3 Access
Grants. These user identity based Amazon S3 prefixes let users in an Athena workgroup
keep their query results isolated from other users in the same workgroup.

When you enable the user prefix option, Athena appends the user ID as an Amazon S3
path prefix to the query result output location for the workgroup (for example,
`s3://amzn-s3-demo-bucket/${`user_id`}`).
To use this feature, you must configure Access Grants to allow only the user
permission to the location that has the `user_id` prefix. For a
sample Amazon S3 Access Grants location role policy that restricts access to Athena
query results, see [Sample role policy](#workgroups-identity-center-access-grant-location-sample-role-policy "#workgroups-identity-center-access-grant-location-sample-role-policy").

###### Note

Selecting the user identity S3 prefix option automatically enables the
override client-side settings option for the workgroup, as described in the
next step. The override client-side settings option is a requirement for the
user identity prefix feature. 11. Expand **Settings**, and then confirm that **Override
client-side settings** is selected.

When you select **Override client-side settings**, workgroup
settings are enforced at the workgroup level for all clients in the workgroup.
For more information, see [Override client-side settings](workgroups-settings-override.md "workgroups-settings-override.md"). 12. (Optional) Make any other configuration settings that you require as described
in [Create a workgroup](creating-workgroups.md "creating-workgroups.md"). 13. Choose **Create workgroup**. 14. Use the **Workgroups** section of the Athena console to assign
users or groups from your IAM Identity Center directory to your IAM Identity Center enabled Athena
workgroup.

The following sample shows a policy for a role to attach to an Amazon S3 Access Grant
location that restricts access to Athena query results.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:*"
 ],
 "Condition": {
 "ArnNotEquals": {
 "s3:AccessGrantsInstanceArn": "arn:aws:s3:`us-east-1`:`111122223333`:access-grants/default"
 },
 "StringNotEquals": {
 "aws:ResourceAccount": "`111122223333`"
 }
 },
 "Effect": "Deny",
 "Resource": "*",
 "Sid": "ExplicitDenyS3"
 },
 {
 "Action": [
 "kms:*"
 ],
 "Effect": "Deny",
 "NotResource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`${keyid}`",
 "Sid": "ExplictDenyKMS"
 },
 {
 "Action": [
 "s3:ListMultipartUploadParts",
 "s3:GetObject"
 ],
 "Condition": {
 "ArnEquals": {
 "s3:AccessGrantsInstanceArn": "arn:aws:s3:`us-east-1`:`111122223333`:access-grants/default"
 },
 "StringEquals": {
 "aws:ResourceAccount": "`111122223333`"
 }
 },
 "Effect": "Allow",
 "Resource": "arn:aws:s3:::`ATHENA-QUERY-RESULT-LOCATION`/`${identitystore:UserId}`/*",
 "Sid": "ObjectLevelReadPermissions"
 },
 {
 "Action": [
 "s3:PutObject",
 "s3:AbortMultipartUpload"
 ],
 "Condition": {
 "ArnEquals": {
 "s3:AccessGrantsInstanceArn": "arn:aws:s3:`us-east-1`:`111122223333`:access-grants/default"
 },
 "StringEquals": {
 "aws:ResourceAccount": "`111122223333`"
 }
 },
 "Effect": "Allow",
 "Resource": "arn:aws:s3:::`ATHENA-QUERY-RESULT-LOCATION`/`${identitystore:UserId}`/*",
 "Sid": "ObjectLevelWritePermissions"
 },
 {
 "Action": "s3:ListBucket",
 "Condition": {
 "ArnEquals": {
 "s3:AccessGrantsInstanceArn": "arn:aws:s3:`us-east-1`:`111122223333`:access-grants/default"
 },
 "StringEquals": {
 "aws:ResourceAccount": "`111122223333`"
 },
 "StringLikeIfExists": {
 "s3:prefix": [
 "`${identitystore:UserId}`",
 "`${identitystore:UserId}`/*"
 ]
 }
 },
 "Effect": "Allow",
 "Resource": "arn:aws:s3:::`ATHENA-QUERY-RESULT-LOCATION`",
 "Sid": "BucketLevelReadPermissions"
 },
 {
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`${keyid}`",
 "Sid": "KMSPermissions"
 }
 ]
}`

```
