

# API Tokens
<a name="acxd-api-tokens"></a>

Manage ACXD SDK API tokens for programmatic users. Tokens are the credentials used to authenticate with the ACXD SDK.

**Topics**
+ [CreateApiToken](#acxd-api-tokens-createapitoken)
+ [ListApiTokens](#acxd-api-tokens-listapitokens)
+ [DeleteApiToken](#acxd-api-tokens-deleteapitoken)
+ [Request Parameters](#acxd-api-tokens-request-parameters)

## CreateApiToken
<a name="acxd-api-tokens-createapitoken"></a>

Creates a new API token for a programmatic user. The full token is returned only once.

### Input
<a name="acxd-api-tokens-createapitoken-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| userId | string | Yes | 
| description | string | No | 

### Sample Request
<a name="acxd-api-tokens-createapitoken-sample-request"></a>

```
await client.send(new CreateApiTokenCommand({
    userId: 'programmatic-user-uuid',
    description: 'CI/CD pipeline',
}));
```

### Output
<a name="acxd-api-tokens-createapitoken-output"></a>

```
{
  "token": "acxd_live_mPj4Y4hfXKg5NIuhX24d.K9mN2pQ4rS6tU8vW0xY1zA3bC5dE7fG9",
  "keyPrefix": "mPj4Y4hfXKg5NIuhX24d",
  "description": "CI/CD pipeline",
  "createdAt": "2026-08-01T12:00:00.000Z"
}
```

**Important**  
The `token` field is only returned on creation. Store it securely, it cannot be retrieved again.

### Errors
<a name="acxd-api-tokens-createapitoken-errors"></a>
+ `ValidationException` (400)
+ `ConflictException` (409)
+ `InternalServerException` (500)

## ListApiTokens
<a name="acxd-api-tokens-listapitokens"></a>

Lists all API tokens for a programmatic user. Returns metadata only, secrets are never exposed.

### Input
<a name="acxd-api-tokens-listapitokens-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| userId | string | Yes | 

### Sample Request
<a name="acxd-api-tokens-listapitokens-sample-request"></a>

```
await client.send(new ListApiTokensCommand({
    userId: 'programmatic-user-uuid',
}));
```

### Output
<a name="acxd-api-tokens-listapitokens-output"></a>

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
<a name="acxd-api-tokens-listapitokens-errors"></a>
+ `ValidationException` (400)
+ `InternalServerException` (500)

## DeleteApiToken
<a name="acxd-api-tokens-deleteapitoken"></a>

Permanently revokes an API token.

### Input
<a name="acxd-api-tokens-deleteapitoken-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| userId | string | Yes | 
| keyPrefix | string | Yes | 

### Sample Request
<a name="acxd-api-tokens-deleteapitoken-sample-request"></a>

```
await client.send(new DeleteApiTokenCommand({
    userId: 'programmatic-user-uuid',
    keyPrefix: 'mPj4Y4hfXKg5NIuhX24d',
}));
```

### Output
<a name="acxd-api-tokens-deleteapitoken-output"></a>

No response body.

### Errors
<a name="acxd-api-tokens-deleteapitoken-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## Request Parameters
<a name="acxd-api-tokens-request-parameters"></a>

`userId`  
Type: String  
Description: The programmatic user ID that owns the token.

`description`  
Type: String  
Description: An optional human-readable label for the token (e.g., "CI/CD pipeline", "staging environment").

`token`  
Type: String  
Description: The full API token value. Format: `acxd_live_<prefix>.<secret>` . Only returned once on creation, store it securely.

`keyPrefix`  
Type: String  
Description: The 20-character public prefix of the token. Used to identify tokens in list and delete operations. This is not a secret.

`createdAt`  
Type: String  
Description: When the token was created (ISO 8601).