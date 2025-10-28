# Dashboard Permissions API

Use the Dashboard Permissions API to update or retrieve the permissions for a
dashboard.

Permissions with `dashboardId=-1` are the default permissions for users
with the Viewer and Editor roles. Permissions can be set for a user, a team or a role
(Viewer or Editor). Permissions cannot be set for Admins - they always have access to
everything.

The permission levels for the `permission` field are as follows:

- 1 = View
- 2 = Edit
- 4 = Admin

###### Note

To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid Grafana
API token. You include this in the `Authorization` field in the API
request. For information about how to create a token to authenticate your API calls,
see [Authenticate with tokens](authenticating-grafana-apis.md "authenticating-grafana-apis.md").

## Get permissions for a

dashboard

```
GET /api/dashboards/id/:dashboardId/permissions
```

Gets all existing permissions for the dashboard with the given
`dashboardId`.

**Example request**

```
GET /api/dashboards/id/1/permissions HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Content-Length: 551

[
  {
    "id": 1,
    "dashboardId": -1,
    "created": "2017-06-20T02:00:00+02:00",
    "updated": "2017-06-20T02:00:00+02:00",
    "userId": 0,
    "userLogin": "",
    "userEmail": "",
    "teamId": 0,
    "team": "",
    "role": "Viewer",
    "permission": 1,
    "permissionName": "View",
    "uid": "",
    "title": "",
    "slug": "",
    "isFolder": false,
    "url": ""
  },
  {
    "id": 2,
    "dashboardId": -1,
    "created": "2017-06-20T02:00:00+02:00",
    "updated": "2017-06-20T02:00:00+02:00",
    "userId": 0,
    "userLogin": "",
    "userEmail": "",
    "teamId": 0,
    "team": "",
    "role": "Editor",
    "permission": 2,
    "permissionName": "Edit",
    "uid": "",
    "title": "",
    "slug": "",
    "isFolder": false,
    "url": ""
  }
]
```

Status Codes:

- **200**— OK
- **401**— Unauthorized
- **403**— Access denied
- **404**— Dashboard not found

## Update permissions for a

dashboard

```
POST /api/dashboards/id/:dashboardId/permissions
```

Updates the permissions for a dashboard. This operation removes existing
permissions if they are not included in the request.

**Example request**

```
POST /api/dashboards/id/1/permissions
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "items": [
    {
      "role": "Viewer",
      "permission": 1
    },
    {
      "role": "Editor",
      "permission": 2
    },
    {
      "teamId": 1,
      "permission": 1
    },
    {
      "userId": 11,
      "permission": 4
    }
  ]
}
```

JSON body schema:

- **items**— The permission items to add
  or update. Existing items that are omitted from the list are removed.

**Example response**

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Content-Length: 35

{"message":"Dashboard permissions updated"}
```

Status Codes:

- **200**— Created
- **401**— Unauthorized
- **403**— Access denied
- **404**— Dashboard not found
