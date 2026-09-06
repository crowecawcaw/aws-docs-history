

# Modalities
<a name="acxd-modalities"></a>

Define input/output schemas for different interaction channels. Modalities describe the structured data shapes your application can send and receive.

**Topics**
+ [ListModalities](#acxd-modalities-listmodalities)
+ [CreateModality](#acxd-modalities-createmodality)
+ [GetModality](#acxd-modalities-getmodality)
+ [UpdateModality](#acxd-modalities-updatemodality)
+ [DeleteModality](#acxd-modalities-deletemodality)
+ [Request Parameters](#acxd-modalities-request-parameters)
+ [Modality Schema](#acxd-modalities-modality-schema)

## ListModalities
<a name="acxd-modalities-listmodalities"></a>

Lists all modalities in the workspace.

### Input
<a name="acxd-modalities-listmodalities-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| nextToken | string | No | 
| maxResults | integer | No | 

### Sample Request
<a name="acxd-modalities-listmodalities-sample-request"></a>

```
await client.send(new ListModalitiesCommand({}));
```

### Output
<a name="acxd-modalities-listmodalities-output"></a>

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
<a name="acxd-modalities-listmodalities-errors"></a>
+ `ValidationException` (400)
+ `InternalServerException` (500)

## CreateModality
<a name="acxd-modalities-createmodality"></a>

Creates a new modality.

### Input
<a name="acxd-modalities-createmodality-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| modalityId | string | Yes | 
| schema | object | Yes | 
| metadata | object | No | 

### Sample Request
<a name="acxd-modalities-createmodality-sample-request"></a>

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
<a name="acxd-modalities-createmodality-output"></a>

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
<a name="acxd-modalities-createmodality-errors"></a>
+ `ValidationException` (400)
+ `ConflictException` (409)
+ `InternalServerException` (500)

## GetModality
<a name="acxd-modalities-getmodality"></a>

Gets a single modality by ID.

### Input
<a name="acxd-modalities-getmodality-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| modalityIdentifier | string | Yes | 

### Sample Request
<a name="acxd-modalities-getmodality-sample-request"></a>

```
await client.send(new GetModalityCommand({
  modalityIdentifier: "checkout_form",
}));
```

### Output
<a name="acxd-modalities-getmodality-output"></a>

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
<a name="acxd-modalities-getmodality-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## UpdateModality
<a name="acxd-modalities-updatemodality"></a>

Updates an existing modality. Only include fields you want to change.

### Input
<a name="acxd-modalities-updatemodality-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| modalityIdentifier | string | Yes | 
| schema | object | No | 
| metadata | object | No | 

### Sample Request
<a name="acxd-modalities-updatemodality-sample-request"></a>

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
<a name="acxd-modalities-updatemodality-output"></a>

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
<a name="acxd-modalities-updatemodality-errors"></a>
+ `ResourceNotFoundException` (404)
+ `ValidationException` (400)
+ `InternalServerException` (500)

## DeleteModality
<a name="acxd-modalities-deletemodality"></a>

Deletes a modality.

### Input
<a name="acxd-modalities-deletemodality-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| modalityIdentifier | string | Yes | 

### Sample Request
<a name="acxd-modalities-deletemodality-sample-request"></a>

```
await client.send(new DeleteModalityCommand({
  modalityIdentifier: "checkout_form",
}));
```

### Output
<a name="acxd-modalities-deletemodality-output"></a>

No output returned. HTTP Status Code: 204.

### Errors
<a name="acxd-modalities-deletemodality-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## Request Parameters
<a name="acxd-modalities-request-parameters"></a>

### modalityId
<a name="acxd-modalities-request-parameters-modalityid"></a>

Type: String

The modality identifier. Alphanumeric \+ underscores, cannot start with a digit. Max 50 characters.

### modalityIdentifier
<a name="acxd-modalities-request-parameters-modalityidentifier"></a>

Type: String

The modality ID used in Get, Update, and Delete operations.

### schema
<a name="acxd-modalities-request-parameters-schema"></a>

Type: Object

The modality's data schema. A recursive structure defining the shape of data this modality handles. See Modality Schema.

### metadata
<a name="acxd-modalities-request-parameters-metadata"></a>

Type: Object

Organizational metadata. See Common Types.

### createdAt
<a name="acxd-modalities-request-parameters-createdat"></a>

Type: String

When the modality was created (ISO 8601).

### updatedAt
<a name="acxd-modalities-request-parameters-updatedat"></a>

Type: String

When the modality was last modified (ISO 8601).

### lastUpdatedBy
<a name="acxd-modalities-request-parameters-lastupdatedby"></a>

Type: String

The identity of who last modified the modality.

### nextToken
<a name="acxd-modalities-request-parameters-nexttoken"></a>

Type: String

Pagination token. See Common Types.

### maxResults
<a name="acxd-modalities-request-parameters-maxresults"></a>

Type: Integer

Max items per page (1–500). See Common Types.

## Modality Schema
<a name="acxd-modalities-modality-schema"></a>

A recursive schema definition describing the structure of data for this modality.


| Field | Type | Required | 
| --- | --- | --- | 
| type | string | Yes | 
| description | string | No | 
| isSensitive | boolean | No | 
| properties | object | No | 
| items | object | No | 

### type
<a name="acxd-modalities-modality-schema-type"></a>

Type: String

The data type. One of: `string`, `number`, `boolean`, `array`, `object`.

### description
<a name="acxd-modalities-modality-schema-description"></a>

Type: String

Human-readable description of this field. Max 255 characters.

### isSensitive
<a name="acxd-modalities-modality-schema-issensitive"></a>

Type: Boolean

Whether this field contains sensitive data (will be masked in logs/exports).

### properties
<a name="acxd-modalities-modality-schema-properties"></a>

Type: Object

Nested field schemas. Required when `type` is `object`. A map of field names to schema objects (recursive).

### items
<a name="acxd-modalities-modality-schema-items"></a>

Type: Object

Item schema. Required when `type` is `array`. A schema object describing each array element (recursive).

### Example:
<a name="acxd-modalities-modality-schema-example"></a>

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