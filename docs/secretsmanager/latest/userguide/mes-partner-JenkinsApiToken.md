# Jenkins API Token

## Secret Value Fields

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "apiToken": "`API token value`",
  "tokenUuid": "`token UUID`",
  "username": "`user that owns the token`",
  "jenkinsUrl": "https://jenkins.example.com"
}
```

apiToken

The Jenkins API token value (a 32-34 character hexadecimal string). The rotation process updates this field.

tokenUuid

The universally unique identifier (UUID) of the API token. Rotation uses this UUID to revoke the old token, and updates this field with the new token's UUID after each rotation.

username

The Jenkins user that owns the token.

jenkinsUrl

Your Jenkins instance URL (for example, `https://jenkins.example.com`). The URL must use HTTPS and must not end with a trailing slash.

## Secret Metadata Fields

The following are the metadata fields for Jenkins API Token:

```
{
  "adminSecretArn": "arn:aws:secretsmanager:us-east-1:111122223333:secret:`JenkinsAdmin`"
}
```

adminSecretArn

(Optional) The Amazon Resource Name (ARN) for a secret of type JenkinsApiToken that
contains an admin token. The admin token can generate and revoke API tokens for the target
user. If omitted, the token rotates itself (self-rotation).

## Usage Flow

This rotation supports both single-secret (self-rotation) and two-secret (admin-assisted)
architectures. When you provide `adminSecretArn`, the admin token generates and revokes the
target user's tokens. If you omit it, the current token rotates itself.

To create your secret, use the [CreateSecret](../apireference/API_CreateSecret.md "../apireference/API_CreateSecret.md") API call. Set the secret value to the
fields described above and set the secret type to JenkinsApiToken. To configure rotation, use the
[RotateSecret](../apireference/API_RotateSecret.md "../apireference/API_RotateSecret.md") API call. In the RotateSecret call, provide a role ARN that grants the
service permission to rotate the secret. For an example permissions policy, see [Security and Permissions](mes-security.md "mes-security.md"). When using admin-assisted rotation,
explicitly grant the rotation role access to the admin secret ARN.

During rotation, the driver validates the current token and obtains a Cross-Site Request Forgery
(CSRF) crumb from Jenkins. It then generates a new API token and stores it as the pending
version. It verifies the new token against the Jenkins API, promotes it to current, then
revokes the old token by its `tokenUuid`. Applications using the Secrets Manager caching library pick up
the new token on their next refresh.

Jenkins is customer-hosted, so your Jenkins instance must be reachable
over HTTPS from the Secrets Manager rotation service. Rotation calls originate from the AWS-managed prefix list
`com.amazonaws.`region`.secretsmanager-managed-external-secrets`. Allow
inbound access from this prefix list on your instance's security group or firewall, and ensure the
instance presents a publicly trusted TLS certificate. For more information, see
[AWS-managed prefix lists](../../../vpc/latest/userguide/working-with-aws-managed-prefix-lists.md "../../../vpc/latest/userguide/working-with-aws-managed-prefix-lists.md") in the _Amazon VPC User Guide_.
Instances that are not reachable over the public internet are not supported.
