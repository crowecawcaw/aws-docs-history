# Plugin API

Use the Plugin API to manage plugins in the Amazon Managed Grafana workspace. To make changes to
plugins with this API, the workspace must have [plugin management enabled](AMG-configure-workspace.md "AMG-configure-workspace.md") for your
workspace. The user defined by the Grafana API key must also be an [admin](Grafana-user-roles.md "Grafana-user-roles.md") for the Amazon Managed Grafana workspace.

###### Note

To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid Grafana
API token. You include this in the `Authorization` field in the API
request. For information about how to create a token to authenticate your API calls,
see [Authenticate with tokens](authenticating-grafana-apis.md "authenticating-grafana-apis.md").

## Install plugin

```
POST /api/plugins/:id/install
```

**Example request**

```
POST /api/plugins/grafana-athena-datasource/install HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "version": "2.12.0" # optional, uses the latest compatible version if not provided
}
```

**Example response**

```
HTTP/1.1 200
```

## Uninstall plugin

```
POST /api/plugins/:id/uninstall
```

**Example request**

```
POST /api/plugins/grafana-athena-datasource/uninstall HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk

{
  "version": "2.12.0" # optional, uninstalls whatever is installed if not provided
}
```

**Example response**

```
HTTP/1.1 200
```

## Get all plugins

```
GET /api/gnet/plugins
```

**Example request**

```
GET /api/gnet/plugins HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json
{
  "items": [
    {
      "status": "active",
      "id": 74,
      "typeId": 1,
      "typeName": "Application",
      "typeCode": "app",
      "slug": "alexanderzobnin-zabbix-app",
      "name": "Zabbix",
      "description": "Zabbix plugin for Grafana",
      "version": "4.4.3",
      "versionStatus": "active",
      "versionSignatureType": "grafana",
      "versionSignedByOrg": "grafana",
      "versionSignedByOrgName": "Grafana Labs",
      "userId": 0,
      "orgId": 13056,
      "orgName": "Alexander Zobnin",
      "orgSlug": "alexanderzobnin",
      "orgUrl": "https://github.com/alexanderzobnin",
      "url": "https://github.com/grafana/grafana-zabbix/",
      "createdAt": "2016-04-06T20:23:41.000Z",
      "updatedAt": "2023-10-10T12:53:51.000Z",
      "downloads": 90788771,
      "verified": false,
      "featured": 180,
      "internal": false,
      "downloadSlug": "alexanderzobnin-zabbix-app",
      "popularity": 0.2485,
      "signatureType": "grafana",
      "packages": {
        "linux-amd64": {
          "md5": "baa06e8f26731f99748c58522cd4ffb6",
          "sha256": "a4a108f2e04a2114810c7b60419b4b04bf80d3377e2394b0586e2dc96b5a929c",
          "packageName": "linux-amd64",
          "downloadUrl": "/api/plugins/alexanderzobnin-zabbix-app/versions/4.4.3/download?os=linux&arch=amd64"
        },
        `<... further packages>`
      },
      "links": [
        {
          "rel": "self",
          "href": "/plugins/alexanderzobnin-zabbix-app"
        },
        `<... further links>`
      ],
      "angularDetected": false
    },
    `<... further plugins>`
  ],
  "orderBy": "weight",
  "direction": "asc",
  "links": [
    {
      "rel": "self",
      "href": "/plugins"
    }
  ]
}
```

## Get plugin

```
GET /api/gnet/plugins/:id
```

**Example request**

```
GET /api/gnet/plugins/grafana-athena-datasource HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json
{
  "status": "active",
  "id": 764,
  "typeId": 2,
  "typeName": "Data Source",
  "typeCode": "datasource",
  "slug": "grafana-athena-datasource",
  "name": "Amazon Athena",
  "description": "Use Amazon Athena with Grafana",
  "version": "2.13.0",
  "versionStatus": "active",
  "versionSignatureType": "grafana",
  "versionSignedByOrg": "grafana",
  "versionSignedByOrgName": "Grafana Labs",
  "userId": 0,
  "orgId": 5000,
  "orgName": "Grafana Labs",
  "orgSlug": "grafana",
  "orgUrl": "https://grafana.org",
  "url": "https://github.com/grafana/athena-datasource/",
  "createdAt": "2021-11-24T08:55:41.000Z",
  "updatedAt": "2023-10-31T17:20:32.000Z",
  "json": {
    "$schema": "https://raw.githubusercontent.com/grafana/grafana/master/docs/sources/developers/plugins/plugin.schema.json",
    "alerting": true,
    "annotations": true,
    "backend": true,
    "dependencies": {
      "grafanaDependency": ">=8.0.0",
      "plugins": []
    },
    "executable": "gpx_athena",
    "id": "grafana-athena-datasource",
    "includes": [
      {
        "name": "Cost Usage Report Monitoring",
        "path": "dashboards/cur-monitoring.json",
        "type": "dashboard"
      },
      {
        "name": "Amazon VPC Flow Logs",
        "path": "dashboards/vpc-flow-logs.json",
        "type": "dashboard"
      }
    ],
    "info": {
      "author": {
        "name": "Grafana Labs",
        "url": "https://grafana.com"
      },
      "build": {
        "time": 1698764559022,
        "repo": "https://github.com/grafana/athena-datasource",
        "branch": "main",
        "hash": "25cc131300f1ed22593bc3ba08b2bef7d23fbcd01",
        "build": 1462
      },
      "description": "Use Amazon Athena with Grafana",
      "keywords": [
        "datasource",
        "athena"
      ],
      "links": [
        {
          "name": "Website",
          "url": "https://github.com/grafana/athena-datasource"
        },
        {
          "name": "License",
          "url": "https://github.com/grafana/athena-datasource/blob/master/LICENSE"
        }
      ],
      "logos": {
        "large": "img/logo.svg",
        "small": "img/logo.svg"
      },
      "screenshots": [],
      "updated": "2023-10-31",
      "version": "2.13.0"
    },
    "metrics": true,
    "name": "Amazon Athena",
    "type": "datasource"
  },
  "readme": "`<... full HTML readme>`",
  "statusContext": "",
  "downloads": 2505825,
  "verified": false,
  "featured": 0,
  "internal": false,
  "downloadSlug": "grafana-athena-datasource",
  "popularity": 0.0594,
  "signatureType": "grafana",
  "grafanaDependency": ">=8.0.0",
  "packages": {
    "linux-amd64": {
      "md5": "7efef359bf917b4ca6b149de42a1282d",
      "sha256": "cd2fc5737c321dc3d8bbe2852c801c01adb64eacc9f60420bd21dc18bee43531",
      "packageName": "linux-amd64",
      "downloadUrl": "/api/plugins/grafana-athena-datasource/versions/2.13.0/download?os=linux&arch=amd64"
    },
    `<... other packages>`
  },
  "links": [
    {
      "rel": "self",
      "href": "/plugins/grafana-athena-datasource"
    },
    `<... other links>`
  ],
  "angularDetected": false
}
```

## Get plugin versions

```
POST /api/gnet/plugins/:id/versions
```

**Example request**

```
GET /api/gnet/plugins/grafana-athena-datasource/versions HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer eyJrIjoiT0tTcG1pUlY2RnVKZTFVaDFsNFZXdE9ZWmNrMkZYbk
```

**Example response**

```
HTTP/1.1 200
Content-Type: application/json
{
  "items": [
    {
      "id": 5306,
      "pluginId": 764,
      "pluginSlug": "grafana-athena-datasource",
      "version": "2.13.0",
      "url": "https://github.com/grafana/athena-datasource/",
      "commit": "",
      "description": "Use Amazon Athena with Grafana",
      "createdAt": "2023-10-31T17:20:31.000Z",
      "updatedAt": null,
      "downloads": 33790,
      "verified": false,
      "status": "active",
      "statusContext": "",
      "downloadSlug": "grafana-athena-datasource",
      "packages": {},
      "links": [
        {
          "rel": "self",
          "href": "/plugins/grafana-athena-datasource/versions/2.13.0"
        },
        {
          "rel": "images",
          "href": "/plugins/grafana-athena-datasource/versions/2.13.0/images"
        },
        {
          "rel": "thumbnails",
          "href": "/plugins/grafana-athena-datasource/versions/2.13.0/thumbnails"
        },
        {
          "rel": "plugin",
          "href": "/plugins/grafana-athena-datasource"
        },
        {
          "rel": "download",
          "href": "/plugins/grafana-athena-datasource/versions/2.13.0/download"
        }
      ],
      "grafanaDependency": ">=8.0.0",
      "angularDetected": false
    },
    {
      "id": 5244,
      "pluginId": 764,
      "pluginSlug": "grafana-athena-datasource",
      "version": "2.12.0",
      "url": "https://github.com/grafana/athena-datasource/",
      "commit": "",
      "description": "Use Amazon Athena with Grafana",
      "createdAt": "2023-10-17T12:42:13.000Z",
      "updatedAt": null,
      "downloads": 60742,
      "verified": false,
      "status": "active",
      "statusContext": "",
      "downloadSlug": "grafana-athena-datasource",
      "packages": {},
      "links": [
        {
          "rel": "self",
          "href": "/plugins/grafana-athena-datasource/versions/2.12.0"
        },
        {
          "rel": "images",
          "href": "/plugins/grafana-athena-datasource/versions/2.12.0/images"
        },
        {
          "rel": "thumbnails",
          "href": "/plugins/grafana-athena-datasource/versions/2.12.0/thumbnails"
        },
        {
          "rel": "plugin",
          "href": "/plugins/grafana-athena-datasource"
        },
        {
          "rel": "download",
          "href": "/plugins/grafana-athena-datasource/versions/2.12.0/download"
        }
      ],
      "grafanaDependency": ">=8.0.0",
      "angularDetected": false
    },
    `<... other versions>`
  ]
}
```
