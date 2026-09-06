# Analytics Tags

Tag conversation events with sentiment classifications for reporting and analysis.

###### Contents

- [CreateAnalyticsTag](#acxd-analytics-tags-createanalyticstag "#acxd-analytics-tags-createanalyticstag")
- [ListAnalyticsTags](#acxd-analytics-tags-listanalyticstags "#acxd-analytics-tags-listanalyticstags")
- [UpdateAnalyticsTag](#acxd-analytics-tags-updateanalyticstag "#acxd-analytics-tags-updateanalyticstag")
- [DeleteAnalyticsTag](#acxd-analytics-tags-deleteanalyticstag "#acxd-analytics-tags-deleteanalyticstag")
- [Request Parameters](#acxd-analytics-tags-request-parameters "#acxd-analytics-tags-request-parameters")

## CreateAnalyticsTag

Creates a new analytics tag.

### Input

| Parameter     | Type   | Required |
| ------------- | ------ | -------- |
| `name`        | string | Yes      |
| `type`        | enum   | Yes      |
| `description` | string | Yes      |
| `metadata`    | object | No       |

### Sample Request

```
await client.send(new CreateAnalyticsTagCommand({
  name: 'AnalyticsTagName',
  type: 'positive',
  description: 'Analytics Tag Description',
  metadata: { path: '/support', tags: ['support'] },
}));
```

### Output

Returns the analytics tags entry that was created.

```
{
  "name": "AnalyticsTagName",
  "type": "positive",
  "description": "Analytics Tag Description",
  "isSystemTag": false,
  "metadata": { "path": "/support", "tags": ["support"] },
  "createdAt": "2026-08-01T12:00:00.000Z",
  "updatedAt": "2026-08-01T12:00:00.000Z",
  "lastUpdatedBy": "ci-deploy-bot"
}
```

### Errors

- `ValidationException` (400)
- `ConflictException` (409)
- `InternalServerException` (500)

## ListAnalyticsTags

Lists all analytics tags in the workspace.

### Input

No parameters.

### Sample Request

```
await client.send(new ListAnalyticsTagsCommand({}));
```

### Output

Returns the full analytics tags collection:

```
{
  "items": [
    {
      "name": "resolved_issue",
      "type": "positive",
      "description": "Customer issue was resolved",
      "isSystemTag": false,
      "metadata": { "path": "/support", "tags": ["support"] },
      "createdAt": "2026-08-01T12:00:00.000Z",
      "updatedAt": "2026-08-01T12:00:00.000Z",
      "lastUpdatedBy": "ci-deploy-bot"
    }
  ]
}
```

### Errors

- `ValidationException` (400)
- `InternalServerException` (500)

## UpdateAnalyticsTag

Updates an existing analytics tag by name.

### Input

| Parameter     | Type   | Required |
| ------------- | ------ | -------- |
| `name`        | string | Yes      |
| `type`        | enum   | No       |
| `description` | string | No       |
| `metadata`    | object | No       |

### Sample Request

```
await client.send(new UpdateAnalyticsTagCommand({
    name: 'AnalyticsTagName',
    type: 'negative',
    description: 'Updated description',
    metadata: { path: '/support', tags: ['support'] },
}));
```

### Output

Returns the analytics tags entry that was updated.

```
{
  "name": "AnalyticsTagName",
  "type": "negative",
  "description": "Updated description",
  "isSystemTag": false,
  "metadata": { "path": "/support", "tags": ["support"] },
  "createdAt": "2026-08-01T12:00:00.000Z",
  "updatedAt": "2026-08-01T12:00:00.000Z",
  "lastUpdatedBy": "ci-deploy-bot"
}
```

### Errors

- `ResourceNotFoundException` (404)
- `ValidationException` (400)
- `InternalServerException` (500)

## DeleteAnalyticsTag

Deletes an analytics tag by name.

### Input

| Parameter | Type   | Required |
| --------- | ------ | -------- |
| `name`    | string | Yes      |

### Sample Request

```
await client.send(new DeleteAnalyticsTagCommand({
    name: 'AnalyticsTagName',
}));
```

### Output

No response body.

### Errors

- `ResourceNotFoundException` (404)
- `ValidationException` (400)
- `InternalServerException` (500)

## Request Parameters

`name`

Type: String

Description: The tag identifier. Alphanumeric characters and underscores only. Max 36 characters.

`type`

Type: String

Description: The sentiment classification of the tag. One of: `positive` , `negative` , `neutral` .

`description`

Type: String

Description: A short human-readable description of the tag. Max 64 characters.

`isSystemTag`

Type: Boolean

Description: Whether this tag is system-managed (read-only). System tags cannot be modified or deleted.

`metadata`

Type: Object

Description: Organizational metadata for categorizing the resource. See [Common Types](acxd-common-types.md "acxd-common-types.md").

`createdAt`

Type: String

Description: When the tag was created (ISO 8601).

`updatedAt`

Type: String

Description: When the tag was last modified (ISO 8601).

`lastUpdatedBy`

Type: String

Description: The identity of who last modified the tag.
