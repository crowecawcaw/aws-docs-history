# KMS

Permissions for resources provisioned by Amazon SageMaker Unified Studio

You can encrypt the resources provisioned by Amazon SageMaker Unified Studio with your
customer managed AWS KMS keys. You can do this by adding to your default KMS key
policy the permissions that you can find in the following policy for the Tooling
blueprint config.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "key-policy-for-smus",
 "Statement": [
 {
 "Sid": "AllowKmsPermissionsForCloudWatch",
 "Effect": "Allow",
 "Principal": {
 "Service": "logs.us-east-1.amazonaws.com"
 },
 "Action": [
 "kms:Encrypt*",
 "kms:Decrypt*",
 "kms:ReEncrypt*",
 "kms:GenerateDataKey*",
 "kms:Describe*"
 ],
 "Resource": "*",
 "Condition": {
 "ArnLike": {
 "kms:EncryptionContext:aws:logs:arn": "arn:aws:logs:us-east-1:111122223333:log-group:datazone-*"
 }
 }
 },
 {
 "Sid": "RedshiftCreateGrantKmsPermissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/service-role/AmazonSageMakerProvisioning-111122223333"
 },
 "Action": "kms:CreateGrant",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 },
 "StringLike": {
 "kms:ViaService": [
 "redshift-serverless.*.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "AthenaKmsPermissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/service-role/AmazonSageMakerProvisioning-111122223333"
 },
 "Action": "kms:GenerateDataKey",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:CalledViaLast": "athena.amazonaws.com",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "EmrServerlessKmsPermissions",
 "Effect": "Allow",
 "Principal": {
 "Service": "emr-serverless.amazonaws.com"
 },
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "*",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:emr-serverless:us-east-1:111122223333:/applications/*"
 }
 }
 },
 {
 "Sid": "EmrServerlessKmsPermissionsForProvisioning",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/service-role/AmazonSageMakerProvisioning-111122223333"
 },
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowKmsKeyUsageForSageMakerDomain",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "datazone.amazonaws.com"
 ],
 "AWS": [
 "arn:aws:iam::`111122223333`:role/service-role/AmazonSageMakerDomainExecution"
 ]
 },
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:ReEncrypt*",
 "kms:GenerateDataKey*",
 "kms:DescribeKey",
 "kms:CreateGrant"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowSageMakerDomainKmsGrantPermissions",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "datazone.amazonaws.com"
 ],
 "AWS": [
 "arn:aws:iam::`111122223333`:role/service-role/AmazonSageMakerDomainExecution"
 ]
 },
 "Action": [
 "kms:ListGrants",
 "kms:RevokeGrant"
 ],
 "Resource": "*"
 },
 {
 "Sid": "GrantKMSPermissionsForAllProjectRoles",
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Effect": "Allow",
 "Principal": {
 "AWS": "*"
 },
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:PrincipalTag/AmazonDataZoneDomain": "`dzd_0123456789`",
 "kms:EncryptionContext:aws:datazone:domainId": "`dzd_0123456789`",
 "kms:ViaService": [
 "datazone.`us-east-1`.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```
