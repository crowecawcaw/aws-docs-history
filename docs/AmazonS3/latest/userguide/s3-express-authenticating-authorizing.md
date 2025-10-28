# Authenticating and authorizing requests

By default, directory buckets are private and can be accessed only by users who are
explicitly granted access. The access control boundary for directory buckets is set only
at the bucket level. In contrast, the access control boundary for general purpose buckets can be
set at the bucket, prefix, or object tag level. This difference means that
directory buckets are the only resource that you can include in bucket policies or IAM
identity policies for S3 Express One Zone access.

Amazon S3 Express One Zone supports both AWS Identity and Access Management (AWS IAM) authorization and session-based
authorization:

- To use Regional endpoint API operations (bucket-level, or control plane,
  operations) with S3 Express One Zone, you use the IAM authorization model, which doesn't
  involve session management. Permissions are granted for actions individually. For
  more information, see [Authorizing Regional endpoint API operations with IAM](s3-express-security-iam.md "s3-express-security-iam.md").
- To use Zonal endpoint API operations (object-level, or data plane, operations), except for
  `CopyObject` and `HeadBucket`,
  you use the `CreateSession` API operation to create and manage sessions
  that are optimized for low-latency authorization of data requests. To retrieve and
  use a session token, you must allow the `s3express:CreateSession` action
  for your directory bucket in an identity-based policy or a bucket policy. For more
  information, see [Authorizing Regional endpoint API operations with IAM](s3-express-security-iam.md "s3-express-security-iam.md"). If you're accessing S3 Express One Zone in
  the Amazon S3 console, through the AWS Command Line Interface (AWS CLI), or by using the AWS SDKs,
  S3 Express One Zone creates a session on your behalf.
  With the
  `CreateSession` API operation, you authenticate and authorize
  requests through a new session-based mechanism. You can use `CreateSession` to
  request temporary credentials that provide low-latency access to your bucket. These
  temporary credentials are scoped to a specific directory bucket.

To work with `CreateSession`, we recommend using the latest version of the
AWS SDKs or using the AWS Command Line Interface (AWS CLI). The supported AWS SDKs and the AWS CLI handle
session establishment, refreshment, and termination on your behalf.

You use session tokens with only Zonal (object-level) operations (except for
`CopyObject` and `HeadBucket`) to distribute the latency that’s
associated with authorization over a number of requests in a session. For Regional endpoint
API operations (bucket-level operations), you use IAM authorization, which doesn’t involve
managing a session. For more information, see [Authorizing Regional endpoint API operations with IAM](s3-express-security-iam.md "s3-express-security-iam.md") and [Authorizing Zonal endpoint API operations with
CreateSession](s3-express-create-session.md "s3-express-create-session.md").

## How API operations are authenticated and authorized

The following table lists authentication and authorization information for directory bucket
API operations. For each API operation, the table shows the API operation name, IAM
policy action, endpoint type (Regional or Zonal), and authorization mechanism (IAM or
session-based). This table also indicates whether cross-account access is supported.
Access to bucket-level actions can be granted only in IAM identity-based policies
(user or role), not bucket policies.

| API                                   | Endpoint type | IAM action                                      | Cross-account access |
| ------------------------------------- | ------------- | ----------------------------------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CreateBucket`                        | Regional      | `s3express:CreateBucket`                        | No                   |
| `DeleteBucket`                        | Regional      | `s3express:DeleteBucket`                        | No                   |
| `ListDirectoryBuckets`                | Regional      | `s3express:ListAllMyDirectoryBuckets`           | No                   |
| `PutBucketPolicy`                     | Regional      | `s3express:PutBucketPolicy`                     | No                   |
| `GetBucketPolicy`                     | Regional      | `s3express:GetBucketPolicy`                     | No                   |
| `DeleteBucketPolicy`                  | Regional      | `s3express:DeleteBucketPolicy`                  | No                   |
| `CreateSession`                       | Zonal         | `s3express:CreateSession`                       | Yes                  |
| `CopyObject`                          | Zonal         | `s3express:CreateSession`                       | Yes                  |
| `DeleteObject`                        | Zonal         | `s3express:CreateSession`                       | Yes                  |
| `DeleteObjects`                       | Zonal         | `s3express:CreateSession`                       | Yes                  |
| `HeadObject`                          | Zonal         | `s3express:CreateSession`                       | Yes                  |
| `PutObject`                           | Zonal         | `s3express:CreateSession`                       | Yes                  |
| `RenameObject`                        | Zonal         | `s3express:CreateSession`                       | No                   |
| `GetObjectAttributes`                 | Zonal         | `s3express:CreateSession`                       | Yes                  |
| `ListObjectsV2`                       | Zonal         | `s3express:CreateSession`                       | Yes                  |
| `HeadBucket`                          | Zonal         | `s3express:CreateSession`                       | Yes                  |
| `CreateMultipartUpload`               | Zonal         | `s3express:CreateSession`                       | Yes                  |
| `UploadPart`                          | Zonal         | `s3express:CreateSession`                       | Yes                  |
| `UploadPartCopy`                      | Zonal         | `s3express:CreateSession`                       | Yes                  |
| `CompleteMultipartUpload`             | Zonal         | `s3express:CreateSession`                       | Yes                  |
| `AbortMultipartUpload`                | Zonal         | `s3express:CreateSession`                       | Yes                  |
| `ListParts`                           | Zonal         | `s3express:CreateSession`                       | Yes                  |
| `ListMultipartUploads`                | Zonal         | `s3express:CreateSession`                       | Yes                  |
| `ListAccessPointsForDirectoryBuckets` | Zonal         | `s3express:ListAccessPointsForDirectoryBuckets` | Yes                  |
| `GetAccessPointScope`                 | Zonal         | `s3express:GetAccessPointScope`                 | Yes                  |
| `PutAccessPointScope`                 | Zonal         | `s3express:PutAccessPointScope`                 | Yes                  |
| `DeleteAccessPointScope`              | Zonal         | `s3express:DeleteAccessPointScope`              | Yes                  | ###### Topics <br>• [Authorizing Regional endpoint API operations with IAM](s3-express-security-iam.md "s3-express-security-iam.md") <br>• [Authorizing Zonal endpoint API operations with CreateSession](s3-express-create-session.md "s3-express-create-session.md") |
