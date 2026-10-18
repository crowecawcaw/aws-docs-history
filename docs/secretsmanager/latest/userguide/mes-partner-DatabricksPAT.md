

# Databricks Personal Access Token
<a name="mes-partner-DatabricksPAT"></a>

## Secret Value Fields
<a name="w2aac27c13c19b3"></a>

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "token": "{{dapi followed by 32 hexadecimal characters}}",
  "tokenId": "{{64-character hexadecimal token ID}}",
  "workspaceUrl": "{{https://dbc-xxxxxxxx-xxxx.cloud.databricks.com}}",
  "comment": "{{Comment shown in the token list}}"
}
```

token  
The Databricks personal access token. Secrets Manager rotates this field.

tokenId  
The token ID. Secrets Manager uses it to read the scopes of the current token and to revoke the token that it replaces.

workspaceUrl  
Your Databricks workspace URL, for example `https://dbc-xxxxxxxx-xxxx.cloud.databricks.com`. Provide a bare HTTPS origin. Secrets Manager rejects a URL that contains user information, a port, a path, a query string, a fragment, or a trailing slash.

comment  
(Optional) The comment shown beside the token in the Databricks token list. The maximum length is 255 characters.

## Secret Metadata Fields
<a name="w2aac27c13c19b5"></a>

The following are the metadata fields for Databricks Personal Access Token:

```
{
  "adminSecretArn": "arn:aws:secretsmanager:us-east-1:111122223333:secret:{{DatabricksRotatorToken}}",
  "tokenLifetimeDays": "{{90}}"
}
```

adminSecretArn  
(Optional) The Amazon Resource Name (ARN) of another secret of type DatabricksPAT that rotates this secret. Omit this field to let the token rotate itself.

tokenLifetimeDays  
(Optional) The lifetime of each new token, in days. The value must be greater than your rotation interval. Default: 90.  
A workspace administrator can set a maximum token lifetime that is lower than the value you choose here. If the workspace maximum is lower, token creation fails and rotation cannot complete. Check the workspace setting before you choose a value.

## Usage Flow
<a name="w2aac27c13c19b7"></a>

This rotation type supports two modes. In self-rotation, the token rotates itself. In assisted rotation, a second token of the same type rotates it. In both cases the replacement token inherits the scopes of the token it replaces. Rotation fails instead of creating a token with different privileges when Secrets Manager cannot read those scopes.

You can create your secret using the [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) call with the secret value containing the fields mentioned above and secret type as DatabricksPAT. The rotation configurations can be set using a [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) call. If you opt for self-rotation, you can omit the optional `adminSecretArn` field. You must provide a role ARN in the [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) call which grants the service the required permissions to rotate the secret. For an example of a permissions policy, see [Security and Permissions](mes-security.md).

During rotation, Secrets Manager validates the current token and reads its scopes. It creates a replacement token that carries the same scopes and stores the replacement as AWSPENDING. It confirms that the new token authenticates. It also confirms that the scopes, the owner, and the `workspaceUrl` of the new token match the token it replaces. It then revokes the previous token and promotes AWSPENDING to AWSCURRENT.

Both tokens authenticate from the moment Secrets Manager creates the replacement until it revokes the previous token. An application that reads the secret during that window is not interrupted. Revocation itself is eventually consistent, because Databricks caches authorization decisions. The previous token might continue to be accepted for a short period after Secrets Manager revokes it. When you rotate in response to a suspected credential compromise, confirm through Databricks that the token is no longer accepted.

Databricks revokes a personal access token that goes unused for 90 days. Rotation uses a rotator token only when it runs, so set a rotation interval shorter than 90 days. Otherwise Databricks revokes the rotator token for inactivity and later rotations fail. A rotation interval of 30 days with the default lifetime of 90 days satisfies both requirements.

Secrets Manager rejects a `workspaceUrl` that resolves to a loopback, link-local, or private address. A workspace that you reach only over front-end AWS PrivateLink, with public access disabled, is therefore not supported for personal access token rotation.