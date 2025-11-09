# Get Code Binding Source

## URI

`/v1/registries/name/`registryName`/schemas/name/`schemaName`/language/`language`/source`

## HTTP methods

### GET

**Operation ID:** `GetCodeBindingSource`

Get the code binding source URI.

| Path parameters | Name   | Type | Required                                                                                                                                                                                | Description |
| --------------- | ------ | ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `registryName`  | String | True | The name of the schema registry.                                                                                                                                                        |
| `schemaName`    | String | True | The name of the schema.                                                                                                                                                                 |
| `language`      | String | True | The language of the code binding. The supported languages and corresponding values are as follows:<br>• Java: Java8<br>• Python: Python36<br>• TypeScript: TypeScript3<br>• Golang: Go1 |

| Query parameters | Name   | Type  | Required                                                        | Description |
| ---------------- | ------ | ----- | --------------------------------------------------------------- | ----------- |
| `schemaVersion`  | String | False | Specifying this limits the results to only this schema version. |

| Responses | Status code                  | Response model | Description |
| --------- | ---------------------------- | -------------- | ----------- |
| `200`     | `GetCodeBindingSourceOutput` | 200 response   |
| `400`     | `ErrorOutput`                | 400 response   |
| `401`     | `ErrorOutput`                | 401 response   |
| `403`     | `ErrorOutput`                | 403 response   |
| `404`     | `ErrorOutput`                | 404 response   |
| `429`     | `ErrorOutput`                | 429 response   |
| `500`     | `ErrorOutput`                | 500 response   |

### OPTIONS

| Path parameters | Name   | Type | Required                                                                                                                                                                                | Description |
| --------------- | ------ | ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `registryName`  | String | True | The name of the schema registry.                                                                                                                                                        |
| `schemaName`    | String | True | The name of the schema.                                                                                                                                                                 |
| `language`      | String | True | The language of the code binding. The supported languages and corresponding values are as follows:<br>• Java: Java8<br>• Python: Python36<br>• TypeScript: TypeScript3<br>• Golang: Go1 |

| Query parameters | Name   | Type  | Required                                                        | Description |
| ---------------- | ------ | ----- | --------------------------------------------------------------- | ----------- |
| `schemaVersion`  | String | False | Specifying this limits the results to only this schema version. |

| Responses | Status code | Response model | Description |
| --------- | ----------- | -------------- | ----------- |
| `200`     | None        | 200 response   |

## Schemas

### Response bodies

```
"string"
```

```
{
  "Message": "string",
  "Code": "string"
}
```

## Properties

### ErrorOutput

| Property  | Type   | Required | Description                             |
| --------- | ------ | -------- | --------------------------------------- |
| `Code`    | string | True     | The error code.                         |
| `Message` | string | True     | The message string of the error output. |
