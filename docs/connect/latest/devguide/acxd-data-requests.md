# Data Requests

Configure webhook integrations for retrieving or sending data during conversations.

###### Contents

- [ListDataRequests](#acxd-data-requests-listdatarequests "#acxd-data-requests-listdatarequests")
- [CreateDataRequest](#acxd-data-requests-createdatarequest "#acxd-data-requests-createdatarequest")
- [GetDataRequest](#acxd-data-requests-getdatarequest "#acxd-data-requests-getdatarequest")
- [UpdateDataRequest](#acxd-data-requests-updatedatarequest "#acxd-data-requests-updatedatarequest")
- [DeleteDataRequest](#acxd-data-requests-deletedatarequest "#acxd-data-requests-deletedatarequest")
- [Request Parameters](#acxd-data-requests-request-parameters "#acxd-data-requests-request-parameters")
- [Webhook Config](#acxd-data-requests-webhook-config "#acxd-data-requests-webhook-config")

## ListDataRequests

Lists all data requests in the workspace.

### Input

| Parameter    | Type    | Required |
| ------------ | ------- | -------- |
| `nextToken`  | string  | No       |
| `maxResults` | integer | No       |

### Sample Request

```
await client.send(new ListDataRequestsCommand({
  maxResults: 20,
}));
```

### Output

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

- `ValidationException` (400)
- `InternalServerException` (500)

## CreateDataRequest

Creates a new data request.

### Input

| Parameter        | Type    | Required |
| ---------------- | ------- | -------- |
| `dataRequestId`  | string  | Yes      |
| `type`           | enum    | Yes      |
| `webhook`        | object  | Yes      |
| `requestSchema`  | object  | No       |
| `responseSchema` | object  | No       |
| `sensitive`      | boolean | No       |
| `description`    | string  | No       |
| `metadata`       | object  | No       |

### Sample Request

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

- `ValidationException` (400)
- `ConflictException` (409)
- `InternalServerException` (500)

## GetDataRequest

Gets a single data request by ID.

### Input

| Parameter               | Type   | Required |
| ----------------------- | ------ | -------- |
| `dataRequestIdentifier` | string | Yes      |

### Sample Request

```
await client.send(new GetDataRequestCommand({
  dataRequestIdentifier: "getCustomerInfo",
}));
```

### Output

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

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## UpdateDataRequest

Updates an existing data request. Only include fields you want to change.

### Input

| Parameter               | Type    | Required |
| ----------------------- | ------- | -------- |
| `dataRequestIdentifier` | string  | Yes      |
| `type`                  | string  | No       |
| `webhook`               | object  | No       |
| `requestSchema`         | object  | No       |
| `responseSchema`        | object  | No       |
| `sensitive`             | boolean | No       |
| `description`           | string  | No       |
| `metadata`              | object  | No       |

### Sample Request

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

- `ResourceNotFoundException` (404)
- `ValidationException` (400)
- `InternalServerException` (500)

## DeleteDataRequest

Deletes a data request.

### Input

| Parameter               | Type   | Required |
| ----------------------- | ------ | -------- |
| `dataRequestIdentifier` | string | Yes      |

### Sample Request

```
await client.send(new DeleteDataRequestCommand({
  dataRequestIdentifier: "getCustomerInfo",
}));
```

### Output

No response body.

### Errors

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## Request Parameters

### dataRequestId

Type: String

The data request identifier. Alphanumeric characters only, 3–100 characters.

### dataRequestIdentifier

Type: String

The data request ID used in Get, Update, and Delete operations.

### type

Type: String

The return type of the data request. One of: `text`, `number`,
`boolean`, `list<text>`, `object`,
`list<object>`.

### webhook

Type: Object

Webhook configuration. See Webhook Config.

### requestSchema

Type: Object

A JSON Schema defining the expected request payload shape. Same format as Context
Variables `schema`, must have `type`, `$ref`, or
`anyOf` at the top level.

### responseSchema

Type: Object

A JSON Schema defining the expected response payload shape.

### sensitive

Type: Boolean

Whether this data request handles sensitive data.

### description

Type: String

Description. Max 200 characters.

### metadata

Type: Object

Organizational metadata. See Common Types.

### createdAt

Type: String

When the data request was created (ISO 8601).

### updatedAt

Type: String

When the data request was last modified (ISO 8601).

### updatedBy

Type: String

The identity of who last modified the data request.

### nextToken

Type: String

Pagination token. See Common Types.

### maxResults

Type: Integer

Max items per page (1–500). See Common Types.

## Webhook Config

| Field            | Type    | Required |
| ---------------- | ------- | -------- |
| `implementation` | enum    | Yes      |
| `method`         | enum    | No       |
| `url`            | string  | No       |
| `headers`        | array   | No       |
| `code`           | string  | No       |
| `environments`   | object  | No       |
| `provider`       | object  | No       |
| `mcp`            | object  | No       |
| `sendContext`    | boolean | No       |

### implementation

Type: String

The webhook implementation type. One of: `inline-static`,
`external`, `mcp`.

### method

Type: String

HTTP method. One of: `GET`, `POST`, `PUT`,
`PATCH`, `DELETE`.

### url

Type: String

Webhook URL. Max 2048 characters.

### headers

Type: Array

Request headers. Each entry:

### headers.key

Type: String

Header name. Max 128 characters.

### headers.value

Type: String

Header value. Max 4096 characters. Supports secret references:
`{{secrets.my_secret}}`.

### headers.sensitive

Type: Boolean

Whether this header contains sensitive data (will be masked in logs).

### headers.dynamic

Type: Boolean

Whether this header value is evaluated at runtime.

### headers.required

Type: Boolean

Whether this header is required.

### code

Type: String

Inline code for `inline-static` implementations. Max 200,000 characters.

### environments

Type: Object

Environment-specific configuration (free-form object).

### provider

Type: Object

Provider reference for managed integrations.

### provider.providerId

Type: String

The provider identifier.

### provider.actionId

Type: String

The action identifier within the provider.

### mcp

Type: Object

Configuration for `mcp` implementation. Contains `method`,
`url`, `headers`, `environments`, and `tools`.

### mcp.tools

Type: Array

MCP tool definitions. Each tool has `name` (string, required),
`enabled` (boolean), `requestSchema` (object),
`responseSchema` (object). Max 100 tools.

### sendContext

Type: Boolean

Whether to send conversation context with the webhook request.
