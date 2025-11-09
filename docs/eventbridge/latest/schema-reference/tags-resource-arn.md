# Tag

A tag is a key-value pair associated with a resource. You can use these metadata
tags to identify the purpose of a broker or configuration.

## URI

`/tags/`resource-arn``

## HTTP methods

### GET

**Operation ID:** `ListTagsForResource`

Get tags for resource.

| Path parameters | Name   | Type | Required                 | Description |
| --------------- | ------ | ---- | ------------------------ | ----------- |
| `resource-arn`  | String | True | The ARN of the resource. |

| Responses | Status code                 | Response model | Description |
| --------- | --------------------------- | -------------- | ----------- |
| `200`     | `ListTagsForResourceOutput` | 200 response   |
| `400`     | `ErrorOutput`               | 400 response   |
| `403`     | `ErrorOutput`               | 403 response   |
| `404`     | `ErrorOutput`               | 404 response   |
| `500`     | `ErrorOutput`               | 500 response   |

### POST

**Operation ID:** `TagResource`

Add tags to a resource.

| Path parameters | Name   | Type | Required                 | Description |
| --------------- | ------ | ---- | ------------------------ | ----------- |
| `resource-arn`  | String | True | The ARN of the resource. |

| Responses | Status code   | Response model | Description |
| --------- | ------------- | -------------- | ----------- |
| `204`     | None          | 204 response   |
| `400`     | `ErrorOutput` | 400 response   |
| `403`     | `ErrorOutput` | 403 response   |
| `404`     | `ErrorOutput` | 404 response   |
| `500`     | `ErrorOutput` | 500 response   |

### DELETE

**Operation ID:** `UntagResource`

Removes tags from a resource.

| Path parameters | Name   | Type | Required                 | Description |
| --------------- | ------ | ---- | ------------------------ | ----------- |
| `resource-arn`  | String | True | The ARN of the resource. |

| Query parameters | Name   | Type | Required                 | Description |
| ---------------- | ------ | ---- | ------------------------ | ----------- |
| `tagKeys`        | String | True | Keys of key-value pairs. |

| Responses | Status code   | Response model | Description |
| --------- | ------------- | -------------- | ----------- |
| `204`     | None          | 204 response   |
| `400`     | `ErrorOutput` | 400 response   |
| `403`     | `ErrorOutput` | 403 response   |
| `404`     | `ErrorOutput` | 404 response   |
| `500`     | `ErrorOutput` | 500 response   |

### OPTIONS

| Responses | Status code | Response model | Description |
| --------- | ----------- | -------------- | ----------- |
| `200`     | None        | 200 response   |

## Schemas

### Request bodies

```
{
  "tags": {
  }
}
```

### Response bodies

```
{
  "tags": {
  }
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

### ListTagsForResourceOutput

| Property | Type                                                                  | Required | Description |
| -------- | --------------------------------------------------------------------- | -------- | ----------- |
| `tags`   | [Tags](#tags-resource-arn-model-tags "#tags-resource-arn-model-tags") | False    |             |

### TagResourceInput

| Property | Type                                                                  | Required | Description                        |
| -------- | --------------------------------------------------------------------- | -------- | ---------------------------------- |
| `tags`   | [Tags](#tags-resource-arn-model-tags "#tags-resource-arn-model-tags") | True     | Tags associated with the resource. |

### Tags

Key-value pairs associated with a resource.

| Property | Type   | Required | Description |
| -------- | ------ | -------- | ----------- |
| `*`      | string | False    |             |
