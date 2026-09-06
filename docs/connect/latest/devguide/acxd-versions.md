# Versions

Access version history for workspace resources. Every change to a versioned
resource creates a new version that can be retrieved later.

###### Contents

- [ListResourceVersions](#acxd-versions-ListResourceVersions "#acxd-versions-ListResourceVersions")
- [GetResourceVersion](#acxd-versions-GetResourceVersion "#acxd-versions-GetResourceVersion")
- [Request Parameters](#acxd-versions-request-parameters "#acxd-versions-request-parameters")

## ListResourceVersions

Lists the version history for a specific resource.

### Input

| Parameter      | Type    | Required |
| -------------- | ------- | -------- |
| `resourceType` | string  | Yes      |
| `resourceId`   | string  | Yes      |
| `nextToken`    | string  | No       |
| `maxResults`   | integer | No       |

### Sample Request

```
client.send(new ListResourceVersionsCommand({
    resourceType: "flows",
    resourceId: "DeployTestFlow",
}));
```

### Output

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

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## GetResourceVersion

Gets the full content of a specific version.

### Input

| Parameter      | Type   | Required |
| -------------- | ------ | -------- |
| `versionId`    | string | Yes      |
| `resourceType` | string | Yes      |
| `resourceId`   | string | Yes      |

### Sample Request

```
await client.send(new GetResourceVersionCommand({
  versionId: "NDjL4SbcnwdK5w3fNBL6A4oFIzwRYeyE",
  resourceType: "flows",
  resourceId: "DeployTestFlow",
}));
```

### Output

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

The `data` field contains exactly one key matching the resource type, with the full
resource content at that version.

### Errors

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## Request Parameters

### versionId

Type: String

The version ID.

### resourceType

Type: String

The type of versioned resource. One of: `slotTypes`, `flows`,
`dataRequests`, `actions`, `lifecycleHooks`,
`journeys`, `guardrails`, `feedbackConfigs`.

### resourceId

Type: String

The identifier of the resource to retrieve versions for.

### lastUpdatedBy

Type: String

Who made this version's change.

### updatedAt

Type: String

When this version was created (ISO 8601).

### isLatest

Type: Boolean

Whether this is the most recent version.

### isPublished

Type: Boolean

Whether this version is currently published (live).

### data

Type: Object

The full resource content at this version. Contains exactly one key corresponding to
the resource type: `slotType`, `flow`, `dataRequest`,
`action`, `lifecycleHook`, `journey`, `guardrail`,
or `feedbackConfig`.

### nextToken

Type: String

Pagination token. See Common Types.

### maxResults

Type: Integer

Max items per page (1–100). See Common Types.
