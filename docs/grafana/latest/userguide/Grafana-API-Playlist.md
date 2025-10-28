# Playlist API

Use the Playlist API to work with playlists in the Amazon Managed Grafana workspace.

###### Note

To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid Grafana
API token. You include this in the `Authorization` field in the API
request. For information about how to create a token to authenticate your API calls,
see [Authenticate with tokens](authenticating-grafana-apis.md "authenticating-grafana-apis.md").

## Search playlist

```
GET /api/playlists
```

Returns all playlists for the current Amazon Managed Grafana workspace, using
pagination.

**Example request**

```
GET /api/playlists HTTP/1.1
Accept: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

Querystring parameters:

- **query**— Limit the responses to
  playlists that have a name like this value.
- **limit**— Limit the response to X
  number of playlists.

**Example response**

```
HTTP/1.1 200
Content-Type: application/json
[
  {
    "id": 1,
    "name": "my playlist",
    "interval": "5m"
  }
]
```

## Get one playlist

```
GET /api/playlists/:id
```

**Example request**

```
GET /api/playlists/1 HTTP/1.1
Accept: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json
{
  "id" : 1,
  "name": "my playlist",
  "interval": "5m",
  "orgId": "my org",
  "items": [
    {
      "id": 1,
      "playlistId": 1,
      "type": "dashboard_by_id",
      "value": "3",
      "order": 1,
      "title":"my third dashboard"
    },
    {
      "id": 2,
      "playlistId": 1,
      "type": "dashboard_by_tag",
      "value": "myTag",
      "order": 2,
      "title":"my other dashboard"
    }
  ]
}
```

## Get playlist items

```
GET /api/playlists/:id/items
```

**Example request**

```
GET /api/playlists/1/items HTTP/1.1
Accept: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json
[
  {
    "id": 1,
    "playlistId": 1,
    "type": "dashboard_by_id",
    "value": "3",
    "order": 1,
    "title":"my third dashboard"
  },
  {
    "id": 2,
    "playlistId": 1,
    "type": "dashboard_by_tag",
    "value": "myTag",
    "order": 2,
    "title":"my other dashboard"
  }
]
```

## Get playlist

dashboards

```
GET /api/playlists/:id/dashboards
```

**Example request**

```
GET /api/playlists/1/dashboards HTTP/1.1
Accept: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json
[
  {
    "id": 3,
    "title": "my third dashboard",
    "order": 1,
  },
  {
    "id": 5,
    "title":"my other dashboard"
    "order": 2,

  }
]
```

## Create a playlist

```
POST /api/playlists/
```

**Example request**

```
PUT /api/playlists/1 HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
  {
    "name": "my playlist",
    "interval": "5m",
    "items": [
      {
        "type": "dashboard_by_id",
        "value": "3",
        "order": 1,
        "title":"my third dashboard"
      },
      {
        "type": "dashboard_by_tag",
        "value": "myTag",
        "order": 2,
        "title":"my other dashboard"
      }
    ]
  }
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json
  {
    "id": 1,
    "name": "my playlist",
    "interval": "5m"
  }
```

## Update a playlist

```
PUT /api/playlists/:id
```

**Example request**

```
PUT /api/playlists/1 HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
  {
    "name": "my playlist",
    "interval": "5m",
    "items": [
      {
        "playlistId": 1,
        "type": "dashboard_by_id",
        "value": "3",
        "order": 1,
        "title":"my third dashboard"
      },
      {
        "playlistId": 1,
        "type": "dashboard_by_tag",
        "value": "myTag",
        "order": 2,
        "title":"my other dashboard"
      }
    ]
  }
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json
{
  "id" : 1,
  "name": "my playlist",
  "interval": "5m",
  "orgId": "my org",
  "items": [
    {
      "id": 1,
      "playlistId": 1,
      "type": "dashboard_by_id",
      "value": "3",
      "order": 1,
      "title":"my third dashboard"
    },
    {
      "id": 2,
      "playlistId": 1,
      "type": "dashboard_by_tag",
      "value": "myTag",
      "order": 2,
      "title":"my other dashboard"
    }
  ]
}
```

## Delete a playlist

```
DELETE /api/playlists/:id
```

**Example request**

```
DELETE /api/playlists/1 HTTP/1.1
Accept: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json
{}
```
