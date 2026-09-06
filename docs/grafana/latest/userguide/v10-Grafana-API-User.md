

# User API
<a name="v10-Grafana-API-User"></a>

Use the User API to work with users in an Amazon Managed Grafana workspace. 

**Note**  
To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid service account token. You include this in the `Authorization` field in the API request.

## Get teams that the user is a member of
<a name="v10-Grafana-API-User-teammember"></a>

```
GET /api/user/teams
```

**Example request**

```
GET /api/user/teams HTTP/1.1
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
    "id": 1,
    "orgId": 1,
    "name": "MyTestTeam",
    "email": "",
    "avatarUrl": "\/avatar\/3f49c15916554246daa714b9bd0ee3",
    "memberCount": 1
  }
]
```

## Get list of snapshots
<a name="v10-Grafana-API-User-stardashboard"></a>

Stars the given Dashboard for the actual user.

```
POST /api/user/stars/dashboard/:dashboardId
```

**Example request**

```
POST /api/user/stars/dashboard/1 HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{"message":"Dashboard starred!"}
```

## Unstar a dashboard
<a name="v10-Grafana-API-User-unstardashboard"></a>

Deletes the starring of the given Dashboard for the actual user.

```
DELETE /api/user/stars/dashboard/:dashboardId
```

**Example request**

```
DELETE /api/user/stars/dashboard/1 HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{"message":"Dashboard unstarred"}
```

## Get auth tokens of the actual user
<a name="v10-Grafana-API-User-authtokens"></a>

```
GET /api/user/auth-tokens
```

**Example request**

```
GET /api/user/auth-tokens HTTP/1.1
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
    "id": 361,
    "isActive": true,
    "clientIp": "127.0.0.1",
    "browser": "Chrome",
    "browserVersion": "72.0",
    "os": "Linux",
    "osVersion": "",
    "device": "Other",
    "createdAt": "2019-03-05T21:22:54+01:00",
    "seenAt": "2019-03-06T19:41:06+01:00"
  },
  {
    "id": 364,
    "isActive": false,
    "clientIp": "127.0.0.1",
    "browser": "Mobile Safari",
    "browserVersion": "11.0",
    "os": "iOS",
    "osVersion": "11.0",
    "device": "iPhone",
    "createdAt": "2019-03-06T19:41:19+01:00",
    "seenAt": "2019-03-06T19:41:21+01:00"
  }
]
```

## Revoke an auth token of the actual user
<a name="v10-Grafana-API-User-authtokens-revoke"></a>

```
POST /api/user/revoke-auth-token
```

Revokes the given auth token (device) for the actual user. User of issued auth token (device) are no longer logged in and are required to authenticate again at their next activity.

**Example request**

```
POST /api/user/revoke-auth-token HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "authTokenId": 364
}
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "message": "User auth token revoked"
}
```