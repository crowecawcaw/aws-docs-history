# Snapshot API

Use the Snapshot API to work with snapshots in an Amazon Managed Grafana workspace.

###### Note

To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid Grafana
API token. You include this in the `Authorization` field in the API
request. For information about how to create a token to authenticate your API calls,
see [Authenticate with tokens](authenticating-grafana-apis.md "authenticating-grafana-apis.md").

## Create new shapshot

```
POST /api/snapshots
```

**Example request**

```
POST /api/snapshots HTTP/1.1
    Accept: application/json
    Content-Type: application/json
    Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

    {
      "dashboard": {
        "editable":false,
        "hideControls":true,
        "nav":[
        {
          "enable":false,
        "type":"timepicker"
        }
        ],
        "rows": [
          {

          }
        ],
        "style":"dark",
        "tags":[],
        "templating":{
          "list":[
          ]
        },
        "time":{
        },
        "timezone":"browser",
        "title":"Home",
        "version":5
        },
      "expires": 3600
    }

```

JSON body schema:

- **dashboard**— (Required) The complete
  dashboard model.
- **name**— (Optional) A name for the
  snapshot.
- **expires**— (Optional) When the
  snapshot should expire, in seconds. The default is to never expire.
- **external**— (Optional) Save the
  snapshot on an external server rather than locally. Default is false.
- **key**— (Required if
  `external` is `true`) Define a unique key.
- **deletekey**— (Required if
  `external` is `true`) A unique key to be used to
  delete the snapshot. It is different than `key` so that only the
  creator can delete the snapshot.

###### Note

When creating a snapshot using the API, you have to provide the full dashboard
payload including the snapshot data. This endpoint is designed for the Grafana
UI.

**Example response**

```
HTTP/1.1 200
    Content-Type: application/json
    {
      "deleteKey":"XXXXXXX",
      "deleteUrl":"myurl/api/snapshots-delete/XXXXXXX",
      "key":"YYYYYYY",
      "url":"myurl/dashboard/snapshot/YYYYYYY",
      "id": 1,
    }
```

Keys:

- **deleteKey**— A key generated to be
  used to delete the snapshot.
- **key**— A key generated to share the
  dashboard.

## Get list of snapshots

```
GET /api/dashboard/snapshots
```

Query parameters:

- **query**— Search query
- **limit**— Limit the number of
  returned results

**Example request**

```
GET /api/dashboard/snapshots HTTP/1.1
Accept: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

[
  {
    "id":8,
    "name":"Home",
    "key":"YYYYYYY",
    "orgId":1,
    "userId":1,
    "external":false,
    "externalUrl":"",
    "expires":"2200-13-32T25:23:23+02:00",
    "created":"2200-13-32T28:24:23+02:00",
    "updated":"2200-13-32T28:24:23+02:00"
  }
]
```

## Get snapshot by key

```
GET /api/snapshots/:key
```

**Example request**

```
GET /api/snapshots/YYYYYYY HTTP/1.1
Accept: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "meta":{
    "isSnapshot":true,
    "type":"snapshot",
    "canSave":false,
    "canEdit":false,
    "canStar":false,
    "slug":"",
    "expires":"2200-13-32T25:23:23+02:00",
    "created":"2200-13-32T28:24:23+02:00"
  },
  "dashboard": {
    "editable":false,
    "hideControls":true,
    "nav": [
      {
        "enable":false,
        "type":"timepicker"
      }
    ],
    "rows": [
      {

      }
    ],
    "style":"dark",
    "tags":[],
    "templating":{
      "list":[
      ]
    },
    "time":{
    },
    "timezone":"browser",
    "title":"Home",
    "version":5
  }
}
```

## Delete snapshot by key

```
DELETE /api/snapshots/:key
```

**Example request**

```
DELETE /api/snapshots/YYYYYYY HTTP/1.1
Accept: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{"message":"Snapshot deleted. It might take an hour before it's cleared from any CDN caches.", "id": 1}
```

## Delete snapshot by

deleteKey

This API call can be used without authentication by using the secret delete key
for the snapshot.

```
GET /api/snapshots-delete/:deleteKey
```

**Example request**

```
GET /api/snapshots-delete/XXXXXXX HTTP/1.1
Accept: application/json
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{"message":"Snapshot deleted. It might take an hour before it's cleared from any CDN caches.", "id": 1}
```
