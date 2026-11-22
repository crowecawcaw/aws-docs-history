

# Palo Alto Networks API Key

## Secret Value Fields
<a name="w2aac29c13c49b3"></a>

The following are the fields that must be contained in the Secrets Manager secret:

```json
{
  "apiKey": "{{API key value}}",
  "tenantId": "{{tenant ID}}",
  "tenantUri": "{{https://api-mytenant.example.com}}"
}
```

apiKey  
The API key generated for your Palo Alto Networks tenant. Secrets Manager rotates this field.

tenantId  
The identifier of the Palo Alto Networks tenant that issued the API key. Find it in the tenant console alongside the API key.

tenantUri  
The base URI that API requests for the tenant are sent to, for example `https://api-mytenant.example.com` or `https://api.example.com/tenant/v1`. The URI must use HTTPS and must not end with a trailing slash. Add the port if your tenant does not serve on 443, and include any path segments that the tenant requires.

## Secret Metadata Fields
<a name="w2aac29c13c49b5"></a>

This secret type requires no rotation metadata fields.

## Usage Flow
<a name="w2aac29c13c49b7"></a>

This rotation type self-rotates. The current API key authorizes the request for its replacement, so no separate administrator credential is needed.

To create your secret, use the [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) API call. Set the secret value to the fields described above and set the secret type to PaloAltoApiKey. To configure rotation, use the [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) API call. In the RotateSecret call, provide a role ARN that grants the service permission to rotate the secret. For an example permissions policy, see [Security and Permissions](mes-security.md).

During rotation, Secrets Manager authenticates with the current key and asks Palo Alto Networks to generate a new key. It stores the new key as AWSPENDING, together with a `rotatedAt` timestamp. It confirms that the new key is valid, and then promotes AWSPENDING to AWSCURRENT.

Palo Alto Networks invalidates the previous key as soon as it generates the new one, so this type has no overlap window. Until Secrets Manager promotes AWSPENDING, AWSCURRENT names a key that no longer works. Applications that cache the key should re-read AWSCURRENT and retry after an HTTP 401 response.

If a rotation is interrupted after Palo Alto Networks generates the new key but before Secrets Manager stores it, the previous key no longer works and the new key is lost. In that case, generate a new key in the Palo Alto Networks console and update the secret.