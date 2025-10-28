# Granting access to an Amazon S3 bucket

When you create a file share, your File Gateway requires access to upload files into your
Amazon S3 bucket, and to perform actions on any access points or virtual private cloud (VPC)
endpoints that it uses to connect to the bucket. To grant this access, your File Gateway
assumes an AWS Identity and Access Management (IAM) role that is associated with an IAM policy that grants this
access.

The role requires this IAM policy and a security token service trust (STS) relationship
for it. The policy determines which actions the role can perform. In addition, your S3
bucket and any associated access points or VPC endpoints must have an access policy that
allows the IAM role to access them.

You can create the role and access policy yourself, or your File Gateway can create them
for you. If your File Gateway creates the policy for you, the policy contains a list of S3
actions. For information about roles and permissions, see [Creating a role to delegate
permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
_IAM User Guide_.

The following example is a trust policy that allows your File Gateway to assume an IAM
role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "storagegateway.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

###### Important

Storage Gateway can assume existing service roles that are passed using the
`iam:PassRole` policy action, but it does not support IAM policies that
use the `iam:PassedToService` context key to limit the action to specific
services.

For more information, see the following topics in the _AWS Identity and Access Management User
Guide_:

- [IAM: Pass an IAM role to a specific AWS service](../../../IAM/latest/UserGuide/reference_policies_examples_iam-passrole-service.md "../../../IAM/latest/UserGuide/reference_policies_examples_iam-passrole-service.md")
- [Granting a user
  permissions to pass a role to an AWS service](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md")
- [Available keys for IAM](../../../IAM/latest/UserGuide/reference_policies_iam-condition-keys.md#ck_PassedToService "../../../IAM/latest/UserGuide/reference_policies_iam-condition-keys.md#ck_PassedToService")
  If you don't want your File Gateway to create a policy on your behalf, you can create
  your own policy and attach it to your file share. For more information about how to do this,
  see [Creating a file share](GettingStartedCreateFileShare.md "GettingStartedCreateFileShare.md").

The following example policy allows your File Gateway to perform all the Amazon S3 actions
listed in the policy. The first part of the statement allows all the actions listed to be
performed on the S3 bucket named `amzn-s3-demo-bucket`. The second part allows
the listed actions on all objects in `amzn-s3-demo-bucket`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:GetAccelerateConfiguration",
 "s3:GetBucketLocation",
 "s3:GetBucketVersioning",
 "s3:ListBucket",
 "s3:ListBucketVersions",
 "s3:ListBucketMultipartUploads"
 ],
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket",
 "Effect": "Allow"
 },
 {
 "Action": [
 "s3:AbortMultipartUpload",
 "s3:DeleteObject",
 "s3:DeleteObjectVersion",
 "s3:GetObject",
 "s3:GetObjectAcl",
 "s3:GetObjectVersion",
 "s3:ListMultipartUploadParts",
 "s3:PutObject",
 "s3:PutObjectAcl"
 ],
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*",
 "Effect": "Allow"
 }
 ]
}`

```

The following example policy is similar to the preceding one, but allows your
File Gateway to perform actions required to access a bucket through an access point.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:AbortMultipartUpload",
 "s3:DeleteObject",
 "s3:DeleteObjectVersion",
 "s3:GetObject",
 "s3:GetObjectAcl",
 "s3:GetObjectVersion",
 "s3:ListMultipartUploadParts",
 "s3:PutObject",
 "s3:PutObjectAcl"
 ],
 "Resource": "arn:aws:s3:us-east-1:`111122223333`:accesspoint/TestAccessPointName/*",
 "Effect": "Allow"
 }
 ]
}`

```

###### Note

If you need to connect your file share to an S3 bucket through a VPC endpoint, see
[Endpoint policies for Amazon S3](../../../vpc/latest/privatelink/vpc-endpoints-s3.md#vpc-endpoints-policies-s3 "../../../vpc/latest/privatelink/vpc-endpoints-s3.md#vpc-endpoints-policies-s3") in the _AWS PrivateLink User
Guide_.

###### Note

For encrypted buckets, the fileshare must use the key in the destination S3 bucket
account.
