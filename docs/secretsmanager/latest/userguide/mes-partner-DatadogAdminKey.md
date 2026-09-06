

# Datadog Admin Key
<a name="mes-partner-DatadogAdminKey"></a>

## Secret Value Fields
<a name="w2aac27c11c19b3"></a>

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "adminApiKey": "{{32-character hex API key}}",
  "adminApiKeyId": "{{API key UUID}}",
  "adminAppKey": "{{Application key starting with ddapp_}}",
  "adminAppKeyId": "{{Application key UUID}}",
  "serviceAccountId": "{{Service Account UUID}}",
  "site": "{{datadoghq.com}}"
}
```

adminApiKey  
The Datadog admin API key (32-character hexadecimal string).

adminApiKeyId  
The unique identifier (UUID) for the admin API key.

adminAppKey  
The Datadog admin Application key. Must be owned by a service account and have scopes: `api_keys_write`, `api_keys_delete`, `org_app_keys_read`, `org_app_keys_write`, `service_account_write`.

adminAppKeyId  
The unique identifier (UUID) for the admin Application key.

serviceAccountId  
The Datadog Service Account ID (UUID) that owns the admin Application key.

site  
Your Datadog site (for example, `datadoghq.com`, `datadoghq.eu`, `us5.datadoghq.com`).

## Secret Metadata Fields
<a name="w2aac27c11c19b5"></a>

The following are the metadata fields for Datadog Admin Key:

```
{
  "adminSecretArn": "arn:aws:secretsmanager:us-east-1:111122223333:secret:{{DatadogAdminKey}}"
}
```

adminSecretArn  
(Optional) The Amazon Resource Name (ARN) for a separate admin secret used for authentication. If not provided, this secret rotates itself using its own credentials (self-rotation).

## Usage Flow
<a name="w2aac27c11c19b7"></a>

This rotation type rotates both the API key and Application key together as a pair. It supports self-rotation (default) where the secret uses its own credentials to create replacements, or admin-assisted rotation using a separate admin secret.

You can create your secret using the [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) call with the secret value containing the fields mentioned above and secret type as DatadogAdminKey. The rotation configurations can be set using a [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) call. If you opt for self-rotation, you can omit the optional `adminSecretArn` field. You must provide a role ARN in the [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) call which grants the service the required permissions to rotate the secret. For an example of a permissions policy, see [Security and Permissions](mes-security.md).

During rotation, the driver validates the current API key, creates a new API key and a new Application key (inheriting scopes from the current key), verifies both new keys, deletes the old pair using the new credentials, and promotes the new secret version to AWSCURRENT.