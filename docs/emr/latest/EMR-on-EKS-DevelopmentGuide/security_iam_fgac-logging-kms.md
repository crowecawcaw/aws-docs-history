# Encrypting Amazon EMR on EKS logs with managed storage

The sections that follow show you how to configure encryption for logs.

## Enable encryption

To encrypt logs in managed storage with your own KMS key, use the following configuration when you submit a job run.

```
"monitoringConfiguration": {
            "managedLogs": {
                "allowAWSToRetainLogs":"ENABLED",
                "encryptionKeyArn":"`KMS key arn`"
            },
            "persistentAppUI": "ENABLED"
        }
```

The `allowAWSToRetainLogs` configuration allows AWS to retain system namespace logs when running a job using Native FGAC. The `persistentAppUI` configuration
allows AWS to save event logs which are used to generate the Spark UI. The `encryptionKeyArn` is used to specify the KMS key ARN you want to use to encrypt the logs stored by AWS.

## Required permissions for log encryption

The user who submits the job or views the Spark UI must be allowed the actions `kms:DescribeKey`, `kms:GenerateDataKey`, and `kms:Decrypt` for the
encryption key. These permissions are used to verify the validity of the key and check that the user has the necessary permissions to read and write
logs encrypted with the KMS key. If the user who submits the job lacks the necessary key permissions, Amazon EMR on EKS rejects the job run submission.

**Example IAM Policy for Role Used to Call StartJobRun**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "emr-containers:StartJobRun"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow",
 "Sid": "AllowEMRCONTAINERSStartjobrun"
 },
 {
 "Action": [
 "kms:DescribeKey",
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": [
 "arn:aws:kms:*:*:key/`key-id`"
 ],
 "Effect": "Allow",
 "Sid": "AllowKMSDescribekey"
 }
 ]
}`

```

You must also configure the KMS key to allow the `persistentappui.elasticmapreduce.amazonaws.com` and `elasticmapreduce.amazonaws.com` Service Principals to `kms:GenerateDataKey`
and `kms:Decrypt`. This allows EMR to read and write logs encrypted with the KMS key to managed storage.

**Example KMS Key Policy**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:DescribeKey"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringLike": {
 "kms:viaService": "emr-containers.*.amazonaws.com"
 }
 },
 "Sid": "AllowKMSDescribekey"
 },
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
 "StringLike": {
 "kms:viaService": "emr-containers.*.amazonaws.com",
 "kms:EncryptionContext:aws:emr-containers:virtualClusterId": "`virtual cluster id`"
 }
 },
 "Sid": "AllowKMSDecryptGenerate"
 },
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
 "StringLike": {
 "kms:EncryptionContext:aws:emr-containers:virtualClusterId": "`virtual cluster id`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:emr-containers:*:*:/virtualclusters/`virtual_cluster_id`"
 }
 },
 "Sid": "AllowKMSDecryptService"
 }
 ]
}`

```

As a security best practice, we recommend that you add the `kms:viaService`, `kms:EncryptionContext`, and `aws:SourceArn` conditions. These conditions
help ensure the key is only used by Amazon EMR on EKS and only used for logs generated from jobs running in a specific virtual cluster.
