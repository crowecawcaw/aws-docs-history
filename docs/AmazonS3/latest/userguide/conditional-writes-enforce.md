# Enforce conditional writes on Amazon S3 buckets

By using Amazon S3 bucket policies, you can enforce conditional writes for object uploads in your
general purpose buckets.

A bucket policy is a resource-based policy that you can use to grant access
permissions to your Amazon S3 bucket and the objects in it. Only the bucket owner can
associate a policy with a bucket. For more information about bucket policies, see [Bucket policies for Amazon S3](bucket-policies.md "bucket-policies.md").

You can use the condition keys `s3:if-match` or
`s3:if-none-match` as the optional `Condition` element or
`Condition` block to specify when a policy is in effect. For multipart uploads you
must specify the `s3:ObjectCreationOperation` condition key to exempt the
`CreateMultipartUpload`, `UploadPart`, and
`UploadPartCopy` operations, as these APIs don't accept conditional
headers. For more information about using conditions in bucket policies, see [Bucket policy examples using condition keys](amazon-s3-policy-keys.md "amazon-s3-policy-keys.md").

###### Note

If you use a bucket policy to enforce conditional writes, you can't perform copy
operations to the bucket or prefix specified in your bucket policy.
`CopyObject` requests without an `If-None-Match` or
`If-Match` HTTP header fail with a `403 Access Denied`
error. `CopyObject` requests made with those HTTP headers fail with a `501 Not
 Implemented` response.

The following examples show how to use conditions in a bucket policy to force clients
to use the `If-None-Match` or `If-Match` HTTP header.

###### Topics

- [Example 1: Only allow object
  uploads using PutObject and CompleteMultipartUpload
  requests that include the if-none-match header](#conditional-writes-enforce-ex1 "#conditional-writes-enforce-ex1")
- [Example 2: Only allow object
  uploads using PutObject and CompleteMultipartUpload
  requests that include the if-match header](#conditional-writes-enforce-ex2 "#conditional-writes-enforce-ex2")
- [Example 3: Only allow object upload
  requests that includes the if-none-match or if-match
  header](#conditional-writes-enforce-ex3 "#conditional-writes-enforce-ex3")

## Example 1: Only allow object

uploads using `PutObject` and `CompleteMultipartUpload`
requests that include the `if-none-match` header

This policy allows account 111122223333, user Alice, to write to the
`amzn-s3-demo-bucket1` bucket if the request includes the `if-none-match`
header, ensuring that the object key doesn't already exist in the bucket. All `PutObject` and `CompleteMultipartUpload` requests
to the specified bucket must include the `if-none-match` header to
succeed. Using this header, customers can write to this bucket only if the object
key does not exist in the bucket.

###### Note

This policy also sets the `s3:ObjectCreationOperation` condition
key which allows for multipart uploads using the
`CreateMultipartUpload`, `UploadPart`, and
`UploadPartCopy` APIs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowConditionalPut",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/Alice"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket1/*",
 "Condition": {
 "Null": {
 "s3:if-none-match": "false"
 }
 }
 },
 {
 "Sid": "AllowConditionalPutwithMPUs",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/Alice"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket1/*",
 "Condition": {
 "Bool": {
 "s3:ObjectCreationOperation": "false"
 }
 }
 }
 ]
}`

```

## Example 2: Only allow object

uploads using `PutObject` and `CompleteMultipartUpload`
requests that include the `if-match` header

This policy allows account 111122223333, user Alice to write to
`amzn-s3-demo-bucket1` only if the request includes the `if-match` header.
This header compares the ETag value of an object in S3 with one you provide during
the `WRITE` operation. If the ETag values do not match, the operation
will fail. All `PutObject` and `CompleteMultipartUpload`
requests to the specified bucket must include the `if-match` header to
succeed.

###### Note

This policy also sets the `s3:ObjectCreationOperation` condition
key which allows for multipart uploads using the
`CreateMultipartUpload`, `UploadPart`, and
`UploadPartCopy` APIs.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowPutObject",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:user/Alice"
            },
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket1`/*",
        },
        {
            "Sid": "BlockNonConditionalObjectCreation",
            "Effect": "Deny",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:user/Alice"
            },
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket1`/*",
            "Condition": {
                "Null": {
                    "s3:if-match": "true"
                },
                "Bool": {
                    "s3:ObjectCreationOperation": "true"
                }
            }
        },
        {
            "Sid": "AllowGetObjectBecauseConditionalPutIfMatchETag",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:user/Alice"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket1`/*"
        }
    ]
}
```

## Example 3: Only allow object upload

requests that includes the `if-none-match` or `if-match`
header

This policy allows account 111122223333, user Alice to write to
`amzn-s3-demo-bucket1` if the requests include the `if-none-match` or
`if-match` header. This allows Alice to upload an object if the key
name does not exist in the bucket, or if the key name does exist, Alice can
overwrite the object if the object ETag matches the ETag provided in the
`PUT` request.

###### Note

This policy also sets the `s3:ObjectCreationOperation` condition
key which allows for multipart uploads using the
`CreateMultipartUpload`, `UploadPart`, and
`UploadPartCopy` APIs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": " AllowConditionalPutifAbsent",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/Alice"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket1/*",
 "Condition": {
 "Null": {
 "s3:if-none-match": "false"
 }
 }
 },
 {
 "Sid": "AllowConditionalPutIfMatchEtag",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/Alice"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket1/*",
 "Condition": {
 "Null": {
 "s3:if-match": "false"
 }
 }
 },
 {
 "Sid": "AllowConditionalObjectCreation",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/Alice"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket1/*",
 "Condition": {
 "Bool": {
 "s3:ObjectCreationOperation": "false"
 }
 }
 },
 {
 "Sid": " AllowGetObjectBecauseConditionalPutIfMatchETag",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/Alice"
 },
 "Action": "s3:GetObject",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket1/*"
 }
 ]
}`

```
