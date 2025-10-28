# Giving Amazon Personalize permission to use your AWS KMS key

If you specify a AWS Key Management Service (AWS KMS) key when you use the Amazon Personalize console or APIs, or if you use your AWS KMS key
to encrypt an Amazon S3 bucket, you must grant Amazon Personalize
permission to use your key. To grant permissions, your AWS KMS key policy _and_ IAM policy attached to your service role must grant
Amazon Personalize permission to use your key. This applies for creating the following in Amazon Personalize.

- Dataset groups
- Dataset import job (only AWS KMS key policy must grant permissions)
- Dataset export jobs
- Batch inference jobs
- Batch segment jobs
- Metric attributions

Your AWS KMS key policy and IAM policies must grant permissions for the following actions:

- Decrypt
- GenerateDataKey
- DescribeKey
- CreateGrant (only required in key policy)
- ListGrants
  Revoking AWS KMS key permissions after creating a resource can lead to issues when creating a filter or getting recommendations. For more information about AWS KMS policies, see
  [Using key policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the
  _AWS Key Management Service Developer Guide_. For information on creating an IAM policy, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_. For information on attaching an IAM policy to
  role, see [Adding and
  removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _IAM User Guide_.

###### Topics

- [Key policy example](#export-job-key-policy "#export-job-key-policy")
- [IAM policy example](#export-job-iam-policy "#export-job-iam-policy")

## Key policy example

The following key policy example grants Amazon Personalize and your role the minimum permissions for the preceding Amazon Personalize operations.

If you specify a key when you create a dataset group and want to export data from a dataset, your key policy must include the `GenerateDataKeyWithoutPlaintext` action.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "key-policy-123",
 "Statement": [
 {
 "Sid": "Allow use of the key",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`<personalize-role-name>`",
 "Service": "personalize.amazonaws.com"
 },
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey",
 "kms:DescribeKey",
 "kms:CreateGrant",
 "kms:ListGrants"
 ],
 "Resource": "*"
 }
 ]
}`

```

## IAM policy example

The following IAM policy example grants a role the minimum AWS KMS permissions required for the preceding Amazon Personalize operations.
For dataset import jobs, only the AWS KMS key policy needs to grant permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey",
 "kms:DescribeKey",
 "kms:ListGrants"
 ],
 "Resource": "*"
 }
 ]
}`

```
