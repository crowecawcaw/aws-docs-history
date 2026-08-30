# Cisco Security Platform API Key

## Secret Value Fields

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "refreshToken": "`refresh token value`",
  "organizationId": "`organization ID`",
  "apiKeyId": "`API key ID`",
  "apiBaseUrl": "https://api.security.cisco.com"
}
```

refreshToken

The Cisco API key, which is an OAuth refresh token with a 60-day life. The rotation process updates this field. Your application exchanges this token for a short-lived access token.

organizationId

The Cisco Security Cloud Control organization that owns the API key. This value is the `enterpriseId` shown in the URL of the API Keys page. Do not use the organization ID embedded in the token.

apiKeyId

The identifier of the API key that rotates. You can find this value on the same API Keys page as the organization ID.

apiBaseUrl

The Cisco API base URL, for example `https://api.security.cisco.com`. The value must be an HTTPS origin with no path, port, query string, or user information.

Rotation also writes an `expiresDate` field into the secret value. This field records the expiry of the current refresh token in ISO 8601 format. It is not a field that you provide.

Secrets Manager does not store the access token. An access token lives about 18 hours, so a stored copy would be invalid most of the time. Your application mints an access token from the refresh token when it needs one.

## Secret Metadata Fields

This secret type requires no rotation metadata fields. Secrets Manager reads the routing values from the secret itself, and this secret type uses no admin secret.

## Usage Flow

This rotation uses a single-secret architecture. No admin secret is required. The stored refresh token authenticates its own rotation call.

To create your secret, use the [CreateSecret](../apireference/API_CreateSecret.md "../apireference/API_CreateSecret.md") API call. Set the secret value to the fields described above and set the secret type to CiscoSecurityPlatformApiKey. To configure rotation, use the [RotateSecret](../apireference/API_RotateSecret.md "../apireference/API_RotateSecret.md") API call. In the RotateSecret call, provide a role ARN that grants the service permission to rotate the secret. For an example permissions policy, see [Security and Permissions](mes-security.md "mes-security.md").

During rotation, Secrets Manager calls the Cisco token refresh endpoint with the current refresh token. Cisco returns an access token, and after day 45 of the 60-day cycle it also returns a new refresh token. Secrets Manager stores the most recent refresh token as the pending version and discards the access token. It then verifies the pending token against the Cisco API and promotes it to current. There is no revoke step, because Cisco provides no API to invalidate a refresh token.

Your application reads the refresh token from the secret and exchanges it for an access token. It then caches that access token for its 18-hour life. Read the refresh token from the secret each time rather than hardcoding it. Handle an HTTP 401 response by reading the secret again, because the previous refresh token might stop working after Cisco issues a replacement.

Rotate this secret at least every 15 days. Secrets Manager rejects a rotation interval longer than 50 days, which follows Cisco guidance to refresh at least that often. A longer interval can also skip the window between day 45 and day 60 in which Cisco issues the replacement refresh token. If the remaining life of the token is shorter than your rotation interval, rotation fails with an error instead of letting the token expire.

A refresh token that expires cannot be renewed. If that happens, issue a new API key in the Cisco Security Cloud Control console and update the secret. Monitor rotation failures so that a prolonged outage does not reach that state.
