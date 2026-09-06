

# External Group Synchronization API
<a name="v10-Grafana-API-ExternalGroupSynchronization"></a>

**Note**  
To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid service account token. You include this in the `Authorization` field in the API request.

## Get external groups
<a name="v10-Grafana-API-ExternalGroupSynchronization-get"></a>

```
GET /api/teams/:teamId/groups
```

**Example request**

```
GET /api/teams/1/groups HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk]
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

[
  {
    "orgId": 1,
    "teamId": 1,
    "groupId": "cn=editors,ou=groups,dc=grafana,dc=org"
  }
]
```

Status Codes:
+ **200**— Ok
+ **401**— Unauthorized
+ **403**— Access denied

## Add external group
<a name="v10-Grafana-API-ExternalGroupSynchronization-add"></a>

```
POST /api/teams/:teamId/groups
```

**Example request**

```
POST /api/teams/1/members HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk]

{
  "groupId": "cn=editors,ou=groups,dc=grafana,dc=org"
}
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{"message":"Group added to Team"}
```

Status Codes:
+ **200**— Ok
+ **400**— Group is already added to this team
+ **401**— Unauthorized
+ **403**— Permission denied
+ **404**— Team not found

## Remove external group
<a name="v10-Grafana-API-ExternalGroupSynchronization-remove"></a>

```
DELETE /api/teams/:teamId/groups/:groupId
```

**Example request**

```
DELETE /api/teams/1/groups/cn=editors,ou=groups,dc=grafana,dc=org HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk]
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{"message":"Team Group removed"}
```

Status Codes:
+ **200**— Ok
+ **401**— Unauthorized
+ **403**— Permission denied
+ **404**— Team not found or group not found