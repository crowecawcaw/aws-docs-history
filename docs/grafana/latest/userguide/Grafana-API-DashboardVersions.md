# Dashboard Versions API

Use the Dashboard Versions API to retrieve dashboard versions and restore a dashboard
to a specified version.

###### Note

To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid Grafana
API token. You include this in the `Authorization` field in the API
request. For information about how to create a token to authenticate your API calls,
see [Authenticate with tokens](authenticating-grafana-apis.md "authenticating-grafana-apis.md").

## Get all dashboard

versions

```
GET /api/dashboards/id/:dashboardId/versions
```

Gets all existing dashboard versions for the dashboard with the given
`dashboardId`.

Query parameters:

- **limit**— Maximum number of results
  to return.
- **start**— Version to start from when
  returning queries.

**Example request**

```
GET /api/dashboards/id/1/versions?limit=2?start=0 HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Content-Length: 428

[
  {
    "id": 2,
    "dashboardId": 1,
    "parentVersion": 1,
    "restoredFrom": 0,
    "version": 2,
    "created": "2017-06-08T17:24:33-04:00",
    "createdBy": "admin",
    "message": "Updated panel title"
  },
  {
    "id": 1,
    "dashboardId": 1,
    "parentVersion": 0,
    "restoredFrom": 0,
    "version": 1,
    "created": "2017-06-08T17:23:33-04:00",
    "createdBy": "admin",
    "message": "Initial save"
  }
]
```

Status Codes:

- **200**— OK
- **400**— Errors
- **401**— Unauthorized
- **404**— Dashboard version not
  found

## Get dashboard version

```
GET /api/dashboards/id/:dashboardId/versions/:id
```

Get the dashboard version with the given id, for the dashboard with the given
`dashboardId`.

**Example request**

```
GET /api/dashboards/id/1/versions/1 HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Content-Length: 1300

{
  "id": 1,
  "dashboardId": 1,
  "parentVersion": 0,
  "restoredFrom": 0,
  "version": 1,
  "created": "2017-04-26T17:18:38-04:00",
  "message": "Initial save",
  "data": {
    "annotations": {
      "list": [

      ]
    },
    "editable": true,
    "gnetId": null,
    "graphTooltip": 0,
    "hideControls": false,
    "id": 1,
    "links": [

    ],
    "rows": [
      {
        "collapse": false,
        "height": "250px",
        "panels": [

        ],
        "repeat": null,
        "repeatIteration": null,
        "repeatRowId": null,
        "showTitle": false,
        "title": "Dashboard Row",
        "titleSize": "h6"
      }
    ],
    "schemaVersion": 14,
    "style": "dark",
    "tags": [

    ],
    "templating": {
      "list": [

      ]
    },
    "time": {
      "from": "now-6h",
      "to": "now"
    },
    "timepicker": {
      "refresh_intervals": [
        "5s",
        "10s",
        "30s",
        "1m",
        "5m",
        "15m",
        "30m",
        "1h",
        "2h",
        "1d"
      ],
      "time_options": [
        "5m",
        "15m",
        "1h",
        "6h",
        "12h",
        "24h",
        "2d",
        "7d",
        "30d"
      ]
    },
    "timezone": "browser",
    "title": "test",
    "version": 1
  },
  "createdBy": "admin"
}
```

Status Codes:

- **200**— OK
- **401**— Unauthorized
- **404**— Dashboard version not
  found

## Restore dashboard

```
POST /api/dashboards/id/:dashboardId/restore
```

Restores a dashboard to the dashboard version that you specify.

**Example request**

```
POST /api/dashboards/id/1/restore
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "version": 1
}
```

JSON body schema:

- **version**— The dashboard version to
  restore to.

**Example response**

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Content-Length: 67

{
  "slug": "my-dashboard",
  "status": "success",
  "version": 3
}
```

JSON response body schema:

- **slug**— The URL-friendly slug of the
  dashboard's title.
- **status**— Whether the restore was
  successful or not.
- **version**— The new dashboard version
  following the restore.

Status Codes:

- **200**— Created
- **401**— Unauthorized
- **404**— Dashboard or dashboard
  version not found
- **500**— Internal server error
  (indicates issue retrieving dashboard tags from database)

Example error response:

```
HTTP/1.1 404 Not Found
Content-Type: application/json; charset=UTF-8
Content-Length: 46

{
  "message": "Dashboard version not found"
}
```

JSON response body schema:

- **message**— A message explaining the
  reason for the failure.

## Compare dashboard

versions

```
POST /api/dashboards/calculate-diff
```

Compares two dashboard versions by calculating the JSON diff of them.

**Example request**

```
POST /api/dashboards/calculate-diff HTTP/1.1
Accept: text/html
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "base": {
    "dashboardId": 1,
    "version": 1
  },
  "new": {
    "dashboardId": 1,
    "version": 2
  },
  "diffType": "json"
}
```

JSON body schema:

- **base**— An object representing the
  base dashboard version.
- **new**— An object representing the
  new dashboard version.
- **difftype**— The type of diff to
  return. Valid values are `json` and `basic`.

Example response (JSON diff)

```
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8

<p id="l1" class="diff-line diff-json-same">
  <!-- Diff omitted -->
</p>
```

The response is a textual representation of the diff, with the dashboard values
being in JSON, similar to the diffs seen on sites like GitHub or GitLab.

Status Codes:

- **200**— OK
- **200**— Bad request, invalid JSON
  sent
- **401**— Unauthorized
- **404**— Not found

Example response (Basic diff)

```
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8

<div class="diff-group">
  <!-- Diff omitted -->
</div>
```

The response is a summary of the changes, derived from the diff between the two
JSON objects.

Status Codes:

- **200**— OK
- **200**— Bad request, invalid JSON
  sent
- **401**— Unauthorized
- **404**— Not found
