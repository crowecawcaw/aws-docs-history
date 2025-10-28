# Amazon Bedrock in SageMaker Unified

Studio KMS Permissions

- **KMS Key Policy — Amazon DataZone domain key and the
  Tooling blueprint Key**: manually set the following key policy to
  the domain key and the Tooling blueprint key.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow administrators to manage key",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`444455556666`:role/ExampleAdminRole"
 },
 "Action": [
 "kms:Create*",
 "kms:Describe*",
 "kms:Enable*",
 "kms:List*",
 "kms:Put*",
 "kms:Update*",
 "kms:Revoke*",
 "kms:Disable*",
 "kms:Get*",
 "kms:Delete*",
 "kms:TagResource",
 "kms:UntagResource",
 "kms:ScheduleKeyDeletion",
 "kms:CancelKeyDeletion",
 "kms:RotateKeyOnDemand"
 ],
 "Resource": "*"
 },
 {
 "Sid": "Allow administrators and SageMaker domain execution role to encrypt and decrypt DataZone data",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`444455556666`:role/ExampleAdminRole",
 "arn:aws:iam::`444455556666`:role/ExampleDomainUser",
 "arn:aws:iam::`111122223333`:role/service-role/AmazonSageMakerDomainExecution"
 ]
 },
 "Action": [
 "kms:CreateGrant",
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "kms:EncryptionContext:aws:datazone:`DOMAIN_ID`": "`domain_id`"
 }
 }
 },
 {
 "Sid": "Allow SageMaker provisioning role to encrypt and decrypt Amazon Bedrock resources",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/service-role/AmazonSageMakerProvisioning-111122223333"
 },
 "Action": [
 "kms:CreateGrant",
 "kms:Decrypt",
 "kms:DescribeKey",
 "kms:Encrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "*"
 },
 {
 "Sid": "Allow SageMaker project roles to describe key",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": "kms:DescribeKey",
 "Resource": "*",
 "Condition": {
 "Null": {
 "aws:PrincipalTag/AmazonDataZoneProject": "false"
 }
 }
 },
 {
 "Sid": "Allow SageMaker project roles to encrypt and decrypt data in Tooling blueprint S3 bucket",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "*",
 "Condition": {
 "Null": {
 "aws:PrincipalTag/AmazonDataZoneProject": "false"
 },
 "StringLike": {
 "kms:ViaService": "s3.*.amazonaws.com"
 }
 }
 },
 {
 "Sid": "Allow SageMaker project roles to encrypt and decrypt Amazon Bedrock secrets",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "kms:Decrypt",
 "kms:Encrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "*",
 "Condition": {
 "Null": {
 "aws:PrincipalTag/AmazonDataZoneProject": "false"
 },
 "StringLike": {
 "kms:ViaService": "secretsmanager.*.amazonaws.com"
 },
 "ArnLike": {
 "kms:EncryptionContext:SecretARN": "arn:aws:secretsmanager:*:*:secret:amazon-bedrock*"
 }
 }
 },
 {
 "Sid": "Allow SageMaker project roles to encrypt and decrypt Amazon Bedrock data",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "*",
 "Condition": {
 "Null": {
 "aws:PrincipalTag/AmazonDataZoneProject": "false"
 },
 "ForAnyValue:StringLike": {
 "kms:EncryptionContextKeys": [
 "aws:bedrock*",
 "evaluationJobArn"
 ]
 }
 }
 },
 {
 "Sid": "Allow Amazon Bedrock to encrypt and decrypt Amazon Bedrock data",
 "Effect": "Allow",
 "Principal": {
 "Service": "bedrock.amazonaws.com"
 },
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringLike": {
 "kms:EncryptionContextKeys": [
 "aws:bedrock*",
 "evaluationJobArn"
 ]
 }
 }
 },
 {
 "Sid": "Allow Amazon Bedrock to create and revoke grants for Amazon Bedrock resources",
 "Effect": "Allow",
 "Principal": {
 "Service": "bedrock.amazonaws.com"
 },
 "Action": [
 "kms:CreateGrant",
 "kms:ListGrants",
 "kms:RevokeGrant"
 ],
 "Resource": "*",
 "Condition": {
 "Bool": {
 "kms:GrantIsForAWSResource": "true"
 }
 }
 },
 {
 "Sid": "Allow CloudWatch Logs to encrypt and decrypt Amazon Bedrock log groups",
 "Effect": "Allow",
 "Principal": {
 "Service": "logs.amazonaws.com"
 },
 "Action": [
 "kms:Decrypt*",
 "kms:Describe*",
 "kms:Encrypt*",
 "kms:GenerateDataKey*",
 "kms:ReEncrypt*"
 ],
 "Resource": "*",
 "Condition": {
 "ArnLike": {
 "kms:EncryptionContext:aws:logs:arn": "arn:aws:logs:*:*:log-group:/aws/lambda/amazon-bedrock*"
 }
 }
 }
 ]
}`

```

- **AmazonSageMakerDomainExecution role — inline
  Policy**: manually attach the following to the
  AmazonSageMakerDomainExecution role or any role that is used for domain
  execution role in IAM console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "KmsDescribeKeyPermissions",
 "Effect": "Allow",
 "Action": "kms:DescribeKey",
 "Resource": "arn:aws:kms:us-east-1:`111122223333`:key/dzd-12345"
 },
 {
 "Sid": "KmsPermissions",
 "Effect": "Allow",
 "Action": [
 "kms:CreateGrant",
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:us-east-1:`111122223333`:key/dzd-12345",
 "Condition": {
 "StringLike": {
 "kms:EncryptionContext:aws:datazone:domainId": "dzd*"
 }
 }
 }
 ]
}`

```

- \*\*AmazonSageMakerProvisioning-<domainAccountId> role

* inline Policy\*\*: manually attach the following to the
  AmazonSageMakerProvisioning-<domainAccountId> role or the role that is
  used as the provisioning role in the IAM console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "KmsDescribeKeyPermissions",
 "Effect": "Allow",
 "Action": "kms:DescribeKey",
 "Resource": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
 },
 {
 "Sid": "ToolingBlueprintS3BucketKmsPermissions",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
 "Condition": {
 "StringLike": {
 "kms:ViaService": "s3.*.amazonaws.com"
 }
 }
 },
 {
 "Sid": "LambdaFunctionKmsPermissions",
 "Effect": "Allow",
 "Action": [
 "kms:CreateGrant",
 "kms:Decrypt",
 "kms:Encrypt"
 ],
 "Resource": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
 "Condition": {
 "StringLike": {
 "kms:ViaService": "lambda.*.amazonaws.com"
 },
 "ArnLike": {
 "kms:EncryptionContext:aws:lambda:FunctionArn": "arn:aws:lambda:*:*:function:amazon-bedrock*"
 }
 }
 },
 {
 "Sid": "SecretsManagerKmsPermissions",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:Encrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
 "Condition": {
 "StringLike": {
 "kms:ViaService": "secretsmanager.*.amazonaws.com"
 },
 "ArnLike": {
 "kms:EncryptionContext:SecretARN": "arn:aws:secretsmanager:*:*:secret:amazon-bedrock*"
 }
 }
 },
 {
 "Sid": "BedrockKmsPermissions",
 "Effect": "Allow",
 "Action": [
 "kms:CreateGrant",
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
 "Condition": {
 "StringLike": {
 "kms:ViaService": "bedrock.*.amazonaws.com"
 },
 "ForAnyValue:StringLike": {
 "kms:EncryptionContextKeys": "aws:bedrock*:arn"
 }
 }
 }
 ]
}`

```
