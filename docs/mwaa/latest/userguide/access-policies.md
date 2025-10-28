# Accessing an Amazon MWAA environment

To use Amazon Managed Workflows for Apache Airflow, you must use an account and IAM entities with the necessary permissions.
This topic describes the access policies you can attach to your Apache Airflow development team and
Apache Airflow users for your Amazon Managed Workflows for Apache Airflow environment.

We recommend using temporary credentials and configuring federated identities with groups and roles to access your Amazon MWAA resources. As a best practice, avoid attaching policies directly to your IAM users.
Instead, define groups or roles to provide temporary access to AWS resources.

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an IAM identity that
you can create in your account that has specific permissions. An IAM role is similar to
an IAM user in that it is an AWS identity with permissions policies that determine
what the identity can and cannot do in AWS. However, instead of being uniquely associated
with one person, a role is intended to be assumable by anyone who needs it. Also, a role
does not have standard long-term credentials such as a password or access keys associated
with it. Instead, when you assume a role, it provides you with temporary security credentials
for your role session.

To assign permissions to a federated identity, you create a role and define permissions for the role. When a federated identity authenticates, the identity is associated with the role and is granted the permissions that are defined by the role. For information about roles for federation, see [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md") in the _IAM User Guide_.

If you use IAM Identity Center, you configure a permission set. To control what your identities can access after they authenticate, IAM Identity Center correlates the permission set to a role in IAM.
For information about permissions sets, see [Permission sets](../../../singlesignon/latest/userguide/permissionsetsconcept.md "../../../singlesignon/latest/userguide/permissionsetsconcept.md") in the _AWS IAM Identity Center User Guide_.

You can use an IAM
role in your account to grant another AWS account permissions to access your account's
resources. For an example, see [IAM tutorial: Delegate access across AWS accounts using IAM roles](../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md "../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md") in the
_IAM User Guide_.

###### Sections

- [How it works](#access-policies-how "#access-policies-how")
- [Full console access policy: AmazonMWAAFullConsoleAccess](#console-full-access "#console-full-access")
- [Full API and console access policy: AmazonMWAAFullApiAccess](#full-access-policy "#full-access-policy")
- [Read-only console access policy: AmazonMWAAReadOnlyAccess](#mwaa-read-only "#mwaa-read-only")
- [Apache Airflow UI access policy: AmazonMWAAWebServerAccess](#web-ui-access "#web-ui-access")
- [Apache Airflow Rest API access policy:
  AmazonMWAARestAPIAccess](#rest-api-access "#rest-api-access")
- [Apache Airflow CLI policy: AmazonMWAAAirflowCliAccess](#cli-access "#cli-access")
- [Creating a JSON policy](#access-policy-iam-console-create "#access-policy-iam-console-create")
- [Example use case to attach policies to a developer group](#access-policy-use-case "#access-policy-use-case")
- [What's next?](#access-policy-next-up "#access-policy-next-up")

## How it works

The resources and services used in an Amazon MWAA environment are not accessible to all AWS Identity and Access Management (IAM) entities. You must create a policy that grants Apache Airflow users permission to access these resources. For example,
you need to grant access to your Apache Airflow development team.

Amazon MWAA uses these policies to validate whether a user has the permissions needed to perform an action on the AWS console or through the APIs used by an environment.

You can use the JSON policies in this topic to create a policy for your Apache Airflow users in IAM, and then attach the policy to a user, group, or role in IAM.

- [AmazonMWAAFullConsoleAccess](#console-full-access "#console-full-access") – Use this policy to grant permission to configure an environment on the Amazon MWAA console.
- [AmazonMWAAFullApiAccess](#full-access-policy "#full-access-policy") – Use this policy to grant access to all Amazon MWAA APIs used to manage an environment.
- [AmazonMWAAReadOnlyAccess](#mwaa-read-only "#mwaa-read-only") – Use this policy to grant access to the resources used by an environment on the Amazon MWAA console.
- [AmazonMWAAWebServerAccess](#web-ui-access "#web-ui-access") – Use this policy to grant access to the Apache Airflow webserver.
- [AmazonMWAAAirflowCliAccess](#cli-access "#cli-access") – Use this policy to grant access to run Apache Airflow CLI commands.

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

## Full console access policy: AmazonMWAAFullConsoleAccess

A user might need access to the `AmazonMWAAFullConsoleAccess` permissions policy if they need to configure an environment on the Amazon MWAA console.

###### Note

Your full console access policy must include permissions to perform `iam:PassRole`. This allows the user to pass [service-linked roles](mwaa-slr.md "mwaa-slr.md"), and
[execution roles](mwaa-create-role.md "mwaa-create-role.md"), to Amazon MWAA. Amazon MWAA assumes each role to call other AWS services on your behalf.
The following example uses the `iam:PassedToService` condition key to specify the Amazon MWAA service principal (`airflow.amazonaws.com`)
as the service to which a role can be passed.

For more information about `iam:PassRole`, refer to
[Granting a user permissions to pass a role to an AWS service](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md") in the
_IAM User Guide_.

Use the following policy if you want to create, and manage, your Amazon MWAA environments using an
[AWS owned key](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") for
[encryption at-rest](encryption.md#encryption-at-rest "encryption.md#encryption-at-rest").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "airflow:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "airflow.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:ListRoles"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreatePolicy"
 ],
 "Resource": "arn:aws:iam::`111122223333`:policy/service-role/MWAA-Execution-Policy*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:CreateRole"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/service-role/AmazonMWAA*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": "arn:aws:iam::*:role/aws-service-role/airflow.amazonaws.com/AWSServiceRoleForAmazonMWAA"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation",
 "s3:ListAllMyBuckets",
 "s3:ListBucket",
 "s3:ListBucketVersions"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucket",
 "s3:PutObject",
 "s3:GetEncryptionConfiguration"
 ],
 "Resource": "arn:aws:s3:::*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:DescribeRouteTables"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:CreateSecurityGroup"
 ],
 "Resource": "arn:aws:ec2:*:*:security-group/airflow-security-group-*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:ListAliases"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "ec2:CreateVpcEndpoint",
 "Resource": [
 "arn:aws:ec2:*:*:vpc-endpoint/*",
 "arn:aws:ec2:*:*:vpc/*",
 "arn:aws:ec2:*:*:subnet/*",
 "arn:aws:ec2:*:*:security-group/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:subnet/*",
 "arn:aws:ec2:*:*:network-interface/*"
 ]
 }
 ]
}`

```

Use the following policy if you want to create, and manage, your Amazon MWAA environments using a
[customer managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") for encryption at-rest.
To use a customer managed key, the IAM principal must have permission to access AWS KMS resources using the key stored in your account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "airflow:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "airflow.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:ListRoles"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreatePolicy"
 ],
 "Resource": "arn:aws:iam::`111122223333`:policy/service-role/MWAA-Execution-Policy*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:CreateRole"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/service-role/AmazonMWAA*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": "arn:aws:iam::*:role/aws-service-role/airflow.amazonaws.com/AWSServiceRoleForAmazonMWAA"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation",
 "s3:ListAllMyBuckets",
 "s3:ListBucket",
 "s3:ListBucketVersions"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucket",
 "s3:PutObject",
 "s3:GetEncryptionConfiguration"
 ],
 "Resource": "arn:aws:s3:::*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:DescribeRouteTables"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:CreateSecurityGroup"
 ],
 "Resource": "arn:aws:ec2:*:*:security-group/airflow-security-group-*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:ListAliases"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:DescribeKey",
 "kms:ListGrants",
 "kms:CreateGrant",
 "kms:RevokeGrant",
 "kms:Decrypt",
 "kms:Encrypt",
 "kms:GenerateDataKey*",
 "kms:ReEncrypt*"
 ],
 "Resource": "arn:aws:kms:*:`111122223333`:key/`YOUR_KMS_ID`"
 },
 {
 "Effect": "Allow",
 "Action": "ec2:CreateVpcEndpoint",
 "Resource": [
 "arn:aws:ec2:*:*:vpc-endpoint/*",
 "arn:aws:ec2:*:*:vpc/*",
 "arn:aws:ec2:*:*:subnet/*",
 "arn:aws:ec2:*:*:security-group/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:subnet/*",
 "arn:aws:ec2:*:*:network-interface/*"
 ]
 }
 ]
}`

```

## Full API and console access policy: AmazonMWAAFullApiAccess

A user might need access to the `AmazonMWAAFullApiAccess` permissions policy if they need access to all Amazon MWAA APIs used to manage an environment. It does not grant permissions to access the Apache Airflow UI.

###### Note

A full API access policy must include permissions to perform `iam:PassRole`. This allows the user to pass [service-linked roles](mwaa-slr.md "mwaa-slr.md"), and
[execution roles](mwaa-create-role.md "mwaa-create-role.md"), to Amazon MWAA. Amazon MWAA assumes each role to call other AWS services on your behalf.
The following example uses the `iam:PassedToService` condition key to specify the Amazon MWAA service principal (`airflow.amazonaws.com`)
as the service to which a role can be passed.

For more information about `iam:PassRole`, refer to
[Granting a user permissions to pass a role to an AWS service](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md") in the
_IAM User Guide_.

Use the following policy if you want to create, and manage, your Amazon MWAA environments using an AWS owned key for encryption at-rest.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":"airflow:*",
 "Resource":"*"
 },
 {
 "Effect":"Allow",
 "Action":[
 "iam:PassRole"
 ],
 "Resource":"*",
 "Condition":{
 "StringLike":{
 "iam:PassedToService":"airflow.amazonaws.com"
 }
 }
 },
 {
 "Effect":"Allow",
 "Action":[
 "iam:CreateServiceLinkedRole"
 ],
 "Resource":"arn:aws:iam::*:role/aws-service-role/airflow.amazonaws.com/AWSServiceRoleForAmazonMWAA"
 },
 {
 "Effect":"Allow",
 "Action":[
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:DescribeRouteTables"
 ],
 "Resource":"*"
 },
 {
 "Effect":"Allow",
 "Action":[
 "s3:GetEncryptionConfiguration"
 ],
 "Resource":"arn:aws:s3:::*"
 },
 {
 "Effect":"Allow",
 "Action":"ec2:CreateVpcEndpoint",
 "Resource":[
 "arn:aws:ec2:*:*:vpc-endpoint/*",
 "arn:aws:ec2:*:*:vpc/*",
 "arn:aws:ec2:*:*:subnet/*",
 "arn:aws:ec2:*:*:security-group/*"
 ]
 },
 {
 "Effect":"Allow",
 "Action":[
 "ec2:CreateNetworkInterface"
 ],
 "Resource":[
 "arn:aws:ec2:*:*:subnet/*",
 "arn:aws:ec2:*:*:network-interface/*"
 ]
 }
 ]
}`

```

Use the following policy if you want to create, and manage, your Amazon MWAA environments using a customer managed key for encryption at-rest.
To use a customer managed key, the IAM principal must have permission to access AWS KMS resources using the key stored in your account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "airflow:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "airflow.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": "arn:aws:iam::*:role/aws-service-role/airflow.amazonaws.com/AWSServiceRoleForAmazonMWAA"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:DescribeRouteTables"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:DescribeKey",
 "kms:ListGrants",
 "kms:CreateGrant",
 "kms:RevokeGrant",
 "kms:Decrypt",
 "kms:Encrypt",
 "kms:GenerateDataKey*",
 "kms:ReEncrypt*"
 ],
 "Resource": "arn:aws:kms:*:``111122223333``:key/``YOUR_KMS_ID``"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetEncryptionConfiguration"
 ],
 "Resource": "arn:aws:s3:::*"
 },
 {
 "Effect": "Allow",
 "Action": "ec2:CreateVpcEndpoint",
 "Resource": [
 "arn:aws:ec2:*:*:vpc-endpoint/*",
 "arn:aws:ec2:*:*:vpc/*",
 "arn:aws:ec2:*:*:subnet/*",
 "arn:aws:ec2:*:*:security-group/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:subnet/*",
 "arn:aws:ec2:*:*:network-interface/*"
 ]
 }
 ]
}`

```

## Read-only console access policy: AmazonMWAAReadOnlyAccess

A user might need access to the `AmazonMWAAReadOnlyAccess` permissions policy if they need to access the resources used by an environment on the Amazon MWAA console environment details page. It doesn't allow a user to create new environments, edit existing environments, or allow a user to access the Apache Airflow UI.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "airflow:ListEnvironments",
 "airflow:GetEnvironment",
 "airflow:ListTagsForResource"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Apache Airflow UI access policy: AmazonMWAAWebServerAccess

A user might need access to the `AmazonMWAAWebServerAccess` permissions policy if they need to access the Apache Airflow UI. It does not allow the user to access environments on the Amazon MWAA console or use the Amazon MWAA APIs to perform any actions. Specify the `Admin`, `Op`, `User`, `Viewer` or the `Public` role in `{airflow-role}` to customize the level of access for the user of the web token. For more information, refer to [Default Roles](https://airflow.apache.org/docs/apache-airflow/1.10.6/security.html?highlight=ldap#default-roles "https://airflow.apache.org/docs/apache-airflow/1.10.6/security.html?highlight=ldap#default-roles") in the _Apache Airflow reference guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "airflow:CreateWebLoginToken",
 "Resource": [
 "arn:aws:airflow:`us-east-1`:`111122223333`:role/`{your-environment-name}`/`{airflow-role}`"
 ]
 }
 ]
}`

```

###### Note

- Amazon MWAA provides IAM integration with the five [default Apache Airflow role-based access control (RBAC) roles](https://airflow.apache.org/docs/apache-airflow/stable/security/access-control.html?highlight=roles "https://airflow.apache.org/docs/apache-airflow/stable/security/access-control.html?highlight=roles"). For more
  information about working with custom Apache Airflow roles, refer to [Tutorial: Restricting an Amazon MWAA user's access to a subset of DAGs](limit-access-to-dags.md "limit-access-to-dags.md").
- The `Resource` field in this policy can be used to specify
  the Apache Airflow role-based access control roles for the Amazon MWAA environment.
  However, it does not support the Amazon MWAA environment ARN (Amazon Resource
  Name) in the `Resource` field of the policy.

## Apache Airflow Rest API access policy:

AmazonMWAARestAPIAccess

To access the Apache Airflow REST API, you must grant the `airflow:InvokeRestApi`
permission in your IAM policy. In the following policy sample, specify the
`Admin`, `Op`, `User`, `Viewer` or the
`Public` role in `{airflow-role}` to customize the level of
user access. For more information, refer to [Default Roles](https://airflow.apache.org/docs/apache-airflow/1.10.6/security.html?highlight=ldap#default-roles "https://airflow.apache.org/docs/apache-airflow/1.10.6/security.html?highlight=ldap#default-roles") in the _Apache Airflow reference guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowMwaaRestApiAccess",
 "Effect": "Allow",
 "Action": "airflow:InvokeRestApi",
 "Resource": [
 "arn:aws:airflow:`us-east-1`:`111122223333`:role/{your-environment-name}/{airflow-role}"
 ]
 }
 ]
}`

```

###### Note

- While configuring a private webserver, the `InvokeRestApi` action cannot be
  invoked from outside of a Virtual Private Cloud (VPC). You can use the
  `aws:SourceVpc` key to apply more granular access control for
  this operation. For more information, refer to [aws:SourceVpc](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcevpc "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcevpc")
- The `Resource` field in this policy can be used to specify
  the Apache Airflow role-based access control roles for the Amazon MWAA environment. However, it does not
  support the Amazon MWAA environment ARN (Amazon Resource Name) in the
  `Resource` field of the policy.

## Apache Airflow CLI policy: AmazonMWAAAirflowCliAccess

A user might need access to the `AmazonMWAAAirflowCliAccess` permissions policy if they need to run Apache Airflow CLI commands (such as `trigger_dag`). It does not allow the user to access environments on the Amazon MWAA console or use the Amazon MWAA APIs to perform any actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "airflow:CreateCliToken"
 ],
 "Resource": "arn:aws:airflow:`us-east-1`:`111122223333`:environment/${EnvironmentName}"
 }
 ]
}`

```

## Creating a JSON policy

You can create the JSON policy, and attach the policy to your user, role, or group on the IAM console. The following steps describe how to create a JSON policy in IAM.

###### To create the JSON policy

1. Open the [Policies page](https://console.aws.amazon.com/iam/home#/policies "https://console.aws.amazon.com/iam/home#/policies") on the IAM console.
2. Choose **Create policy**.
3. Choose the **JSON** tab.
4. Add your JSON policy.
5. Choose **Review policy**.
6. Enter a value in the text field for **Name** and **Description** (optional).

For example, you can name the policy `AmazonMWAAReadOnlyAccess`. 7. Choose **Create policy**.

## Example use case to attach policies to a developer group

Let's say you're using a group in IAM named `AirflowDevelopmentGroup` to apply permissions to all of the developers on your Apache Airflow development team. These users need access to the `AmazonMWAAFullConsoleAccess`, `AmazonMWAAAirflowCliAccess`, and `AmazonMWAAWebServerAccess` permission policies. This section describes how to create a group in IAM, create and attach these policies, and associate the group to an IAM user. The steps assume you're using an [AWS-owned key](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk").

###### To create the AmazonMWAAFullConsoleAccess policy

1. Download the [AmazonMWAAFullConsoleAccess access policy](samples/AmazonMWAAFullConsoleAccess.md "samples/AmazonMWAAFullConsoleAccess.md").
2. Open the [Policies page](https://console.aws.amazon.com/iam/home#/policies "https://console.aws.amazon.com/iam/home#/policies") on the IAM console.
3. Choose **Create policy**.
4. Choose the **JSON** tab.
5. Paste the JSON policy for `AmazonMWAAFullConsoleAccess`.
6. Substitute the following values:
   1. `123456789012` – Your AWS account ID (such as `0123456789`)
   2. `{your-kms-id}` – The unique identifer for a customer managed key, applicable only if you use a customer managed key for encryption at-rest.

7. Choose the **Review policy**.
8. Type `AmazonMWAAFullConsoleAccess` in **Name**.
9. Choose **Create policy**.

###### To create the AmazonMWAAWebServerAccess policy

1. Download the [AmazonMWAAWebServerAccess access policy](samples/AmazonMWAAWebServerAccess.md "samples/AmazonMWAAWebServerAccess.md").
2. Open the [Policies page](https://console.aws.amazon.com/iam/home#/policies "https://console.aws.amazon.com/iam/home#/policies") on the IAM console.
3. Choose **Create policy**.
4. Choose the **JSON** tab.
5. Paste the JSON policy for `AmazonMWAAWebServerAccess`.
6. Substitute the following values:
   1. `us-east-1` – the region of your Amazon MWAA environment (such as `us-east-1`)
   2. `123456789012` – your AWS account ID (such as `0123456789`)
   3. `{your-environment-name}` – your Amazon MWAA environment name (such as `MyAirflowEnvironment`)
   4. `{airflow-role}` – the `Admin` Apache Airflow [Default Role](https://airflow.apache.org/docs/apache-airflow/1.10.6/security.html?highlight=ldap#default-roles "https://airflow.apache.org/docs/apache-airflow/1.10.6/security.html?highlight=ldap#default-roles")

7. Choose **Review policy**.
8. Type `AmazonMWAAWebServerAccess` in **Name**.
9. Choose **Create policy**.

###### To create the AmazonMWAAAirflowCliAccess policy

1. Download the [AmazonMWAAAirflowCliAccess access policy](samples/AmazonMWAAAirflowCliAccess.md "samples/AmazonMWAAAirflowCliAccess.md").
2. Open the [Policies page](https://console.aws.amazon.com/iam/home#/policies "https://console.aws.amazon.com/iam/home#/policies") on the IAM console.
3. Choose **Create policy**.
4. Choose the **JSON** tab.
5. Paste the JSON policy for `AmazonMWAAAirflowCliAccess`.
6. Choose the **Review policy**.
7. Type `AmazonMWAAAirflowCliAccess` in **Name**.
8. Choose **Create policy**.

###### To create the group

1. Open the [Groups page](https://console.aws.amazon.com/iam/home#/groups "https://console.aws.amazon.com/iam/home#/groups") on the IAM console.
2. Enter a name of `AirflowDevelopmentGroup`.
3. Choose **Next Step**.
4. Type `AmazonMWAA` to filter results in **Filter**.
5. Select the three policies you created.
6. Choose **Next Step**.
7. Choose **Create Group**.

###### To associate to a user

1. Open the [Users page](https://console.aws.amazon.com/iam/home#/users "https://console.aws.amazon.com/iam/home#/users") on the IAM console.
2. Choose a user.
3. Choose **Groups**.
4. Choose **Add user to groups**.
5. Select the **AirflowDevelopmentGroup**.
6. Choose **Add to Groups**.

## What's next?

- Learn how to generate a token to access the Apache Airflow UI in [Accessing Apache Airflow](access-airflow-ui.md "access-airflow-ui.md").
- Learn more about creating IAM policies in [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md").
