# Alerting API

###### Note

This section only applies to classic alerting. For more information, see [Grafana alerting](alerts-overview.md "alerts-overview.md").

Use the Preferences API to get information about classic dashboard alerts and their
states. However, you can't use this API to modify the alert. To create new alerts or
modify them you need to update the dashboard JSON that contains the alerts.

###### Note

To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid Grafana
API token. You include this in the `Authorization` field in the API
request. For information about how to create a token to authenticate your API calls,
see [Authenticate with tokens](authenticating-grafana-apis.md "authenticating-grafana-apis.md").

## Get alerts

```
GET /api/alerts
```

**Example request**

```
GET /api/alerts HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Querystring parameters:**

These parameters are used as querystring parameters. For example:
`/api/alerts?dashboardId=1`

- **dashboardId**— Limit the responses
  to alerts in the specified dashboards value. You can specify multiple
  dashboards. For example,
  `dashboardId=23&dashboardId=35`
- **panelId**— Limit the response to
  alert for a specified panel on a dashboard.
- **query**— Limit the response to
  alerts having a name like this value.
- **state**— Return the alerts that have
  one ore more of the following alert states: `ALL`,
  `alerting`, `ok`, `no_data`,
  `paused`, or `pending`. To specify multiple
  states, use the following format:
  `?state=paused&state=alerting`
- **limit**— Limit the response to X
  number of alerts.
- **folderId**— Limit the response to
  alerts of dashboards in the specified folders. You can specify multiple
  folders. For example, `folderId=23&folderId=35`
- **dashboardQuery**— Limit the
  responses to alerts having a dashboard name like this value.
- **dashboardTag**— Limit the response
  alerts of dashboards with specified tags. To do "AND" filtering with
  multiple tags, specify the tags parameter multiple times. For example,
  `dashboardTag=tag1&dashboardTag=tag2`. Note that these
  are Grafana tags, not AWS tags.

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

[
  {
    "id": 1,
    "dashboardId": 1,
    "dashboardUId": "ABcdEFghij"
    "dashboardSlug": "sensors",
    "panelId": 1,
    "name": "fire place sensor",
    "state": "alerting",
    "newStateDate": "2018-05-14T05:55:20+02:00",
    "evalDate": "0001-01-01T00:00:00Z",
    "evalData": null,
    "executionError": "",
    "url": "http://grafana.com/dashboard/db/sensors"
  }
]
```

## Get alert by Id

```
GET /api/alerts/:id
```

**Example request**

```
GET /api/alerts/1 HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "id": 1,
  "dashboardId": 1,
  "dashboardUId": "ABcdEFghij"
  "dashboardSlug": "sensors",
  "panelId": 1,
  "name": "fire place sensor",
  "state": "alerting",
  "message": "Someone is trying to break in through the fire place",
  "newStateDate": "2018-05-14T05:55:20+02:00",
  "evalDate": "0001-01-01T00:00:00Z",
  "evalData": "evalMatches": [
    {
      "metric": "movement",
      "tags": {
        "name": "fireplace_chimney"
      },
      "value": 98.765
    }
  ],
  "executionError": "",
  "url": "http://grafana.com/dashboard/db/sensors"
}
```

###### Important

`evalMatches` data is cached in the database when and only when the
state of the alert changes. If data from one server triggers the alert first
and, before that server is seen leaving the alerting state, a second server also
enters a state that would trigger the alert, the second server is not visible in
the `evalMatches` data.

## Pause alert by Id

```
POST /api/alerts/:id/pause
```

**Example request**

```
POST /api/alerts/1/pause HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "paused": true
}

```

The `:id` query parameter is the Id of the alert to be paused or
unpaused. `paused` can be `true` to pause an alert or
`false` to unpause the alert.

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "alertId": 1,
  "state":   "Paused",
  "message": "alert paused"
}
```
