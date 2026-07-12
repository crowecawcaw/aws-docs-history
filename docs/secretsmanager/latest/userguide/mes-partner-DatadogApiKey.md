# Datadog API Key

## Secret Value Fields

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "apiKey": "`32-character hex API key`",
  "apiKeyId": "`API key UUID`"
}
```

apiKey

The current Datadog API key. A 32-character hexadecimal string used to submit metrics, logs, and traces to Datadog.

apiKeyId

The unique identifier (UUID) for the API key. Found via the Datadog API or Organization Settings.

## Secret Metadata Fields

The following are the metadata fields for Datadog API Key:

```
{
  "adminSecretArn": "arn:aws:secretsmanager:us-east-1:111122223333:secret:`DatadogAdminKey`"
}
```

adminSecretArn

The Amazon Resource Name (ARN) for a secret of type DatadogAdminKey that contains the
administrative Datadog credentials (API key and Application key) used to rotate this secret.
The Application key must have scopes: `api_keys_write`, `api_keys_delete`.

## Usage Flow

This rotation uses a two-secret architecture. An admin secret of type DatadogAdminKey provides the
API key and Application key needed to authenticate Datadog Key Management API calls.

You can create your secret using the [CreateSecret](../apireference/API_CreateSecret.md "../apireference/API_CreateSecret.md") call with the secret
value containing the fields mentioned above and secret type as DatadogApiKey. The rotation configurations can be set using a
[RotateSecret](../apireference/API_RotateSecret.md "../apireference/API_RotateSecret.md") call.
You must provide the `adminSecretArn` in the rotation metadata. You must also provide a role ARN in the
[RotateSecret](../apireference/API_RotateSecret.md "../apireference/API_RotateSecret.md") call which grants the service the required permissions to
rotate the secret. For an example of a permissions policy, see [Security and Permissions](mes-security.md "mes-security.md").

The admin secret type (`DatadogAdminKey`) differs from the user secret type
(`DatadogApiKey`). Because of this difference, the default rotation role policy scoped by
`secretsmanager:resource/Type` will not grant access to the admin secret.
You must explicitly provide the rotation role access to the admin secret.
You can do this by adding a statement scoped to the `DatadogAdminKey` type.
Alternatively, specify the admin secret `ARN` directly in the role policy.

During rotation, the driver creates a new API key via the Datadog Key Management API v2,
verifies the new key using the validation endpoint, promotes the new key to AWSCURRENT,
and deletes the displaced key (two rotations old) from Datadog. This maintains a 2-key alternating
pattern ensuring zero-downtime rotation.
