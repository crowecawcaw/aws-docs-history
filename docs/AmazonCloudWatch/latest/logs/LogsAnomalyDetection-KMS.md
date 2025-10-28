# Encrypt an anomaly detector and its results

with AWS KMS

Anomaly detector data is always encrypted in CloudWatch Logs. By default, CloudWatch Logs uses server-side
encryption for the data at rest. As an alternative, you can use AWS Key Management Service for this
encryption. If you do, the encryption is done using an AWS KMS key. Encryption using AWS KMS
is enabled at the anomaly detector level, by associating a KMS key with an anomaly
detector.

###### Important

CloudWatch Logs supports only symmetric KMS keys. Do not use an asymmetric key to encrypt
the data in your log groups. For more information, see [Using Symmetric and Asymmetric
Keys](../../../kms/latest/developerguide/symmetric-asymmetric.md "../../../kms/latest/developerguide/symmetric-asymmetric.md").

## Limits

- To perform the following steps, you must have the following permissions:
  `kms:CreateKey`, `kms:GetKeyPolicy`, and
  `kms:PutKeyPolicy`.
- After you associate or disassociate a key from an anomaly detector, it can
  take up to five minutes for the operation to take effect.
- If you revoke CloudWatch Logs access to an associated key or delete an associated
  KMS key, your encrypted data in CloudWatch Logs can no longer be retrieved.

### Step 1: Create an AWS KMS key

To create an KMS key, use the following [create-key](../../../cli/latest/reference/kms/create-key.md "../../../cli/latest/reference/kms/create-key.md") command:

```
`aws kms create-key`
```

The output contains the key ID and Amazon Resource Name (ARN) of the key. The
following is example output:

```
{
    "KeyMetadata": {
        "Origin": "AWS_KMS",
        "KeyId": "key-default-1",
        "Description": "",
        "KeyManager": "CUSTOMER",
        "Enabled": true,
        "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
        "KeyUsage": "ENCRYPT_DECRYPT",
        "KeyState": "Enabled",
        "CreationDate": 1478910250.94,
        "Arn": "arn:aws:kms:us-west-2:123456789012:key/key-default-1",
        "AWSAccountId": "123456789012",
        "EncryptionAlgorithms": [
            "SYMMETRIC_DEFAULT"
        ]
    }
}
```

### Step 2: Set permissions on the

KMS key

By default, all AWS KMS keys are private. Only the resource owner can use it to
encrypt and decrypt data. However, the resource owner can grant permissions to
access the KMS key to other users and resources. With this step, you give the
CloudWatch Logs service principal permission to use the key. This service principal must
be in the same AWS Region where the KMS key is stored.

As a best practice, we recommend that you restrict the use of the KMS key to
only those AWS accounts or anomaly detectors that you specify.

First, save the default policy for your KMS key as
`policy.json` using the following [get-key-policy](../../../cli/latest/reference/kms/get-key-policy.md "../../../cli/latest/reference/kms/get-key-policy.md")
command:

```
`aws kms get-key-policy --key-id `key-id` --policy-name default --output text > ./policy.json`
```

Open the `policy.json` file in a text editor and add the
section in bold from one of the following statements. Separate the existing
statement from the new statement with a comma. These statements use
`Condition` sections to enhance the security of the AWS KMS key.
For more information, see [AWS KMS keys and encryption context](encrypt-log-data-kms.md#encrypt-log-data-kms-policy "encrypt-log-data-kms.md#encrypt-log-data-kms-policy").

The `Condition` section in this example limits the use of the AWS KMS
key to the specified account, but it can be used for any anomaly
detector.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "key-default-1",
 "Statement": [
 {
 "Sid": "EnableIAMUserPermissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": "kms:*",
 "Resource": "*"
 },
 {
 "Sid": "AllowCloudWatchLogsEncryption",
 "Effect": "Allow",
 "Principal": {
 "Service": "logs.`us-east-1`.amazonaws.com"
 },
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:GenerateDataKey*"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "StringLike": {
 "kms:EncryptionContext:aws:logs:arn": "arn:aws:logs:`us-east-1`:`123456789012`:anomaly-detector:*"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:logs:`us-east-1`:`123456789012`:anomaly-detector:*"
 }
 }
 },
 {
 "Sid": "AllowCloudWatchLogsDescribeKey",
 "Effect": "Allow",
 "Principal": {
 "Service": "logs.`us-east-1`.amazonaws.com"
 },
 "Action": "kms:DescribeKey",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 }
 }
 },
 {
 "Sid": "AllowCloudWatchLogsReEncryption",
 "Effect": "Allow",
 "Principal": {
 "Service": "logs.`us-east-1`.amazonaws.com"
 },
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:ReEncrypt*",
 "kms:GenerateDataKey*"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "StringLike": {
 "kms:EncryptionContext:aws-crypto-ec:aws:logs:arn": "arn:aws:logs:`us-east-1`:`123456789012`:anomaly-detector:*"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:logs:`us-east-1`:`123456789012`:anomaly-detector:*"
 }
 }
 },
 {
 "Sid": "AllowCloudWatchLogsDescribeKeyForReEncryption",
 "Effect": "Allow",
 "Principal": {
 "Service": "logs.`us-east-1`.amazonaws.com"
 },
 "Action": "kms:DescribeKey",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 }
 }
 }
 ]
}`

```

Finally, add the updated policy using the following [put-key-policy](../../../cli/latest/reference/kms/put-key-policy.md "../../../cli/latest/reference/kms/put-key-policy.md")
command:

```
aws kms put-key-policy --key-id `key-id` --policy-name default --policy file://policy.json
```

### Step 3: Associate a KMS key with an anomaly

detector

You can associate a KMS key with an anomaly detector when you create it in
the console or using the AWS CLI or APIs.

#### Step 4: Disassociate key from an anomaly

detector

After a key has been associated with an anomaly detector, you can't update
the key. The only way to remove the key is to delete the anomaly detector,
and then re-create it.
