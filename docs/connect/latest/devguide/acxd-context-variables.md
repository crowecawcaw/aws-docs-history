# Context Variables

Define typed variables available across conversations within a workspace. Context
variables can be referenced in flows and set by external systems.

###### Contents

- [ListContextVariables](#acxd-context-variables-listcontextvariables "#acxd-context-variables-listcontextvariables")
- [CreateContextVariable](#acxd-context-variables-createcontextvariable "#acxd-context-variables-createcontextvariable")
- [UpdateContextVariable](#acxd-context-variables-updatecontextvariable "#acxd-context-variables-updatecontextvariable")
- [DeleteContextVariable](#acxd-context-variables-deletecontextvariable "#acxd-context-variables-deletecontextvariable")
- [Request Parameters](#acxd-context-variables-request-parameters "#acxd-context-variables-request-parameters")

## ListContextVariables

Lists all context variables in the workspace.

### Input

No parameters.

### Sample Request

```
await client.send(new ListContextVariablesCommand({}));
```

### Output

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

- `ValidationException` (400)
- `InternalServerException` (500)

## CreateContextVariable

Creates a new context variable.

### Input

| Parameter                      | Type    | Required |
| ------------------------------ | ------- | -------- |
| `name`                         | string  | Yes      |
| `schema`                       | object  | No       |
| `disallowExternalModification` | boolean | No       |
| `metadata`                     | object  | No       |

### Sample Request

```
await client.send(new CreateContextVariableCommand({
  name: "customer_tier",
  schema: { type: "string", isSensitive: false },
  disallowExternalModification: false,
  metadata: { path: "/crm", tags: ["segmentation"] },
}));
```

### Output

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

- `ValidationException` (400)
- `ConflictException` (409)
- `InternalServerException` (500)

## UpdateContextVariable

Updates an existing context variable.

### Sample Request

```
await client.send(new UpdateContextVariableCommand({
  contextVariableIdentifier: "customer_tier",
  schema: { type: "string", isSensitive: true },
  disallowExternalModification: true,
  metadata: { path: "/crm", tags: ["segmentation"] },
}));
```

### Input

| Parameter                      | Type    | Required |
| ------------------------------ | ------- | -------- |
| `contextVariableIdentifier`    | string  | Yes      |
| `schema`                       | object  | No       |
| `disallowExternalModification` | boolean | No       |
| `metadata`                     | object  | No       |

### Output

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

- `ResourceNotFoundException` (404)
- `ValidationException` (400)
- `InternalServerException` (500)

## DeleteContextVariable

Deletes a context variable by name.

### Input

| Parameter                   | Type   | Required |
| --------------------------- | ------ | -------- |
| `contextVariableIdentifier` | string | Yes      |

### Sample Request

```
await client.send(new DeleteContextVariableCommand({
  contextVariableIdentifier: "customer_tier",
}));
```

### Output

No response body.

### Errors

- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## Request Parameters

### name

Type: String

The variable name. Letters and underscores only, cannot start with `nlx_context`.
Max 64 characters.

### contextVariableIdentifier

Type: String

The context variable name used in Update and Delete operations.

### type

Type: String

The data type of the variable. One of: `text`, `string`,
`number`, `boolean`.

### schema

Type: Object

A JSON Schema object defining the variable's structure and validation rules. Must
be an object with at least one of: `type`, `$ref`, or `anyOf`
at the top level. If omitted, a default schema is used.

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

Type: Boolean

If true, the variable cannot be modified by external systems during a conversation.
Only flows can update it.

### metadata

Type: Object

Organizational metadata. See Common Types.

### createdAt

Type: String

When the variable was created (ISO 8601).

### updatedAt

Type: String

When the variable was last modified (ISO 8601).

### updatedBy

Type: String

The identity of who last modified the variable.
