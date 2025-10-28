# Authentication API

Use the Authentication API to work with authentication keys in an Amazon Managed Grafana
workspace.

###### Note

To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid Grafana
API token. You include this in the `Authorization` field in the API
request. For information about how to create a token to authenticate your API calls,
see [Authenticate with tokens](authenticating-grafana-apis.md "authenticating-grafana-apis.md").

## Get API keys

```
GET /api/auth/keys
```

**Example request**

```
GET /api/auth/keys HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Query parameter:**

- **includeExpired**— (Optional) Boolean
  parameter that specifies whether to include expired keys in the returned
  results. The default is `false`.

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

[
  {"id": 3,"name": "API","role": "Admin"},
  {"id": 1,"name": "TestAdmin","role": "Admin","expiration": "2019-06-26T10:52:03+03:00"}
]
```

## Create API key

```
POST /api/auth/keys
```

**Example request**

```
POST /api/auth/keys HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "name": "mykey",
  "role": "Admin",
  "secondsToLive": 86400
}
```

JSON body schema:

- **name**— The name for the key.
- **role**— Sets the access level
  (Grafana role) for the key. Valid values are `Admin`,
  `Editor`, or `Viewer`.
- **secondsToLive**— Sets the amount of
  time before the key expires. It must be 2592000 (30 days) or less.

**Example response**

```
{"name":"mykey","key":"eyJrIjoiWHZiSWd3NzdCYUZnNUtibE9obUpESmE3bzJYNDRIc0UiLCJuIjoibXlrZXkiLCJpZCI6MX1=","id":1}
```

Error statuses:

- **400**— `secondsToLive` is
  greater than 2592000
- **500**— The key couldn't be stored in
  the database.

## Delete API key

```
DELETE /api/auth/keys/:id
```

**Example request**

```
DELETE /api/auth/keys/3 HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{"message":"API key deleted"}
```
