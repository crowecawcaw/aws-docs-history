# Stop Discoverer

## URI

`/v1/discoverers/id/`discovererId`/stop`

## HTTP methods

### POST

**Operation ID:** `StopDiscoverer`

Stops the discoverer

| Path parameters | Name   | Type | Required                  | Description |
| --------------- | ------ | ---- | ------------------------- | ----------- |
| `discovererId`  | String | True | The ID of the discoverer. |

| Responses | Status code             | Response model | Description |
| --------- | ----------------------- | -------------- | ----------- |
| `200`     | `DiscovererStateOutput` | 200 response   |
| `400`     | `ErrorOutput`           | 400 response   |
| `401`     | `ErrorOutput`           | 401 response   |
| `403`     | `ErrorOutput`           | 403 response   |
| `404`     | `ErrorOutput`           | 404 response   |
| `500`     | `ErrorOutput`           | 500 response   |
| `503`     | `ErrorOutput`           | 503 response   |

### OPTIONS

| Path parameters | Name   | Type | Required                  | Description |
| --------------- | ------ | ---- | ------------------------- | ----------- |
| `discovererId`  | String | True | The ID of the discoverer. |

| Responses | Status code | Response model | Description |
| --------- | ----------- | -------------- | ----------- |
| `200`     | None        | 200 response   |

## Schemas

### Response bodies

```
{
  "DiscovererId": "string",
  "State": enum
}
```

```
{
  "Message": "string",
  "Code": "string"
}
```

## Properties

### DiscovererState

- `STARTED`
- `STOPPED`

### DiscovererStateOutput

| Property       | Type                                                                                                                                       | Required | Description                  |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | -------- | ---------------------------- |
| `DiscovererId` | string                                                                                                                                     | False    | The ID of the discoverer.    |
| `State`        | [DiscovererState](#v1-discoverers-id-discovererid-stop-model-discovererstate "#v1-discoverers-id-discovererid-stop-model-discovererstate") | False    | The state of the discoverer. |

### ErrorOutput

| Property  | Type   | Required | Description                             |
| --------- | ------ | -------- | --------------------------------------- |
| `Code`    | string | True     | The error code.                         |
| `Message` | string | True     | The message string of the error output. |
