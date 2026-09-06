

# Context Variables
<a name="acxd-context-variables"></a>

Define typed variables available across conversations within a workspace. Context variables can be referenced in flows and set by external systems.

**Topics**
+ [ListContextVariables](#acxd-context-variables-listcontextvariables)
+ [CreateContextVariable](#acxd-context-variables-createcontextvariable)
+ [UpdateContextVariable](#acxd-context-variables-updatecontextvariable)
+ [DeleteContextVariable](#acxd-context-variables-deletecontextvariable)
+ [Request Parameters](#acxd-context-variables-request-parameters)

## ListContextVariables
<a name="acxd-context-variables-listcontextvariables"></a>

Lists all context variables in the workspace.

### Input
<a name="acxd-context-variables-listcontextvariables-input"></a>

No parameters.

### Sample Request
<a name="acxd-context-variables-listcontextvariables-sample-request"></a>

```
await client.send(new ListContextVariablesCommand({}));
```

### Output
<a name="acxd-context-variables-listcontextvariables-output"></a>

```
{
  "items": [
    {
      "name": "sampleContextVariable",
      "type": "string",
      "schema": {
        "type": "string",
        "isSensitive": false
      },
      "disallowExternalModification": false,
      "metadata": { "path": "/crm", "tags": ["segmentation"] }
    }
  ]
}
```

### Errors
<a name="acxd-context-variables-listcontextvariables-errors"></a>
+ `ValidationException` (400)
+ `InternalServerException` (500)

## CreateContextVariable
<a name="acxd-context-variables-createcontextvariable"></a>

Creates a new context variable.

### Input
<a name="acxd-context-variables-createcontextvariable-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| name | string | Yes | 
| schema | object | No | 
| disallowExternalModification | boolean | No | 
| metadata | object | No | 

### Sample Request
<a name="acxd-context-variables-createcontextvariable-sample-request"></a>

```
await client.send(new CreateContextVariableCommand({
  name: "customer_tier",
  schema: { type: "string", isSensitive: false },
  disallowExternalModification: false,
  metadata: { path: "/crm", tags: ["segmentation"] },
}));
```

### Output
<a name="acxd-context-variables-createcontextvariable-output"></a>

```
{
  "name": "customer_tier",
  "type": "string",
  "schema": {
    "type": "string",
    "isSensitive": false
  },
  "disallowExternalModification": false,
  "metadata": { "path": "/crm", "tags": ["segmentation"] }
}
```

### Errors
<a name="acxd-context-variables-createcontextvariable-errors"></a>
+ `ValidationException` (400)
+ `ConflictException` (409)
+ `InternalServerException` (500)

## UpdateContextVariable
<a name="acxd-context-variables-updatecontextvariable"></a>

Updates an existing context variable.

### Sample Request
<a name="acxd-context-variables-updatecontextvariable-sample-request"></a>

```
await client.send(new UpdateContextVariableCommand({
  contextVariableIdentifier: "customer_tier",
  schema: { type: "string", isSensitive: true },
  disallowExternalModification: true,
  metadata: { path: "/crm", tags: ["segmentation"] },
}));
```

### Input
<a name="acxd-context-variables-updatecontextvariable-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| contextVariableIdentifier | string | Yes | 
| schema | object | No | 
| disallowExternalModification | boolean | No | 
| metadata | object | No | 

### Output
<a name="acxd-context-variables-updatecontextvariable-output"></a>

```
{
  "name": "customer_tier",
  "type": "string",
  "schema": { "type": "string", "isSensitive": true },
  "disallowExternalModification": true,
  "metadata": { "path": "/crm", "tags": ["segmentation"] }
}
```

### Errors
<a name="acxd-context-variables-updatecontextvariable-errors"></a>
+ `ResourceNotFoundException` (404)
+ `ValidationException` (400)
+ `InternalServerException` (500)

## DeleteContextVariable
<a name="acxd-context-variables-deletecontextvariable"></a>

Deletes a context variable by name.

### Input
<a name="acxd-context-variables-deletecontextvariable-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| contextVariableIdentifier | string | Yes | 

### Sample Request
<a name="acxd-context-variables-deletecontextvariable-sample-request"></a>

```
await client.send(new DeleteContextVariableCommand({
  contextVariableIdentifier: "customer_tier",
}));
```

### Output
<a name="acxd-context-variables-deletecontextvariable-output"></a>

No response body.

### Errors
<a name="acxd-context-variables-deletecontextvariable-errors"></a>
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## Request Parameters
<a name="acxd-context-variables-request-parameters"></a>

### name
<a name="acxd-context-variables-request-parameters-name"></a>

Type: String

The variable name. Letters and underscores only, cannot start with `nlx_context`. Max 64 characters.

### contextVariableIdentifier
<a name="acxd-context-variables-request-parameters-contextvariableidentifier"></a>

Type: String

The context variable name used in Update and Delete operations.

### type
<a name="acxd-context-variables-request-parameters-type"></a>

Type: String

The data type of the variable. One of: `text`, `string`, `number`, `boolean`.

### schema
<a name="acxd-context-variables-request-parameters-schema"></a>

Type: Object

A JSON Schema object defining the variable's structure and validation rules. Must be an object with at least one of: `type`, `$ref`, or `anyOf` at the top level. If omitted, a default schema is used.

Examples:

Simple string:

```
{ "type": "string" }
```

Number with constraints:

```
{ "type": "number", "minimum": 0, "maximum": 100 }
```

Object with properties:

```
{
  "type": "object",
  "properties": {
    "tier": { "type": "string" },
    "score": { "type": "number" }
  }
}
```

Union type:

```
{
  "anyOf": [
    { "type": "string" },
    { "type": "number" }
  ]
}
```

### disallowExternalModification
<a name="acxd-context-variables-request-parameters-disallowexternalmodification"></a>

Type: Boolean

If true, the variable cannot be modified by external systems during a conversation. Only flows can update it.

### metadata
<a name="acxd-context-variables-request-parameters-metadata"></a>

Type: Object

Organizational metadata. See Common Types.

### createdAt
<a name="acxd-context-variables-request-parameters-createdat"></a>

Type: String

When the variable was created (ISO 8601).

### updatedAt
<a name="acxd-context-variables-request-parameters-updatedat"></a>

Type: String

When the variable was last modified (ISO 8601).

### updatedBy
<a name="acxd-context-variables-request-parameters-updatedby"></a>

Type: String

The identity of who last modified the variable.