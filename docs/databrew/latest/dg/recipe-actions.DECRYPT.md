# DECRYPT

You can use the DECRYPT transform to decrypt inside of DataBrew. Your data can also be
decrypted outside of DataBrew with the AWS Encryption SDK. If the provided KMS key ARN
does not match what was used to encrypt the column, the decrypt operation fails. For
more information on the AWS Encryption SDK, see
[What
is the AWS Encryption SDK](../../../encryption-sdk/latest/developer-guide/introduction.md "../../../encryption-sdk/latest/developer-guide/introduction.md") in the _AWS Encryption SDK Developer Guide_.

###### Parameters

- `sourceColumns` – An array of existing columns.
- `kmsKeyArn` – The key ARN of the AWS Key Management Service key to use to
  decrypt the source columns. For more information on the key ARN, see
  [Key ARN](../../../kms/latest/developerguide/concepts.md#key-id-key-ARN "../../../kms/latest/developerguide/concepts.md#key-id-key-ARN")
  in the _AWS Key Management Service Developer Guide_.

```
{
   "sourceColumns": ["phonenumber"],
   "kmsKeyArn": "arn:aws:kms:us-east-1:012345678901:key/<kms-key-id>"
}
```

When working in the interactive experience, in addition to the project’s role, the console
user must have permission to `kms:GenerateDataKey` and `kms:Decrypt` on the provided KMS key.

**Sample policy:**

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
 "arn:aws:kms:us-east-1:012345678901:key/`kms-key-id`"
 ]
 }
 ]
}`

```
