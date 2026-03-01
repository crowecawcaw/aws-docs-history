# Manage access to Amazon Q Developer for third-party integration

For third-party integrations, you must use the AWS Key Management Service (KMS) to manage access
to Amazon Q Developer instead of IAM policies that are neither identity-based or resource-based.

## Allow administrators to use customer managed keys to update role policies

The following example key policy grants permission to use [customer managed keys
(CMK)](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md") when creating your key policy on a configured role in the KMS Console. When
configuring the CMK, you must provide the [IAM role ARN](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns"), an identifier, used by your integration to call Amazon Q. If you already
onboarded an integration such as a GitLab instance, you must reonboard the instance for all
resources to be encrypted with CMK.

The `kms:ViaService` condition key limits the use of a KMS key to requests from
specified AWS services. Additionally, it’s used to deny permission to use a KMS key when the
request comes from particular services. With the condition key, you can limit who can use CMK for
encrypting or decrypting content. For more information, see [kms:ViaService](../../../kms/latest/developerguide/conditions-kms.md#conditions-kms-via-service "../../../kms/latest/developerguide/conditions-kms.md#conditions-kms-via-service") in the _AWS Key Management Service Developer
Guide_.

With KMS encryption context, you have an optional set of key-value pairs that can be included
in cryptographic operations with symmetric encryption KMS keys to enhance authorization and
auditability. The encryption context can be used to verify the integrity and authenticity of
encrypted data, control access to symmetric encryption KMS keys in key policies and IAM policies,
and identify and categorize cryptographic operations in AWS CloudTrail logs. For more information,
see [Encryption context](../../../kms/latest/developerguide/encrypt_context.md "../../../kms/latest/developerguide/encrypt_context.md") in the _AWS Key Management Service Developer
Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Sid0",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`rolename`"
 },
 "Action": [
 "kms:GenerateDataKeyWithoutPlaintext",
 "kms:Decrypt",
 "kms:ReEncryptFrom",
 "kms:ReEncryptTo",
 "kms:GenerateDataKey",
 "kms:Encrypt"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "q.`us-east-1`.amazonaws.com",
 "kms:EncryptionContext:aws-crypto-ec:aws:qdeveloper:accountId": "`111122223333`"
 }
 }
 },
 {
 "Sid": "Sid1",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`rolename`"
 },
 "Action": "kms:DescribeKey",
 "Resource": "*"
 }
 ]
}`

```
