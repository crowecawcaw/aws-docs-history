# Secrets

Store sensitive values (API keys, credentials, connection strings) encrypted at rest.
Secrets can be referenced in data requests and integrations without exposing the
value.

###### Contents

- [ListSecrets](#acxd-secrets-listsecrets "#acxd-secrets-listsecrets")
- [CreateSecret](#acxd-secrets-createsecret "#acxd-secrets-createsecret")
- [GetSecret](#acxd-secrets-getsecret "#acxd-secrets-getsecret")
- [UpdateSecret](#acxd-secrets-updatesecret "#acxd-secrets-updatesecret")
- [DeleteSecret](#acxd-secrets-deletesecret "#acxd-secrets-deletesecret")
- [Request Parameters](#acxd-secrets-request-parameters "#acxd-secrets-request-parameters")

## ListSecrets

Lists all secrets in the workspace. Values are never included in list responses.

### Input

| Parameter    | Type    | Required |
| ------------ | ------- | -------- |
| `nextToken`  | string  | No       |
| `maxResults` | integer | No       |

### Sample Request

```
await client.send(new ListSecretsCommand({}));
```

### Output

```
{
  "items": [
    {
      "name": "stripe_api_key",
      "description": "Stripe production API key",
      "isSensitive": true,
      "metadata": { "path": "/integrations", "tags": ["payments"] },
      "createdAt": "2026-08-01T12:00:00.000Z",
      "updatedAt": "2026-08-01T12:00:00.000Z"
    }
  ],
  "nextToken": null
}
```

### Errors

- `ValidationException` (400)
- `InternalServerException` (500)

## CreateSecret

Creates a new secret.

### Input

| Parameter     | Type    | Required |
| ------------- | ------- | -------- |
| `name`        | string  | Yes      |
| `secretValue` | string  | Yes      |
| `description` | string  | No       |
| `isSensitive` | boolean | No       |
| `metadata`    | object  | No       |

### Sample Request

```
await client.send(new CreateSecretCommand({
  name: "stripe_api_key",
  secretValue: "sk_live_test123456789",
  description: "Stripe production API key",
  isSensitive: true,
}));
```

### Output

```
{
  "name": "stripe_api_key",
  "secretValue": "*******89",
  "description": "Stripe production API key",
  "isSensitive": true,
  "metadata": {},
  "createdAt": "2026-08-01T12:00:00.000Z",
  "updatedAt": "2026-08-01T12:00:00.000Z",
  "lastUpdatedBy": "ci-deploy-bot"
}
```

### Errors

- `ValidationException` (400)
- `ConflictException` (409) a secret with this name already exists
- `InternalServerException` (500)

## GetSecret

Gets a single secret by name, including its value.

### Input

| Parameter          | Type   | Required |
| ------------------ | ------ | -------- |
| `secretIdentifier` | string | Yes      |

### Sample Request

```
await client.send(new GetSecretCommand({
  secretIdentifier: "stripe_api_key",
}));
```

### Output

```
{
  "name": "stripe_api_key",
  "secretValue": "*******89",
  "description": "Stripe production API key",
  "isSensitive": true,
  "metadata": {},
  "createdAt": "2026-08-01T12:00:00.000Z",
  "updatedAt": "2026-08-01T12:00:00.000Z",
  "lastUpdatedBy": "ci-deploy-bot"
}
```

### Errors

- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## UpdateSecret

Updates an existing secret. Only include fields you want to change.

### Input

| Parameter          | Type    | Required |
| ------------------ | ------- | -------- |
| `secretIdentifier` | string  | Yes      |
| `secretValue`      | string  | No       |
| `description`      | string  | No       |
| `isSensitive`      | boolean | No       |
| `metadata`         | object  | No       |

### Sample Request

```
const updated = await client.send(new UpdateSecretCommand({
  secretIdentifier: "stripe_api_key",
  description: "Updated - Stripe prod key (rotated Aug 2026)",
  secretValue: "sk_live_rotated_987654321",
}));
```

### Output

```
{
  "name": "stripe_api_key",
  "secretValue": "************1",
  "description": "Updated - Stripe prod key (rotated Aug 2026)",
  "isSensitive": true,
  "metadata": {},
  "createdAt": "2026-08-01T12:00:00.000Z",
  "updatedAt": "2026-08-01T12:00:00.000Z",
  "lastUpdatedBy": "ci-deploy-bot"
}
```

### Errors

- `ResourceNotFoundException` (404)
- `ValidationException` (400)
- `InternalServerException` (500)

## DeleteSecret

Deletes a secret.

### Input

| Parameter          | Type   | Required |
| ------------------ | ------ | -------- |
| `secretIdentifier` | string | Yes      |

### Sample Request

```
await client.send(new DeleteSecretCommand({
  secretIdentifier: "stripe_api_key",
}));
```

### Output

No response body.

### Errors

- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## Request Parameters

`name`

Type: String

The secret name. Alphanumeric + underscores, 3–100 characters.

`secretIdentifier`

Type: String

The secret name used in Get, Update, and Delete operations.

`secretValue`

Type: String

The secret value. 1–4096 characters. This value is encrypted at rest and never
logged.

`description`

Type: String

Description. Max 200 characters.

`isSensitive`

Type: Boolean

Whether this secret contains sensitive data.

`metadata`

Type: Object

Organizational metadata. See Common Types.

`createdAt`

Type: String

When the secret was created (ISO 8601).

`updatedAt`

Type: String

When the secret was last modified (ISO 8601).

`lastUpdatedBy`

Type: String

The identity of who last modified the secret.

`nextToken`

Type: String

Pagination token. See Common Types.

`maxResults`

Type: Integer

Max items per page (1–500). See Common Types.
