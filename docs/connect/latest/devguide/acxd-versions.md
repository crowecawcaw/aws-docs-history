

# Versions
<a name="acxd-versions"></a>

Access version history for workspace resources. Every change to a versioned resource creates a new version that can be retrieved later.

**Topics**
+ [ListResourceVersions](#acxd-versions-ListResourceVersions)
+ [GetResourceVersion](#acxd-versions-GetResourceVersion)
+ [Request Parameters](#acxd-versions-request-parameters)

## ListResourceVersions
<a name="acxd-versions-ListResourceVersions"></a>

Lists the version history for a specific resource.

### Input
<a name="acxd-versions-ListResourceVersions-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| resourceType | string | Yes | 
| resourceId | string | Yes | 
| nextToken | string | No | 
| maxResults | integer | No | 

### Sample Request
<a name="acxd-versions-ListResourceVersions-sample-request"></a>

```
client.send(new ListResourceVersionsCommand({
    resourceType: "flows",
    resourceId: "DeployTestFlow",
}));
```

### Output
<a name="acxd-versions-ListResourceVersions-output"></a>

```
{
  "items": [
    {
      "versionId": "v-a1b2c3d4",
      "lastUpdatedBy": "ci-deploy-bot",
      "updatedAt": "2026-08-01T14:00:00.000Z",
      "isLatest": true,
      "isPublished": false
    },
    {
      "versionId": "v-e5f6g7h8",
      "lastUpdatedBy": "jane@example.com",
      "updatedAt": "2026-08-01T12:00:00.000Z",
      "isLatest": false,
      "isPublished": true
    }
  ],
  "nextToken": null
}
```

### Errors
<a name="acxd-versions-ListResourceVersions-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## GetResourceVersion
<a name="acxd-versions-GetResourceVersion"></a>

Gets the full content of a specific version.

### Input
<a name="acxd-versions-GetResourceVersion-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| versionId | string | Yes | 
| resourceType | string | Yes | 
| resourceId | string | Yes | 

### Sample Request
<a name="acxd-versions-GetResourceVersion-sample-request"></a>

```
await client.send(new GetResourceVersionCommand({
  versionId: "NDjL4SbcnwdK5w3fNBL6A4oFIzwRYeyE",
  resourceType: "flows",
  resourceId: "DeployTestFlow",
}));
```

### Output
<a name="acxd-versions-GetResourceVersion-output"></a>

```
{
  "data": {
    "flow": {
      "flowId": "DeployTestFlow",
      "description": "Flow for deployment testing",
      "mainLanguageCode": "en-US",
      "createdAt": "2026-08-08T16:12:06.767Z",
      "updatedAt": "2026-08-08T16:12:06.767Z",
      "updatedBy": "ci-deploy-bot"
    }
  }
}
```

The `data` field contains exactly one key matching the resource type, with the full resource content at that version.

### Errors
<a name="acxd-versions-GetResourceVersion-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## Request Parameters
<a name="acxd-versions-request-parameters"></a>

### versionId
<a name="acxd-versions-request-parameters-versionId"></a>

Type: String

The version ID.

### resourceType
<a name="acxd-versions-request-parameters-resourceType"></a>

Type: String

The type of versioned resource. One of: `slotTypes`, `flows`, `dataRequests`, `actions`, `lifecycleHooks`, `journeys`, `guardrails`, `feedbackConfigs`.

### resourceId
<a name="acxd-versions-request-parameters-resourceId"></a>

Type: String

The identifier of the resource to retrieve versions for.

### lastUpdatedBy
<a name="acxd-versions-request-parameters-lastUpdatedBy"></a>

Type: String

Who made this version's change.

### updatedAt
<a name="acxd-versions-request-parameters-updatedAt"></a>

Type: String

When this version was created (ISO 8601).

### isLatest
<a name="acxd-versions-request-parameters-isLatest"></a>

Type: Boolean

Whether this is the most recent version.

### isPublished
<a name="acxd-versions-request-parameters-isPublished"></a>

Type: Boolean

Whether this version is currently published (live).

### data
<a name="acxd-versions-request-parameters-data"></a>

Type: Object

The full resource content at this version. Contains exactly one key corresponding to the resource type: `slotType`, `flow`, `dataRequest`, `action`, `lifecycleHook`, `journey`, `guardrail`, or `feedbackConfig`.

### nextToken
<a name="acxd-versions-request-parameters-nextToken"></a>

Type: String

Pagination token. See Common Types.

### maxResults
<a name="acxd-versions-request-parameters-maxResults"></a>

Type: Integer

Max items per page (1–100). See Common Types.