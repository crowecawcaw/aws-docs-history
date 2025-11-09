# Search Schemas

## URI

`/v1/registries/name/`registryName`/schemas/search`

## HTTP methods

### GET

**Operation ID:** `SearchSchemas`

Search the schemas

| Path parameters | Name   | Type | Required                         | Description |
| --------------- | ------ | ---- | -------------------------------- | ----------- |
| `registryName`  | String | True | The name of the schema registry. |

| Query parameters | Name   | Type  | Required                                                                                                                                                                                          | Description |
| ---------------- | ------ | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `keywords`       | String | True  | Specifying this limits the results to only schemas that include the provided<br>keywords.                                                                                                         |
| `limit`          | String | False | The maximum number of results to return per page.                                                                                                                                                 |
| `nextToken`      | String | False | The token that specifies the next page of results to return. To request the first<br>page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared<br>with other accounts. |

| Responses | Status code           | Response model | Description |
| --------- | --------------------- | -------------- | ----------- |
| `200`     | `SearchSchemasOutput` | 200 response   |
| `400`     | `ErrorOutput`         | 400 response   |
| `401`     | `ErrorOutput`         | 401 response   |
| `403`     | `ErrorOutput`         | 403 response   |
| `500`     | `ErrorOutput`         | 500 response   |
| `503`     | `ErrorOutput`         | 503 response   |

### OPTIONS

| Path parameters | Name   | Type | Required                         | Description |
| --------------- | ------ | ---- | -------------------------------- | ----------- |
| `registryName`  | String | True | The name of the schema registry. |

| Responses | Status code | Response model | Description |
| --------- | ----------- | -------------- | ----------- |
| `200`     | None        | 200 response   |

## Schemas

### Response bodies

```
{
  "NextToken": "string",
  "Schemas": [
    {
      "Type": "string",
      "RegistryName": "string",
      "SchemaVersions": [
        {
          "SchemaVersion": "string",
          "CreatedDate": "string"
        }
      ],
      "SchemaName": "string",
      "SchemaArn": "string"
    }
  ]
}
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

### SearchSchemaSummary

| Property         | Type                                     | Required | Description                                                                         |
| ---------------- | ---------------------------------------- | -------- | ----------------------------------------------------------------------------------- |
| `RegistryName`   | string                                   | False    | The name of the registry.                                                           |
| `SchemaArn`      | string                                   | False    | The ARN of the schema.                                                              |
| `SchemaName`     | string                                   | False    | The name of the schema.                                                             |
| `SchemaVersions` | Array of type SearchSchemaVersionSummary | False    | An array of schema version summaries.                                               |
| `Type`           | string                                   | False    | The type of schema to export.Valid types include `OpenApi3` and `JSONSchemaDraft4`. |

### SearchSchemaVersionSummary

| Property        | Type                    | Required | Description                              |
| --------------- | ----------------------- | -------- | ---------------------------------------- |
| `CreatedDate`   | stringFormat: date-time | False    | The date the schema version was created. |
| `SchemaVersion` | string                  | False    | The version number of the schema         |

### SearchSchemasOutput

| Property    | Type                              | Required | Description                                                                                                                                                                                       |
| ----------- | --------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `NextToken` | string                            | False    | The token that specifies the next page of results to return. To request the first<br>page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared<br>with other accounts. |
| `Schemas`   | Array of type SearchSchemaSummary | False    | An array of `SearchSchemaSummary` information.                                                                                                                                                    |
