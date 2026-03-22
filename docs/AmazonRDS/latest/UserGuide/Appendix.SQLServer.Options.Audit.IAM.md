# Manually creating an IAM role for SQL Server Audit

Typically, when you create a new option, the AWS Management Console creates the IAM role and the IAM
trust policy for you. However, you can manually create a new IAM role to use with
SQL Server Audits, so that you can customize it with any additional requirements you
might have. To do this, you create an IAM role and delegate permissions so that
the Amazon RDS service can use your Amazon S3 bucket. When you create this IAM role, you
attach trust and permissions policies. The trust policy allows Amazon RDS to assume this
role. The permission policy defines the actions that this role can do. For more
information, see [Creating a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
_AWS Identity and Access Management User
Guide_.

You can use the examples in this section to create the trust relationships and permissions policies you need.

The following example shows a trust relationship for SQL Server Audit. It uses the _service
principal_
`rds.amazonaws.com` to allow RDS to write to the S3 bucket. A _service
principal_ is an identifier that is used to grant permissions to a service. Anytime you allow access to
`rds.amazonaws.com` in this way, you are allowing RDS to perform an action on your behalf. For more
information about service principals, see [AWS JSON policy elements:
Principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md").

###### Example trust relationship for SQL Server Audit

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "`rds.amazonaws.com`"
 },
 "Action": "sts:AssumeRole"
 }
 ]
 }`

```

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource-based trust relationships to limit
the service's permissions to a specific resource. This is the most effective way to protect against the [confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md").

You might use both global condition context keys and have the `aws:SourceArn` value contain the account ID. In
this case, the `aws:SourceAccount` value and the account in the `aws:SourceArn` value must use the
same account ID when used in the same statement.

- Use `aws:SourceArn` if you want cross-service access for a single resource.
- Use `aws:SourceAccount` if you want to allow any resource in that account to be associated with the
  cross-service use.
  In the trust relationship, make sure to use the `aws:SourceArn` global condition context key with the full
  Amazon Resource Name (ARN) of the resources accessing the role. For SQL Server Audit, make sure to include both the DB
  option group and the DB instances, as shown in the following example.

###### Example trust relationship with global condition context key for SQL Server Audit

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "rds.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": [
 "arn:aws:rds:`Region`:`my_account_ID`:db:`db_instance_identifier`",
 "arn:aws:rds:`Region`:`my_account_ID`:og:`option_group_name`"
 ]
 }
 }
 }
 ]
}`

```

In the following example of a permissions policy for SQL Server Audit, we specify an ARN for the Amazon S3 bucket. You can use ARNs
to identify a specific account, user, or role that you want grant access to. For more information about using ARNs, see
[Amazon resource names
(ARNs)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

###### Example permissions policy for SQL Server Audit

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "s3:ListAllMyBuckets",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:GetBucketACL",
 "s3:GetBucketLocation"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:ListMultipartUploadParts",
 "s3:AbortMultipartUpload"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/`key_prefix`/*"
 }
 ]
 }`

```

###### Note

The `s3:ListAllMyBuckets` action is required for verifying that the same AWS account owns both the S3
bucket and the SQL Server DB instance. The action lists the names of the buckets in the account.

S3 bucket namespaces are global. If you accidentally delete your bucket, another user can create a bucket with the
same name in a different account. Then the SQL Server Audit data is written to the new bucket.
