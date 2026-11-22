

# Fortinet FortiSASE API Key

**Note**  
FortiSASE creates this secret for you. When you connect your AWS account in the FortiSASE portal, FortiSASE creates the secret in your account and writes its value. Don't create this secret yourself. You can't create a secret of this type in the Secrets Manager console.

## Secret Value Fields
<a name="w2aac29c13c31b5"></a>

The following are the fields that must be contained in the Secrets Manager secret:

```json
{
  "apiKey": "{{FortiSASE API key value}}",
  "apiBaseUrl": "{{FortiSASE API endpoint URL}}"
}
```

apiKey  
The FortiSASE API key. The key starts with `fsagw_`, followed by a 16-character lowercase hexadecimal key ID, an underscore, and 43 base64url characters. Secrets Manager rotates this field.

apiBaseUrl  
The FortiSASE API endpoint for your FortiSASE environment. The URL must use HTTPS and a host that ends in `.fortisase.com`. It must not include user information, a port, a query string, or a fragment. Rotation sends the API key to this endpoint.

FortiSASE writes both fields when it creates the secret and manages their values. Editing either field can break the connection between AWS and FortiSASE or make rotation fail.

## Secret Metadata Fields
<a name="w2aac29c13c31b7"></a>

This secret type requires no rotation metadata fields.

## Usage Flow
<a name="w2aac29c13c31b9"></a>

FortiSASE creates this secret in your account when you connect your AWS account in the FortiSASE portal.

This rotation type self-rotates. The current API key authorizes the request for its replacement, so no separate administrator credential is needed.

The secret is created with the [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) API call, with the secret value set to the fields described above and the secret type set to FortiSASEApiKey. Rotation is configured with the [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) API call, with a role ARN that grants the service permission to rotate the secret. For an example permissions policy, see [Security and Permissions](mes-security.md).

During rotation, Secrets Manager uses the current key to ask FortiSASE for a new key. It stores the new key as AWSPENDING, confirms with FortiSASE that the new key is the tenant's current key, and then promotes AWSPENDING to AWSCURRENT.

FortiSASE keeps the replaced key valid for 24 hours after rotation, so an application that still holds the previous key keeps working until it reads the new one. FortiSASE provides no API to revoke the previous key sooner. To invalidate it before the 24 hours end, rotate the secret again. FortiSASE keeps only one previous key, so the second rotation invalidates the key that the first rotation replaced.

If a rotation is interrupted after FortiSASE issues the new key but before Secrets Manager stores it, Secrets Manager retries the rotation with the previous key. FortiSASE treats a rotation request made with the previous key within its 24 hours as a retry, so the retry completes. If the rotation does not complete within 24 hours, the previous key expires and the secret no longer holds a working key.

Rotate the key only through Secrets Manager. If the key is rotated in FortiSASE directly, the secret still holds the replaced key, which stops working 24 hours later. If you disconnect your AWS account in the FortiSASE portal, FortiSASE invalidates the key and rotation fails.