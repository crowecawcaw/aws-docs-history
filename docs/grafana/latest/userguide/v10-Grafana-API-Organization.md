

# Organization API
<a name="v10-Grafana-API-Organization"></a>

Use the Organization API to work with organizations in an Amazon Managed Grafana workspace.

**Note**  
To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid service account token. You include this in the `Authorization` field in the API request.

## Get current organization
<a name="v10-Grafana-API-Organization-getcurrent"></a>

```
GET /api/org/
```

**Example request**

```
GET /api/org/ HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "id":1,
  "name":"Main Org."
}
```

## Get all users within the current organization
<a name="v10-Grafana-API-Organization-getusers"></a>

```
GET /api/org/users
```

Required permissions: the `org.users:read` action with the scope `users:*`

**Example request**

```
GET /api/org/users HTTP/1.1
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
    "orgId": 1,
    "userId": 1,
    "email": "admin@localhost",
    "avatarUrl": "/avatar/46d229b033af06a191ff2267bca9ae",
    "login": "admin",
    "role": "Admin",
    "lastSeenAt": "2019-08-09T11:02:49+02:00",
    "lastSeenAtAge": "< 1m"
  }
]
```

## Get all users within the current organization (lookup)
<a name="v10-Grafana-API-Organization-getuserslookup"></a>

```
GET /api/org/users/lookup
```

Returns all users within the current organization, but with less detailed information. Accessible to users with org admin role, admin in any folder or admin of any team. Used mostly by the Grafana UI to provide a list of users when adding team members and when e diting folder/dashboard permissions.

**Example request**

```
GET /api/org/users/lookup HTTP/1.1
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
    "userId": 1,
    "login": "admin",
    "avatarUrl": "/avatar/46d229b033af06a191ff2267bca9ae"
  }
]
```

## Updates the given user
<a name="v10-Grafana-API-Organization-updateuser"></a>

```
PATCH /api/org/users/:userId
```

Required permissions: the `org.users.role:update` action with the scope `users:*`

**Example request**

```
PATCH /api/org/users/1 HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "role": "Viewer",
}
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{"message":"Organization user updated"}
```

## Deletes user in current organization
<a name="v10-Grafana-API-Organization-deleteuser"></a>

```
DELETE /api/org/users/:userId
```

Required permissions: the `org.users:remove` action with the scope `users:*`

**Example request**

```
DELETE /api/org/users/1 HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{"message":"User removed from organization"}
```

## Update the current organization
<a name="v10-Grafana-API-Organization-update"></a>

```
PUT /api/org
```

**Example request**

```
PUT /api/org HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "name":"Main Org."
}
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{"message":"Organization updated"}
```

## Add user to the current organization
<a name="v10-Grafana-API-Organization-adduser"></a>

```
POST /api/org/users
```

Required permissions: the `org.users:add` action with the scope `users:*`

**Example request**

```
POST /api/org/users HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "role": "Admin",
  "loginOrEmail": "admin"
}
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{"message":"User added to organization","userId":1}
```