# Data Source Permissions API

Use the Data Source Permissions API to enable, disable, list, add, and remove
permissions for data sources.

You can set permissions for a user or a team. Permissions can't be set for Admins,
because they always have access to everything.

The permission levels for the permission field are as follows:

- 1 = Query

###### Note

To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid Grafana
API token. You include this in the `Authorization` field in the API
request. For information about how to create a token to authenticate your API calls,
see [Authenticate with tokens](authenticating-grafana-apis.md "authenticating-grafana-apis.md").

## Enable permissions for a

data source

```
POST /api/datasources/:id/enable-permissions
```

Enables permissions for the data source with the given id. No one except Org
Admins are able to query the data source until permissions have been added to permit
certain users or teams to query the data source.

**Example request**

```
POST /api/datasources/1/enable-permissions
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

```

**Example response**

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Content-Length: 35

{"message":"Datasource permissions enabled"}
```

Status Codes:

- **200**— Created
- **400**— Permissions can't be enabled,
  see the response body for details.
- **401**— Unauthorized
- **403**— Access denied
- **404**— Data source not found

## Disable permissions for

a data source

```
POST /api/datasources/:id/disable-permissions
```

Disables permissions for the data source with the given id. All existing
permissions are removed and anyone is able to query the data source.

**Example request**

```
POST /api/datasources/1/disable-permissions
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{}
```

**Example response**

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Content-Length: 35

{"message":"Datasource permissions disabled"}
```

Status Codes:

- **200**— Ok
- **400**— Permissions can't be
  disabled, see the response body for details.
- **401**— Unauthorized
- **403**— Access denied
- **404**— Data source not found

## Get permissions for a data

source

```
GET /api/datasources/:id/permissions
```

Gets all existing permissions for the data source with the given
`id`.

**Example request**

```
GET /api/datasources/1/permissions HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Content-Length: 551

{
  "datasourceId": 1,
  "enabled": true,
  "permissions":
  [
    {
      "id": 1,
      "datasourceId": 1,
      "userId": 1,
      "userLogin": "user",
      "userEmail": "user@test.com",
      "userAvatarUrl": "/avatar/46d229b033af06a191ff2267bca9ae",
      "permission": 1,
      "permissionName": "Query",
      "created": "2017-06-20T02:00:00+02:00",
      "updated": "2017-06-20T02:00:00+02:00",
    },
    {
      "id": 2,
      "datasourceId": 1,
      "teamId": 1,
      "team": "A Team",
      "teamAvatarUrl": "/avatar/46d229b033af06a191ff2267bca9ae",
      "permission": 1,
      "permissionName": "Query",
      "created": "2017-06-20T02:00:00+02:00",
      "updated": "2017-06-20T02:00:00+02:00",
    }
  ]
}
```

Status Codes:

- **200**— Ok
- **401**— Unauthorized
- **403**— Access denied
- **404**— Data source not found

## Add permission for a data

source

```
POST /api/datasources/:id/permissions
```

Adds a user permission for the data source with the given `id`.

**Example request to add user permission**

```
POST /api/datasources/1/permissions
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "userId": 1,
  "permission": 1
}
```

**Example response for adding a user
permission**

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Content-Length: 35

{"message":"Datasource permission added"}
```

**Example request to add team permission**

```
POST /api/datasources/1/permissions
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "teamId": 1,
  "permission": 1
}
```

**Example response for adding a team
permission**

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Content-Length: 35

{"message":"Datasource permission added"}
```

Status Codes:

- **200**— Ok
- **400**— Permission can't be added,
  see response body for details.
- **401**— Unauthorized
- **403**— Access denied
- **404**— Data source not found

## Remove permission for a

data source

```
DELETE /api/datasources/:id/permissions/:permissionId
```

Removes the permission with the given permissionId for the data source with the
given `id`.

**Example request**

```
DELETE /api/datasources/1/permissions/2
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Content-Length: 35

{"message":"Datasource permission removed"}
```

Status Codes:

- **200**— Ok
- **401**— Unauthorized
- **403**— Access denied
- **404**— Data source not found or
  permission not found
