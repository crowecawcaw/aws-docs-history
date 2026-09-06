

# Analytics Tags
<a name="acxd-analytics-tags"></a>

Tag conversation events with sentiment classifications for reporting and analysis.

**Topics**
+ [CreateAnalyticsTag](#acxd-analytics-tags-createanalyticstag)
+ [ListAnalyticsTags](#acxd-analytics-tags-listanalyticstags)
+ [UpdateAnalyticsTag](#acxd-analytics-tags-updateanalyticstag)
+ [DeleteAnalyticsTag](#acxd-analytics-tags-deleteanalyticstag)
+ [Request Parameters](#acxd-analytics-tags-request-parameters)

## CreateAnalyticsTag
<a name="acxd-analytics-tags-createanalyticstag"></a>

Creates a new analytics tag.

### Input
<a name="acxd-analytics-tags-createanalyticstag-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| name | string | Yes | 
| type | enum | Yes | 
| description | string | Yes | 
| metadata | object | No | 

### Sample Request
<a name="acxd-analytics-tags-createanalyticstag-sample-request"></a>

```
await client.send(new CreateAnalyticsTagCommand({
  name: 'AnalyticsTagName',
  type: 'positive',
  description: 'Analytics Tag Description',
  metadata: { path: '/support', tags: ['support'] },
}));
```

### Output
<a name="acxd-analytics-tags-createanalyticstag-output"></a>

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
<a name="acxd-analytics-tags-createanalyticstag-errors"></a>
+ `ValidationException` (400)
+ `ConflictException` (409)
+ `InternalServerException` (500)

## ListAnalyticsTags
<a name="acxd-analytics-tags-listanalyticstags"></a>

Lists all analytics tags in the workspace.

### Input
<a name="acxd-analytics-tags-listanalyticstags-input"></a>

No parameters.

### Sample Request
<a name="acxd-analytics-tags-listanalyticstags-sample-request"></a>

```
await client.send(new ListAnalyticsTagsCommand({}));
```

### Output
<a name="acxd-analytics-tags-listanalyticstags-output"></a>

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
<a name="acxd-analytics-tags-listanalyticstags-errors"></a>
+ `ValidationException` (400)
+ `InternalServerException` (500)

## UpdateAnalyticsTag
<a name="acxd-analytics-tags-updateanalyticstag"></a>

Updates an existing analytics tag by name.

### Input
<a name="acxd-analytics-tags-updateanalyticstag-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| name | string | Yes | 
| type | enum | No | 
| description | string | No | 
| metadata | object | No | 

### Sample Request
<a name="acxd-analytics-tags-updateanalyticstag-sample-request"></a>

```
await client.send(new UpdateAnalyticsTagCommand({
    name: 'AnalyticsTagName',
    type: 'negative',
    description: 'Updated description',
    metadata: { path: '/support', tags: ['support'] },
}));
```

### Output
<a name="acxd-analytics-tags-updateanalyticstag-output"></a>

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
<a name="acxd-analytics-tags-updateanalyticstag-errors"></a>
+ `ResourceNotFoundException` (404)
+ `ValidationException` (400)
+ `InternalServerException` (500)

## DeleteAnalyticsTag
<a name="acxd-analytics-tags-deleteanalyticstag"></a>

Deletes an analytics tag by name.

### Input
<a name="acxd-analytics-tags-deleteanalyticstag-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| name | string | Yes | 

### Sample Request
<a name="acxd-analytics-tags-deleteanalyticstag-sample-request"></a>

```
await client.send(new DeleteAnalyticsTagCommand({
    name: 'AnalyticsTagName',
}));
```

### Output
<a name="acxd-analytics-tags-deleteanalyticstag-output"></a>

No response body.

### Errors
<a name="acxd-analytics-tags-deleteanalyticstag-errors"></a>
+ `ResourceNotFoundException` (404)
+ `ValidationException` (400)
+ `InternalServerException` (500)

## Request Parameters
<a name="acxd-analytics-tags-request-parameters"></a>

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
Description: Organizational metadata for categorizing the resource. See [Common Types](acxd-common-types.md).

`createdAt`  
Type: String  
Description: When the tag was created (ISO 8601).

`updatedAt`  
Type: String  
Description: When the tag was last modified (ISO 8601).

`lastUpdatedBy`  
Type: String  
Description: The identity of who last modified the tag.