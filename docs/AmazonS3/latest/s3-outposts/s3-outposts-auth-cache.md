# Authorization and authentication caching

S3 on Outposts securely caches authentication and authorization data locally on Outposts
racks. The cache removes round trips to the parent AWS Region for every request. This
eliminates the variability that is introduced by network round trips. With the
authentication and authorization cache in S3 on Outposts, you get consistent latencies that
are independent from the latency of the connection between the Outposts and the
AWS Region.

When you make an S3 on Outposts API request, the authentication and authorization data is
securely cached. The cached data is then used to authenticate subsequent S3 object API
requests. S3 on Outposts only caches authentication and authorization data when the request
is signed using Signature Version 4A (SigV4A). The cache is stored locally on the Outposts
within the S3 on Outposts service. It asynchronously refreshes when you make an S3 API
request. The cache is encrypted, and no plaintext cryptographic keys are stored on Outposts.

The cache is valid for up to 10 minutes when the Outpost is connected to the AWS Region.
It is refreshed asynchronously when you make an S3 on Outposts API request, to ensure that
the latest policies are used. If the Outpost is disconnected from the AWS Region, the
cache will be valid for up to 12 hours.

## Configuring the authorization and authentication

cache

S3 on Outposts automatically caches authentication and authorization data for requests
signed with the SigV4A algorithm. For more information, see [Signing AWS API
requests](../../../IAM/latest/UserGuide/reference_aws-signing.md "../../../IAM/latest/UserGuide/reference_aws-signing.md") in the _AWS Identity and Access Management User Guide_. The SigV4A
algorithm is available in the latest versions of the AWS SDKs. You can obtain it
through a dependency on the [AWS Common Runtime (CRT)
libraries](../../../sdkref/latest/guide/common-runtime.md "../../../sdkref/latest/guide/common-runtime.md").

You need to use the latest version of the AWS SDK and install the latest version of
the CRT. For example, you can run `pip install awscrt` to obtain the latest
version of the CRT with Boto3.

S3 on Outposts does not cache authentication and authorization data for requests
signed with the SigV4 algorithm.

## Validating SigV4A signing

You can use AWS CloudTrail to validate that requests were signed with SigV4A. For more
information on setting up CloudTrail for S3 on Outposts, see [Monitoring S3 on Outposts with AWS CloudTrail
logs](S3OutpostsCloudtrail.md "S3OutpostsCloudtrail.md").

After you have configured CloudTrail, you can verify how a request was signed in the
`SignatureVersion` field of the CloudTrail logs. Requests that were signed with
SigV4A will have a `SignatureVersion` set to
`AWS4-ECDSA-P256-SHA256`. Requests that were signed with SigV4 will
have `SignatureVersion` set to `AWS4-HMAC-SHA256`.
