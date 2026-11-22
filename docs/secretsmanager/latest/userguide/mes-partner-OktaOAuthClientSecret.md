

# Okta OAuth Client Secret

## Secret Value Fields
<a name="w2aac29c13c45b3"></a>

The following are the fields that must be contained in the Secrets Manager secret:

```json
{
  "clientId": "{{0oa followed by 17 letters or digits}}",
  "clientSecret": "{{current client secret}}",
  "domain": "{{trial-1234567.okta.com}}",
  "secretId": "{{ocs followed by 17 letters or digits}}"
}
```

clientId  
The client ID of the Okta application whose secret you want to rotate. Find it in the Okta Admin Console under Applications, on the General tab of the application.  
The application must use client secret authentication. An application that uses Public key / Private key authentication has no client secret to rotate. Okta also refuses credential changes on any application that holds an administrator role.

clientSecret  
The current client secret of the application. Secrets Manager rotates this field. Before it creates a replacement, Secrets Manager confirms that this value still authenticates at Okta.

domain  
The Okta organization domain that hosts the application, for example `trial-1234567.okta.com`. Do not include a scheme or a trailing slash. The domain must end in `okta.com`, `oktapreview.com`, `okta-emea.com`, `okta-gov.com`, or `okta.mil`. Do not enter the Admin Console host, which inserts `-admin` before the domain suffix.

secretId  
(Optional) The Okta identifier of the stored client secret, which begins with `ocs`. Leave this field blank. The first rotation finds the identifier by matching the stored value, and Secrets Manager records it after each rotation.

## Secret Metadata Fields
<a name="w2aac29c13c45b5"></a>

The following are the metadata fields for Okta OAuth Client Secret:

```json
{
  "adminSecretArn": "arn:aws:secretsmanager:us-east-1:111122223333:secret:{{OktaAdminJwtKey}}"
}
```

adminSecretArn  
The Amazon Resource Name (ARN) of a secret of type OktaAdminJwtKey. The administrator secret must use the same Okta domain as this secret.

## Usage Flow
<a name="w2aac29c13c45b7"></a>

This rotation uses a two-secret architecture. A secret of type OktaAdminJwtKey holds the administrator credential that creates and revokes client secrets at Okta.

To create your secret, use the [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) API call. Set the secret value to the fields described above and set the secret type to OktaOAuthClientSecret. To configure rotation, use the [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) API call. You must provide the `adminSecretArn` in the rotation metadata. In the RotateSecret call, provide a role ARN that grants the service permission to rotate the secret. For an example permissions policy, see [Security and Permissions](mes-security.md).

The administrator secret type (`OktaAdminJwtKey`) differs from the user secret type (`OktaOAuthClientSecret`). Because of this difference, the default rotation role policy scoped by `secretsmanager:resource/Type` does not grant access to the administrator secret. You must explicitly provide the rotation role access to the administrator secret. You can do this by adding a statement scoped to the administrator secret type. Alternatively, specify the administrator secret `ARN` directly in the role policy.

During rotation, Secrets Manager confirms that the current client secret authenticates. It creates a second client secret for the application and stores it as AWSPENDING. It confirms that the new secret authenticates through the Okta token introspection endpoint. It then deactivates the previous client secret, attempts to delete it, and promotes AWSPENDING to AWSCURRENT.

Both client secrets authenticate from the moment Secrets Manager creates the replacement until it deactivates the previous secret. An application that reads the secret during that window is not interrupted. Secrets Manager deactivates the previous secret just before it promotes AWSPENDING, so applications should re-read AWSCURRENT and retry after an authentication failure.

Okta allows at most two client secrets per application. If the application already holds two, rotation has no free slot. Secrets Manager then removes a secret only when its value matches AWSPREVIOUS, which proves that rotation created it. Otherwise rotation fails until you deactivate and delete the secret that you no longer need in the Okta Admin Console.