

# Preferences API
<a name="v10-Grafana-API-Preferences"></a>

Use the Preferences API to work with user preferences in the Amazon Managed Grafana workspace. 

Keys:
+ **theme**— Valid values are `light`, `dark`, or an empty string to use the default theme.
+ **homeDashboardId**— The numerical `:id` of a favorited dashboard. The default is 0.
+ **timezone**— Valid values are `utc`, `browser`, or an empty string to use the default.

Omitting a key causes the current value to be replaced with the system default value.

**Note**  
To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid service account token. You include this in the `Authorization` field in the API request.

## Get current user preferences
<a name="v10-Grafana-API-Preferences-get"></a>

```
GET /api/user/preferences
```

**Example request**

```
GET /api/user/preferences HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{"theme":"","homeDashboardId":0,"timezone":""}
```

## Update current user preferences
<a name="v10-Grafana-API-Preferences-update"></a>

```
PUT /api/user/preferences
```

**Example request**

```
PUT /api/user/preferences HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "theme": "",
  "homeDashboardId":0,
  "timezone":"utc"
}
```

**Example response**

```
HTTP/1.1 200
Content-Type: text/plain; charset=utf-8

{"message":"Preferences updated"}
```

## Get current org preferences
<a name="v10-Grafana-API-Preferences-get-org"></a>

```
GET /api/org/preferences
```

**Example request**

```
GET /api/org/preferences HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json

{"theme":"","homeDashboardId":0,"timezone":""}
```

## Update current org preferences
<a name="v10-Grafana-API-Playlist-Preferences-update-org"></a>

```
PUT /api/org/preferences
```

**Example request**

```
PUT /api/org/preferences HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "theme": "",
  "homeDashboardId":0,
  "timezone":"utc"
}
```

**Example response**

```
HTTP/1.1 200
Content-Type: text/plain; charset=utf-8

{"message":"Preferences updated"}
```