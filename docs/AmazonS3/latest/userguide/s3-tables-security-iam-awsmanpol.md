# AWS managed policies for S3 Tables

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

AmazonS3TablesFullAccess

You can attach the `AmazonS3TablesFullAccess` policy to your IAM
identities. This policy grants permissions that allow full access to Amazon S3
Tables.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3tables:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy:

AmazonS3TablesReadOnlyAccess

You can attach the `AmazonS3TablesReadOnlyAccess` policy to your IAM
identities. This policy grants permissions that allow read-only access to Amazon S3
Tables.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3tables:Get*",
 "s3tables:List*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy:

AmazonS3TablesLakeFormationServiceRole

You can attach the `AmazonS3TablesLakeFormationServiceRole` policy to your IAM
identities. This policy grants permissions that allow the AWS Lake Formation service role access to S3 Tables. AWS KMS permissions are used to allow Lake Formation to access encrypted tables.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PermissionsForS3ListTableBuckets",
 "Effect": "Allow",
 "Action": [
 "s3tables:ListTableBuckets"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "111122223333"
 }
 }
 },
 {
 "Sid": "DataAccessPermissionsForS3TablesResources",
 "Effect": "Allow",
 "Action": [
 "s3tables:CreateTableBucket",
 "s3tables:GetTableBucket",
 "s3tables:CreateNamespace",
 "s3tables:GetNamespace",
 "s3tables:ListNamespaces",
 "s3tables:DeleteNamespace",
 "s3tables:DeleteTableBucket",
 "s3tables:CreateTable",
 "s3tables:DeleteTable",
 "s3tables:GetTable",
 "s3tables:ListTables",
 "s3tables:RenameTable",
 "s3tables:UpdateTableMetadataLocation",
 "s3tables:GetTableMetadataLocation",
 "s3tables:GetTableData",
 "s3tables:PutTableData"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "111122223333"
 }
 }
 },
 {
 "Sid": "KMSDataAccessPermissionsForS3TablesResources",
 "Effect": "Allow",
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "s3.*.amazonaws.com"
 ],
 "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3tables:*:*:bucket/*/table/*"
 },
 "StringEquals": {
 "aws:ResourceAccount": "111122223333"
 }
 }
 },
 {
 "Sid": "KMSDescribeKeyAccessPermissionsForS3TablesResources",
 "Effect": "Allow",
 "Action": [
 "kms:DescribeKey"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "s3tables.*.amazonaws.com"
 ]
 },
 "StringEquals": {
 "aws:ResourceAccount": "111122223333"
 }
 }
 }
 ]
}`

```

## Amazon S3 Tables updates to AWS

managed policies

View details about updates to AWS managed policies for Amazon S3 Tables since S3 Tables began tracking these changes.

| Change                                                           | Description                                                                                                                                                                                  | Date              |
| ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| Amazon S3 Tables added `AmazonS3TablesLakeFormationServiceRole`. | S3 Tables added a new AWS-managed policy called `AmazonS3TablesLakeFormationServiceRole`.<br>This policy grants permissions that allows the Lake Formation service role access to S3 Tables. | May 19, 2025      |
| Amazon S3 Tables added `AmazonS3TablesFullAccess`.               | S3 Tables added a new AWS-managed policy called `AmazonS3TablesFullAccess`.<br>This policy grants permissions that allow full access to Amazon S3<br>Tables.                                 | December 03, 2024 |
| Amazon S3 Tables added `AmazonS3TablesReadOnlyAccess`.           | S3 Tables added a new AWS-managed policy called `AmazonS3TablesReadOnlyAccess`.<br>This policy grants permissions to allow read-only access to Amazon S3<br>Tables.                          | December 03, 2024 |
| Amazon S3 Tables started tracking changes.                       | Amazon S3 Tables started tracking changes for its AWS managed policies.                                                                                                                      | December 03, 2024 |
