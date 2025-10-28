# Granting permissions for MediaConvert to access encrypted Amazon S3 buckets

When you [enable
Amazon S3 default encryption](../../../AmazonS3/latest/userguide/bucket-encryption.md#bucket-encryption-how-to-set-up "../../../AmazonS3/latest/userguide/bucket-encryption.md#bucket-encryption-how-to-set-up"), Amazon S3 automatically encrypts your objects as you
upload them. You can optionally choose to use AWS Key Management Service (AWS KMS) to manage the key.
This is called SSE-KMS encryption.

If you enable SSE-KMS default encryption on the buckets that hold your
AWS Elemental MediaConvert input or output files, you must [add inline policies](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console") to your IAM service role. If you don't add inline
policies, MediaConvert can't read your input files or write your output files.

Grant these permissions in the following use cases:

- If your input bucket has SSE-KMS default encryption, grant
  `kms:Decrypt`.
- If your output bucket has SSE-KMS default encryption, grant
  `kms:GenerateDataKey`.
  The following example inline policy grants both permissions.

## Example

inline policy with kms:Decrypt and
kms:GenerateDataKey

This policy grants permissions for both `kms:Decrypt` and
`kms:GenerateDataKey`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike":

{ "kms:ViaService": "s3.*.amazonaws.com" }
 }
 }
 ]
}`

```
