# Modalities

Define input/output schemas for different interaction channels. Modalities describe
the structured data shapes your application can send and receive.

###### Contents

- [ListModalities](#acxd-modalities-listmodalities "#acxd-modalities-listmodalities")
- [CreateModality](#acxd-modalities-createmodality "#acxd-modalities-createmodality")
- [GetModality](#acxd-modalities-getmodality "#acxd-modalities-getmodality")
- [UpdateModality](#acxd-modalities-updatemodality "#acxd-modalities-updatemodality")
- [DeleteModality](#acxd-modalities-deletemodality "#acxd-modalities-deletemodality")
- [Request Parameters](#acxd-modalities-request-parameters "#acxd-modalities-request-parameters")
- [Modality Schema](#acxd-modalities-modality-schema "#acxd-modalities-modality-schema")

## ListModalities

Lists all modalities in the workspace.

### Input

| Parameter    | Type    | Required |
| ------------ | ------- | -------- |
| `nextToken`  | string  | No       |
| `maxResults` | integer | No       |

### Sample Request

```
await client.send(new ListModalitiesCommand({}));
```

### Output

```
{
  "items": [
    {
      "modalityId": "checkout_form",
      "schema": {
        "type": "object",
        "description": "Checkout form data",
        "properties": {
          "productId": { "type": "string", "description": "Product SKU" },
          "quantity": { "type": "number", "description": "Quantity to order" },
          "confirmed": { "type": "boolean", "description": "User confirmed" }
        }
      },
      "metadata": { "path": "/commerce", "tags": ["checkout"] },
      "createdAt": "2026-08-01T12:00:00.000Z",
      "updatedAt": "2026-08-01T12:00:00.000Z",
      "lastUpdatedBy": "ci-deploy-bot"
    }
  ],
  "nextToken": null
}
```

### Errors

- `ValidationException` (400)
- `InternalServerException` (500)

## CreateModality

Creates a new modality.

### Input

| Parameter    | Type   | Required |
| ------------ | ------ | -------- |
| `modalityId` | string | Yes      |
| `schema`     | object | Yes      |
| `metadata`   | object | No       |

### Sample Request

```
await client.send(new CreateModalityCommand({
  modalityId: "checkout_form",
  schema: {
    type: "object",
    description: "Checkout form data",
    properties: {
      productId: { type: "string", description: "Product SKU" },
      quantity: { type: "number", description: "Quantity to order" },
      confirmed: { type: "boolean", description: "User confirmed" },
      ssn: { type: "string", description: "Social security number", isSensitive: true },
    },
  },
  metadata: { path: "/commerce", tags: ["checkout"] },
}));
```

### Output

```
{
  "modalityId": "checkout_form",
  "schema": {
    "type": "object",
    "description": "Checkout form data",
    "isSensitive": false,
    "properties": {
      "productId": {
        "type": "string",
        "description": "Product SKU",
        "isSensitive": false
      },
      "quantity": {
        "type": "number",
        "description": "Quantity to order",
        "isSensitive": false
      },
      "confirmed": {
        "type": "boolean",
        "description": "User confirmed",
        "isSensitive": false
      },
      "ssn": {
        "type": "string",
        "description": "Social security number",
        "isSensitive": true
      }
    }
  },
  "metadata": {
    "path": "/commerce",
    "tags": [
      "checkout"
    ]
  },
  "createdAt": "2026-08-10T17:56:03.985Z",
  "updatedAt": "2026-08-10T17:56:03.985Z"
}
```

### Errors

- `ValidationException` (400)
- `ConflictException` (409)
- `InternalServerException` (500)

## GetModality

Gets a single modality by ID.

### Input

| Parameter            | Type   | Required |
| -------------------- | ------ | -------- |
| `modalityIdentifier` | string | Yes      |

### Sample Request

```
await client.send(new GetModalityCommand({
  modalityIdentifier: "checkout_form",
}));
```

### Output

```
{
  "modalityId": "checkout_form",
  "schema": {
    "type": "object",
    "description": "Checkout form data",
    "isSensitive": false,
    "properties": {
      "productId": {
        "type": "string",
        "description": "Product SKU",
        "isSensitive": false
      },
      "quantity": {
        "type": "number",
        "description": "Quantity to order",
        "isSensitive": false
      },
      "confirmed": {
        "type": "boolean",
        "description": "User confirmed",
        "isSensitive": false
      },
      "ssn": {
        "type": "string",
        "description": "Social security number",
        "isSensitive": true
      }
    }
  },
  "metadata": {
    "path": "/commerce",
    "tags": [
      "checkout"
    ]
  },
  "createdAt": "2026-08-10T17:56:03.985Z",
  "updatedAt": "2026-08-10T17:56:03.985Z"
}
```

### Errors

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## UpdateModality

Updates an existing modality. Only include fields you want to change.

### Input

| Parameter            | Type   | Required |
| -------------------- | ------ | -------- |
| `modalityIdentifier` | string | Yes      |
| `schema`             | object | No       |
| `metadata`           | object | No       |

### Sample Request

```
await client.send(new UpdateModalityCommand({
  modalityIdentifier: "checkout_form",
  schema: {
    type: "object",
    description: "Checkout form data - updated",
    properties: {
      productId: { type: "string", description: "Product SKU" },
      quantity: { type: "number", description: "Quantity to order" },
      confirmed: { type: "boolean", description: "User confirmed" },
      ssn: { type: "string", description: "Social security number", isSensitive: true },
      couponCode: { type: "string", description: "Optional coupon code" },
    },
  },
}));
```

### Output

```
{
  "modalityId": "checkout_form",
  "schema": {
    "type": "object",
    "description": "Checkout form data - updated",
    "isSensitive": false,
    "properties": {
      "quantity": {
        "type": "number",
        "description": "Quantity to order",
        "isSensitive": false
      },
      "productId": {
        "type": "string",
        "description": "Product SKU",
        "isSensitive": false
      },
      "confirmed": {
        "type": "boolean",
        "description": "User confirmed",
        "isSensitive": false
      },
      "couponCode": {
        "type": "string",
        "description": "Optional coupon code",
        "isSensitive": false
      },
      "ssn": {
        "type": "string",
        "description": "Social security number",
        "isSensitive": true
      }
    }
  },
  "metadata": {
    "path": "/commerce",
    "tags": [
      "checkout"
    ]
  },
  "createdAt": "2026-08-10T17:56:03.985Z",
  "updatedAt": "2026-08-10T17:56:06.157Z"
}
```

### Errors

- `ResourceNotFoundException` (404)
- `ValidationException` (400)
- `InternalServerException` (500)

## DeleteModality

Deletes a modality.

### Input

| Parameter            | Type   | Required |
| -------------------- | ------ | -------- |
| `modalityIdentifier` | string | Yes      |

### Sample Request

```
await client.send(new DeleteModalityCommand({
  modalityIdentifier: "checkout_form",
}));
```

### Output

No output returned. HTTP Status Code: 204.

### Errors

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## Request Parameters

### modalityId

Type: String

The modality identifier. Alphanumeric + underscores, cannot start with a digit. Max 50
characters.

### modalityIdentifier

Type: String

The modality ID used in Get, Update, and Delete operations.

### schema

Type: Object

The modality's data schema. A recursive structure defining the shape of data this
modality handles. See Modality Schema.

### metadata

Type: Object

Organizational metadata. See Common Types.

### createdAt

Type: String

When the modality was created (ISO 8601).

### updatedAt

Type: String

When the modality was last modified (ISO 8601).

### lastUpdatedBy

Type: String

The identity of who last modified the modality.

### nextToken

Type: String

Pagination token. See Common Types.

### maxResults

Type: Integer

Max items per page (1–500). See Common Types.

## Modality Schema

A recursive schema definition describing the structure of data for this modality.

| Field         | Type    | Required |
| ------------- | ------- | -------- |
| `type`        | string  | Yes      |
| `description` | string  | No       |
| `isSensitive` | boolean | No       |
| `properties`  | object  | No       |
| `items`       | object  | No       |

### type

Type: String

The data type. One of: `string`, `number`, `boolean`,
`array`, `object`.

### description

Type: String

Human-readable description of this field. Max 255 characters.

### isSensitive

Type: Boolean

Whether this field contains sensitive data (will be masked in logs/exports).

### properties

Type: Object

Nested field schemas. Required when `type` is `object`. A map of
field names to schema objects (recursive).

### items

Type: Object

Item schema. Required when `type` is `array`. A schema object
describing each array element (recursive).

### Example:

```
{
  "type": "object",
  "description": "User profile card",
  "properties": {
    "name": { "type": "string", "description": "Display name" },
    "age": { "type": "number" },
    "preferences": {
      "type": "array",
      "items": { "type": "string", "description": "A preference tag" }
    },
    "ssn": { "type": "string", "isSensitive": true }
  }
}
```
