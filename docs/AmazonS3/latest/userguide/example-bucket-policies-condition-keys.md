# Policy examples for ACLs

You can use condition keys in bucket policies to control access to Amazon S3.

###### Topics

- [Granting s3:PutObject permission with a condition requiring the bucket owner to get full control](#grant-putobject-conditionally-1 "#grant-putobject-conditionally-1")
- [Granting s3:PutObject permission with a condition on the x-amz-acl header](#example-acl-header "#example-acl-header")

## Granting s3:PutObject permission with a condition requiring the bucket owner to get full control

The [PUT Object](../API/RESTObjectPUT.md "../API/RESTObjectPUT.md")
operation allows access control list (ACL)–specific headers that you
can use to grant ACL-based permissions. Using these keys, the bucket owner
can set a condition to require specific access permissions when the user
uploads an object.

Suppose that Account A owns a bucket, and the account administrator wants
to grant Dave, a user in Account B, permissions to upload objects. By
default, objects that Dave uploads are owned by Account B, and Account A has
no permissions on these objects. Because the bucket owner is paying the
bills, it wants full permissions on the objects that Dave uploads. The
Account A administrator can do this by granting the
`s3:PutObject` permission to Dave, with a condition that the
request include ACL-specific headers that either grant full permission
explicitly or use a canned ACL. For more information, see [PUT Object](../API/RESTObjectPUT.md "../API/RESTObjectPUT.md").

### Require the x-amz-full-control header

You can require the `x-amz-full-control` header in the
request with full control permission to the bucket owner. The following
bucket policy grants the `s3:PutObject` permission to user
Dave with a condition using the `s3:x-amz-grant-full-control`
condition key, which requires the request to include the
`x-amz-full-control` header.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "statement1",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/Dave"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`awsexamplebucket1`/*",
 "Condition": {
 "StringEquals": {
 "s3:x-amz-grant-full-control": "id=`AccountA-CanonicalUserID`"
 }
 }
 }
 ]
}`

```

###### Note

This example is about cross-account permission. However, if Dave
(who is getting the permission) belongs to the AWS account that
owns the bucket, this conditional permission is not necessary. This
is because the parent account to which Dave belongs owns objects
that the user uploads.

###### Add explicit deny

The preceding bucket policy grants conditional permission to user
Dave in Account B. While this policy is in effect, it is possible
for Dave to get the same permission without any condition via some
other policy. For example, Dave can belong to a group, and you grant
the group `s3:PutObject` permission without any
condition. To avoid such permission loopholes, you can write a
stricter access policy by adding explicit deny. In this example, you
explicitly deny the user Dave upload permission if he does not
include the necessary headers in the request granting full
permissions to the bucket owner. Explicit deny always supersedes any
other permission granted. The following is the revised access policy
example with explicit deny added.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "statement1",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/AccountBadmin"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`awsexamplebucket1`/*",
 "Condition": {
 "StringEquals": {
 "s3:x-amz-grant-full-control": "id=`AccountA-CanonicalUserID`"
 }
 }
 },
 {
 "Sid": "statement2",
 "Effect": "Deny",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/AccountBadmin"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`awsexamplebucket1`/*",
 "Condition": {
 "StringNotEquals": {
 "s3:x-amz-grant-full-control": "id=`AccountA-CanonicalUserID`"
 }
 }
 }
 ]
}`

```

###### Test the policy with the AWS CLI

If you have two AWS accounts, you can test the policy using the
AWS Command Line Interface (AWS CLI). You attach the policy and use Dave's credentials
to test the permission using the following AWS CLI
`put-object` command. You provide Dave's credentials
by adding the `--profile` parameter. You grant full
control permission to the bucket owner by adding the
`--grant-full-control` parameter. For more
information about setting up and using the AWS CLI, see [Developing with Amazon S3 using the AWS CLI](../API/setup-aws-cli.md "../API/setup-aws-cli.md") in the _Amazon S3 API Reference_.

```
aws s3api put-object --bucket `examplebucket` --key HappyFace.jpg --body c:\HappyFace.jpg --grant-full-control id="`AccountA-CanonicalUserID`" --profile AccountBUserProfile
```

### Require the x-amz-acl header

You can require the `x-amz-acl` header with a canned ACL
granting full control permission to the bucket owner. To require the
`x-amz-acl` header in the request, you can replace the
key-value pair in the `Condition` block and specify the
`s3:x-amz-acl` condition key, as shown in the following
example.

```
"Condition": {
    "StringEquals": {
        "s3:x-amz-acl": "bucket-owner-full-control"
    }
}
```

To test the permission using the AWS CLI, you specify the
`--acl` parameter. The AWS CLI then adds the
`x-amz-acl` header when it sends the request.

```
aws s3api put-object --bucket `examplebucket` --key HappyFace.jpg --body c:\HappyFace.jpg --acl "bucket-owner-full-control" --profile AccountBadmin
```

## Granting s3:PutObject permission with a condition on the x-amz-acl header

The following bucket policy grants the `s3:PutObject` permission
for two AWS accounts if the request includes the `x-amz-acl` header
making the object publicly readable. The `Condition` block uses the
`StringEquals` condition, and it is provided a key-value pair,
`"s3:x-amz-acl":["public-read"]`, for evaluation. In the key-value
pair, the `s3:x-amz-acl` is an Amazon S3–specific key, as
indicated by the prefix `s3:`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AddCannedAcl",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`111122223333`:root",
 "arn:aws:iam::`111122223333`:root"
 ]
 },
 "Action": "s3:PutObject",
 "Resource": [
 "arn:aws:s3:::`awsexamplebucket1`/*"
 ],
 "Condition": {
 "StringEquals": {
 "s3:x-amz-acl": [
 "public-read"
 ]
 }
 }
 }
 ]
}`

```

###### Important

Not all conditions make sense for all actions. For example, it makes sense
to include an `s3:LocationConstraint` condition on a policy that
grants the `s3:CreateBucket` Amazon S3 permission. However, it does
not make sense to include this condition on a policy that grants the
`s3:GetObject` permission. Amazon S3 can test for semantic errors
of this type that involve Amazon S3–specific conditions. However, if you
are creating a policy for an IAM user or role and you include a semantically
invalid Amazon S3 condition, no error is reported because IAM cannot validate
Amazon S3 conditions.
