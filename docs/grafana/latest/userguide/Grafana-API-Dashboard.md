# Dashboard API

Use the Dashboard API to create, update, delete, and work with dashboards in the
Amazon Managed Grafana workspace.

The identifier (id) of a dashboard is an auto-incrementing numeric value and is only
unique per workspace. The unique identifier (uid) of a dashboard can be used to uniquely
identify a dashboard between multiple Amazon Managed Grafana workspaces. It’s automatically generated
if you don't provide one when you create a dashboard. The uid allows having consistent
URLs for accessing dashboards and when synchronizing dashboards between multiple
workspaces. The use of the uid means that changing the title of a dashboard does not
break any bookmarked links to that dashboard.

The uid can have a maximum length of 40 characters.

###### Note

To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid Grafana
API token. You include this in the `Authorization` field in the API
request. For information about how to create a token to authenticate your API calls,
see [Authenticate with tokens](authenticating-grafana-apis.md "authenticating-grafana-apis.md").

## Create/Update dashboard

```
POST /api/dashboards/db
```

Creates a new dashboard or updates an existing dashboard.

**Example request to create a new dashboard**

```
POST /api/dashboards/db HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "dashboard": {
    "id": null,
    "uid": null,
    "title": "Production Overview",
    "tags": [ "templated" ],
    "timezone": "browser",
    "schemaVersion": 16,
    "version": 0,
    "refresh": "25s"
  },
  "folderId": 0,
  "folderUid": "l3KqBxCMz",
  "message": "Made changes to xyz",
  "overwrite": false
}

```

JSON body schema:

- **dashboard**— The complete dashboard
  model. Use null to create a new dashboard.
- **dashboard.id**— Use null to create a
  new dashboard.
- **dashboard.uid**— Optional unique
  identifer when you use this to create a new dashboard. If null, a new uid is
  generated.
- **folderid**— The id of the folder to
  save the dashboard in.
- **folderUid**— The Uid of the folder
  to save the dashboard in. Overrides the value of
  `folderid`
- **overwrite**— Specify
  `true` to overwrite an existing dashboard with a newer
  version, same dashboard title in folder or same dashboard uid.
- **message**— Set a commit message for
  the version history.
- **refresh**— Set the dashboard refresh
  interval. If this is lower than the minimum refresh interval, it is ignored
  and the minimum refresh interval is used.

To add or update an alert rule for a dashboard panel, declare a
`dashboard.panels.alert` block.

**Example request to update a dashboard alert
rule**

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Content-Length: 78

{
 "dashboard":  {
        "id": 104,
        "panels": [
            {
                "alert": {
                    "alertRuleTags": {},
                    "conditions": [
                        {
                            "evaluator": {
                                "params": [
                                    25
                                ],
                                "type": "gt"
                            },
                            "operator": {
                                "type": "and"
                            },
                            "query": {
                                "params": [
                                    "A",
                                    "5m",
                                    "now"
                                ]
                            },
                            "reducer": {
                                "params": [],
                                "type": "avg"
                            },
                            "type": "query"
                        }
                    ],
                    "executionErrorState": "alerting",
                    "for": "5m",
                    "frequency": "1m",
                    "handler": 1,
                    "name": "Panel Title alert",
                    "noDataState": "no_data",
                    "notifications": []
                },
                "aliasColors": {},
                "bars": false,
                "dashLength": 10,
                "dashes": false,
                "datasource": null,
                "fieldConfig": {
                    "defaults": {
                        "custom": {}
                    },
                    "overrides": []
                },
                "fill": 1,
                "fillGradient": 0,
                "gridPos": {
                    "h": 9,
                    "w": 12,
                    "x": 0,
                    "y": 0
                },
                "hiddenSeries": false,
                "id": 2,
                "legend": {
                    "avg": false,
                    "current": false,
                    "max": false,
                    "min": false,
                    "show": true,
                    "total": false,
                    "values": false
                },
                "lines": true,
                "linewidth": 1,
                "nullPointMode": "null",
                "options": {
                    "dataLinks": []
                },
                "percentage": false,
                "pointradius": 2,
                "points": false,
                "renderer": "flot",
                "seriesOverrides": [],
                "spaceLength": 10,
                "stack": false,
                "steppedLine": false,
                "targets": [
                    {
                        "refId": "A",
                        "scenarioId": "random_walk"
                    }
                ],
                "thresholds": [
                    {
                        "colorMode": "critical",
                        "fill": true,
                        "line": true,
                        "op": "gt",
                        "value": 50
                    }
                ],
                "timeFrom": null,
                "timeRegions": [],
                "timeShift": null,
                "title": "Panel Title",
                "tooltip": {
                    "shared": true,
                    "sort": 0,
                    "value_type": "individual"
                },
                "type": "graph",
                "xaxis": {
                    "buckets": null,
                    "mode": "time",
                    "name": null,
                    "show": true,
                    "values": []
                },
                "yaxes": [
                    {
                        "format": "short",
                        "label": null,
                        "logBase": 1,
                        "max": null,
                        "min": null,
                        "show": true
                    },
                    {
                        "format": "short",
                        "label": null,
                        "logBase": 1,
                        "max": null,
                        "min": null,
                        "show": true
                    }
                ],
                "yaxis": {
                    "align": false,
                    "alignLevel": null
                }
            }
        ],
        "title": "Update alert rule via API",
        "uid": "dHEquNzGz",
        "version": 1
    }
}
```

**Example response**

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Content-Length: 78

{
  "id":      1,
  "uid":     "cIBgcSjkk",
  "url":     "/d/cIBgcSjkk/production-overview",
  "status":  "success",
  "version": 1,
  "slug":    "production-overview" //deprecated in Grafana v5.0
}

```

Status Codes:

- **200**— Created
- **400**— Error such as invalid JSON,
  invalid or missing fields
- **401**— Unauthorized
- **403**— Access denied
- **412**— Precondition failed

The **412** status code is used to explain why the dashboard
can't be created.

- The dashboard has been changed by someone else
  `status=version-mismatch`
- A dashboard with the same name in the folder already exists
  `status=name-exists`
- A dashboard with the same uid already exists
  `status=name-exists`
- The dashboard belongs to plugin `plugin title`
  `status=plugin-dashboard`

The response body has the following properties. If another dashboard has the same
title, the `status` value is `name-exists`.

```
HTTP/1.1 412 Precondition Failed
Content-Type: application/json; charset=UTF-8
Content-Length: 97

{
  "message": "The dashboard has been changed by someone else",
  "status": "version-mismatch"
}
```

## Get dashboard by uid

```
GET /api/dashboards/uid/:uid
```

Returns the dashboard matching the uid. The metadata returned might contain
information about the UID of the folder that contains the dashboard.

**Example request**

```
GET /api/dashboards/uid/cIBgcSjkk HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "dashboard": {
    "id": 1,
    "uid": "cIBgcSjkk",
    "title": "Production Overview",
    "tags": [ "templated" ],
    "timezone": "browser",
    "schemaVersion": 16,
    "version": 0
  },
  "meta": {
    "isStarred": false,
    "url": "/d/cIBgcSjkk/production-overview",
    "folderId": 2,
    "folderUid": "l3KqBxCMz",
    "slug": "production-overview" //deprecated in Grafana v5.0
  }
}
```

Status Codes:

- **200**— Found
- **401**— Unauthorized
- **403**— Access denied
- **404**— Not found

## Delete dashboard by uid

```
DELETE /api/dashboards/uid/:uid
```

Deletes the dashboard matching the uid.

**Example request**

```
DELETE /api/dashboards/uid/cIBgcSjkk HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "title": "Production Overview",
  "message": "Dashboard Production Overview deleted",
  "id": 2
}
```

Status Codes:

- **200**— Deleted
- **401**— Unauthorized
- **403**— Access denied
- **404**— Not found

## Gets the home dashboard

```
GET /api/dashboards/home
```

Returns the home dashboard.

**Example request**

```
GET /api/dashboards/home HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "dashboard": {
    "editable":false,
    "hideControls":true,
    "nav":[
      {
        "enable":false,
        "type":"timepicker"
      }
    ],
    "style":"dark",
    "tags":[],
    "templating":{
      "list":[
      ]
    },
    "time":{
    },
    "timezone":"browser",
    "title":"Home",
    "version":5
  },
  "meta":	{
    "isHome":true,
    "canSave":false,
    "canEdit":false,
    "canStar":false,
    "url":"",
    "expires":"0001-01-01T00:00:00Z",
    "created":"0001-01-01T00:00:00Z"
  }
}
```

## Get dashboard tags

```
GET /api/dashboards/tags
```

Returns all tags of dashboards.

**Example request**

```
GET /api/dashboards/tags HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

[
  {
    "term":"tag1",
    "count":1
  },
  {
    "term":"tag2",
    "count":4
  }
]
```
