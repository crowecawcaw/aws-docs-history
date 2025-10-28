# Encrypting data at rest in your Amazon Neptune database

Neptune encrypted instances provide an additional layer of data protection by helping to
secure your data from unauthorized access to the underlying storage. You can use Neptune
encryption to increase data protection of your applications that are deployed in the cloud. You
can also use it to fulfill compliance requirements for data-at-rest encryption.

To manage the keys used for encrypting and decrypting your Neptune resources, you use
[AWS Key Management Service (AWS KMS)](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md"). AWS KMS combines secure,
highly available hardware and software to provide a key management system scaled for the cloud.
Using AWS KMS, you can create encryption keys and define the policies that control how these keys
can be used. AWS KMS supports AWS CloudTrail, so you can audit key usage to verify that keys are being
used appropriately. You can use your AWS KMS keys in combination with Neptune and supported AWS
services such as Amazon Simple Storage Service (Amazon S3), Amazon Elastic Block Store (Amazon EBS), and Amazon Redshift. For a list of services that
support AWS KMS, see [How AWS Services Use AWS KMS](../../../kms/latest/developerguide/services.md "../../../kms/latest/developerguide/services.md")
in the _AWS Key Management Service Developer Guide_.

All logs, backups, and snapshots are encrypted for a Neptune encrypted instance.

## Enabling Encryption for a Neptune DB Instance

To enable encryption for a new Neptune DB instance, choose **Yes** in the
**Enable encryption** section on the Neptune console. For information about
creating a Neptune DB instance, see [Creating an Amazon Neptune cluster](get-started-create-cluster.md "get-started-create-cluster.md").

When you create an encrypted Neptune DB instance, you can also supply the AWS KMS key identifier
for your encryption key. If you don't specify an AWS KMS key identifier, Neptune uses your
default Amazon RDS encryption key (`aws/rds`) for your new Neptune DB instance. AWS KMS creates
your default encryption key for Neptune for your AWS account. Your AWS account has a
different default encryption key for each AWS Region.

After you create an encrypted Neptune DB instance, you can't change the encryption key for that
instance. So, be sure to determine your encryption key requirements before you create your
encrypted Neptune DB instance.

You can use the Amazon Resource Name (ARN) of a key from another account to encrypt a
Neptune DB instance. If you create a Neptune DB instance with the same AWS account that owns the AWS KMS
encryption key that's used to encrypt that new Neptune DB instance, the AWS KMS key ID that you pass
can be the AWS KMS key alias instead of the key's ARN.

###### Important

If Neptune loses access to the encryption key for a Neptune DB instance—for example, when
Neptune access to a key is revoked—the encrypted DB instance is placed into a
terminal state and can only be restored from a backup. We strongly recommend that you always
enable backups for encrypted NeptuneDB instances to guard against the loss of encrypted
data in your databases.

## Key permissions needed when enabling encryption

The IAM user or role creating an encrypted Neptune DB instance must have at least the
following permissions for the KMS key:

- `"kms:Encrypt"`
- `"kms:Decrypt"`
- `"kms:GenerateDataKey"`
- `"kms:ReEncryptTo"`
- `"kms:GenerateDataKeyWithoutPlaintext"`
- `"kms:CreateGrant"`
- `"kms:ReEncryptFrom"`
- `"kms:DescribeKey"`

Here is an example of a key policy that includes the necessary permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "key-consolepolicy-3",
 "Statement": [
 {
 "Sid": "Allow use of the key for Neptune",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:role/NeptuneFullAccess"
 },
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:GenerateDataKey",
 "kms:ReEncryptTo",
 "kms:GenerateDataKeyWithoutPlaintext",
 "kms:CreateGrant",
 "kms:ReEncryptFrom",
 "kms:DescribeKey"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "rds.us-east-1.amazonaws.com"
 }
 }
 },
 {
 "Sid": "Deny use of the key for non Neptune",
 "Effect": "Deny",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:role/NeptuneFullAccess"
 },
 "Action": [
 "kms:*"
 ],
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "kms:ViaService": "rds.us-east-1.amazonaws.com"
 }
 }
 }
 ]
}`

```

- The first statement provides access to all the required AWS KMS APIs for this role,
  scoped down to the RDS Service Principal.
- The second statement tightens the security more by enforcing that this key is not usable
  by this role for any other AWS service.

You could also scope `createGrant` permissions down further by adding:

```
"Condition": {
  "Bool": {
    "kms:GrantIsForAWSResource": true
  }
}
```

## Limitations of Neptune Encryption

The following limitations exist for encrypting Neptune clusters:

- You cannot convert an unencrypted DB cluster to an encrypted one.

However, you can restore an unencrypted DB cluster snapshot to an
encrypted DB cluster. To do this, specify a KMS encryption key when you
restore from the unencrypted DB cluster snapshot.

- You cannot convert an unencrypted DB instance to an encrypted one.
  You can only enable encryption for a DB instance when you create it.
- Also, DB instances that are encrypted can't be modified to disable encryption.
- You can't have an encrypted Read Replica of an unencrypted DB instance,
  or an unencrypted Read Replica of an encrypted DB instance.
- Encrypted Read Replicas must be encrypted with the same key as
  the source DB instance.
