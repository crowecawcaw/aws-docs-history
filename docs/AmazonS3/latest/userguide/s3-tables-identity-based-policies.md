# IAM identity-based policies for S3 Tables

By default, users and roles don't have permission to create or modify tables and table
buckets. They also can't perform tasks by using the s3 console, AWS Command Line Interface
(AWS CLI), or Amazon S3 REST APIs. To create and access table buckets and tables, an AWS Identity and Access Management (IAM)
administrator must grant the necessary permissions to the IAM role or users. To learn how
to create an IAM identity-based policy by using these example JSON policy documents, see
[Creating IAM
policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the _IAM User Guide_.

The following topic includes examples of IAM identity-based policies. To use the following example policies, replace the `user input
 placeholders` with your own information.

###### Topics

- [Example 1: Allow access to create and use table buckets](#example-1-s3-tables-identity-based-policies "#example-1-s3-tables-identity-based-policies")
- [Example 2: Allow access to create and use tables in a table bucket](#example-2-s3-tables-identity-based-policies "#example-2-s3-tables-identity-based-policies")

## Example 1: Allow access to create and use table buckets

**.**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowBucketActions",
 "Effect": "Allow",
 "Action": [
 "s3tables:CreateTableBucket",
 "s3tables:PutTableBucketPolicy",
 "s3tables:GetTableBucketPolicy",
 "s3tables:ListTableBuckets",
 "s3tables:GetTableBucket"
 ],
 "Resource": "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/*"
 }
 ]
}`

```

## Example 2: Allow access to create and use tables in a table bucket

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowBucketActions",
 "Effect": "Allow",
 "Action": [
 "s3tables:GetTableBucket",
 "s3tables:ListTables",
 "s3tables:CreateTable",
 "s3tables:PutTableData",
 "s3tables:GetTableData",
 "s3tables:GetTable",
 "s3tables:GetTableMetadataLocation",
 "s3tables:UpdateTableMetadataLocation",
 "s3tables:GetNamespace",
 "s3tables:CreateNamespace",
 "s3tables:ListNamespaces"
 ],
 "Resource": [
 "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-bucket`",
 "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-bucket`/table/*"
 ]
 }
 ]
}`

```
