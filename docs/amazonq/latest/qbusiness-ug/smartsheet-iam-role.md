# IAM role for

Smartsheet connector

If you use the AWS CLI or an AWS SDK, you must create an AWS Identity and Access Management (IAM)
policy before you create an Amazon Q resource. When you call the operation,
you provide the Amazon Resource Name (ARN) role with the policy attached.

If you use the AWS Management Console, you can create a new IAM role in the Amazon Q console or use an existing IAM role.

To connect your data source connector to Amazon Q, you must give Amazon Q an IAM role that has the following permissions:

- Permission to access the `BatchPutDocument` and
  `BatchDeleteDocument` operations to ingest documents.
- Permission to access the [User Store](connector-principal-store.md "connector-principal-store.md") API operations to ingest user and
  group access control information from documents.
- Permission to access your AWS Secrets Manager secret to
  authenticate your data source connector instance.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowsAmazonQToGetS3Objects",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::bucket/*"
 ],
 "Effect": "Allow",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "`111122223333`"
 }
 }
 },
 {
 "Sid": "AllowsAmazonQToGetSecret",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:us-west-2:`111122223333`:secret:`QBusiness-Smartsheet-Example-Secret`"
 ]
 },
 {
 "Sid": "AllowsAmazonQToDecryptSecret",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:us-west-2:`111122223333`:key/`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.*.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "AllowsAmazonQToIngestDocuments",
 "Effect": "Allow",
 "Action": [
 "qbusiness:BatchPutDocument",
 "qbusiness:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:qbusiness:us-west-2:`111122223333`:application/`312ba974-4afc-8b7a-3180-6aec1db0d57c`/index/`e2a71750-c4fd0-b34a-bf23-ddcce192d11d`"
 },
 {
 "Sid": "AllowsAmazonQToIngestPrincipalMapping",
 "Effect": "Allow",
 "Action": [
 "qbusiness:PutGroup",
 "qbusiness:CreateUser",
 "qbusiness:DeleteGroup",
 "qbusiness:UpdateUser",
 "qbusiness:ListGroups"
 ],
 "Resource": [
 "arn:aws:qbusiness:us-west-2:`111122223333`:application/`312ba974-4afc-8b7a-3180-6aec1db0d57c`",
 "arn:aws:qbusiness:us-west-2:`111122223333`:application/`312ba974-4afc-8b7a-3180-6aec1db0d57c`/index/`e2a71750-c4fd0-b34a-bf23-ddcce192d11d`",
 "arn:aws:qbusiness:us-west-2:`111122223333`:application/`312ba974-4afc-8b7a-3180-6aec1db0d57c`/index/`e2a71750-bf23-4fd0-b34a-192d11dddcce`/data-source/*"
 ]
 }
 ]
}`

```

**To allow Amazon Q to assume a role, you must also use
the following trust policy:**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowsAmazonQServicePrincipal",
 "Effect": "Allow",
 "Principal": {
 "Service": "qbusiness.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "111122223333"
 },
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`"
 }
 }
 }
 ]
}`

```

For more information on Amazon Q data source connector IAM
roles, see [IAM
roles for Amazon Q data source connectors](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").
