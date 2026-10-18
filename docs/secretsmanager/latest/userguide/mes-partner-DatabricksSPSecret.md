

# Databricks Service Principal OAuth Client Secret
<a name="mes-partner-DatabricksSPSecret"></a>

## Secret Value Fields
<a name="w2aac27c13c21b3"></a>

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "accountId": "{{Databricks account UUID}}",
  "servicePrincipalId": "{{Numeric service principal ID}}",
  "clientId": "{{Service principal application UUID}}",
  "clientSecret": "{{dose followed by the secret value}}",
  "oauthSecretId": "{{Hexadecimal OAuth secret ID}}"
}
```

accountId  
Your Databricks account ID, which is a UUID.

servicePrincipalId  
The numeric internal ID of the service principal. This value differs from the application ID.

clientId  
The application ID of the service principal. Secrets Manager sends it as `client_id` in OAuth requests.

clientSecret  
The current OAuth client secret. Secrets Manager rotates this field.

oauthSecretId  
The Databricks ID of the current OAuth secret. Secrets Manager uses it to read the scopes of the current secret and to delete the secret that it replaces.

## Secret Metadata Fields
<a name="w2aac27c13c21b5"></a>

The following are the metadata fields for Databricks Service Principal OAuth Client Secret:

```
{
  "adminSecretArn": "arn:aws:secretsmanager:us-east-1:111122223333:secret:{{DatabricksAdminServicePrincipal}}",
  "secretLifetimeDays": "{{730}}"
}
```

adminSecretArn  
(Optional) The Amazon Resource Name (ARN) of another secret of type DatabricksSPSecret that rotates this secret. Omit this field to let the service principal rotate its own secret.

secretLifetimeDays  
(Optional) The lifetime of each new secret, in days. The value must be greater than your rotation interval. The maximum is 730. Default: 730.

## Usage Flow
<a name="w2aac27c13c21b7"></a>

This rotation type supports two modes. In self-rotation, the service principal rotates its own secret. In assisted rotation, a second service principal rotates it. The service principal that performs the rotation needs the `account_admin` role, because the OAuth secret endpoints are account-level.

You can create your secret using the [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) call with the secret value containing the fields mentioned above and secret type as DatabricksSPSecret. The rotation configurations can be set using a [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) call. If you opt for self-rotation, you can omit the optional `adminSecretArn` field. You must provide a role ARN in the [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) call which grants the service the required permissions to rotate the secret. For an example of a permissions policy, see [Security and Permissions](mes-security.md).

During rotation, Secrets Manager requests an access token using the client credentials flow. It creates a replacement secret that carries the scopes of the secret it replaces and stores the replacement as AWSPENDING. It confirms that the new secret authenticates. It then deletes the previous secret and promotes AWSPENDING to AWSCURRENT.

A service principal supports at most five OAuth secrets. If the service principal already holds five, Databricks rejects the request and rotation fails. Delete an unused secret before you rotate again.

The `account_admin` role that this type needs differs from the workspace access that Databricks Personal Access Token rotation needs. A single grant does not cover both flows.