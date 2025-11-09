# Discover

Allows you get the discovered schemas that have been inferred from events on an
event bus.

###### Note

Discoverer will only infer events that are nested up to 255 levels. Any events past 255 levels are ignored.

## URI

`/v1/discover`

## HTTP methods

### POST

**Operation ID:** `GetDiscoveredSchema`

Get the discovered schema that was generated based on sampled events.

| Responses | Status code                 | Response model | Description |
| --------- | --------------------------- | -------------- | ----------- |
| `200`     | `GetDiscoveredSchemaOutput` | 200 response   |
| `400`     | `ErrorOutput`               | 400 response   |
| `401`     | `ErrorOutput`               | 401 response   |
| `403`     | `ErrorOutput`               | 403 response   |
| `500`     | `ErrorOutput`               | 500 response   |
| `503`     | `ErrorOutput`               | 503 response   |

### OPTIONS

| Responses | Status code | Response model | Description |
| --------- | ----------- | -------------- | ----------- |
| `200`     | None        | 200 response   |

## Schemas

### Request bodies

```
{
  "Type": enum,
  "Events": [
    "string"
  ]
}
```

### Response bodies

```
{
  "Content": "string"
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

### GetDiscoveredSchemaInput

| Property | Type                                                      | Required | Description                                                                                                                                                                                             |
| -------- | --------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Events` | Array of type string                                      | True     | An array of strings where each string is a JSON event. These are the events that<br>were used to generate the schema. The array includes a single type of event and has a<br>maximum size of 10 events. |
| `Type`   | [Type](#v1-discover-model-type "#v1-discover-model-type") | True     | The type of event.                                                                                                                                                                                      |

### GetDiscoveredSchemaOutput

| Property  | Type   | Required | Description                          |
| --------- | ------ | -------- | ------------------------------------ |
| `Content` | string | False    | The source of the schema definition. |

### Type

The type of schema to export.

- `OpenApi3`
- `JSONSchemaDraft4`
