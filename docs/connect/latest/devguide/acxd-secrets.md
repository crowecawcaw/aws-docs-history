

# Secrets
<a name="acxd-secrets"></a>

Store sensitive values (API keys, credentials, connection strings) encrypted at rest. Secrets can be referenced in data requests and integrations without exposing the value.

**Topics**
+ [ListSecrets](#acxd-secrets-listsecrets)
+ [CreateSecret](#acxd-secrets-createsecret)
+ [GetSecret](#acxd-secrets-getsecret)
+ [UpdateSecret](#acxd-secrets-updatesecret)
+ [DeleteSecret](#acxd-secrets-deletesecret)
+ [Request Parameters](#acxd-secrets-request-parameters)

## ListSecrets
<a name="acxd-secrets-listsecrets"></a>

Lists all secrets in the workspace. Values are never included in list responses.

### Input
<a name="w2aac18c13d159b7b5"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| nextToken | string | No | 
| maxResults | integer | No | 

### Sample Request
<a name="w2aac18c13d159b7b7"></a>

```
await client.send(new ListSecretsCommand({}));
```

### Output
<a name="w2aac18c13d159b7b9"></a>

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
<a name="w2aac18c13d159b7c11"></a>
+ `ValidationException` (400)
+ `InternalServerException` (500)

## CreateSecret
<a name="acxd-secrets-createsecret"></a>

Creates a new secret.

### Input
<a name="w2aac18c13d159b9b5"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| name | string | Yes | 
| secretValue | string | Yes | 
| description | string | No | 
| isSensitive | boolean | No | 
| metadata | object | No | 

### Sample Request
<a name="w2aac18c13d159b9b7"></a>

```
await client.send(new CreateSecretCommand({
  name: "stripe_api_key",
  secretValue: "sk_live_test123456789",
  description: "Stripe production API key",
  isSensitive: true,
}));
```

### Output
<a name="w2aac18c13d159b9b9"></a>

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
<a name="w2aac18c13d159b9c11"></a>
+ `ValidationException` (400)
+ `ConflictException` (409) a secret with this name already exists
+ `InternalServerException` (500)

## GetSecret
<a name="acxd-secrets-getsecret"></a>

Gets a single secret by name, including its value.

### Input
<a name="w2aac18c13d159c11b5"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| secretIdentifier | string | Yes | 

### Sample Request
<a name="w2aac18c13d159c11b7"></a>

```
await client.send(new GetSecretCommand({
  secretIdentifier: "stripe_api_key",
}));
```

### Output
<a name="w2aac18c13d159c11b9"></a>

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
<a name="w2aac18c13d159c11c11"></a>
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## UpdateSecret
<a name="acxd-secrets-updatesecret"></a>

Updates an existing secret. Only include fields you want to change.

### Input
<a name="w2aac18c13d159c13b5"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| secretIdentifier | string | Yes | 
| secretValue | string | No | 
| description | string | No | 
| isSensitive | boolean | No | 
| metadata | object | No | 

### Sample Request
<a name="w2aac18c13d159c13b7"></a>

```
const updated = await client.send(new UpdateSecretCommand({
  secretIdentifier: "stripe_api_key",
  description: "Updated - Stripe prod key (rotated Aug 2026)",
  secretValue: "sk_live_rotated_987654321",
}));
```

### Output
<a name="w2aac18c13d159c13b9"></a>

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
<a name="w2aac18c13d159c13c11"></a>
+ `ResourceNotFoundException` (404)
+ `ValidationException` (400)
+ `InternalServerException` (500)

## DeleteSecret
<a name="acxd-secrets-deletesecret"></a>

Deletes a secret.

### Input
<a name="w2aac18c13d159c15b5"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| secretIdentifier | string | Yes | 

### Sample Request
<a name="w2aac18c13d159c15b7"></a>

```
await client.send(new DeleteSecretCommand({
  secretIdentifier: "stripe_api_key",
}));
```

### Output
<a name="w2aac18c13d159c15b9"></a>

No response body.

### Errors
<a name="w2aac18c13d159c15c11"></a>
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## Request Parameters
<a name="acxd-secrets-request-parameters"></a>

`name`  
Type: String  
The secret name. Alphanumeric \+ underscores, 3–100 characters.

`secretIdentifier`  
Type: String  
The secret name used in Get, Update, and Delete operations.

`secretValue`  
Type: String  
The secret value. 1–4096 characters. This value is encrypted at rest and never logged.

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