# AWS managed policies for Amazon AppFlow

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

## AWS managed policy:

AmazonAppFlowFullAccess

You can attach the `AmazonAppFlowFullAccess` policy to your IAM
identities.

This policy grants administrative permissions that allow you to view, create,
update, run, and delete flows, and also to list, create, and delete connections. In
addition, this policy grants access to the API actions that are required to
configure other AWS services as a source or destinations. This policy also
provides access to AWS Key Management Service to allow use of customer managed CMKs for encryption.
It does not grant the ability to add other users.

###### Note

This policy automatically grants read and write permissions to S3 buckets with
an `appflow-` prefix only. You will not have access rights to any
other S3 buckets without this prefix.

**Permissions details**

This policy includes the following permissions.

- `appflow` – Allows principals to have full access to
  Amazon AppFlow. This is required so that you can view, create, update, run, and
  delete flows, in addition to list, create, and delete connections.
- `iam` – Allows principals to list IAM roles from Amazon Redshift.
  This is required so that you can use Amazon Redshift as a flow destination.
- `s3` – Allows principals to access buckets, bucket
  locations, and bucket policies for Amazon Simple Storage Service (Amazon S3). This is required so that
  you can use Amazon S3 as a flow source or destination (or use it to support the
  use of another source or destination).
- `kms` – Allows principals to view the key ID and Amazon
  Resource Name (ARN) of all the customer master keys (CMKs) in the account,
  view detailed information about a CMK, view the aliases that are defined in
  the account, and add a grant to a CMK. This is required so that you can use
  customer managed CMKs for encryption.
- `secretsmanager` – Allows principals to create secrets
  in Secrets Manager. This is required so that Amazon AppFlow can store the encrypted
  credentials that you use to connect to flow source and destination
  applications in your Secrets Manager account.
- `lambda` – Allows principals to list all the functions
  in customer account. This is required so that you can register new
  connectors

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "appflow:*",
 "Resource": "*"
 },
 {
 "Sid": "ListRolesForRedshift",
 "Effect": "Allow",
 "Action": "iam:ListRoles",
 "Resource": "*"
 },
 {
 "Sid": "KMSListAccess",
 "Action": [
 "kms:ListKeys",
 "kms:DescribeKey",
 "kms:ListAliases"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Sid": "KMSGrantAccess",
 "Effect": "Allow",
 "Action": [
 "kms:CreateGrant"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "kms:ViaService": "appflow.*.amazonaws.com"
 },
 "Bool": {
 "kms:GrantIsForAWSResource": "true"
 }
 }
 },
 {
 "Sid": "KMSListGrantAccess",
 "Effect": "Allow",
 "Action": [
 "kms:ListGrants"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "kms:ViaService": "appflow.*.amazonaws.com"
 }
 }
 },
 {
 "Sid": "S3ReadAccess",
 "Effect": "Allow",
 "Action": [
 "s3:ListAllMyBuckets",
 "s3:ListBucket",
 "s3:GetBucketLocation",
 "s3:GetBucketPolicy"
 ],
 "Resource": "*"
 },
 {
 "Sid": "S3PutBucketPolicyAccess",
 "Effect": "Allow",
 "Action": [
 "s3:PutBucketPolicy"
 ],
 "Resource": "arn:aws:s3:::appflow-*"
 },
 {
 "Sid": "SecretsManagerCreateSecretAccess",
 "Effect": "Allow",
 "Action": "secretsmanager:CreateSecret",
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "secretsmanager:Name": "appflow!*"
 },
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": [
 "appflow.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "SecretsManagerPutResourcePolicyAccess",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:PutResourcePolicy"
 ],
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": [
 "appflow.amazonaws.com"
 ]
 },
 "StringEqualsIgnoreCase": {
 "secretsmanager:ResourceTag/aws:secretsmanager:owningService": "appflow"
 }
 }
 },
 {
 "Sid": "LambdaListFunctions",
 "Effect": "Allow",
 "Action": [
 "lambda:ListFunctions"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy:

AmazonAppFlowReadOnlyAccess

You can attach the `AmazonAppFlowReadOnlyAccess` policy to your IAM
identities.

This policy grants read-only permissions that allow you to view flows and
connections in an AWS account. This policy doesn't allow you to create or delete
flows or connections, and it doesn't grant the ability to add other users or grant
access to other AWS services.

**Permissions details**

This policy includes the following permissions.

- `appflow` – Allows principals to describe and list
  resources from Amazon AppFlow. This is required so that Amazon AppFlow users can
  view connectors, connector profiles, flows, and their associated metadata.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [
 {
 "Effect": "Allow",
 "Action":
 [
 "appflow:DescribeConnector",
 "appflow:DescribeConnectors",
 "appflow:DescribeConnectorProfiles",
 "appflow:DescribeFlows",
 "appflow:DescribeFlowExecution",
 "appflow:DescribeConnectorFields",
 "appflow:ListConnectors",
 "appflow:ListConnectorFields",
 "appflow:ListTagsForResource"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Amazon AppFlow updates to AWS managed

policies

View details about updates to AWS managed policies for Amazon AppFlow since this
service began tracking these changes. For automatic alerts about changes to this
page, subscribe to the RSS feed on the Amazon AppFlow [Document history](doc-history.md "doc-history.md") page.

| Change                                                                                                                            | Description                                                                                                                               | Date       |
| --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [AmazonAppFlowFullAccess](#security-iam-awsmanpol-full "#security-iam-awsmanpol-full") – Update to an existing policy             | Amazon AppFlow now allows the `lambda:ListFunctions` action in the AmazonAppFlowFullAccess policy.                                        | 03/01/2022 |
| [AmazonAppFlowReadOnlyAccess](#security-iam-awsmanpol-readonly "#security-iam-awsmanpol-readonly") – Update to an existing policy | Amazon AppFlow now allows the `appflow:DescribeConnector` and `appflow:ListConnectors` actions in the AmazonAppFlowReadOnlyAccess policy. | 03/01/2022 |
| Amazon AppFlow started tracking changes                                                                                           | Amazon AppFlow started tracking changes for its AWS managed policies.                                                                     | 03/26/2021 |
