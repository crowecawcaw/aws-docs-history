# Knowledge Bases

Manage knowledge sources for AI-powered responses. Knowledge bases can contain articles
(structured Q&A) or documents (uploaded files). They must be published before they are
available in conversations.

###### Contents

- [ListKnowledgeBases](#acxd-knowledge-bases-listknowledgebases "#acxd-knowledge-bases-listknowledgebases")
- [CreateKnowledgeBase](#acxd-knowledge-bases-createknowledgebase "#acxd-knowledge-bases-createknowledgebase")
- [GetKnowledgeBase](#acxd-knowledge-bases-getknowledgebase "#acxd-knowledge-bases-getknowledgebase")
- [UpdateKnowledgeBase](#acxd-knowledge-bases-updateknowledgebase "#acxd-knowledge-bases-updateknowledgebase")
- [DeleteKnowledgeBase](#acxd-knowledge-bases-deleteknowledgebase "#acxd-knowledge-bases-deleteknowledgebase")
- [CloneKnowledgeBase](#acxd-knowledge-bases-cloneknowledgebase "#acxd-knowledge-bases-cloneknowledgebase")
- [PublishKnowledgeBase](#acxd-knowledge-bases-publishknowledgebase "#acxd-knowledge-bases-publishknowledgebase")
- [GetKnowledgeBasePublication](#acxd-knowledge-bases-getknowledgebasepublication "#acxd-knowledge-bases-getknowledgebasepublication")
- [ListKnowledgeBasePublications](#acxd-knowledge-bases-listknowledgebasepublications "#acxd-knowledge-bases-listknowledgebasepublications")
- [Request Parameters](#acxd-knowledge-bases-request-parameters "#acxd-knowledge-bases-request-parameters")
- [Response Config](#acxd-knowledge-bases-response-config "#acxd-knowledge-bases-response-config")

## ListKnowledgeBases

Lists all knowledge bases in the workspace.

### Input

| Parameter    | Type    | Required |
| ------------ | ------- | -------- |
| `nextToken`  | string  | No       |
| `maxResults` | integer | No       |

### Sample Request

```
await client.send(new ListKnowledgeBasesCommand({}));
```

### Output

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

- `ValidationException` (400)
- `InternalServerException` (500)

## CreateKnowledgeBase

Creates a new knowledge base.

### Input

| Parameter          | Type   | Required |
| ------------------ | ------ | -------- |
| `name`             | string | Yes      |
| `type`             | enum   | Yes      |
| `description`      | string | No       |
| `response`         | object | No       |
| `mainLanguageCode` | enum   | No       |
| `languageCodes`    | array  | No       |
| `metadataSchema`   | object | No       |
| `metadata`         | object | No       |

### Sample Request

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

- `ValidationException` (400)
- `ConflictException` (409)
- `InternalServerException` (500)

## GetKnowledgeBase

Gets a single knowledge base by ID.

### Input

| Parameter         | Type   | Required |
| ----------------- | ------ | -------- |
| `knowledgeBaseId` | string | Yes      |

### Sample Request

```
await client.send(new GetKnowledgeBaseCommand({
    knowledgeBaseId: "kb-a1b2c3d4-5678-90ab-cdef-1234567890ab",
}));
```

### Output

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

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## UpdateKnowledgeBase

Updates an existing knowledge base. Only include fields you want to change.

### Input

| Parameter          | Type   | Required |
| ------------------ | ------ | -------- |
| `knowledgeBaseId`  | string | Yes      |
| `name`             | string | No       |
| `type`             | enum   | No       |
| `description`      | string | No       |
| `response`         | object | No       |
| `mainLanguageCode` | enum   | No       |
| `languageCodes`    | array  | No       |
| `metadataSchema`   | object | No       |
| `metadata`         | object | No       |

### Sample Request

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

- `ResourceNotFoundException` (404)
- `ValidationException` (400)
- `InternalServerException` (500)

## DeleteKnowledgeBase

Deletes a knowledge base.

### Input

| Parameter         | Type   | Required |
| ----------------- | ------ | -------- |
| `knowledgeBaseId` | string | Yes      |

### Sample Request

```
await client.send(new DeleteKnowledgeBaseCommand({
  knowledgeBaseId: "kb-a1b2c3d4-5678-90ab-cdef-1234567890ab",
}));
```

### Output

No response body.

### Errors

- `ResourceNotFoundException` (404)
- `ValidationException` (400)
- `InternalServerException` (500)

## CloneKnowledgeBase

Creates a copy of an existing knowledge base with a new ID.

### Input

| Parameter          | Type    | Required |
| ------------------ | ------- | -------- |
| `knowledgeBaseId`  | string  | Yes      |
| `name`             | string  | No       |
| `portTranslations` | boolean | No       |

### Sample Request

```
await client.send(new CloneKnowledgeBaseCommand({
  knowledgeBaseId: created.knowledgeBaseId,
  name: "Product FAQ Clone",
  portTranslations: false,
}));
```

### Output

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

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## PublishKnowledgeBase

Publishes a knowledge base, triggering indexing and making it available for
conversations.

### Input

| Parameter         | Type   | Required |
| ----------------- | ------ | -------- |
| `knowledgeBaseId` | string | Yes      |
| `deploymentId`    | string | No       |
| `version`         | string | No       |
| `description`     | string | No       |

### Sample Request

```
await client.send(new PublishKnowledgeBaseCommand({
  knowledgeBaseId: created.knowledgeBaseId,
  version: "1.0",
  description: "Initial publish",
}));
```

### Output

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

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## GetKnowledgeBasePublication

Gets a specific publication record.

### Input

| Parameter         | Type   | Required |
| ----------------- | ------ | -------- |
| `knowledgeBaseId` | string | Yes      |
| `deploymentId`    | string | Yes      |

### Sample Request

```
await client.send(new GetKnowledgeBasePublicationCommand({
  knowledgeBaseId: created.knowledgeBaseId,
  deploymentId: publications.items[0].deploymentId,
}));
```

### Output

Same shape as PublishKnowledgeBase output. Status may be `scheduled`,
`published`, or `failed`.

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

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## ListKnowledgeBasePublications

Lists all publications for a knowledge base.

### Input

| Parameter         | Type    | Required |
| ----------------- | ------- | -------- |
| `knowledgeBaseId` | string  | Yes      |
| `nextToken`       | string  | No       |
| `maxResults`      | integer | No       |

### Sample Request

```
await client.send(new ListKnowledgeBasePublicationsCommand({
      knowledgeBaseId: "kb-a1b2c3d4-...",
}));
```

### Output

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

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## Request Parameters

### knowledgeBaseId

Type: String

The knowledge base ID.

### name

Type: String

Knowledge base name. Alphanumeric + spaces/dashes/underscores, 1–100
characters.

### type

Type: String

The type of knowledge base. One of: `articles` or `documents`.

### description

Type: String

Description. Max 200 characters.

### response

Type: Object

Response behavior configuration. See Response Config.

### mainLanguageCode

Type: String

Primary language. See Common Types.

### languageCodes

Type: Array

Supported languages. See Common Types.

### metadataSchema

Type: Object

A JSON Schema defining the structure of article/document metadata.

### metadata

Type: Object

Organizational metadata. See Common Types.

### creationStatus

Type: String

Creation status of the knowledge base. One of: `PENDING`,
`SUCCEEDED`.

### deploymentId

Type: String

The publication/deployment ID.

### version

Type: String

Version label for a publication.

### status

Type: String

Publication status. One of: `scheduled`, `published`,
`failed`.

### portTranslations

Type: Boolean

Whether to copy translations when cloning.

### nextToken

Type: String

Pagination token. See Common Types.

### maxResults

Type: Integer

Max items per page (1–100). See Common Types.

### createdAt

Type: String

When the knowledge base was created (ISO 8601).

### updatedAt

Type: String

When the knowledge base was last modified (ISO 8601).

### lastUpdatedBy

Type: String

The identity of who last modified the knowledge base.

## Response Config

| Field                | Type    | Required |
| -------------------- | ------- | -------- |
| `summarize`          | boolean | No       |
| `minConfidenceScore` | float   | No       |
| `temperature`        | float   | No       |
| `topP`               | float   | No       |
| `k`                  | integer | No       |

### summarize

Type: Boolean

Whether to summarize retrieved content before returning to the user.

### minConfidenceScore

Type: Number

Minimum confidence threshold (0–100). Results below this score are not
returned.

### temperature

Type: Number

LLM temperature for response generation.

### topP

Type: Number

Top-p sampling parameter.

### k

Type: Integer

Number of results to retrieve from the knowledge base.
