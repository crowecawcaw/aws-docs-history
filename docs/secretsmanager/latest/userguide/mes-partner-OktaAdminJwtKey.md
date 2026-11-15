

# Okta Administrator JWT Key
<a name="mes-partner-OktaAdminJwtKey"></a>

## Secret Value Fields
<a name="w2aac29c13c41b3"></a>

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "domain": "{{trial-1234567.okta.com}}",
  "clientId": "{{0oa followed by 17 letters or digits}}",
  "privateKey": "{{PEM-encoded RSA private key, including the BEGIN and END markers}}",
  "keyId": "{{key ID of the registered public key}}",
  "scopes": "{{okta.apps.manage okta.apps.read}}"
}
```

domain  
The Okta organization domain of the administrator application, for example `trial-1234567.okta.com`. Do not include a scheme or a trailing slash. The domain must end in `okta.com`, `oktapreview.com`, `okta-emea.com`, `okta-gov.com`, or `okta.mil`.  
Do not enter the Admin Console host, which inserts `-admin` before the domain suffix. This domain must match the domain of every secret that this key rotates, because a credential from one Okta organization cannot manage an application in another.

clientId  
The client ID of the Okta API Services application that performs rotation. Set the client authentication of the application to Public key / Private key, and grant it the `okta.apps.manage` scope. Assign it an administrator role that covers the applications that you want to rotate.

privateKey  
The unencrypted RSA private key, in PEM format, that signs the client assertion of the administrator application. Include the BEGIN and END markers. The markers are optional only for a PKCS\#8 key. Encrypted private keys are not supported.

keyId  
The key ID (`kid`) of the public key that is registered on the administrator application. Okta uses it to select the public key that verifies the signed assertion.

scopes  
(Optional) The space-separated Okta scopes that Secrets Manager requests for the administrator access token. Default: `okta.apps.manage okta.apps.read`. Rotation requires `okta.apps.manage`, so do not remove it.

## Secret Metadata Fields
<a name="w2aac29c13c41b5"></a>

This secret type has no metadata fields, because Secrets Manager does not rotate it.

## Usage Flow
<a name="w2aac29c13c41b7"></a>

This secret type stores the Okta administrator credential that Secrets Manager uses to create and revoke client secrets when it rotates a secret of type OktaOAuthClientSecret. Secrets Manager does not rotate a secret of this type, because Okta does not allow API credential changes on an application that holds an administrator role.

Secrets Manager authenticates as the administrator application with the OAuth 2.0 `private_key_jwt` method. It supports applications that require Demonstrating Proof of Possession (DPoP), which Okta turns on by default for new API Services applications.

To create your secret, use the [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) API call. Set the secret value to the fields described above and set the secret type to OktaAdminJwtKey. Do not configure rotation for this secret. Reference it from a secret of type OktaOAuthClientSecret through the `adminSecretArn` rotation metadata field.

To replace the key pair, generate a new one in the Okta Admin Console. Then update this secret with the new `privateKey` and `keyId`.