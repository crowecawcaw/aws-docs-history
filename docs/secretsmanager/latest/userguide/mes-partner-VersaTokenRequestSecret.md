

# Versa Networks Token Request Credential
<a name="mes-partner-VersaTokenRequestSecret"></a>

## Secret Value Fields
<a name="w2aac29c13c63b3"></a>

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "host": "{{https://versa.example.com}}",
  "clientId": "{{OAuth client ID}}",
  "clientSecret": "{{OAuth client secret}}",
  "username": "{{user or user@tenant}}",
  "password": "{{current password}}"
}
```

host  
The base URL of the Versa Networks host that issues access tokens, for example `https://versa.example.com` or `https://203.0.113.10:9182`. The host can be a fully qualified domain name or an IP address. The URL must use HTTPS. Add the port if your deployment does not serve on 443, and do not include a path or a trailing slash.  
The host must present a certificate from a trusted certificate authority, issued for the name or IP address that you enter. Secrets Manager rejects a self-signed certificate.

clientId  
The client ID of the OAuth client registered in Versa Networks. Secrets Manager sends it with every token request.

clientSecret  
The OAuth client secret paired with the client ID. Secrets Manager sends it with every token request.

username  
The Versa Networks user that access tokens are requested for. In multi-tenant deployments, qualify the user with its tenant, for example `user@tenant`.

password  
The current password of the user. Secrets Manager rotates this field. If you change the password in Versa Networks yourself, update this field so that the next rotation can sign in.

## Secret Metadata Fields
<a name="w2aac29c13c63b5"></a>

This secret type requires no rotation metadata fields.

## Usage Flow
<a name="w2aac29c13c63b7"></a>

This rotation type self-rotates. Secrets Manager signs in as the stored user and changes the password of that user, so no separate administrator credential is needed. The secret does not store an access token. Do not write an access token or a refresh token into the secret.

To create your secret, use the [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) API call. Set the secret value to the fields described above and set the secret type to VersaTokenRequestSecret. To configure rotation, use the [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) API call. In the RotateSecret call, provide a role ARN that grants the service permission to rotate the secret. For an example permissions policy, see [Security and Permissions](mes-security.md).

During rotation, Secrets Manager generates a new 24-character password and stores it as AWSPENDING. The password excludes the characters that Versa Networks rejects. Secrets Manager requests an access token with the current password and uses it to change the password in Versa Networks. It confirms that the new password can request an access token, and then promotes AWSPENDING to AWSCURRENT.

The password change takes effect immediately, so the previous password stops working before Secrets Manager promotes AWSPENDING. Your application should read the secret each time it requests an access token, and keep the access token in memory for its lifetime. If a token request fails with HTTP 401, re-read the secret and retry.

Your Versa Networks host must be reachable over HTTPS from the Secrets Manager rotation service. Secrets Manager rejects a host that resolves to a loopback, link-local, or private address. If you restrict inbound access, allow the AWS-managed prefix list `com.amazonaws.{{region}}.secretsmanager-managed-external-secrets`. For more information, see [Security and Permissions](mes-security.md).