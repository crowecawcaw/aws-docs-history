# Enforcing and scoping SSE-KMS use for tables and
 table buckets

You can use S3 Tables resource-based policies, KMS key policies, IAM
 identity-based policies, or any combination of these, to enforce the use of SSE-KMS for
 S3 tables and table buckets. For more information on identity and resource polices for
 tables, see [Access management for S3 Tables](s3-tables-setting-up.md "s3-tables-setting-up.md").
 For information on writing key policies, see [Key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html "https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html") in the
 *AWS Key Management Service Developer Guide*. The following examples show how you
 can use policies to enforce SSE-KMS.

This is an example of table bucket policy that prevents users from creating
 tables in a specific table bucket unless they encrypt tables with a specific
 AWS KMS key. To use this policy, replace the `user
 input placeholders` with your own information: 


JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "EnforceKMSEncryption",
 "Effect": "Deny",
 "Principal": "*",
 "Action": [
 "s3tables:CreateTable"
 ],
 "Resource": [
 "`arn:aws:s3tables:us-west-2:111122223333:bucket/example-table-bucket`/*"
 ],
 "Condition": {
 "StringNotEquals": {
 "s3tables:sseAlgorithm": "aws:kms",
 "s3tables:kmsKeyArn": "`arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`"
 }
 }
 }
 ]
}`

```




This IAM identity policy requires users to use a specific AWS KMS key for
 encryption when creating or configuring S3 Tables resources. To use this policy, replace the `user input
 placeholders` with your own information:


```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "RequireKMSKeyOnTables",
      "Action": [
          "s3tables:CreateTableBucket",
          "s3tables:PutTableBucketEncryption",
          "s3tables:CreateTable"
      ]
      "Effect": "Deny",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
            "s3tables:sseAlgorithm": "aws:kms",
            "s3tables:kmsKeyArn": "`<key_arn>`"
        }
      }
    }
  ]
}
```
This example KMS key policy allows the key to be used by a specific user only
 for encryption operations in a specific table bucket. This type of policy is useful for
 limiting access to a key in cross-account scenarios. To use this policy, replace
 the `user input placeholders` with your own
 information: 


JSON





```
`{
 "Version":"2012-10-17", 
 "Id": "Id",
 "Statement": [
 {
 "Sid": "AllowPermissionsToKMS",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "kms:EncryptionContext:aws:s3:arn": "`<table-bucket-arn>`/*"
 }
 }
 }
 ]
}` 

```
