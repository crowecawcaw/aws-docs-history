# Using IAM with DynamoDB backup and restore

You can use AWS Identity and Access Management (IAM) to restrict Amazon DynamoDB backup and restore actions for some
resources. The `CreateBackup` and `RestoreTableFromBackup` APIs
operate on a per-table basis.

For more information about using IAM policies in DynamoDB, see
[Identity-based
policies for DynamoDB](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies").

The following are examples of IAM policies that you can use to configure specific backup
and restore functionality in DynamoDB.

## Example 1: Allow the CreateBackup and

RestoreTableFromBackup actions

The following IAM policy grants permissions to allow the `CreateBackup`
and `RestoreTableFromBackup` DynamoDB actions on all tables:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:CreateBackup",
 "dynamodb:RestoreTableFromBackup",
 "dynamodb:PutItem",
 "dynamodb:UpdateItem",
 "dynamodb:DeleteItem",
 "dynamodb:GetItem",
 "dynamodb:Query",
 "dynamodb:Scan",
 "dynamodb:BatchWriteItem"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Important

DynamoDB RestoreTableFromBackup permissions are necessary on the source backup, and DynamoDB read and write
permissions on the target table are necessary for restore functionality.

DynamoDB RestoreTableToPointInTime permissions are necessary on the source table, and DynamoDB read and write
permissions on the target table are necessary for restore functionality.

## Example 2: Allow CreateBackup and deny

RestoreTableFromBackup

The following IAM policy grants permissions for the `CreateBackup` action
and denies the `RestoreTableFromBackup` action:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": ["dynamodb:CreateBackup"],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": ["dynamodb:RestoreTableFromBackup"],
 "Resource": "*"
 }

 ]
}`

```

## Example 3: Allow ListBackups and deny

CreateBackup and RestoreTableFromBackup

The following IAM policy grants permissions for the `ListBackups` action
and denies the `CreateBackup` and `RestoreTableFromBackup`
actions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": ["dynamodb:ListBackups"],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "dynamodb:CreateBackup",
 "dynamodb:RestoreTableFromBackup"
 ],
 "Resource": "*"
 }

 ]
}`

```

## Example 4: Allow ListBackups and deny

DeleteBackup

The following IAM policy grants permissions for the `ListBackups` action
and denies the `DeleteBackup` action:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": ["dynamodb:ListBackups"],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": ["dynamodb:DeleteBackup"],
 "Resource": "*"
 }

 ]
}`

```

## Example 5: Allow RestoreTableFromBackup and

DescribeBackup for all resources and deny DeleteBackup for a specific backup

The following IAM policy grants permissions for the
`RestoreTableFromBackup` and `DescribeBackup` actions and
denies the `DeleteBackup` action for a specific backup resource:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:DescribeBackup",
 "dynamodb:RestoreTableFromBackup"
 ],
 "Resource": "arn:aws:dynamodb:us-east-1:123456789012:table/Music/backup/01489173575360-b308cd7d"
 },
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:PutItem",
 "dynamodb:UpdateItem",
 "dynamodb:DeleteItem",
 "dynamodb:GetItem",
 "dynamodb:Query",
 "dynamodb:Scan",
 "dynamodb:BatchWriteItem"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "dynamodb:DeleteBackup"
 ],
 "Resource": "arn:aws:dynamodb:us-east-1:123456789012:table/Music/backup/01489173575360-b308cd7d"
 }
 ]
}`

```

###### Important

DynamoDB RestoreTableFromBackup permissions are necessary on the source backup, and DynamoDB read and write
permissions on the target table are necessary for restore functionality.

DynamoDB RestoreTableToPointInTime permissions are necessary on the source table, and DynamoDB read and write
permissions on the target table are necessary for restore functionality.

## Example 6: Allow CreateBackup for a specific

table

The following IAM policy grants permissions for the `CreateBackup` action
on the `Movies` table only:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": ["dynamodb:CreateBackup"],
 "Resource": [
 "arn:aws:dynamodb:us-east-1:123456789012:table/Movies"
 ]
 }
 ]
}`

```

## Example 7: Allow ListBackups

The following IAM policy grants permissions for the `ListBackups`
action:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": ["dynamodb:ListBackups"],
 "Resource": "*"
 }
 ]
}`

```

###### Important

You can't grant permissions for the `ListBackups`
action on a specific table.

## Example 8: Allow access to AWS Backup features

You will need API permissions for the `StartAwsBackupJob` action for a successful
backup with advanced features, and the `dynamodb:RestoreTableFromAwsBackup` action
to successfully restore that backup.

The following IAM policy grants AWS Backup the permissions to
trigger backups with advanced features and restores. Also note that if the tables are encrypted
the policy will need access to the [AWS KMS key](encryption.md#dynamodb-kms-authz "encryption.md#dynamodb-kms-authz").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DescribeQueryScanBooksTable",
 "Effect": "Allow",
 "Action": [
 "dynamodb:StartAwsBackupJob",
 "dynamodb:DescribeTable",
 "dynamodb:Query",
 "dynamodb:Scan"
 ],
 "Resource": "arn:aws:dynamodb:us-west-2:`111122223333`:table/Books"
 },
 {
 "Sid": "AllowRestoreFromAwsBackup",
 "Effect": "Allow",
 "Action": [
 "dynamodb:RestoreTableFromAwsBackup"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Example 9: Deny RestoreTableToPointInTime for a Specific Source Table

The following IAM policy denies permissions for the `RestoreTableToPointInTime` action for a specific source table:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "dynamodb:RestoreTableToPointInTime"
 ],
 "Resource": "arn:aws:dynamodb:us-east-1:123456789012:table/Music"
 }
 ]
}`

```

## Example 10: Deny RestoreTableFromBackup for all Backups for a Specific Source Table

The following IAM policy denies permissions for the `RestoreTableToPointInTime` action for all backups for a specific source table:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "dynamodb:RestoreTableFromBackup"
 ],
 "Resource": "arn:aws:dynamodb:us-east-1:123456789012:table/Music/backup/*"
 }
 ]
}`

```
