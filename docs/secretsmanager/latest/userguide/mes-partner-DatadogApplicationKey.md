# Datadog Application Key

## Secret Value Fields

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "appKey": "`Application key starting with ddapp_`",
  "appKeyId": "`Application key UUID`",
  "serviceAccountId": "`Service Account UUID`"
}
```

appKey

The Datadog Application key owned by a service account. Starts with `ddapp_` followed by 34 alphanumeric characters.

appKeyId

The unique identifier (UUID) for the Application key.

serviceAccountId

The Datadog Service Account ID (UUID) that owns this Application key. Only service
account-owned Application keys can be rotated.

## Secret Metadata Fields

The following are the metadata fields for Datadog Application Key:

```
{
  "adminSecretArn": "arn:aws:secretsmanager:us-east-1:111122223333:secret:`DatadogAdminKey`"
}
```

adminSecretArn

The Amazon Resource Name (ARN) for a secret of type DatadogAdminKey that contains the
administrative Datadog credentials (API key and Application key) used to rotate this secret.
The admin secret must belong to the same service account as this Application key.

## Usage Flow

This rotation uses a two-secret architecture. An admin secret of type DatadogAdminKey provides
authentication credentials. The admin secret's `serviceAccountId` must match the user secret's
`serviceAccountId` to prevent privilege escalation.

You can create your secret using the [CreateSecret](../apireference/API_CreateSecret.md "../apireference/API_CreateSecret.md") call with the secret
value containing the fields mentioned above and secret type as DatadogApplicationKey. The rotation configurations can be set using a
[RotateSecret](../apireference/API_RotateSecret.md "../apireference/API_RotateSecret.md") call.
You must provide the `adminSecretArn` in the rotation metadata. You must also provide a role ARN in the
[RotateSecret](../apireference/API_RotateSecret.md "../apireference/API_RotateSecret.md") call which grants the service the required permissions to
rotate the secret. For an example of a permissions policy, see [Security and Permissions](mes-security.md "mes-security.md").

The admin secret type (`DatadogAdminKey`) differs from the user secret type
(`DatadogApplicationKey`). Because of this difference, the default rotation role policy scoped by
`secretsmanager:resource/Type` will not grant access to the admin secret.
You must explicitly provide the rotation role access to the admin secret.
You can do this by adding a statement scoped to the `DatadogAdminKey` type.
Alternatively, specify the admin secret `ARN` directly in the role policy.

During rotation, the driver validates ownership of the current key, creates a new Application key
via the Datadog Service Account API, verifies the new key, promotes it to AWSCURRENT, and deletes the old key.
