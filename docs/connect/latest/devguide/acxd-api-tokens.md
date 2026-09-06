# API Tokens

Manage ACXD SDK API tokens for programmatic users. Tokens are the credentials
used to authenticate with the ACXD SDK.

###### Contents

- [CreateApiToken](#acxd-api-tokens-createapitoken "#acxd-api-tokens-createapitoken")
- [ListApiTokens](#acxd-api-tokens-listapitokens "#acxd-api-tokens-listapitokens")
- [DeleteApiToken](#acxd-api-tokens-deleteapitoken "#acxd-api-tokens-deleteapitoken")
- [Request Parameters](#acxd-api-tokens-request-parameters "#acxd-api-tokens-request-parameters")

## CreateApiToken

Creates a new API token for a programmatic user. The full token is returned only
once.

### Input

| Parameter     | Type   | Required |
| ------------- | ------ | -------- |
| `userId`      | string | Yes      |
| `description` | string | No       |

### Sample Request

```
await client.send(new CreateApiTokenCommand({
    userId: 'programmatic-user-uuid',
    description: 'CI/CD pipeline',
}));
```

### Output

```
{
  "token": "acxd_live_mPj4Y4hfXKg5NIuhX24d.K9mN2pQ4rS6tU8vW0xY1zA3bC5dE7fG9",
  "keyPrefix": "mPj4Y4hfXKg5NIuhX24d",
  "description": "CI/CD pipeline",
  "createdAt": "2026-08-01T12:00:00.000Z"
}
```

###### Important

The `token` field is only returned on creation. Store it securely, it
cannot be retrieved again.

### Errors

- `ValidationException` (400)
- `ConflictException` (409)
- `InternalServerException` (500)

## ListApiTokens

Lists all API tokens for a programmatic user. Returns metadata only, secrets are never
exposed.

### Input

| Parameter | Type   | Required |
| --------- | ------ | -------- |
| `userId`  | string | Yes      |

### Sample Request

```
await client.send(new ListApiTokensCommand({
    userId: 'programmatic-user-uuid',
}));
```

### Output

```
{
  "items": [
    {
      "keyPrefix": "mPj4Y4hfXKg5NIuhX24d",
      "description": "CI/CD pipeline",
      "createdAt": "2026-08-01T12:00:00.000Z"
    }
  ]
}
```

### Errors

- `ValidationException` (400)
- `InternalServerException` (500)

## DeleteApiToken

Permanently revokes an API token.

### Input

| Parameter   | Type   | Required |
| ----------- | ------ | -------- |
| `userId`    | string | Yes      |
| `keyPrefix` | string | Yes      |

### Sample Request

```
await client.send(new DeleteApiTokenCommand({
    userId: 'programmatic-user-uuid',
    keyPrefix: 'mPj4Y4hfXKg5NIuhX24d',
}));
```

### Output

No response body.

### Errors

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## Request Parameters

`userId`

Type: String

Description: The programmatic user ID that owns the token.

`description`

Type: String

Description: An optional human-readable label for the token (e.g., "CI/CD pipeline",
"staging environment").

`token`

Type: String

Description: The full API token value. Format: `acxd_live_<prefix>.<secret>` . Only
returned once on creation, store it securely.

`keyPrefix`

Type: String

Description: The 20-character public prefix of the token. Used to identify tokens in
list and delete operations. This is not a secret.

`createdAt`

Type: String

Description: When the token was created (ISO 8601).
