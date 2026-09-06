

# Slot Types
<a name="acxd-slot-types"></a>

Custom entity types for extracting structured data from user input. A slot type defines a list of values (with optional synonyms) that the NLP engine uses to identify entities in conversation.

**Topics**
+ [ListSlotTypes](#acxd-slot-types-listslottypes)
+ [CreateSlotType](#acxd-slot-types-createslottype)
+ [GetSlotType](#acxd-slot-types-getslottype)
+ [UpdateSlotType](#acxd-slot-types-updateslottype)
+ [DeleteSlotType](#acxd-slot-types-deleteslottype)
+ [Request Parameters](#acxd-slot-types-request-parameters)
+ [Slot Type Value](#acxd-slot-types-slot-type-value)

## ListSlotTypes
<a name="acxd-slot-types-listslottypes"></a>

Lists all slot types in the workspace.

### Input
<a name="acxd-slot-types-listslottypes-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| nextToken | string | No | 
| maxResults | integer | No | 

### Sample Request
<a name="acxd-slot-types-listslottypes-sample-request"></a>

```
await client.send(new ListSlotTypesCommand({}));
```

### Output
<a name="acxd-slot-types-listslottypes-output"></a>

```
{
  "items": [
    {
      "slotTypeId": "ProductCategory",
      "values": [
        { 
          "value": "Electronics",
          "valueId": "YgpzvBgO5UOe-t29GbY_0",
          "synonyms": ["tech", "gadgets"]
        },
        { 
          "value": "Clothing",
          "valueId": "Up978eurWeqncYG9bxVof",
          "synonyms": ["apparel", "fashion"] 
        }
      ],
      "sensitive": false,
      "mainLanguageCode": "en-US",
      "languageCodes": ["en-US"],
      "description": "Product categories for the catalog",
      "metadata": { "path": "/commerce", "tags": ["catalog"] },
      "createdAt": "2026-08-01T12:00:00.000Z",
      "updatedAt": "2026-08-01T12:00:00.000Z",
      "lastUpdatedBy": "ci-deploy-bot"
    }
  ],
  "nextToken": null
}
```

### Errors
<a name="acxd-slot-types-listslottypes-errors"></a>
+ `ValidationException` (400)
+ `InternalServerException` (500)

## CreateSlotType
<a name="acxd-slot-types-createslottype"></a>

Creates a new slot type.

### Input
<a name="acxd-slot-types-createslottype-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| slotTypeId | string | Yes | 
| values | array | Yes | 
| sensitive | boolean | No | 
| mainLanguageCode | string | No | 
| languageCodes | array | No | 
| description | string | No | 
| metadata | object | No | 

### Sample Request
<a name="acxd-slot-types-createslottype-sample-request"></a>

```
await client.send(new CreateSlotTypeCommand({
  slotTypeId: "ProductCategory",
  values: [
    { value: "Electronics", synonyms: ["tech", "gadgets", "devices"] },
    { value: "Clothing", synonyms: ["apparel", "fashion"] },
    { value: "Home", synonyms: ["household", "furniture"] },
  ],
  sensitive: false,
  mainLanguageCode: "en-US",
  languageCodes: ["en-US"],
  description: "Product categories for the catalog",
  metadata: { path: "/commerce", tags: ["catalog"] },
}));
```

### Output
<a name="acxd-slot-types-createslottype-output"></a>

```
{
  "slotTypeId": "ProductCategory",
  "values": [
    { 
      "value": "Electronics",
      "valueId": "YgpzvBgO5UOe-t29GbY_0",
      "synonyms": ["tech", "gadgets", "devices"]
    },
    { 
      "value": "Clothing",
      "valueId": "Up978eurWeqncYG9bxVof",
      "synonyms": ["apparel", "fashion"] 
    },
    {
      "value": "Home",
      "valueId": "S8SBNDXOeJvRyQvlVkq0G",
      "synonyms": ["household","furniture"]
    }
  ],
  "sensitive": false,
  "mainLanguageCode": "en-US",
  "languageCodes": ["en-US"],
  "description": "Product categories for the catalog",
  "metadata": { "path": "/commerce", "tags": ["catalog"] },
  "createdAt": "2026-08-01T12:00:00.000Z",
  "updatedAt": "2026-08-01T12:00:00.000Z",
  "lastUpdatedBy": "ci-deploy-bot"
}
```

### Errors
<a name="acxd-slot-types-createslottype-errors"></a>
+ `ValidationException` (400)
+ `ConflictException` (409)
+ `InternalServerException` (500)

## GetSlotType
<a name="acxd-slot-types-getslottype"></a>

Gets a single slot type by ID.

### Input
<a name="acxd-slot-types-getslottype-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| slotTypeIdentifier | string | Yes | 
| languageCode | string | No | 

### Sample Request
<a name="acxd-slot-types-getslottype-sample-request"></a>

```
await client.send(new GetSlotTypeCommand({
  slotTypeIdentifier: "ProductCategory",
}));
```

### Output
<a name="acxd-slot-types-getslottype-output"></a>

```
{
  "slotTypeId": "ProductCategory",
  "values": [
    { 
      "value": "Electronics",
      "valueId": "YgpzvBgO5UOe-t29GbY_0",
      "synonyms": ["tech", "gadgets", "devices"]
    },
    { 
      "value": "Clothing",
      "valueId": "Up978eurWeqncYG9bxVof",
      "synonyms": ["apparel", "fashion"] 
    },
    {
      "value": "Home",
      "valueId": "S8SBNDXOeJvRyQvlVkq0G",
      "synonyms": ["household","furniture"]
    }
  ],
  "sensitive": false,
  "mainLanguageCode": "en-US",
  "languageCodes": ["en-US"],
  "description": "Product categories for the catalog",
  "metadata": { "path": "/commerce", "tags": ["catalog"] },
  "createdAt": "2026-08-01T12:00:00.000Z",
  "updatedAt": "2026-08-01T12:00:00.000Z",
  "lastUpdatedBy": "ci-deploy-bot"
}
```

### Errors
<a name="acxd-slot-types-getslottype-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## UpdateSlotType
<a name="acxd-slot-types-updateslottype"></a>

Updates an existing slot type. Only include fields you want to change.

### Input
<a name="acxd-slot-types-updateslottype-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| slotTypeIdentifier | string | Yes | 
| values | array | No | 
| sensitive | boolean | No | 
| mainLanguageCode | string | No | 
| languageCodes | array | No | 
| description | string | No | 
| metadata | object | No | 

### Sample Request
<a name="acxd-slot-types-updateslottype-sample-request"></a>

```
await client.send(new UpdateSlotTypeCommand({
  slotTypeIdentifier: "ProductCategory",
  values: [
    { value: "Electronics", synonyms: ["tech", "gadgets", "devices"] },
    { value: "Clothing", synonyms: ["apparel", "fashion"] },
    { value: "Home", synonyms: ["household", "furniture"] },
    { value: "Sports", synonyms: ["fitness", "athletic", "outdoor"] },
  ],
  sensitive: false,
  mainLanguageCode: "en-US",
  languageCodes: ["en-US"],
  description: "Updated - product categories with sports",
  metadata: { path: "/commerce", tags: ["catalog"] },
}));
```

### Output
<a name="acxd-slot-types-updateslottype-output"></a>

```
{
  "slotTypeId": "ProductCategory",
  "values": [
    { 
      "value": "Electronics",
      "valueId": "YgpzvBgO5UOe-t29GbY_0",
      "synonyms": ["tech", "gadgets", "devices"]
    },
    { 
      "value": "Clothing",
      "valueId": "Up978eurWeqncYG9bxVof",
      "synonyms": ["apparel", "fashion"] 
    },
    {
      "value": "Home",
      "valueId": "S8SBNDXOeJvRyQvlVkq0G",
      "synonyms": ["household","furniture"]
    },
    {
      "value": "Sports",
      "valueId": "YmMQgeQllEKErJCclWl7Z",
      "synonyms": ["fitness","athletic","outdoor"]
    }
  ],
  "sensitive": false,
  "mainLanguageCode": "en-US",
  "languageCodes": ["en-US"],
  "description": "Updated - product categories with sports",
  "metadata": { "path": "/commerce", "tags": ["catalog"] },
  "createdAt": "2026-08-01T12:00:00.000Z",
  "updatedAt": "2026-08-01T12:00:00.000Z",
  "lastUpdatedBy": "ci-deploy-bot"
}
```

### Errors
<a name="acxd-slot-types-updateslottype-errors"></a>
+ `ResourceNotFoundException` (404)
+ `ValidationException` (400)
+ `InternalServerException` (500)

## DeleteSlotType
<a name="acxd-slot-types-deleteslottype"></a>

Deletes a slot type.

### Input
<a name="acxd-slot-types-deleteslottype-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| slotTypeIdentifier | string | Yes | 

### Sample Request
<a name="acxd-slot-types-deleteslottype-sample-request"></a>

```
await client.send(new DeleteSlotTypeCommand({
  slotTypeIdentifier: "ProductCategory",
}));
```

### Output
<a name="acxd-slot-types-deleteslottype-output"></a>

No response body.

### Errors
<a name="acxd-slot-types-deleteslottype-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## Request Parameters
<a name="acxd-slot-types-request-parameters"></a>

`slotTypeId`  
Type: String  
The slot type identifier. Alphabetic characters only, 3–100 characters.

`slotTypeIdentifier`  
Type: String  
The slot type ID used in Get, Update, and Delete operations.

`values`  
Type: Array  
Slot type values. See Slot Type Value.

`sensitive`  
Type: Boolean  
Whether values contain sensitive data.

`mainLanguageCode`  
Type: String  
Primary language. See Common Types.

`languageCode`  
Type: String  
Get values in a specific language. See Common Types.

`languageCodes`  
Type: Array  
Supported languages. See Common Types.

`description`  
Type: String  
Description. Max 200 characters.

`metadata`  
Type: Object  
Organizational metadata. See Common Types.

`createdAt`  
Type: String  
When the slot type was created (ISO 8601).

`updatedAt`  
Type: String  
When the slot type was last modified (ISO 8601).

`lastUpdatedBy`  
Type: String  
The identity of who last modified the slot type.

`nextToken`  
Type: String  
Pagination token. See Common Types.

`maxResults`  
Type: Integer  
Max items per page (1–500). See Common Types.

## Slot Type Value
<a name="acxd-slot-types-slot-type-value"></a>


| Field | Type | Required | 
| --- | --- | --- | 
| value | string | Yes | 
| valueId | string | No | 
| synonyms | array | No | 
| skipTraining | boolean | No | 
| skipTranslation | boolean | No | 
| choicePayload | string | No | 

`value`  
Type: String  
The canonical value. 1–256 characters.

`valueId`  
Type: String  
Optional value identifier.

`synonyms`  
Type: Array  
Alternative phrases that map to this value (array of strings, each 1–256 characters).  
Example:  

```
{ "value": "Electronics", "synonyms": ["tech", "gadgets", "devices"] }
```

`skipTraining`  
Type: Boolean  
Exclude this value from NLP training.

`skipTranslation`  
Type: Boolean  
Skip auto-translation for this value.

`choicePayload`  
Type: String  
Payload sent when this value is selected in a choice node. Max 200 characters.