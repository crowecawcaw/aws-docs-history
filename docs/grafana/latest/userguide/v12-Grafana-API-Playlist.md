

# Playlist API
<a name="v12-Grafana-API-Playlist"></a>

Use the Playlist API to work with playlists in the Amazon Managed Grafana workspace. 

**Note**  
To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid service account token. You include this in the `Authorization` field in the API request.

## List playlists
<a name="v12-Grafana-API-Playlist-list"></a>

```
GET /apis/playlist.grafana.app/v1/namespaces/default/playlists
```

Lists all playlists in the workspace.

**Example request**

```
GET /apis/playlist.grafana.app/v1/namespaces/default/playlists HTTP/1.1
Accept: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "kind": "PlaylistList",
  "apiVersion": "playlist.grafana.app/v1",
  "metadata": {},
  "items": [
    {
      "kind": "Playlist",
      "apiVersion": "playlist.grafana.app/v1",
      "metadata": {
        "name": "my-playlist-uid",
        "namespace": "default"
      },
      "spec": {
        "title": "My Playlist",
        "interval": "5m",
        "items": [
          {"type": "dashboard_by_uid", "value": "dashboard-uid-1"}
        ]
      }
    }
  ]
}
```

## Get a playlist
<a name="v12-Grafana-API-Playlist-get"></a>

```
GET /apis/playlist.grafana.app/v1/namespaces/default/playlists/:name
```

Retrieves a specific playlist by name (UID).

**Example request**

```
GET /apis/playlist.grafana.app/v1/namespaces/default/playlists/my-playlist-uid HTTP/1.1
Accept: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "kind": "Playlist",
  "apiVersion": "playlist.grafana.app/v1",
  "metadata": {
    "name": "my-playlist-uid",
    "namespace": "default"
  },
  "spec": {
    "title": "My Playlist",
    "interval": "5m",
    "items": [
      {"type": "dashboard_by_uid", "value": "dashboard-uid-1"}
    ]
  }
}
```

## Create a playlist
<a name="v12-Grafana-API-Playlist-create"></a>

```
POST /apis/playlist.grafana.app/v1/namespaces/default/playlists
```

Creates a new playlist.

**Example request**

```
POST /apis/playlist.grafana.app/v1/namespaces/default/playlists HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "metadata": {"name": "my-new-playlist-uid"},
  "spec": {
    "title": "My New Playlist",
    "interval": "5m",
    "items": [
      {"type": "dashboard_by_uid", "value": "dashboard-uid-1"}
    ]
  }
}
```

## Update a playlist
<a name="v12-Grafana-API-Playlist-update"></a>

```
PUT /apis/playlist.grafana.app/v1/namespaces/default/playlists/:name
```

Updates an existing playlist. The entire playlist spec must be provided.

**Example request**

```
PUT /apis/playlist.grafana.app/v1/namespaces/default/playlists/my-playlist-uid HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "metadata": {
    "name": "my-playlist-uid",
    "resourceVersion": "1234567890"
  },
  "spec": {
    "title": "Updated Playlist",
    "interval": "10m",
    "items": [
      {"type": "dashboard_by_uid", "value": "dashboard-uid-1"},
      {"type": "dashboard_by_tag", "value": "monitoring"}
    ]
  }
}
```

## Delete a playlist
<a name="v12-Grafana-API-Playlist-delete"></a>

```
DELETE /apis/playlist.grafana.app/v1/namespaces/default/playlists/:name
```

Deletes a playlist by name (UID).

**Example request**

```
DELETE /apis/playlist.grafana.app/v1/namespaces/default/playlists/my-playlist-uid HTTP/1.1
Accept: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "kind": "Status",
  "apiVersion": "v1",
  "status": "Success",
  "code": 200
}
```

## Search playlist (deprecated)
<a name="v12-Grafana-API-Playlist-search"></a>

**Important**  
This endpoint is deprecated. Use [List playlists](#v12-Grafana-API-Playlist-list) instead.

```
GET /api/playlists
```

Returns all playlists for the current Amazon Managed Grafana workspace, using pagination.

**Example request**

```
GET /api/playlists HTTP/1.1
Accept: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

Querystring parameters:
+ **query**— Limit the responses to playlists that have a name like this value.
+ **limit**— Limit the response to X number of playlists.

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

## Get one playlist (deprecated)
<a name="v12-Grafana-API-Playlist-getone"></a>

**Important**  
This endpoint is deprecated. Use [Get a playlist](#v12-Grafana-API-Playlist-get) instead.

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

## Get playlist items (deprecated)
<a name="v12-Grafana-API-Playlist-get-items"></a>

**Important**  
This endpoint is deprecated. Use [Get a playlist](#v12-Grafana-API-Playlist-get) instead. Playlist items are included in the playlist response.

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

## Get playlist dashboards (deprecated)
<a name="v12-Grafana-API-Playlist-get-dashboards"></a>

**Important**  
This endpoint is deprecated. Use [Get a playlist](#v12-Grafana-API-Playlist-get) instead.

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

## Create a playlist (deprecated)
<a name="v12-Grafana-API-Playlist-create-legacy"></a>

**Important**  
This endpoint is deprecated. Use [Create a playlist](#v12-Grafana-API-Playlist-create) instead.

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

## Update a playlist (deprecated)
<a name="v12-Grafana-API-Playlist-update-legacy"></a>

**Important**  
This endpoint is deprecated. Use [Update a playlist](#v12-Grafana-API-Playlist-update) instead.

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

## Delete a playlist (deprecated)
<a name="v12-Grafana-API-Playlist-delete-legacy"></a>

**Important**  
This endpoint is deprecated. Use [Delete a playlist](#v12-Grafana-API-Playlist-delete) instead.

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