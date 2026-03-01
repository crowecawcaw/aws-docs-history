# Authorizing Zonal endpoint API operations with `CreateSession`

To use Zonal endpoint API operations (object-level, or data plane operations), except for
`CopyObject` and `HeadBucket`, you use the
`CreateSession` API operation to create and manage sessions that are
optimized for low-latency authorization of data requests. To retrieve and use a session
token, you must allow the `s3express:CreateSession` action for your directory
bucket in an identity-based policy or a bucket policy. For more information, see [Authorizing Regional endpoint API operations with IAM](s3-express-security-iam.md "s3-express-security-iam.md"). If you're
accessing S3 Express One Zone in the Amazon S3 console, through the AWS Command Line Interface (AWS CLI), or by using the
AWS SDKs, S3 Express One Zone creates a session on your behalf. However, you can't modify the
`SessionMode` parameter when using the AWS CLI or AWS SDKs.

If you use the Amazon S3 REST API, you can then use the `CreateSession` API
operation to obtain temporary security credentials that include an access key ID, a secret
access key, a session token, and an expiration time. The temporary credentials provide the
same permissions as long-term security credentials, such as IAM user credentials, but
temporary security credentials must include a session token.

###### Session Mode

Session mode defines the scope of the session. If the session mode is not specified in the CreateSession API request,
the CreateSession action will attempt to create the session with the maximum allowable privilege, attempting `ReadWrite`
first, then falling back to `ReadOnly` only if `ReadWrite` is not permitted by the policies. In your bucket
policy, you can specify the `s3express:SessionMode` condition key to explicitly control who can create a
`ReadWrite` or `ReadOnly` session. For more information about
`ReadWrite` or `ReadOnly` sessions, see the
`x-amz-create-session-mode` parameter for [CreateSession](../API/API_CreateSession.md "../API/API_CreateSession.md") in the _Amazon S3 API
Reference_. For more information about the bucket policy to create, see
[Example bucket policies for directory buckets](s3-express-security-iam-example-bucket-policies.md "s3-express-security-iam-example-bucket-policies.md").

###### Session Token

When you make a call by using temporary security credentials, the call must include a
session token. The session token is returned along with the temporary credentials. A
session token is scoped to your directory bucket and is used to verify that the security
credentials are valid and haven't expired. To protect your sessions, temporary security
credentials expire after 5 minutes.

###### `CopyObject` and `HeadBucket`

Temporary security credentials are scoped to a specific directory bucket and are
automatically enabled for all Zonal (object-level) operation API calls to a given
directory bucket. Unlike other Zonal endpoint API operations, `CopyObject`
and `HeadBucket` don't use `CreateSession` authentication. All
`CopyObject` and `HeadBucket` requests must be authenticated
and signed by using IAM credentials. However, `CopyObject` and
`HeadBucket` are still authorized by
`s3express:CreateSession`, like other Zonal endpoint API operations.

For more information, see [CreateSession](../API/API_CreateSession.md "../API/API_CreateSession.md") in
the _Amazon Simple Storage Service API Reference_.
