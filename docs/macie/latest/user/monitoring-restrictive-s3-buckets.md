# Allowing Macie to access S3 buckets and

objects

When you enable Amazon Macie for your AWS account, Macie creates a [service-linked role](service-linked-roles.md "service-linked-roles.md") that grants Macie the
permissions that it requires to call Amazon Simple Storage Service (Amazon S3) and other AWS services on your
behalf. A service-linked role simplifies the process of setting up an AWS service because
you don't have to manually add permissions for the service to complete actions on your
behalf. To learn about this type of role, see [IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") in the _AWS Identity and Access Management User Guide_.

The permissions policy for the Macie service-linked role
(`AWSServiceRoleForAmazonMacie`) allows Macie to perform actions that include
retrieving information about your S3 buckets and objects, and retrieving objects from your
buckets. If you're the Macie administrator for an organization, the policy also allows Macie to
perform these actions on your behalf for member accounts in your organization.

Macie uses these permissions to perform tasks such as:

- Generate and maintain an inventory of your S3 general purpose buckets.
- Provide statistical and other data about the buckets and objects in the buckets.
- Monitor and evaluate the buckets for security and access control.
- Analyze objects in the buckets to detect sensitive data.
  In most cases, Macie has the permissions that it needs to perform these tasks. However, if an
  S3 bucket has a restrictive bucket policy, the policy might prevent Macie from performing
  some or all of these tasks.

A _bucket policy_ is a resource-based AWS Identity and Access Management (IAM)
policy that specifies which actions a principal (user, account, service, or other entity)
can perform on an S3 bucket, and the conditions under which a principal can perform those
actions. The actions and conditions can apply to bucket-level operations, such as retrieving
information about a bucket, and object-level operations, such as retrieving objects from a
bucket.

Bucket policies typically grant or restrict access by using explicit `Allow` or
`Deny` statements and conditions. For example, a bucket policy might contain an
`Allow` or `Deny` statement that denies access to the bucket unless
specific source IP addresses, Amazon Virtual Private Cloud (Amazon VPC) endpoints, or VPCs are used to access the
bucket. For information about using bucket policies to grant or restrict access to buckets,
see [Bucket
policies for Amazon S3](../../../AmazonS3/latest/userguide/bucket-policies.md "../../../AmazonS3/latest/userguide/bucket-policies.md") and [How Amazon S3 authorizes a
request](../../../AmazonS3/latest/userguide/how-s3-evaluates-access-control.md "../../../AmazonS3/latest/userguide/how-s3-evaluates-access-control.md") in the _Amazon Simple Storage Service User Guide_.

If a bucket policy uses an explicit `Allow` statement, the policy doesn’t
prevent Macie from retrieving information about the bucket and the bucket’s objects, or
retrieving objects from the bucket. This is because the `Allow` statements in the
permissions policy for the Macie service-linked role grant these permissions.

However, if a bucket policy uses an explicit `Deny` statement with one or more
conditions, Macie might not be allowed to retrieve information about the bucket or the
bucket’s objects, or retrieve the bucket’s objects. For example, if a bucket policy
explicitly denies access from all sources except a specific IP address, Macie won't be
allowed to analyze the bucket’s objects when you run a sensitive data discovery job. This is
because restrictive bucket policies take precedence over the `Allow` statements
in the permissions policy for the Macie service-linked role.

To allow Macie to access an S3 bucket that has a restrictive bucket policy, you can add a
condition for the Macie service-linked role (`AWSServiceRoleForAmazonMacie`) to
the bucket policy. The condition can exclude the Macie service-linked role from matching the
`Deny` restriction in the policy. It can do this by using the
`aws:PrincipalArn`
[global condition
context key](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") and the Amazon Resource Name (ARN) of the Macie service-linked
role.

The following procedure guides you through this process and provides an example.

###### To add the Macie service-linked role to a bucket policy

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Buckets**.
3. Choose the S3 bucket that you want to allow Macie to access.
4. On the **Permissions** tab, under **Bucket
   policy**, choose **Edit**.
5. In the **Bucket policy** editor, identify each `Deny`
   statement that restricts access and prevents Macie from accessing the bucket or the
   bucket's objects.
6. In each `Deny` statement, add a condition that uses the
   `aws:PrincipalArn` global condition context key and specifies the ARN
   of the Macie service-linked role for your AWS account.

The value for the condition key should be
`arn:aws:iam::`123456789012`:role/aws-service-role/macie.amazonaws.com/AWSServiceRoleForAmazonMacie`,
where `123456789012` is the account ID for your
AWS account.
Where you add this to a bucket policy depends on the structure, elements, and conditions
that the policy currently contains. To learn about supported structures and elements, see
[Policies and
permissions in Amazon S3](../../../AmazonS3/latest/userguide/access-policy-language-overview.md "../../../AmazonS3/latest/userguide/access-policy-language-overview.md") in the _Amazon Simple Storage Service User Guide_.

The following is an example of a bucket policy that uses an explicit `Deny`
statement to restrict access to an S3 bucket named `amzn-s3-demo-bucket`. With the current
policy, the bucket can be accessed only from the VPC endpoint whose ID is
`vpce-1a2b3c4d`. Access from all other VPC endpoints is denied, including
access from the AWS Management Console and Macie.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "Policy1415115example",
 "Statement": [
 {
 "Sid": "Access only from specific VPCE",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:*",
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket",
 "arn:aws:s3:::amzn-s3-demo-bucket/*"
 ],
 "Condition": {
 "StringNotEquals": {
 "aws:SourceVpce": "vpce-1a2b3c4d"
 }
 }
 }
 ]
}`

```

To change this policy and allow Macie to access the S3 bucket and the bucket's objects, we
can add a condition that uses the `StringNotLike`
[condition operator](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md") and the `aws:PrincipalArn`
[global condition
context key](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md"). This additional condition excludes the Macie service-linked role
from matching the `Deny` restriction.

JSON

```
`{
 "Version":"2012-10-17",
 "Id":" Policy1415115example ",
 "Statement": [
 {
 "Sid": "Access only from specific VPCE and Macie",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:*",
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket",
 "arn:aws:s3:::amzn-s3-demo-bucket/*"
 ],
 "Condition": {
 "StringNotEquals": {
 "aws:SourceVpce": "vpce-1a2b3c4d"
 },
 "StringNotLike": {
 "aws:PrincipalArn": "arn:aws:iam::123456789012:role/aws-service-role/macie.amazonaws.com/AWSServiceRoleForAmazonMacie"
 }
 }
 }
 ]
}`

```

In the preceding example, the `StringNotLike` condition operator uses the
`aws:PrincipalArn` condition context key to specify the ARN of the Macie
service-linked role, where:

- `123456789012` is the account ID for the AWS account that's permitted
  to use Macie to retrieve information about the bucket and the bucket's objects, and
  retrieve objects from the bucket.
- `macie.amazonaws.com` is the identifier for the Macie service
  principal.
- `AWSServiceRoleForAmazonMacie` is the name of the Macie service-linked
  role.
  We used the `StringNotLike` operator because the policy already uses a
  `StringNotEquals` operator. A policy can use the `StringNotEquals`
  operator only once.

For additional policy examples and detailed information about managing access to Amazon S3
resources, see [Access control](../../../AmazonS3/latest/userguide/access-management.md "../../../AmazonS3/latest/userguide/access-management.md") in the
_Amazon Simple Storage Service User Guide_.
