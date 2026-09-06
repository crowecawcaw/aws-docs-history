

# Knowledge Bases
<a name="acxd-knowledge-bases"></a>

Manage knowledge sources for AI-powered responses. Knowledge bases can contain articles (structured Q&A) or documents (uploaded files). They must be published before they are available in conversations.

**Topics**
+ [ListKnowledgeBases](#acxd-knowledge-bases-listknowledgebases)
+ [CreateKnowledgeBase](#acxd-knowledge-bases-createknowledgebase)
+ [GetKnowledgeBase](#acxd-knowledge-bases-getknowledgebase)
+ [UpdateKnowledgeBase](#acxd-knowledge-bases-updateknowledgebase)
+ [DeleteKnowledgeBase](#acxd-knowledge-bases-deleteknowledgebase)
+ [CloneKnowledgeBase](#acxd-knowledge-bases-cloneknowledgebase)
+ [PublishKnowledgeBase](#acxd-knowledge-bases-publishknowledgebase)
+ [GetKnowledgeBasePublication](#acxd-knowledge-bases-getknowledgebasepublication)
+ [ListKnowledgeBasePublications](#acxd-knowledge-bases-listknowledgebasepublications)
+ [Request Parameters](#acxd-knowledge-bases-request-parameters)
+ [Response Config](#acxd-knowledge-bases-response-config)

## ListKnowledgeBases
<a name="acxd-knowledge-bases-listknowledgebases"></a>

Lists all knowledge bases in the workspace.

### Input
<a name="acxd-knowledge-bases-listknowledgebases-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| nextToken | string | No | 
| maxResults | integer | No | 

### Sample Request
<a name="acxd-knowledge-bases-listknowledgebases-sample-request"></a>

```
await client.send(new ListKnowledgeBasesCommand({}));
```

### Output
<a name="acxd-knowledge-bases-listknowledgebases-output"></a>

```
{
  "items": [
    {
      "knowledgeBaseId": "kb-a1b2c3d4-5678-90ab-cdef-1234567890ab",
      "name": "Product FAQ",
      "type": "articles",
      "description": "Common product questions",
      "response": { "summarize": true, "minConfidenceScore": 70, "k": 3 },
      "mainLanguageCode": "en-US",
      "languageCodes": ["en-US"],
      "creationStatus": "SUCCEEDED",
      "metadata": { "path": "/support", "tags": ["faq"] },
      "createdAt": "2026-08-01T12:00:00.000Z",
      "updatedAt": "2026-08-01T12:00:00.000Z",
      "lastUpdatedBy": "ci-deploy-bot"
    }
  ],
  "nextToken": null
}
```

### Errors
<a name="acxd-knowledge-bases-listknowledgebases-errors"></a>
+ `ValidationException` (400)
+ `InternalServerException` (500)

## CreateKnowledgeBase
<a name="acxd-knowledge-bases-createknowledgebase"></a>

Creates a new knowledge base.

### Input
<a name="acxd-knowledge-bases-createknowledgebase-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| name | string | Yes | 
| type | enum | Yes | 
| description | string | No | 
| response | object | No | 
| mainLanguageCode | enum | No | 
| languageCodes | array | No | 
| metadataSchema | object | No | 
| metadata | object | No | 

### Sample Request
<a name="acxd-knowledge-bases-createknowledgebase-sample-request"></a>

```
await client.send(new CreateKnowledgeBaseCommand({
  name: "Product FAQ",
  type: "articles",
  description: "Common product questions",
  response: {
    summarize: true,
    minConfidenceScore: 70,
    k: 3,
  },
  mainLanguageCode: "en-US",
  languageCodes: ["en-US"],
  metadata: { path: "/support", tags: ["faq"] },
}));
```

### Output
<a name="acxd-knowledge-bases-createknowledgebase-output"></a>

```
{
  "knowledgeBaseId": "kb-a1b2c3d4-5678-90ab-cdef-1234567890ab",
  "name": "Product FAQ",
  "type": "articles",
  "description": "Common product questions",
  "response": { "summarize": true, "minConfidenceScore": 70, "k": 3 },
  "mainLanguageCode": "en-US",
  "languageCodes": ["en-US"],
  "creationStatus": "SUCCEEDED",
  "metadata": { "path": "/support", "tags": ["faq"] },
  "createdAt": "2026-08-01T12:00:00.000Z",
  "updatedAt": "2026-08-01T12:00:00.000Z",
  "lastUpdatedBy": "ci-deploy-bot"
}
```

Same shape as ListKnowledgeBases item.

### Errors
<a name="acxd-knowledge-bases-createknowledgebase-errors"></a>
+ `ValidationException` (400)
+ `ConflictException` (409)
+ `InternalServerException` (500)

## GetKnowledgeBase
<a name="acxd-knowledge-bases-getknowledgebase"></a>

Gets a single knowledge base by ID.

### Input
<a name="acxd-knowledge-bases-getknowledgebase-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| knowledgeBaseId | string | Yes | 

### Sample Request
<a name="acxd-knowledge-bases-getknowledgebase-sample-request"></a>

```
await client.send(new GetKnowledgeBaseCommand({
    knowledgeBaseId: "kb-a1b2c3d4-5678-90ab-cdef-1234567890ab",
}));
```

### Output
<a name="acxd-knowledge-bases-getknowledgebase-output"></a>

```
{
  "knowledgeBaseId": "kb-a1b2c3d4-5678-90ab-cdef-1234567890ab",
  "name": "Product FAQ",
  "type": "articles",
  "description": "Common product questions",
  "response": { "summarize": true, "minConfidenceScore": 70, "k": 3 },
  "mainLanguageCode": "en-US",
  "languageCodes": ["en-US"],
  "creationStatus": "SUCCEEDED",
  "metadata": { "path": "/support", "tags": ["faq"] },
  "createdAt": "2026-08-01T12:00:00.000Z",
  "updatedAt": "2026-08-01T12:00:00.000Z",
  "lastUpdatedBy": "ci-deploy-bot"
}
```

### Errors
<a name="acxd-knowledge-bases-getknowledgebase-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## UpdateKnowledgeBase
<a name="acxd-knowledge-bases-updateknowledgebase"></a>

Updates an existing knowledge base. Only include fields you want to change.

### Input
<a name="acxd-knowledge-bases-updateknowledgebase-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| knowledgeBaseId | string | Yes | 
| name | string | No | 
| type | enum | No | 
| description | string | No | 
| response | object | No | 
| mainLanguageCode | enum | No | 
| languageCodes | array | No | 
| metadataSchema | object | No | 
| metadata | object | No | 

### Sample Request
<a name="acxd-knowledge-bases-updateknowledgebase-sample-request"></a>

```
await client.send(new UpdateKnowledgeBaseCommand({
  knowledgeBaseId: "kb-a1b2c3d4-5678-90ab-cdef-1234567890ab",
  name: "Product FAQ",
  type: "articles",
  description: "Updated - product FAQ and troubleshooting",
  response: {
    summarize: true,
    minConfidenceScore: 80,
    k: 5,
  },
  mainLanguageCode: "en-US",
  languageCodes: ["en-US"],
  metadata: { path: "/support", tags: ["faq"] },
}));
```

### Output
<a name="acxd-knowledge-bases-updateknowledgebase-output"></a>

```
{
  "knowledgeBaseId": "kb-a1b2c3d4-5678-90ab-cdef-1234567890ab",
  "name": "Product FAQ",
  "type": "articles",
  "description": "Updated - product FAQ and troubleshooting",
  "response": { "summarize": true, "minConfidenceScore": 80, "k": 5 },
  "mainLanguageCode": "en-US",
  "languageCodes": ["en-US"],
  "creationStatus": "SUCCEEDED",
  "metadata": { "path": "/support", "tags": ["faq"] },
  "createdAt": "2026-08-01T12:00:00.000Z",
  "updatedAt": "2026-08-01T12:40:00.000Z",
  "lastUpdatedBy": "ci-deploy-bot"
}
```

### Errors
<a name="acxd-knowledge-bases-updateknowledgebase-errors"></a>
+ `ResourceNotFoundException` (404)
+ `ValidationException` (400)
+ `InternalServerException` (500)

## DeleteKnowledgeBase
<a name="acxd-knowledge-bases-deleteknowledgebase"></a>

Deletes a knowledge base.

### Input
<a name="acxd-knowledge-bases-deleteknowledgebase-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| knowledgeBaseId | string | Yes | 

### Sample Request
<a name="acxd-knowledge-bases-deleteknowledgebase-sample-request"></a>

```
await client.send(new DeleteKnowledgeBaseCommand({
  knowledgeBaseId: "kb-a1b2c3d4-5678-90ab-cdef-1234567890ab",
}));
```

### Output
<a name="acxd-knowledge-bases-deleteknowledgebase-output"></a>

No response body.

### Errors
<a name="acxd-knowledge-bases-deleteknowledgebase-errors"></a>
+ `ResourceNotFoundException` (404)
+ `ValidationException` (400)
+ `InternalServerException` (500)

## CloneKnowledgeBase
<a name="acxd-knowledge-bases-cloneknowledgebase"></a>

Creates a copy of an existing knowledge base with a new ID.

### Input
<a name="acxd-knowledge-bases-cloneknowledgebase-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| knowledgeBaseId | string | Yes | 
| name | string | No | 
| portTranslations | boolean | No | 

### Sample Request
<a name="acxd-knowledge-bases-cloneknowledgebase-sample-request"></a>

```
await client.send(new CloneKnowledgeBaseCommand({
  knowledgeBaseId: created.knowledgeBaseId,
  name: "Product FAQ Clone",
  portTranslations: false,
}));
```

### Output
<a name="acxd-knowledge-bases-cloneknowledgebase-output"></a>

```
{
  "knowledgeBaseId": "kb-a1b2c3d4-5678-90ab-cdef-1234567890ab",
  "name": "Product FAQ Clone",
  "type": "articles",
  "description": "Updated - product FAQ and troubleshooting",
  "response": { "summarize": true, "minConfidenceScore": 80, "k": 5 },
  "mainLanguageCode": "en-US",
  "languageCodes": ["en-US"],
  "creationStatus": "SUCCEEDED",
  "metadata": { "path": "/support", "tags": ["faq"] },
  "createdAt": "2026-08-01T12:00:00.000Z",
  "updatedAt": "2026-08-01T12:40:00.000Z",
  "lastUpdatedBy": "ci-deploy-bot"
}
```

### Errors
<a name="acxd-knowledge-bases-cloneknowledgebase-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## PublishKnowledgeBase
<a name="acxd-knowledge-bases-publishknowledgebase"></a>

Publishes a knowledge base, triggering indexing and making it available for conversations.

### Input
<a name="acxd-knowledge-bases-publishknowledgebase-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| knowledgeBaseId | string | Yes | 
| deploymentId | string | No | 
| version | string | No | 
| description | string | No | 

### Sample Request
<a name="acxd-knowledge-bases-publishknowledgebase-sample-request"></a>

```
await client.send(new PublishKnowledgeBaseCommand({
  knowledgeBaseId: created.knowledgeBaseId,
  version: "1.0",
  description: "Initial publish",
}));
```

### Output
<a name="acxd-knowledge-bases-publishknowledgebase-output"></a>

```
{
  "deploymentId": "dep-a1b2c3d4-5678-90ab-cdef-1234567890ab",
  "knowledgeBaseId": "kb-a1b2c3d4-...",
  "status": "scheduled",
  "version": "1.0",
  "description": "Initial publish",
  "updatedBy": "ci-deploy-bot"
}
```

### Errors
<a name="acxd-knowledge-bases-publishknowledgebase-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## GetKnowledgeBasePublication
<a name="acxd-knowledge-bases-getknowledgebasepublication"></a>

Gets a specific publication record.

### Input
<a name="acxd-knowledge-bases-getknowledgebasepublication-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| knowledgeBaseId | string | Yes | 
| deploymentId | string | Yes | 

### Sample Request
<a name="acxd-knowledge-bases-getknowledgebasepublication-sample-request"></a>

```
await client.send(new GetKnowledgeBasePublicationCommand({
  knowledgeBaseId: created.knowledgeBaseId,
  deploymentId: publications.items[0].deploymentId,
}));
```

### Output
<a name="acxd-knowledge-bases-getknowledgebasepublication-output"></a>

Same shape as PublishKnowledgeBase output. Status may be `scheduled`, `published`, or `failed`.

```
{
  "deploymentId": "dep-a1b2c3d4-5678-90ab-cdef-1234567890ab",
  "knowledgeBaseId": "kb-a1b2c3d4-...",
  "status": "published",
  "version": "1.0",
  "description": "Initial publish",
  "updatedBy": "ci-deploy-bot"
}
```

### Errors
<a name="acxd-knowledge-bases-getknowledgebasepublication-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## ListKnowledgeBasePublications
<a name="acxd-knowledge-bases-listknowledgebasepublications"></a>

Lists all publications for a knowledge base.

### Input
<a name="acxd-knowledge-bases-listknowledgebasepublications-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| knowledgeBaseId | string | Yes | 
| nextToken | string | No | 
| maxResults | integer | No | 

### Sample Request
<a name="acxd-knowledge-bases-listknowledgebasepublications-sample-request"></a>

```
await client.send(new ListKnowledgeBasePublicationsCommand({
      knowledgeBaseId: "kb-a1b2c3d4-...",
}));
```

### Output
<a name="acxd-knowledge-bases-listknowledgebasepublications-output"></a>

```
{
  "items": [
    {
      "deploymentId": "dep-a1b2c3d4-...",
      "knowledgeBaseId": "kb-a1b2c3d4-...",
      "status": "published",
      "version": "1.0",
      "description": "Initial publish",
      "updatedBy": "ci-deploy-bot"
    }
  ]
}
```

### Errors
<a name="acxd-knowledge-bases-listknowledgebasepublications-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## Request Parameters
<a name="acxd-knowledge-bases-request-parameters"></a>

### knowledgeBaseId
<a name="acxd-knowledge-bases-request-parameters-knowledgebaseid"></a>

Type: String

The knowledge base ID.

### name
<a name="acxd-knowledge-bases-request-parameters-name"></a>

Type: String

Knowledge base name. Alphanumeric \+ spaces/dashes/underscores, 1–100 characters.

### type
<a name="acxd-knowledge-bases-request-parameters-type"></a>

Type: String

The type of knowledge base. One of: `articles` or `documents`.

### description
<a name="acxd-knowledge-bases-request-parameters-description"></a>

Type: String

Description. Max 200 characters.

### response
<a name="acxd-knowledge-bases-request-parameters-response"></a>

Type: Object

Response behavior configuration. See Response Config.

### mainLanguageCode
<a name="acxd-knowledge-bases-request-parameters-mainlanguagecode"></a>

Type: String

Primary language. See Common Types.

### languageCodes
<a name="acxd-knowledge-bases-request-parameters-languagecodes"></a>

Type: Array

Supported languages. See Common Types.

### metadataSchema
<a name="acxd-knowledge-bases-request-parameters-metadataschema"></a>

Type: Object

A JSON Schema defining the structure of article/document metadata.

### metadata
<a name="acxd-knowledge-bases-request-parameters-metadata"></a>

Type: Object

Organizational metadata. See Common Types.

### creationStatus
<a name="acxd-knowledge-bases-request-parameters-creationstatus"></a>

Type: String

Creation status of the knowledge base. One of: `PENDING`, `SUCCEEDED`.

### deploymentId
<a name="acxd-knowledge-bases-request-parameters-deploymentid"></a>

Type: String

The publication/deployment ID.

### version
<a name="acxd-knowledge-bases-request-parameters-version"></a>

Type: String

Version label for a publication.

### status
<a name="acxd-knowledge-bases-request-parameters-status"></a>

Type: String

Publication status. One of: `scheduled`, `published`, `failed`.

### portTranslations
<a name="acxd-knowledge-bases-request-parameters-porttranslations"></a>

Type: Boolean

Whether to copy translations when cloning.

### nextToken
<a name="acxd-knowledge-bases-request-parameters-nexttoken"></a>

Type: String

Pagination token. See Common Types.

### maxResults
<a name="acxd-knowledge-bases-request-parameters-maxresults"></a>

Type: Integer

Max items per page (1–100). See Common Types.

### createdAt
<a name="acxd-knowledge-bases-request-parameters-createdat"></a>

Type: String

When the knowledge base was created (ISO 8601).

### updatedAt
<a name="acxd-knowledge-bases-request-parameters-updatedat"></a>

Type: String

When the knowledge base was last modified (ISO 8601).

### lastUpdatedBy
<a name="acxd-knowledge-bases-request-parameters-lastupdatedby"></a>

Type: String

The identity of who last modified the knowledge base.

## Response Config
<a name="acxd-knowledge-bases-response-config"></a>


| Field | Type | Required | 
| --- | --- | --- | 
| summarize | boolean | No | 
| minConfidenceScore | float | No | 
| temperature | float | No | 
| topP | float | No | 
| k | integer | No | 

### summarize
<a name="acxd-knowledge-bases-response-config-summarize"></a>

Type: Boolean

Whether to summarize retrieved content before returning to the user.

### minConfidenceScore
<a name="acxd-knowledge-bases-response-config-minconfidencescore"></a>

Type: Number

Minimum confidence threshold (0–100). Results below this score are not returned.

### temperature
<a name="acxd-knowledge-bases-response-config-temperature"></a>

Type: Number

LLM temperature for response generation.

### topP
<a name="acxd-knowledge-bases-response-config-topp"></a>

Type: Number

Top-p sampling parameter.

### k
<a name="acxd-knowledge-bases-response-config-k"></a>

Type: Integer

Number of results to retrieve from the knowledge base.