# Encrypting logs

## Encrypting EMR Serverless

logs with managed storage

To encrypt logs in managed storage with your own KMS key, use the
`managedPersistenceMonitoringConfiguration` configuration when you
submit a job run.

```
{
    "monitoringConfiguration": {
        "managedPersistenceMonitoringConfiguration" : {
            "encryptionKeyArn": "`key-arn`"
        }
    }
}
```

## Encrypting EMR Serverless logs

with Amazon S3 buckets

To encrypt logs in your Amazon S3 bucket with your own KMS key, use the
`s3MonitoringConfiguration` configuration when you submit a job
run.

```
{
    "monitoringConfiguration": {
        "s3MonitoringConfiguration": {
            "logUri": "s3://`amzn-s3-demo-logging-bucket`/logs/",
            "encryptionKeyArn": "`key-arn`"
        }
    }
}
```

## Encrypting EMR Serverless logs with

Amazon CloudWatch

To encrypt logs in Amazon CloudWatch with your own KMS key, use the
`cloudWatchLoggingConfiguration` configuration when you submit a job
run.

```
{
    "monitoringConfiguration": {
        "cloudWatchLoggingConfiguration": {
            "enabled": true,
            "encryptionKeyArn": "key-arn"
         }
     }
}
```

## Required permissions for log

encryption

###### In this section

- [Required user
  permissions](#jobs-log-encryption-permissions-user "#jobs-log-encryption-permissions-user")
- [Encryption key permissions
  for Amazon S3 and managed storage](#jobs-log-encryption-permissions-s3 "#jobs-log-encryption-permissions-s3")
- [Encryption key permissions
  for Amazon CloudWatch](#jobs-log-encryption-permissions-cw "#jobs-log-encryption-permissions-cw")

### Required user

permissions

The user who submits the job or views the logs or the application UIs must
have permissions to use the key. You can specify the permissions in either the
KMS key policy or the IAM policy for the user, group, or role. If the user
who submits the job lacks the KMS key permissions, EMR Serverless rejects the
job run submission.

**Example key policy**

The following key policy provides the permissions to
`kms:GenerateDataKey` and `kms:Decrypt`:

```
{
    "Effect": "Allow",
    "Principal":{
       "AWS": "arn:aws:iam::`111122223333`:user/`user-name`"
     },
     "Action": [
       "kms:GenerateDataKey",
       "kms:Decrypt"
      ],
     "Resource": "*"
 }
```

**Example IAM policy**

The following IAM policy provides the permissions to
`kms:GenerateDataKey` and `kms:Decrypt`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:*:123456789012:key/12345678-1234-1234-1234-123456789012"
 ],
 "Sid": "AllowKMSGeneratedatakey"
 }
 ]
}`

```

To launch the Spark or Tez UI, give your users, groups, or roles
permissions to access the `emr-serverless:GetDashboardForJobRun` API
as follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "emr-serverless:GetDashboardForJobRun"
 ],
 "Resource": [
 "*"
 ],
 "Sid": "AllowEMRSERVERLESSGetdashboardforjobrun"
 }
 ]
}`

```

### Encryption key permissions

for Amazon S3 and managed storage

When you encrypt logs with your own encryption key either in managed storage
or in your S3 buckets, configure KMS key permissions as
follows.

The `emr-serverless.amazonaws.com` principal must have the
following permissions in the policy for the KMS key:

```
{
    "Effect": "Allow",
    "Principal":{
       "Service": "emr-serverless.amazonaws.com"
     },
     "Action": [
       "kms:Decrypt",
       "kms:GenerateDataKey"
      ],
     "Resource": "*"
     "Condition": {
       "StringLike": {
         "aws:SourceArn": "arn:aws:emr-serverless:region:`aws-account-id`:/applications/`application-id`"
       }
     }
 }
```

As a security best practice, we suggest that you add an
`aws:SourceArn` condition key to the KMS key policy. The IAM
global condition key `aws:SourceArn` helps ensure that
EMR Serverless uses the KMS key only for an application ARN.

The job runtime role must have the following permissions in its IAM
policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:*:123456789012:key/12345678-1234-1234-1234-123456789012"
 ],
 "Sid": "AllowKMSGeneratedatakey"
 }
 ]
}`

```

### Encryption key permissions

for Amazon CloudWatch

To associate the KMS key ARN to your log group, use the following IAM
policy for the job runtime role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:AssociateKmsKey"
 ],
 "Resource": [
 "arn:aws:logs:*:123456789012:log-group:my-log-group-name:*"
 ],
 "Sid": "AllowLOGSAssociatekmskey"
 }
 ]
}`

```

Configure the KMS key policy to grant KMS permissions to Amazon CloudWatch:

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "key-default-1",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "ArnLike": {
 "kms:EncryptionContext:aws:logs:arn": "arn:aws:logs:*:123456789012:*"
 }
 },
 "Sid": "AllowKMSDecrypt"
 }
 ]
}`

```
