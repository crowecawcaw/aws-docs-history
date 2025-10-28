# Control access to Amazon S3 from Athena

You can grant access to Amazon S3 locations using identity-based policies, bucket resource
policies, access point policies, or any combination of the above. When actors interact
with Athena, their permissions pass through Athena to determine what Athena can access.
This means that users must have permission to access Amazon S3 buckets in order to query them
with Athena.

Whenever you use IAM policies, make sure that you follow IAM best practices. For more information, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

Note that requests to Amazon S3 come from a private IPv4 address for Athena, not the source
IP specified in `aws:SourceIp`. For this reason, you cannot use the
`aws:SourceIp` condition to deny access to Amazon S3 actions in a given IAM
policy. You also cannot restrict or allow access to Amazon S3 resources based on the
`aws:SourceVpc` or `aws:SourceVpce` condition keys.

###### Note

Athena workgroups that use IAM Identity Center authentication require that S3 Access Grants be
configured to use trusted identity propagation identities. For more information, see
[S3 Access
Grants and directory identities](../../../AmazonS3/latest/userguide/access-grants-directory-ids.md "../../../AmazonS3/latest/userguide/access-grants-directory-ids.md") in the
_Amazon Simple Storage Service User Guide_.

###### Topics

- [Identity-based
  policies](#s3-permissions-identity-based-policies "#s3-permissions-identity-based-policies")
- [Bucket
  resource policies](#s3-permissions-bucket-resource-policies "#s3-permissions-bucket-resource-policies")
- [Access point
  policies](#s3-permissions-aliases "#s3-permissions-aliases")
- [CalledVia context
  keys](#s3-permissions-calledvia "#s3-permissions-calledvia")
- [Additional resources](#s3-permissions-additional-resources "#s3-permissions-additional-resources")

## Use identity-based policies

to control access to Amazon S3 buckets

Identity-based policies are attached to an IAM user, group, or role. These
policies let you specify what that identity can do (its permissions). You can use
identity-based policies to control access to your Amazon S3 buckets.

The following identity-based policy allows `Read` and
`Write` access to objects in a specific Amazon S3 bucket. To use this
policy, replace the `italicized placeholder text` with your
own values.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ListObjectsInBucket",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket"
 ]
 },
 {
 "Sid": "AllObjectActions",
 "Effect": "Allow",
 "Action": "s3:*Object",
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket/*"
 ]
 }
 ]
}`

```

## Use bucket resource

policies to control access to Amazon S3 buckets

You can use Amazon S3 bucket policies to secure access to objects in your buckets so
that only users with the appropriate permissions can access them. For guidance on
creating your Amazon S3 policy, see [Adding a bucket policy by
using the Amazon S3 console](../../../AmazonS3/latest/userguide/add-bucket-policy.md "../../../AmazonS3/latest/userguide/add-bucket-policy.md") in the _Amazon S3 User Guide_.

The following example permissions policy limits a user to reading objects that
have the `environment: production` tag key and value. The example policy
uses the `s3:ExistingObjectTag` condition key to specify the tag key and
value.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`JohnDoe`"
 },
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*",
 "Condition": {
 "StringEquals": {
 "s3:ExistingObjectTag/environment": "production"
 }
 }
 }
 ]
}`

```

For more bucket policy examples, see [Examples of Amazon S3
bucket policies](../../../AmazonS3/latest/userguide/example-bucket-policies.md "../../../AmazonS3/latest/userguide/example-bucket-policies.md") in the _Amazon S3 User Guide_.

## Use Amazon S3 access points for more precise

control over bucket access

If you have a shared dataset in an Amazon S3 bucket, maintaining a single bucket policy
that manages access for hundreds of use cases can be challenging.

Amazon S3 bucket access points, policies, and aliases can help solve this issue. A
bucket can have multiple access points, each with a policy that controls access to
the bucket in a different way.

For each access point that you create, Amazon S3 generates an alias that represents the
access point. Because the alias is in Amazon S3 bucket name format, you can use the alias
in the `LOCATION` clause of your `CREATE TABLE` statements in
Athena. Athena's access to the bucket is then controlled by the policy for the access
point that the alias represents.

For more information, see [Specify a table location in Amazon S3](tables-location-format.md "tables-location-format.md") and [Using access points](../../../AmazonS3/latest/userguide/access-points.md "../../../AmazonS3/latest/userguide/access-points.md")
in the _Amazon S3 User Guide_.

## Use CalledVia context keys to allow only

calls from Athena to another service

For added security, you can use the [aws:CalledVia](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-calledvia "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-calledvia") global condition context key. The
`aws:CalledVia` condition key contains a list of services that you
allow to call another service. For example, you can allow
`InvokeFunction` calls to AWS Lambda only if the calls come from Athena
by specifying the Athena service principal name `athena.amazonaws.com` for
the `aws:CalledVia` context key. For more information, see [Use CalledVia context keys for Athena](security-iam-athena-calledvia.md "security-iam-athena-calledvia.md").

## Additional resources

For detailed information and examples about how to grant Amazon S3 access, see the
following resources:

- [Example
  walkthroughs: Managing access](../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access.md "../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access.md") in the
  _Amazon S3 User Guide_.
- [How can I
  provide cross-account access to objects that are in Amazon S3
  buckets?](https://aws.amazon.com/premiumsupport/knowledge-center/cross-account-access-s3/ "https://aws.amazon.com/premiumsupport/knowledge-center/cross-account-access-s3/") in the AWS Knowledge Center.
- [Configure cross-account access in Athena to Amazon S3
  buckets](cross-account-permissions.md "cross-account-permissions.md").
