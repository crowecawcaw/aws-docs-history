# Code Binding

## URI

`/v1/registries/name/`registryName`/schemas/name/`schemaName`/language/`language``

## HTTP methods

### GET

**Operation ID:** `DescribeCodeBinding`

Describe the code binding URI.

| Path parameters | Name   | Type | Required                                                                                                                                                                                | Description |
| --------------- | ------ | ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `registryName`  | String | True | The name of the schema registry.                                                                                                                                                        |
| `schemaName`    | String | True | The name of the schema.                                                                                                                                                                 |
| `language`      | String | True | The language of the code binding. The supported languages and corresponding values are as follows:<br>• Java: Java8<br>• Python: Python36<br>• TypeScript: TypeScript3<br>• Golang: Go1 |

| Query parameters | Name   | Type  | Required                                                        | Description |
| ---------------- | ------ | ----- | --------------------------------------------------------------- | ----------- |
| `schemaVersion`  | String | False | Specifying this limits the results to only this schema version. |

| Responses | Status code         | Response model | Description |
| --------- | ------------------- | -------------- | ----------- |
| `200`     | `CodeBindingOutput` | 200 response   |
| `400`     | `ErrorOutput`       | 400 response   |
| `401`     | `ErrorOutput`       | 401 response   |
| `403`     | `ErrorOutput`       | 403 response   |
| `404`     | `ErrorOutput`       | 404 response   |
| `429`     | `ErrorOutput`       | 429 response   |
| `500`     | `ErrorOutput`       | 500 response   |

### POST

**Operation ID:** `PutCodeBinding`

Put code binding URI

| Path parameters | Name   | Type | Required                                                                                                                                                                                | Description |
| --------------- | ------ | ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `registryName`  | String | True | The name of the schema registry.                                                                                                                                                        |
| `schemaName`    | String | True | The name of the schema.                                                                                                                                                                 |
| `language`      | String | True | The language of the code binding. The supported languages and corresponding values are as follows:<br>• Java: Java8<br>• Python: Python36<br>• TypeScript: TypeScript3<br>• Golang: Go1 |

| Query parameters | Name   | Type  | Required                                                        | Description |
| ---------------- | ------ | ----- | --------------------------------------------------------------- | ----------- |
| `schemaVersion`  | String | False | Specifying this limits the results to only this schema version. |

| Responses | Status code         | Response model | Description |
| --------- | ------------------- | -------------- | ----------- |
| `202`     | `CodeBindingOutput` | 202 response   |
| `400`     | `ErrorOutput`       | 400 response   |
| `401`     | `ErrorOutput`       | 401 response   |
| `403`     | `ErrorOutput`       | 403 response   |
| `404`     | `ErrorOutput`       | 404 response   |
| `410`     | `ErrorOutput`       | 410 response   |
| `429`     | `ErrorOutput`       | 429 response   |
| `500`     | `ErrorOutput`       | 500 response   |

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
{
  "Status": enum,
  "LastModified": "string",
  "CreationDate": "string",
  "SchemaVersion": "string"
}
```

```
{
  "Message": "string",
  "Code": "string"
}
```

## Properties

### CodeBindingOutput

| Property        | Type                                                                                                                                                                                                                                  | Required | Description                                          |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---------------------------------------------------- |
| `CreationDate`  | stringFormat: date-time                                                                                                                                                                                                               | False    | The time and date that the code binding was created. |
| `LastModified`  | stringFormat: date-time                                                                                                                                                                                                               | False    | The date and time that code bindings were modified.  |
| `SchemaVersion` | string                                                                                                                                                                                                                                | False    | The version number of the schema.                    |
| `Status`        | [CodeGenerationStatus](#v1-registries-name-registryname-schemas-name-schemaname-language-language-model-codegenerationstatus "#v1-registries-name-registryname-schemas-name-schemaname-language-language-model-codegenerationstatus") | False    | The current status of code binding generation.       |

### CodeGenerationStatus

- `CREATE_IN_PROGRESS`
- `CREATE_COMPLETE`
- `CREATE_FAILED`

### ErrorOutput

| Property  | Type   | Required | Description                             |
| --------- | ------ | -------- | --------------------------------------- |
| `Code`    | string | True     | The error code.                         |
| `Message` | string | True     | The message string of the error output. |
