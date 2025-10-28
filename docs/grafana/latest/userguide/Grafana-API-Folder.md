# Folder API

Use the Folder API to work with folders in the Amazon Managed Grafana workspace.

The identifier (id) of a folder is an auto-incrementing numeric value and is only
unique per workspace. The unique identifier (uid) of a folder can be used to uniquely
identify a folder between multiple workspaces. It’s automatically generated if you don't
provide one when you create a folder. The uid allows having consistent URLs for
accessing folder and when synchronizing folder between multiple Amazon Managed Grafana workspaces.
The use of the uid means that changing the title of a folder does not break any
bookmarked links to that folder.

The uid can have a maximum length of 40 characters.

Folders can't be nested.

###### Note

To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid Grafana
API token. You include this in the `Authorization` field in the API
request. For information about how to create a token to authenticate your API calls,
see [Authenticate with tokens](authenticating-grafana-apis.md "authenticating-grafana-apis.md").

The **General** folder, with an `id` of 0, is not part of
the Folder API. You can't use the Folder API to retrieve information about the general
folder.

## Create folder

```
POST /api/folders
```

Creates a new folder.

**Example request**

```
POST /api/folders HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "uid": "nErXDvCkzz",
  "title": "Department ABC"
}

```

JSON body schema:

- **uid**— Optional unique identifer. If
  null, a new uid is generated.
- **title**— The title for the
  folder.

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "id":1,
  "uid": "nErXDvCkzz",
  "title": "Department ABC",
  "url": "/dashboards/f/nErXDvCkzz/department-abc",
  "hasAcl": false,
  "canSave": true,
  "canEdit": true,
  "canAdmin": true,
  "createdBy": "admin",
  "created": "2018-01-31T17:43:12+01:00",
  "updatedBy": "admin",
  "updated": "2018-01-31T17:43:12+01:00",
  "version": 1
}
```

Status Codes:

- **200**— Created
- **400**— Error such as invalid JSON,
  invalid or missing fields
- **401**— Unauthorized
- **403**— Access denied

## Update folder

```
PUT /api/folders/:uid
```

Updates the existing folder that matches the uid.

**Example request**

```
PUT /api/folders/nErXDvCkzz HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "title":"Department DEF",
  "version": 1
}
```

JSON body schema:

- **uid**— Changes the unique identifer,
  if provided.
- **title**— The title of the
  folder.
- **version**— Provide the current
  version to be able to overwrite the folder. Not needed if
  `overwrite=true`.
- **overwrite**— Set to
  `true` to overwrite the existing folder with a newer
  version.

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "id":1,
  "uid": "nErXDvCkzz",
  "title": "Department DEF",
  "url": "/dashboards/f/nErXDvCkzz/department-def",
  "hasAcl": false,
  "canSave": true,
  "canEdit": true,
  "canAdmin": true,
  "createdBy": "admin",
  "created": "2018-01-31T17:43:12+01:00",
  "updatedBy": "admin",
  "updated": "2018-01-31T17:43:12+01:00",
  "version": 1
}
```

Status Codes:

- **200**— Created
- **400**— Error such as invalid JSON,
  invalid or missing fields
- **401**— Unauthorized
- **403**— Access denied
- **404**— Folder not found
- **412**— Precondition failed

The **412** status code is used to explain why the folder can't
be updated.

- The folder has been changed by someone else
  `status=version-mismatch`

The response body has the following properties:

```
HTTP/1.1 412 Precondition Failed
Content-Type: application/json; charset=UTF-8
Content-Length: 97

{
  "message": "The folder has been changed by someone else",
  "status": "version-mismatch"
}
```

## Get all folders

```
GET /api/folders
```

Returns all folders that you have permission to view. You can control the maximum
number of folders returned by using the `limit` query parameter. The
default is 1000.

**Example request**

```
GET /api/folders?limit=10 HTTP/1.1
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
    "id":1,
    "uid": "nErXDvCkzz",
    "title": "Department ABC"
  },
  {
    "id":2,
    "uid": "k3S1cklGk",
    "title": "Department RND"
  }
]
```

## Get folder by uid

```
GET /api/folders/:uid
```

Returns all folders that matches the given uid.

**Example request**

```
GET /api/folders/nErXDvCkzzh HTTP/1.1
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
  "uid": "nErXDvCkzz",
  "title": "Department ABC",
  "url": "/dashboards/f/nErXDvCkzz/department-abc",
  "hasAcl": false,
  "canSave": true,
  "canEdit": true,
  "canAdmin": true,
  "createdBy": "admin",
  "created": "2018-01-31T17:43:12+01:00",
  "updatedBy": "admin",
  "updated": "2018-01-31T17:43:12+01:00",
  "version": 1
}
```

Status Codes:

- **200**— Found
- **401**— Unauthorized
- **403**— Access denied
- **404**— Not found

## Get folder by id

```
GET /api/folders/id/:id
```

Returns the folder that matches the given id.

**Example request**

```
GET /api/folders/id/1 HTTP/1.1
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
  "uid": "nErXDvCkzz",
  "title": "Department ABC",
  "url": "/dashboards/f/nErXDvCkzz/department-abc",
  "hasAcl": false,
  "canSave": true,
  "canEdit": true,
  "canAdmin": true,
  "createdBy": "admin",
  "created": "2018-01-31T17:43:12+01:00",
  "updatedBy": "admin",
  "updated": "2018-01-31T17:43:12+01:00",
  "version": 1
}
```

Status Codes:

- **200**— Found
- **401**— Unauthorized
- **403**— Access denied
- **404**— Not found

## Delete folder by uid

```
DELETE /api/folders/:uid
```

Deletes the folder matching the uid, and also deletes all dashboards stored in the
folder. This oepration can't be reverted.

**Example request**

```
DELETE /api/folders/nErXDvCkzz HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{
  "message":"Folder deleted",
  "id": 2
}
```

Status Codes:

- **200**— Deleted
- **401**— Unauthorized
- **403**— Access denied
- **404**— Not found
