# Folder/Dashboard Search API

Use the FolderDashboard-Search API to search folders and dashboards in an Amazon Managed Grafana
workspace.

###### Note

To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid Grafana
API token. You include this in the `Authorization` field in the API
request. For information about how to create a token to authenticate your API calls,
see [Authenticate with tokens](authenticating-grafana-apis.md "authenticating-grafana-apis.md").

## Search folders and

dashboards

```
GET /api/search/
```

Query parameters:

- **query**— Search query
- **tag**— List of tags to search for.
  These are Grafana tags, not AWS tags.
- **type**— The type to search for,
  either `dash-folder` or `dash-db`.
- **dashboardIds**— List of dashboard
  Id's to search for.
- **folderIds**— List of dashboard Id's
  to search for in dashboards.
- **starred**— Flag to specify that only
  starred dashboards are to be returned.
- **limit**— Limit the number of
  returned results (maximum is 5000).
- **page**— Use this parameter to access
  hits beyond limit. Numbering starts at 1. The `limit` parameter
  acts as page size.

**Example request for retrieving folders and dashboards of the
general folder**

```
GET /api/search?folderIds=0&query=&starred=false HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response for retrieving folders and dashboards of
the general folder**

```
HTTP/1.1 200
Content-Type: application/json

[
  {
    "id": 163,
    "uid": "000000163",
    "title": "Folder",
    "url": "/dashboards/f/000000163/folder",
    "type": "dash-folder",
    "tags": [],
    "isStarred": false,
    "uri":"db/folder" // deprecated in Grafana v5.0
  },
  {
    "id":1,
    "uid": "cIBgcSjkk",
    "title":"Production Overview",
    "url": "/d/cIBgcSjkk/production-overview",
    "type":"dash-db",
    "tags":[prod],
    "isStarred":true,
    "uri":"db/production-overview" // deprecated in Grafana v5.0
  }
]
```

**Example request for searching for starred
dashboards**

```
GET /api/search?query=Production%20Overview&starred=true&tag=prod HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response for searching for starred
dashboards**

```
HTTP/1.1 200
Content-Type: application/json

[HTTP/1.1 200
Content-Type: application/json

[
  {
    "id":1,
    "uid": "cIBgcSjkk",
    "title":"Production Overview",
    "url": "/d/cIBgcSjkk/production-overview",
    "type":"dash-db",
    "tags":[prod],
    "isStarred":true,
    "folderId": 2,
    "folderUid": "000000163",
    "folderTitle": "Folder",
    "folderUrl": "/dashboards/f/000000163/folder",
    "uri":"db/production-overview" // deprecated in Grafana v5.0
  }
]
```
