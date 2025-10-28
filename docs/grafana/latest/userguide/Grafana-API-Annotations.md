# Annotations API

Use the Annotations API to create, update, delete, and work with annotations in the
Amazon Managed Grafana workspace.

Annotations are saved in the workspace's Grafana database (sqlite, mysql or postgres).
Annotations can be global annotations that can be shown on any dashboard by configuring
an annotation data source. Annotations are filtered by tags. Or they can be tied to a
panel on a dashboard, and displayed only on that panel.

###### Note

To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid Grafana
API token. You include this in the `Authorization` field in the API
request. For information about how to create a token to authenticate your API calls,
see [Authenticate with tokens](authenticating-grafana-apis.md "authenticating-grafana-apis.md").

## Find annotations

```
GET /api/annotations?from=1506676478816&to=1507281278816&tags=tag1&tags=tag2&limit=100
```

**Example request**

```
GET /api/annotations?from=1506676478816&to=1507281278816&tags=tag1&tags=tag2&limit=100 HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

Query parameters:

- **from**— (Optional) Epoch datetime in
  milliseconds.
- **to**— (Optional) Epoch datetime in
  milliseconds.
- **limit**— (Optional) Maximum number
  of results returned. The default is 100.
- **alertid**— (Optional) FInd
  annotations for the specified alert.
- **dashboardId**— (Optional) Find
  annotations that are scoped to the specified dashboard.
- **panelId**— (Optional) Find
  annotations that are scoped to the specified panel.
- **userId**— (Optional) Find
  annotations created by the specified user.
- **type**— (Optional) Specify to return
  alerts or user-created annotations. Value values are `alert` and
  `annotation`.
- **tags**— (Optional) Use this to
  filter global annotations. Global annotations are annotations from an
  annotation data source that are not connected specifically to a dashboard or
  panel. To do an “AND” filtering with multiple tags, specify the tags
  parameter multiple times. For example, `tags=tag1&tags=tag2`.
  These are Grafana tags, not AWS tags.

**Example response**

```
HTTP/1.1 200
Content-Type: application/json
[
    {
        "id": 1124,
        "alertId": 0,
        "dashboardId": 468,
        "panelId": 2,
        "userId": 1,
        "userName": "",
        "newState": "",
        "prevState": "",
        "time": 1507266395000,
        "timeEnd": 1507266395000,
        "text": "test",
        "metric": "",
        "tags": [
            "tag1",
            "tag2"
        ],
        "data": {}
    },
    {
        "id": 1123,
        "alertId": 0,
        "dashboardId": 468,
        "panelId": 2,
        "userId": 1,
        "userName": "",
        "newState": "",
        "prevState": "",
        "time": 1507265111000,
        "text": "test",
        "metric": "",
        "tags": [
            "tag1",
            "tag2"
        ],
        "data": {}
    }
]
```

## Create annotation

```
POST /api/annotations
```

Creates an annotation in the workspace's Grafana database. The
`dashboardId` and `panelId` fields are optional. If they
are not specified, a global annotation is created and can be queried in any
dashboard that adds the Grafana annotations data source. When creating a region
annotation, be sure to include the `timeEnd` property.

The format for `time` and `timeEnd` should be epoch numbers
in millisecond resolution.

**Example request**

```
POST /api/annotations HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "dashboardId":468,
  "panelId":1,
  "time":1507037197339,
  "timeEnd":1507180805056,
  "tags":["tag1","tag2"],
  "text":"Annotation Description"
}
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
    "message":"Annotation added",
    "id": 1,
}
```

## Create annotation in

graphite format

```
POST /api/annotations/graphite
```

Creates an annotation by using a Graphite-compatible event format. The
`when` and `data` fields are optional. If
`when` is not specified, the current time is used as annotation’s
timestamp. The `tags` field can also be in prior to Graphite 0.10.0
format (string with multiple tags being separated by a space).

**Example request**

```
POST /api/annotations/graphite HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "what": "Event - deploy",
  "tags": ["deploy", "production"],
  "when": 1467844481,
  "data": "deploy of master branch happened at Wed Jul 6 22:34:41 UTC 2016"
}
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
    "message":"Graphite annotation added",
    "id": 1
}
```

## Update annotation

```
PUT /api/annotations/:id
```

pdates all properties of an annotation that matches the specified id. To only
update certain properties, use the Patch Annotation operation.

**Example request**

```
PUT /api/annotations/1141 HTTP/1.1
Accept: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
Content-Type: application/json

{
  "time":1507037197339,
  "timeEnd":1507180805056,
  "text":"Annotation Description",
  "tags":["tag3","tag4","tag5"]
}
```

**Example response:**

```
HTTP/1.1 200
Content-Type: application/json

{
    "message":"Annotation updated"
}
```

## Patch annotation

```
PATCH /api/annotations/:id
```

Updates one or more properties of an annotation that matches the specified id.
This operation currently supports updating the `text`, `tags`,
`time`, and `timeEnd` properties.

**Example request:**

```
PATCH /api/annotations/1145 HTTP/1.1
Accept: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
Content-Type: application/json

{
   "text":"New Annotation Description",
   "tags":["tag6","tag7","tag8"]
}
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
    "message":"Annotation patched"
}
```

## Delete annotation by Id

```
DELETE /api/annotations/:id
```

Deletes the annotation that matches the specified Id.

**Example request**

```
DELETE /api/annotations/1 HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
    "message":"Annotation deleted"
}
```
