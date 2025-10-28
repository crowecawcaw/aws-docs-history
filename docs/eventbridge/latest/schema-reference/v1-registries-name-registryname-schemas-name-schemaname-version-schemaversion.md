# Delete Schema Version

## URI

`/v1/registries/name/`registryName`/schemas/name/`schemaName`/version/`schemaVersion``

## HTTP methods

### DELETE

**Operation ID:** `DeleteSchemaVersion`

Delete the schema version definition

| Path parameters | Name          | Type         | Required                                | Description |
| --------------- | ------------- | ------------ | --------------------------------------- | ----------- | ------------- | -------------- | -------------------------------------------------------------------------------------------------------- | ---- | ---- | -------- | ----------- |
| `schemaVersion` | String        | True         | The version number of the schema        |
| `registryName`  | String        | True         | The name of the schema registry.        |
| `schemaName`    | String        | True         | The name of the schema.                 | Responses   | Status code   | Response model | Description                                                                                              |
| ---             | ---           | ---          |                                         | `204`       | None          | 204 response   |
| `400`           | `ErrorOutput` | 400 response |                                         | `401`       | `ErrorOutput` | 401 response   |
| `403`           | `ErrorOutput` | 403 response |                                         | `404`       | `ErrorOutput` | 404 response   |
| `500`           | `ErrorOutput` | 500 response |                                         | `503`       | `ErrorOutput` | 503 response   | ### OPTIONS Path parameters                                                                              | Name | Type | Required | Description |
| ---             | ---           | ---          | ---                                     |
| `schemaVersion` | String        | True         | The version number of the schema        |
| `registryName`  | String        | True         | The name of the schema registry.        |
| `schemaName`    | String        | True         | The name of the schema.                 | Responses   | Status code   | Response model | Description                                                                                              |
| ---             | ---           | ---          |                                         | `200`       | None          | 200 response   | ## Schemas ### Response bodies `{ "Message": "string", "Code": "string" }` ## Properties ### ErrorOutput |
| Property        | Type          | Required     | Description                             |
| ---             | ---           | ---          | ---                                     |
| `Code`          | string        | True         | The error code.                         |
| `Message`       | string        | True         | The message string of the error output. |
