# Netskope API Token

## Secret Value Fields

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "apiToken": "`API token value`",
  "tenantUrl": "https://example.goskope.com",
  "serviceAccountName": "`service account name`"
}
```

apiToken

The Netskope REST API bearer token for the service account. The rotation process updates this field.

tenantUrl

Your Netskope tenant URL, for example `https://example.goskope.com`. The URL must use HTTPS, must end in `goskope.com`, and must not end with a trailing slash. A regional host such as `https://example.eu.goskope.com` is also valid.

serviceAccountName

The name of the Netskope service account that owns the token. Secrets Manager records this name for logging and audit.

Rotation also writes `createdDate` and `expiresDate` into the secret value. These fields record the issue time and expiry of the current token in ISO 8601 format. They are not fields that you provide.

The service account role is not stored in the secret. The role belongs to the service account rather than to the token, so rotation never changes it.

## Secret Metadata Fields

This secret type requires no rotation metadata fields. It uses no admin secret, and Secrets Manager sets the token lifetime to 365 days.

## Usage Flow

This rotation uses a single-secret architecture. No admin secret is required. The service account uses its current token to generate its own replacement.

To create your secret, use the [CreateSecret](../apireference/API_CreateSecret.md "../apireference/API_CreateSecret.md") API call. Set the secret value to the fields described above and set the secret type to NetskopeApiToken. To configure rotation, use the [RotateSecret](../apireference/API_RotateSecret.md "../apireference/API_RotateSecret.md") API call. In the RotateSecret call, provide a role ARN that grants the service permission to rotate the secret. For an example permissions policy, see [Security and Permissions](mes-security.md "mes-security.md").

During rotation, Secrets Manager calls the Netskope service account endpoint with the current token to generate a replacement. It stores the new token as the pending version, verifies it against the Netskope API, then promotes it to current. Secrets Manager rejects a rotation interval longer than 350 days, which keeps every interval inside the 365-day token lifetime.

Netskope invalidates the old token as soon as it generates the new one, so the two tokens never overlap. For roughly 30 seconds during rotation, the current version of the secret holds a token that no longer works. Your application must handle an HTTP 401 response by reading the secret again and retrying. An application that caches the token without this pattern fails during every rotation.

If the service account role uses an IP allowlist, add the AWS-managed prefix list `com.amazonaws.`region`.secretsmanager-managed-external-secrets` to that allowlist. Rotation calls originate from this prefix list, and Netskope returns HTTP 403 if the allowlist excludes them. For more information, see [AWS-managed prefix lists](../../../vpc/latest/userguide/working-with-aws-managed-prefix-lists.md "../../../vpc/latest/userguide/working-with-aws-managed-prefix-lists.md") in the _Amazon VPC User Guide_.
