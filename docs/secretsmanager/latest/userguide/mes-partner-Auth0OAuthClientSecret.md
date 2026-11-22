

# Auth0 OAuth Client Secret

## Secret Value Fields
<a name="w2aac29c13c13b3"></a>

The following are the fields that must be contained in the Secrets Manager secret:

```json
{
  "clientId": "{{20 to 64 letters or digits}}",
  "clientSecret": "{{current client secret}}",
  "domain": "{{dev-abc123.us.auth0.com}}",
  "audience": "{{https://dev-abc123.us.auth0.com/api/v2/}}"
}
```

clientId  
The client ID of the Auth0 application whose secret you want to rotate. Find it in the Auth0 Dashboard under Applications, on the Settings tab of the application.  
The application must authenticate with a client secret (`client_secret_post` or `client_secret_basic`). It must also have the Client Credentials grant enabled. Secrets Manager checks both before it changes anything.

clientSecret  
The current client secret of the application. Secrets Manager rotates this field. Before it generates a replacement, Secrets Manager confirms that this value still authenticates at Auth0. If someone changed the secret outside of rotation, rotation stops with an error instead of overwriting it.

domain  
The Auth0 tenant domain in lowercase, for example `dev-abc123.us.auth0.com`. Do not include a scheme or a trailing slash.  
Auth0 custom domains are not supported. If your tenant uses a custom domain, enter the tenant domain, which continues to work alongside the custom domain.

audience  
The API identifier of the API that the application calls, as shown in the Auth0 Dashboard under APIs. Secrets Manager requests a token for this audience to verify the new client secret. The value must begin with `https://`, and the application must already hold a client grant for it.  
For self-rotation, this value must be the Management API of the tenant, `https://{{your-domain}}/api/v2/`. Secrets Manager rejects any other value before rotation begins. A missing trailing slash is accepted.

## Secret Metadata Fields
<a name="w2aac29c13c13b5"></a>

The following are the metadata fields for Auth0 OAuth Client Secret:

```json
{
  "adminSecretArn": "arn:aws:secretsmanager:us-east-1:111122223333:secret:{{Auth0AdminApplication}}"
}
```

adminSecretArn  
(Optional) The Amazon Resource Name (ARN) of another secret of type Auth0OAuthClientSecret that holds the administrator application. Omit this field to let the application rotate its own secret.

## Usage Flow
<a name="w2aac29c13c13b7"></a>

This rotation type supports two modes. The modes differ in which Auth0 application changes the client secret:
+ **Admin-assisted rotation** – A separate administrator application changes the client secret. The rotated application needs no Management API access. To use this mode, set `adminSecretArn` in the rotation metadata.
+ **Self-rotation** – The application uses its own client secret to change that client secret. To use this mode, omit `adminSecretArn` from the rotation metadata.

Auth0 holds one client secret per application, so in both modes Secrets Manager replaces the secret in place.

To create your secret, use the [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) API call. Set the secret value to the fields described above and set the secret type to Auth0OAuthClientSecret. To configure rotation, use the [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) API call. In the RotateSecret call, provide a role ARN that grants the service permission to rotate the secret. For an example permissions policy, see [Security and Permissions](mes-security.md).

### Admin-assisted rotation
<a name="w2aac29c13c13b7c11"></a>

Create the administrator secret as another secret of type Auth0OAuthClientSecret. Use the Client ID and Client secret of a machine-to-machine application in the same tenant. Set its `domain` to the same value as the secret that it rotates, and set its `audience` to the Management API of the tenant. Grant that application the `read:clients` and `update:client_keys` permissions on the Auth0 Management API. Do not use `update:clients` for this purpose, because it does not permit changing a client secret.

The administrator secret has the same type as the secret that it rotates, so a rotation role policy scoped by `secretsmanager:resource/Type` covers both secrets. You can also configure rotation on the administrator secret and omit its own `adminSecretArn`. The administrator secret then rotates itself, so no credential in the chain goes unrotated.

### Self-rotation
<a name="w2aac29c13c13b7c13"></a>

The application itself must hold `read:clients` and `update:client_keys` on the Management API, and its `audience` must be the Management API of the tenant. These permissions apply to the whole tenant, so the application can rotate the client secret of every application in the tenant. Use self-rotation for the administrator application, not for ordinary applications.

Before it promotes AWSPENDING, Secrets Manager also confirms that the new secret still holds `read:clients` and `update:client_keys`. This check prevents a rotation from promoting a secret that cannot perform the next rotation.

### Rotation steps
<a name="w2aac29c13c13b7c15"></a>

In both modes, Secrets Manager confirms that the current client secret authenticates and that the application can be rotated. It generates a new 64-character client secret and stores it as AWSPENDING. It then updates the client secret in Auth0, which invalidates the previous secret immediately. Secrets Manager requests a token with the new secret, retrying for about 45 seconds to allow for Auth0 propagation. It then promotes AWSPENDING to AWSCURRENT.

The update that installs the new secret also invalidates the previous one, so this type has no overlap window in which both secrets authenticate. Until Secrets Manager promotes AWSPENDING, AWSCURRENT names a secret that no longer works. Applications that cache the client secret should re-read AWSCURRENT and retry after an authentication failure.