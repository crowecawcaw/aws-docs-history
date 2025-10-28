# Team API

Use the Team API to work with teams in an Amazon Managed Grafana workspace. All actions in this API
require that you have the Admin role.

###### Note

To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid Grafana
API token. You include this in the `Authorization` field in the API
request. For information about how to create a token to authenticate your API calls,
see [Authenticate with tokens](authenticating-grafana-apis.md "authenticating-grafana-apis.md").

## Team search with pagination

```
GET /api/teams/search?perpage=50&page=1&query=myteam
```

or

```
GET /api/teams/search?name=myteam
```

**Example request**

```
GET /api/teams/search?perpage=10&page=1&query=myteam HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Using the query parameter**

The default value for the `perpage` parameter is 1000 and for the
`page` parameter is 1.

The `totalCount` field in the response can be used for pagination of
the teams list. For example, if `totalCount` is 100 teams and
the`perpage` parameter is set to 10, then there are 10 pages of
teams.

The `query` parameter is optional and returns results where the query
value is contained in the `name` field. Query values with spaces need to
be URL-encoded. For example, `query=my%20team`.

**Using the name parameter**

The `name` parameter returns a single team if the parameter matches the
`name` field.

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "totalCount": 1,
  "teams": [
    {
      "id": 1,
      "orgId": 1,
      "name": "MyTestTeam",
      "email": "",
      "avatarUrl": "\/avatar\/3f49c15916554246daa714b9bd0ee39",
      "memberCount": 1
    }
  ],
  "page": 1,
  "perPage": 1000
```

Status Codes:

- **200**— Created
- **401**— Unauthorized
- **403**— Permission denied
- **404**— Team not found (if searching
  by name)

## Get team by Id

```
GET /api/teams/:id
```

**Example request**

```
GET /api/teams/1 HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HHTTP/1.1 200
Content-Type: application/json

{
  "id": 1,
  "orgId": 1,
  "name": "MyTestTeam",
  "email": "",
  "created": "2017-12-15T10:40:45+01:00",
  "updated": "2017-12-15T10:40:45+01:00"
}
```

## Add a team

The `name` of the team must be unique. The `name` field is
required and the `email` and `orgId` fields are
optional.

```
POST /api/teams
```

**Example request**

```
POST /api/teams HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "name": "MyTestTeam",
  "email": "email@test.com",
  "orgId": 2
}
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{"message":"Team created","teamId":2}
```

Status Codes:

- **200**— Created
- **401**— Unauthorized
- **403**— Permission denied
- **409**— Team name already
  exists

## Update team

```
PUT /api/teams/:id
```

Only the `name` and `email` fields can be updated.

**Example request**

```
PUT /api/teams/2 HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "name": "MyTestTeam",
  "email": "email@test.com"
}
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{"message":"Team updated"}
```

Status Codes:

- **200**— Created
- **401**— Unauthorized
- **403**— Permission denied
- **404**— Team not found
- **409**— Team name already
  exists

## Delete team by Id

```
DELETE /api/teams/:id
```

**Example request**

```
DELETE /api/teams/2 HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{"message":"Team deleted"}
```

Status Codes:

- **200**— Created
- **401**— Unauthorized
- **403**— Permission denied
- **404**— Team not found

## Get team members

```
GET /api/teams/:teamId/members
```

**Example request**

```
GET /api/teams/1/members HTTP/1.1
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
    "teamId": 1,
    "userId": 3,
    "email": "user1@email.com",
    "login": "user1",
    "avatarUrl": "\/avatar\/1b3c32f6386b0185c40d359cdc733a7"
  },
  {
    "orgId": 1,
    "teamId": 1,
    "userId": 2,
    "email": "user2@email.com",
    "login": "user2",
    "avatarUrl": "\/avatar\/cad3c68da76e45d10269e8ef02f8e7"
  }
]
```

Status Codes:

- **200**— Created
- **401**— Unauthorized
- **403**— Permission denied

## Add team member

```
POST /api/teams/:teamId/members
```

**Example request**

```
POST /api/teams/1/members HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "userId": 2
}
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{"message":"Member added to Team"}
```

Status Codes:

- **200**— Created
- **400**— User is already in
  team
- **401**— Unauthorized
- **403**— Permission denied
- **404**— Team not found

## Remove member from team

```
DELETE /api/teams/:teamId/members/:userId
```

**Example request**

```
DELETE /api/teams/2/members/3 HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{"message":"Team Member removed"}
```

Status Codes:

- **200**— Created
- **401**— Unauthorized
- **403**— Permission denied
- **404**— Team not found/team member
  not found

## Get team preferences

```
GET /api/teams/:teamId/preferences
```

**Example request**

```
GET /api/teams/2/preferences HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "theme": "",
  "homeDashboardId": 0,
  "timezone": ""
}
```

## Update team preferences

```
PUT /api/teams/:teamId/preferences
```

**Example request**

```
PUT /api/teams/2/preferences HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "theme": "dark",
  "homeDashboardId": 39,
  "timezone": "utc"
}
```

JSON body schema:

- **theme**— Specify either
  `light`, `dark`, or an empty string to use the
  default theme.
- **homeDashboardId**— The numerical
  `:id` of a dashboard. The default is 0.
- **timezone**— Specify either
  `utc`, `browser`, or an empty string to use the
  default.

Omitting a parameter causes the current value to be replaced with the system
default value.

**Example response**

```
HTTP/1.1 200
Content-Type: text/plain; charset=utf-8

{
  "message":"Preferences updated"
}
```
