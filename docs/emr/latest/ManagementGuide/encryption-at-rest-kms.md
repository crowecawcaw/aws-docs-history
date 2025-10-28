# Encryption at rest using a customer KMS key for the EMR WAL service

EMR write-ahead logs (WAL) provides customer KMS key encryption-at-rest support. The following details at a high level how Amazon EMR WAL
is integrated with AWS KMS:

The EMR write-ahead logs (WAL) interact with AWS during the following operations: `CreateWAL`, `AppendEdit`,
`ArchiveWALCheckPoint`, `CompleteWALFlush`, `DeleteWAL`, `GetCurrentWALTime`,
`ReplayEdits`, `TrimWAL` via the `EMR_EC2_DefaultRole` by default When any the previous operations listed are invoked, the EMR WAL
makes `Decrypt` and `GenerateDataKey` against the KMS key.

## Considerations

Consider the following when using AWS KMS based encryption for EMR WAL:

- The encryption configuration can't be changed after an EMR WAL is created.
- When you use KMS encryption with your own KMS key, the key must exist in
  the same region as your Amazon EMR cluster.
- You are responsible to maintain all required IAM permissions and it's recommended to not revoke the
  needed permissions during the life of the WAL. Otherwise, it will cause unexpected failure scenarios, such as the inability to delete EMR WAL, as the
  associated encryption key doesn't exist.
- There is a cost associated with using AWS KMS keys. For more information, see [AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

## Required IAM permissions

To use your customer KMS key to encrypt EMR WAL at rest, you need to make sure you set proper permission to the EMR WAL client
role and the EMR WAL service principal `emrwal.amazonaws.com`.

### Permissions for the EMR WAL client role

Below is the IAM policy needed for the EMR WAL client role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey*"
 ],
 "Resource": [
 "*"
 ],
 "Sid": "AllowKMSDecrypt"
 }
 ]
}`

```

The EMR WAL client on EMR cluster will use `EMR_EC2_DefaultRole` by default. If you use a different role for the instance profile in
the EMR cluster, make sure that each role has appropriate permissions.

For more information about managing the role policy, refer
to [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md").

### Permissions for the KMS key policy

You need to give the EMR WAL client role and EMR WAL service `Decrypt` and `GenerateDataKey*` permission in
your KMS policy. For more about the key policy management, refer to [KMS key policy](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey*"
 ],
 "Resource": [
 "arn:aws:kms:*:123456789012:key/*"
 ],
 "Sid": "AllowKMSDecrypt"
 }
 ]
}`

```

The role specified in the snippet can change if you change the default role.

## Monitoring Amazon EMR WAL interaction with AWS KMS

### Amazon EMR WAL encryption context

An encryption context is a set of key–value pairs that contains arbitrary non-secret data. When you include an encryption context in
a request to encrypt data, AWS KMS cryptographically binds the encryption context to the encrypted data. To decrypt the data, you must pass in the
same encryption context.

In its [GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") and [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") requests
to AWS KMS, Amazon EMR WAL uses an encryption context with one name–value pairs that identify the EMR WAL name.

```
"encryptionContext": {
    "aws:emrwal:walname": "111222333444555-testworkspace-emrwalclustertest-emrwaltestwalname"
}
```

You can use the encryption context to identify these cryptographic operation in audit records and logs, such
as AWS CloudTrail and [Amazon CloudWatch Logs](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md"), and as a condition for authorization
in policies and grants.
