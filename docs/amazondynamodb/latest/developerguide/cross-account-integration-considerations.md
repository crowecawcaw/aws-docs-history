# Cross-account integration considerations with CMK

When you attempt to integrate from DynamoDB to Amazon Redshift, the initial action is launched from Amazon Redshift.
Without the proper permissions, this action could result in a silent failure.
The following sections detail the permissions required for this cross-account integration.

## Required AWS KMS policies and permissions

Replace the following placeholders in the examples:

- `111122223333`: The AWS account ID where Amazon Redshift is hosted
- `444455556666`: The AWS account ID where DynamoDB is hosted
- `REDSHIFT_ROLE_NAME`: The IAM role name used by Amazon Redshift
- `REGION`: The AWS Region where your resources are located
- `TABLE_NAME`: The name of your DynamoDB table
- `KMS_KEY_ID`: The ID of your KMS key

### KMS key policy in the DynamoDB account

The following AWS KMS key policy enables cross-account access between your DynamoDB and Amazon Redshift services.
In this example, account 444455556666 contains the DynamoDB table and AWS KMS key,
while account 111122223333 contains the Amazon Redshift cluster that needs access to decrypt the data.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Enable IAM User Permissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::444455556666:root"
 },
 "Action": "kms:*",
 "Resource": "*"
 },
 {
 "Sid": "Allow Redshift to use the key",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::111122223333:role/REDSHIFT_ROLE_NAME"
 },
 "Action": [
 "kms:Decrypt",
 "kms:DescribeKey",
 "kms:GenerateDataKey",
 "kms:GenerateDataKeyWithoutPlaintext"
 ],
 "Resource": "*"
 }
 ]
}`

```

### IAM Policy for the Amazon Redshift role (in Amazon Redshift account)

The following IAM policy allows a Amazon Redshift service to access DynamoDB tables and their associated AWS KMS encryption keys in a cross-account scenario.
In this example, account 444455556666 contains the DynamoDB resources and AWS KMS keys that the Amazon Redshift service needs to access.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowDynamoDBAccess",
 "Effect": "Allow",
 "Action": [
 "dynamodb:DescribeTable",
 "dynamodb:BatchGetItem",
 "dynamodb:Scan",
 "dynamodb:Query",
 "dynamodb:BatchGetItem",
 "dynamodb:GetItem",
 "dynamodb:GetRecords",
 "dynamodb:GetShardIterator",
 "dynamodb:DescribeStream",
 "dynamodb:ListStreams"
 ],
 "Resource": [
 "arn:aws:dynamodb:*:444455556666:table/TABLE_NAME",
 "arn:aws:dynamodb:*:444455556666:table/TABLE_NAME/stream/*"
 ]
 },
 {
 "Sid": "AllowKMSAccess",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:DescribeKey",
 "kms:GenerateDataKey",
 "kms:GenerateDataKeyWithoutPlaintext"
 ],
 "Resource": "arn:aws:kms:us-east-1:444455556666:key/KMS_KEY_ID"
 }
 ]
}`

```

### Trust relationship for the Amazon Redshift role

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "redshift.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

### DynamoDB Table policy (if using resource-based policies)

The following resource-based policy allows a Amazon Redshift service in account 111122223333 to access DynamoDB tables and Streams in account 444455556666.
Attach this policy to your DynamoDB table to enable cross-account access.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowRedshiftAccess",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::111122223333:role/REDSHIFT_ROLE_NAME"
 },
 "Action": [
 "dynamodb:DescribeTable",
 "dynamodb:BatchGetItem",
 "dynamodb:Scan",
 "dynamodb:Query",
 "dynamodb:BatchGetItem",
 "dynamodb:GetItem",
 "dynamodb:GetRecords",
 "dynamodb:GetShardIterator",
 "dynamodb:DescribeStream",
 "dynamodb:ListStreams"
 ],
 "Resource": [
 "arn:aws:dynamodb:*:444455556666:table/TABLE_NAME",
 "arn:aws:dynamodb:*:444455556666:table/TABLE_NAME/stream/*"
 ]
 }
 ]
}`

```

## Important considerations

1. Ensure the KMS key is in the same region as your DynamoDB table.
2. The KMS key must be a customer managed key (CMK), not an AWS managed key.
3. If you're using DynamoDB global tables, configure permissions for all relevant regions.
4. Consider adding condition statements to restrict access based on VPC endpoints or IP ranges.
5. For enhanced security, consider using `aws:PrincipalOrgID` condition to restrict access to your organization.
6. Monitor KMS key usage through CloudTrail and CloudWatch metrics.
