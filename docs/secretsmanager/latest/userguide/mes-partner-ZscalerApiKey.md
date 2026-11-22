

# Zscaler API Key

**Note**  
Zscaler creates this secret for you. When you connect your AWS account to Zscaler, Zscaler creates the secret in your account and writes its value. Don't create this secret yourself. You can't create a secret of this type in the Secrets Manager console.

## Secret Value Fields
<a name="w2aac29c13c67b5"></a>

The following are the fields that must be contained in the Secrets Manager secret:

```json
{
  "anchorKey": "{{header}}.{{payload}}.{{signature}}",
  "apiBaseUrl": "https://awsanchorapi.prod.zpath.net",
  "kid": "{{signing key ID}}",
  "issuedAt": "{{2026-11-06T22:20:17Z}}"
}
```

anchorKey  
The anchor key that AWS presents to Zscaler, a signed JSON Web Token that Zscaler issues, made of three base64url parts separated by dots. Secrets Manager rotates this field. Each key expires 12 hours after Zscaler issues it.

apiBaseUrl  
The Zscaler anchor API endpoint that rotation sends the anchor key to, `https://awsanchorapi.prod.zpath.net`. The URL must use HTTPS and a host that ends in `.zpath.net`, and must not include a path.

kid  
(Optional) The ID of the Zscaler signing key that signed the anchor key. Secrets Manager sets this field from each new key.

issuedAt  
(Optional) The time that Zscaler issued the anchor key, as an RFC 3339 timestamp in UTC. Secrets Manager updates this field on each rotation.

Zscaler writes these fields when it creates the secret and manages their values. Editing them can break the connection between AWS and Zscaler or make rotation fail.

## Secret Metadata Fields
<a name="w2aac29c13c67b7"></a>

This secret type requires no rotation metadata fields.

## Usage Flow
<a name="w2aac29c13c67b9"></a>

Zscaler creates this secret in your account when you connect your AWS account to Zscaler.

This rotation type self-rotates. The current anchor key authorizes the request for its replacement, so no separate administrator credential is needed.

The secret is created with the [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) API call, with the secret value set to the fields described above and the secret type set to ZscalerApiKey. Rotation is configured with the [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) API call, with a role ARN that grants the service permission to rotate the secret. For an example permissions policy, see [Security and Permissions](mes-security.md).

Because each anchor key expires 12 hours after it's issued, keep the rotation schedule well under 12 hours, such as `rate(4 hours)`. With that schedule, Secrets Manager can retry a failed rotation before the current key expires. If you lengthen the schedule, the key can expire before the next rotation.

During rotation, Secrets Manager authenticates with the current key and asks Zscaler to issue a new key. It stores the new key as AWSPENDING, together with the new `kid` and `issuedAt` values. It confirms that the new key is valid with a read-only call to Zscaler, asks Zscaler to make the new key active, and then promotes AWSPENDING to AWSCURRENT. Until the new key is active, the current key keeps working, so a rotation that fails earlier leaves your connection unchanged.

Zscaler keeps accepting the previous key for 60 minutes after the new key becomes active, and then rejects it. Zscaler has no call to revoke a key early. A second rotation makes the key from two rotations ago stop working at once. Applications that cache the key should re-read AWSCURRENT within 60 minutes of a rotation, and re-read it and retry after an HTTP 401 response.

If Zscaler rejects the stored key, for example because the key expired before it was rotated, rotation fails until the secret holds a working key. To recover, ask Zscaler to issue a new anchor key.