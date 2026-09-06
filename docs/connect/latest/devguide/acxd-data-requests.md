

# Data Requests
<a name="acxd-data-requests"></a>

Configure webhook integrations for retrieving or sending data during conversations.

**Topics**
+ [ListDataRequests](#acxd-data-requests-listdatarequests)
+ [CreateDataRequest](#acxd-data-requests-createdatarequest)
+ [GetDataRequest](#acxd-data-requests-getdatarequest)
+ [UpdateDataRequest](#acxd-data-requests-updatedatarequest)
+ [DeleteDataRequest](#acxd-data-requests-deletedatarequest)
+ [Request Parameters](#acxd-data-requests-request-parameters)
+ [Webhook Config](#acxd-data-requests-webhook-config)

## ListDataRequests
<a name="acxd-data-requests-listdatarequests"></a>

Lists all data requests in the workspace.

### Input
<a name="acxd-data-requests-listdatarequests-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| nextToken | string | No | 
| maxResults | integer | No | 

### Sample Request
<a name="acxd-data-requests-listdatarequests-sample-request"></a>

```
await client.send(new ListDataRequestsCommand({
  maxResults: 20,
}));
```

### Output
<a name="acxd-data-requests-listdatarequests-output"></a>

```
{
  "items": [
    {
      "dataRequestId": "getCustomerInfo",
      "type": "object",
      "webhook": {
        "implementation": "inline-static",
        "code": "{\"name\":\"John Doe\",\"tier\":\"premium\"}",
        "sendContext": true
      },
      "description": "Returns static customer info for testing",
      "createdAt": "2026-08-01T12:00:00.000Z",
      "updatedAt": "2026-08-01T12:00:00.000Z",
      "responseSchema": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "tier": {
            "type": "string"
          }
        }
      },
      "sensitive": false,
      "updatedBy": "ci-deploy-bot"
    }
  ]
}
```

### Errors
<a name="acxd-data-requests-listdatarequests-errors"></a>
+ `ValidationException` (400)
+ `InternalServerException` (500)

## CreateDataRequest
<a name="acxd-data-requests-createdatarequest"></a>

Creates a new data request.

### Input
<a name="acxd-data-requests-createdatarequest-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| dataRequestId | string | Yes | 
| type | enum | Yes | 
| webhook | object | Yes | 
| requestSchema | object | No | 
| responseSchema | object | No | 
| sensitive | boolean | No | 
| description | string | No | 
| metadata | object | No | 

### Sample Request
<a name="acxd-data-requests-createdatarequest-sample-request"></a>

```
await client.send(new CreateDataRequestCommand({
  dataRequestId: "getCustomerInfo",
  type: "object",
  webhook: {
    implementation: "inline-static",
    code: JSON.stringify({ name: "John Doe", tier: "premium" }),
  },
  responseSchema: {
    type: "object",
    properties: {
      name: { type: "string" },
      tier: { type: "string" },
    },
  },
  description: "Returns static customer info for testing",
  sensitive: false,
}));
```

### Output
<a name="acxd-data-requests-createdatarequest-output"></a>

```
{
  "dataRequestId": "getCustomerInfo",
  "type": "object",
  "webhook": {
    "implementation": "inline-static",
    "code": "{\"name\":\"John Doe\",\"tier\":\"premium\"}",
    "sendContext": true
  },
  "createdAt": "2026-08-10T01:55:34.146Z",
  "updatedAt": "2026-08-10T01:55:37.733Z",
  "responseSchema": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string"
      },
      "tier": {
        "type": "string"
      }
    }
  },
  "sensitive": false,
  "description": "Returns static customer info for testing",
  "updatedBy": "ci-deploy-bot"
}
```

### Errors
<a name="acxd-data-requests-createdatarequest-errors"></a>
+ `ValidationException` (400)
+ `ConflictException` (409)
+ `InternalServerException` (500)

## GetDataRequest
<a name="acxd-data-requests-getdatarequest"></a>

Gets a single data request by ID.

### Input
<a name="acxd-data-requests-getdatarequest-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| dataRequestIdentifier | string | Yes | 

### Sample Request
<a name="acxd-data-requests-getdatarequest-sample-request"></a>

```
await client.send(new GetDataRequestCommand({
  dataRequestIdentifier: "getCustomerInfo",
}));
```

### Output
<a name="acxd-data-requests-getdatarequest-output"></a>

```
{
  "dataRequestId": "getCustomerInfo",
  "type": "object",
  "webhook": {
    "implementation": "inline-static",
    "code": "{\"name\":\"John Doe\",\"tier\":\"premium\"}",
    "sendContext": true
  },
  "createdAt": "2026-08-10T01:55:34.146Z",
  "updatedAt": "2026-08-10T01:55:34.146Z",
  "responseSchema": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string"
      },
      "tier": {
        "type": "string"
      }
    }
  },
  "sensitive": false,
  "description": "Returns static customer info for testing",
  "updatedBy": "ci-deploy-bot"
}
```

### Errors
<a name="acxd-data-requests-getdatarequest-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## UpdateDataRequest
<a name="acxd-data-requests-updatedatarequest"></a>

Updates an existing data request. Only include fields you want to change.

### Input
<a name="acxd-data-requests-updatedatarequest-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| dataRequestIdentifier | string | Yes | 
| type | string | No | 
| webhook | object | No | 
| requestSchema | object | No | 
| responseSchema | object | No | 
| sensitive | boolean | No | 
| description | string | No | 
| metadata | object | No | 

### Sample Request
<a name="acxd-data-requests-updatedatarequest-sample-request"></a>

```
await client.send(new UpdateDataRequestCommand({
  dataRequestIdentifier: "getCustomerInfo",
  type: "object",
  description: "Updated static customer data",
  webhook: {
    implementation: "inline-static",
    code: JSON.stringify({ name: "Jane Smith", tier: "enterprise" }),
  },
  responseSchema: {
    type: "object",
    properties: {
      name: { type: "string" },
      tier: { type: "string" },
    },
  },
  sensitive: false,
}));
```

### Output
<a name="acxd-data-requests-updatedatarequest-output"></a>

```
{
  "dataRequestId": "getCustomerInfo",
  "type": "object",
  "webhook": {
    "implementation": "inline-static",
    "code": "{\"name\":\"Jane Smith\",\"tier\":\"enterprise\"}",
    "sendContext": true
  },
  "createdAt": "2026-08-10T01:55:34.146Z",
  "updatedAt": "2026-08-10T01:55:37.733Z",
  "responseSchema": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string"
      },
      "tier": {
        "type": "string"
      }
    }
  },
  "sensitive": false,
  "description": "Updated static customer data",
  "updatedBy": "ci-deploy-bot"
}
```

### Errors
<a name="acxd-data-requests-updatedatarequest-errors"></a>
+ `ResourceNotFoundException` (404)
+ `ValidationException` (400)
+ `InternalServerException` (500)

## DeleteDataRequest
<a name="acxd-data-requests-deletedatarequest"></a>

Deletes a data request.

### Input
<a name="acxd-data-requests-deletedatarequest-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| dataRequestIdentifier | string | Yes | 

### Sample Request
<a name="acxd-data-requests-deletedatarequest-sample-request"></a>

```
await client.send(new DeleteDataRequestCommand({
  dataRequestIdentifier: "getCustomerInfo",
}));
```

### Output
<a name="acxd-data-requests-deletedatarequest-output"></a>

No response body.

### Errors
<a name="acxd-data-requests-deletedatarequest-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## Request Parameters
<a name="acxd-data-requests-request-parameters"></a>

### dataRequestId
<a name="acxd-data-requests-request-parameters-datarequestid"></a>

Type: String

The data request identifier. Alphanumeric characters only, 3–100 characters.

### dataRequestIdentifier
<a name="acxd-data-requests-request-parameters-datarequestidentifier"></a>

Type: String

The data request ID used in Get, Update, and Delete operations.

### type
<a name="acxd-data-requests-request-parameters-type"></a>

Type: String

The return type of the data request. One of: `text`, `number`, `boolean`, `list<text>`, `object`, `list<object>`.

### webhook
<a name="acxd-data-requests-request-parameters-webhook"></a>

Type: Object

Webhook configuration. See Webhook Config.

### requestSchema
<a name="acxd-data-requests-request-parameters-requestschema"></a>

Type: Object

A JSON Schema defining the expected request payload shape. Same format as Context Variables `schema`, must have `type`, `$ref`, or `anyOf` at the top level.

### responseSchema
<a name="acxd-data-requests-request-parameters-responseschema"></a>

Type: Object

A JSON Schema defining the expected response payload shape.

### sensitive
<a name="acxd-data-requests-request-parameters-sensitive"></a>

Type: Boolean

Whether this data request handles sensitive data.

### description
<a name="acxd-data-requests-request-parameters-description"></a>

Type: String

Description. Max 200 characters.

### metadata
<a name="acxd-data-requests-request-parameters-metadata"></a>

Type: Object

Organizational metadata. See Common Types.

### createdAt
<a name="acxd-data-requests-request-parameters-createdat"></a>

Type: String

When the data request was created (ISO 8601).

### updatedAt
<a name="acxd-data-requests-request-parameters-updatedat"></a>

Type: String

When the data request was last modified (ISO 8601).

### updatedBy
<a name="acxd-data-requests-request-parameters-updatedby"></a>

Type: String

The identity of who last modified the data request.

### nextToken
<a name="acxd-data-requests-request-parameters-nexttoken"></a>

Type: String

Pagination token. See Common Types.

### maxResults
<a name="acxd-data-requests-request-parameters-maxresults"></a>

Type: Integer

Max items per page (1–500). See Common Types.

## Webhook Config
<a name="acxd-data-requests-webhook-config"></a>


| Field | Type | Required | 
| --- | --- | --- | 
| implementation | enum | Yes | 
| method | enum | No | 
| url | string | No | 
| headers | array | No | 
| code | string | No | 
| environments | object | No | 
| provider | object | No | 
| mcp | object | No | 
| sendContext | boolean | No | 

### implementation
<a name="acxd-data-requests-webhook-config-implementation"></a>

Type: String

The webhook implementation type. One of: `inline-static`, `external`, `mcp`.

### method
<a name="acxd-data-requests-webhook-config-method"></a>

Type: String

HTTP method. One of: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.

### url
<a name="acxd-data-requests-webhook-config-url"></a>

Type: String

Webhook URL. Max 2048 characters.

### headers
<a name="acxd-data-requests-webhook-config-headers"></a>

Type: Array

Request headers. Each entry:

### headers.key
<a name="acxd-data-requests-webhook-config-headers-key"></a>

Type: String

Header name. Max 128 characters.

### headers.value
<a name="acxd-data-requests-webhook-config-headers-value"></a>

Type: String

Header value. Max 4096 characters. Supports secret references: `{{secrets.my_secret}}`.

### headers.sensitive
<a name="acxd-data-requests-webhook-config-headers-sensitive"></a>

Type: Boolean

Whether this header contains sensitive data (will be masked in logs).

### headers.dynamic
<a name="acxd-data-requests-webhook-config-headers-dynamic"></a>

Type: Boolean

Whether this header value is evaluated at runtime.

### headers.required
<a name="acxd-data-requests-webhook-config-headers-required"></a>

Type: Boolean

Whether this header is required.

### code
<a name="acxd-data-requests-webhook-config-code"></a>

Type: String

Inline code for `inline-static` implementations. Max 200,000 characters.

### environments
<a name="acxd-data-requests-webhook-config-environments"></a>

Type: Object

Environment-specific configuration (free-form object).

### provider
<a name="acxd-data-requests-webhook-config-provider"></a>

Type: Object

Provider reference for managed integrations.

### provider.providerId
<a name="acxd-data-requests-webhook-config-provider-providerid"></a>

Type: String

The provider identifier.

### provider.actionId
<a name="acxd-data-requests-webhook-config-provider-actionid"></a>

Type: String

The action identifier within the provider.

### mcp
<a name="acxd-data-requests-webhook-config-mcp"></a>

Type: Object

Configuration for `mcp` implementation. Contains `method`, `url`, `headers`, `environments`, and `tools`.

### mcp.tools
<a name="acxd-data-requests-webhook-config-mcp-tools"></a>

Type: Array

MCP tool definitions. Each tool has `name` (string, required), `enabled` (boolean), `requestSchema` (object), `responseSchema` (object). Max 100 tools.

### sendContext
<a name="acxd-data-requests-webhook-config-sendcontext"></a>

Type: Boolean

Whether to send conversation context with the webhook request.