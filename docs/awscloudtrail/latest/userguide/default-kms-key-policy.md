# Default KMS key policy created in CloudTrail console

If you create an AWS KMS key in the CloudTrail console, the following policies are
 automatically created for you. The policy allows these permissions:


* Allows AWS account (root) permissions for the KMS key.
* Allows CloudTrail to encrypt log files and digest files under the KMS key and describe the
 KMS key.
* Allows all users in the specified accounts to decrypt log files and digest files.
* Allows all users in the specified account to create a KMS alias for the
 KMS key.
* Enables cross-account log decryption for the account ID of the account that
 created the trail.
###### Topics

* [Default KMS key policy for trails](#default-kms-key-policy-trail "#default-kms-key-policy-trail")
* [Default KMS key policy for CloudTrail Lake event data stores](#default-kms-key-policy-eds "#default-kms-key-policy-eds")

## Default KMS key policy for trails


The following is the default policy created for a AWS KMS key that you use with a trail.


###### Note

The policy includes a statement to allow cross accounts 
 to decrypt log files and digest files with the KMS key.



JSON





```
`{
 "Version":"2012-10-17", 
 "Id": "Key policy created by CloudTrail",
 "Statement": [
 {
 "Sid": "Enable IAM user permissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`111111111111`:root",
 "arn:aws:iam::`111111111111`:user/`username`"
 ]
 },
 "Action": "kms:*",
 "Resource": "*"
 },
 {
 "Sid": "Allow CloudTrail to encrypt logs",
 "Effect": "Allow",
 "Principal": {
 "Service": "cloudtrail.amazonaws.com"
 },
 "Action": "kms:GenerateDataKey*",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": "arn:aws:cloudtrail:`us-east-1`:`111111111111`:trail/`trail-name`"
 },
 "StringLike": {
 "kms:EncryptionContext:aws:cloudtrail:arn": "arn:aws:cloudtrail:*:`111111111111`:trail/*"
 }
 }
 },
 {
 "Sid": "Allow CloudTrail to describe key",
 "Effect": "Allow",
 "Principal": {
 "Service": "cloudtrail.amazonaws.com"
 },
 "Action": "kms:DescribeKey",
 "Resource": "*"
 },
 {
 "Sid": "Allow principals in the account to decrypt log files",
 "Effect": "Allow",
 "Principal": {
 "AWS": "*"
 },
 "Action": [
 "kms:Decrypt",
 "kms:ReEncryptFrom"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:CallerAccount": "`111111111111`"
 },
 "StringLike": {
 "kms:EncryptionContext:aws:cloudtrail:arn": "arn:aws:cloudtrail:*:`111111111111`:trail/*"
 }
 }
 },
 {
 "Sid": "Enable cross account log decryption",
 "Effect": "Allow",
 "Principal": {
 "AWS": "*"
 },
 "Action": [
 "kms:Decrypt",
 "kms:ReEncryptFrom"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:CallerAccount": "`111111111111`"
 },
 "StringLike": {
 "kms:EncryptionContext:aws:cloudtrail:arn": "arn:aws:cloudtrail:*:`111111111111`:trail/*"
 }
 }
 }
 ]
}`

```





## Default KMS key policy for CloudTrail Lake event data stores


The following is the default policy created for a AWS KMS key that you use with
 an event data store in CloudTrail Lake.



JSON





```
`{
 "Version":"2012-10-17", 
 "Id": "Key policy created by CloudTrail",
 "Statement": [
 {
 "Sid": "The key created by CloudTrail to encrypt event data stores. Created ${new Date().toUTCString()}",
 "Effect": "Allow",
 "Principal": {
 "Service": "cloudtrail.amazonaws.com"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "*"
 },
 {
 "Sid": "Enable IAM user permissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111111111111`:root"
 },
 "Action": "kms:*",
 "Resource": "*"
 },
 {
 "Sid": "Enable user to have permissions",
 "Effect": "Allow",
 "Principal": {
 "AWS" : "arn:aws:sts::`111111111111`:assumed-role/`example-role-name`"
 },
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "*"
 }
 ]
 }`

```
