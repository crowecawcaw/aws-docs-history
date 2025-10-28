# How MediaTailor Secrets Manager

access token authentication works

After you create or update a source location to use access token
authentication, MediaTailor includes the access token in an HTTP header when
requesting source content manifests from your origin.

Here's an overview of how MediaTailor uses Secrets Manager access token authentication for
source location origin authentication:

1. When you create or update a MediaTailor source location that uses access
   token authentication, MediaTailor sends a [DescribeSecret](../../../secretsmanager/latest/apireference/API_DescribeSecret.md#SecretsManager-DescribeSecret-request-SecretId "../../../secretsmanager/latest/apireference/API_DescribeSecret.md#SecretsManager-DescribeSecret-request-SecretId") request to Secrets Manager to determine the AWS KMS key
   associated with the secret. You include the secret ARN in your source
   location access configuration.
2. MediaTailor creates a [grant](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") for the customer managed key, so that MediaTailor can use the key to
   access and decrypt the access token stored in the SecretString. The
   grant name will be `MediaTailor-SourceLocation-`your
   AWS account ID`-`source location
   name``.

You can revoke access to the grant, or remove MediaTailor's access to the
customer managed key at any time. For more information, see [RevokeGrant](../../../kms/latest/APIReference/API_RevokeGrant.md "../../../kms/latest/APIReference/API_RevokeGrant.md") in the _AWS Key Management Service API Reference_. 3. When a VOD source is created or updated, or used in a program, MediaTailor
makes HTTP requests to the source locations to retrieve the source
content manifests associated with the VOD sources in the source
location. If the VOD source is associated with a source location that
has an access token configured, the requests include the access token as
an HTTP header value.
