# Knowledge Base Articles

Manage structured Q&A content within a knowledge base. Articles contain a question
and one or more response messages.

###### Contents

- [ListKnowledgeBaseArticles](#acxd-knowledge-base-articles-listknowledgebasearticles "#acxd-knowledge-base-articles-listknowledgebasearticles")
- [CreateKnowledgeBaseArticle](#acxd-knowledge-base-articles-createknowledgebasearticle "#acxd-knowledge-base-articles-createknowledgebasearticle")
- [GetKnowledgeBaseArticle](#acxd-knowledge-base-articles-getknowledgebasearticle "#acxd-knowledge-base-articles-getknowledgebasearticle")
- [UpdateKnowledgeBaseArticle](#acxd-knowledge-base-articles-updateknowledgebasearticle "#acxd-knowledge-base-articles-updateknowledgebasearticle")
- [DeleteKnowledgeBaseArticle](#acxd-knowledge-base-articles-deleteknowledgebasearticle "#acxd-knowledge-base-articles-deleteknowledgebasearticle")
- [Request Parameters](#acxd-knowledge-base-articles-request-parameters "#acxd-knowledge-base-articles-request-parameters")

## ListKnowledgeBaseArticles

Lists all articles in a knowledge base.

### Input

| Parameter         | Type    | Required |
| ----------------- | ------- | -------- |
| `knowledgeBaseId` | string  | Yes      |
| `nextToken`       | string  | No       |
| `maxResults`      | integer | No       |

### Sample Request

```
await client.send(new ListKnowledgeBaseArticlesCommand({
      knowledgeBaseId: "kb-a1b2c3d4-...",
}));
```

### Output

```
{
  "items": [
    {
      "knowledgeBaseId": "kb-a1b2c3d4-...",
      "articleId": "art-e5f6g7h8-5678-90ab-cdef-1234567890ab",
      "question": {
        "text": "How do I reset my password?",
        "messageId": "5701b504-b3ae-4d65-9834-bb65b5dc7fb0"
      },
      "responses": [{ "type": "text", "body": "Go to Settings > Security > Reset Password.", "messageId": "83c542e2-bb98-4f48-b2b9-292af18796e7" }],
      "tags": ["account"],
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
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## CreateKnowledgeBaseArticle

Creates a new article in a knowledge base.

### Input

| Parameter         | Type   | Required |
| ----------------- | ------ | -------- |
| `knowledgeBaseId` | string | Yes      |
| `question`        | object | Yes      |
| `responses`       | array  | Yes      |
| `articleMetadata` | object | No       |
| `payload`         | string | No       |
| `tags`            | array  | No       |

### Sample Request

```
await client.send(new CreateKnowledgeBaseArticleCommand({
  knowledgeBaseId: "kb-a1b2c3d4-...",
  question: { text: "How do I reset my password?" },
  responses: [
    { type: "text", body: "Go to Settings > Security > Reset Password." },
    { type: "text", body: "If you still have trouble, contact support." },
  ],
  tags: ["account", "security"],
}));
```

### Output

```
{
  "knowledgeBaseId": "kb-a1b2c3d4-...",
  "articleId": "art-e5f6g7h8-5678-90ab-cdef-1234567890ab",
  "question": {
    "text": "How do I reset my password?",
    "messageId": "5701b504-b3ae-4d65-9834-bb65b5dc7fb0"
  },
  "responses": [
    {
      "type": "text",
      "body": "Go to Settings > Security > Reset Password.",
      "messageId": "83c542e2-bb98-4f48-b2b9-292af18796e7"
    },
    {
      "type": "text",
      "body": "If you still have trouble, contact support.",
      "messageId": "806d8c14-d0c0-4eee-a26f-be7f74fb3ad7"
    }
  ],
  "tags": ["account", "security"],
  "createdAt": "2026-08-01T12:00:00.000Z",
  "updatedAt": "2026-08-01T12:00:00.000Z",
  "lastUpdatedBy": "ci-deploy-bot"
}
```

### Errors

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## GetKnowledgeBaseArticle

Gets a single article by ID.

### Input

| Parameter         | Type   | Required |
| ----------------- | ------ | -------- |
| `knowledgeBaseId` | string | Yes      |
| `articleId`       | string | Yes      |

### Sample Request

```
await client.send(new GetKnowledgeBaseArticleCommand({
  knowledgeBaseId: "kb-a1b2c3d4-...",
  articleId: "art-e5f6g7h8-5678-90ab-cdef-1234567890ab",
}));
```

### Output

```
{
  "knowledgeBaseId": "kb-a1b2c3d4-...",
  "articleId": "art-e5f6g7h8-5678-90ab-cdef-1234567890ab",
  "question": {
    "text": "How do I reset my password?",
    "messageId": "5701b504-b3ae-4d65-9834-bb65b5dc7fb0"
  },
  "responses": [
    {
      "type": "text",
      "body": "Go to Settings > Security > Reset Password.",
      "messageId": "83c542e2-bb98-4f48-b2b9-292af18796e7"
    },
    {
      "type": "text",
      "body": "If you still have trouble, contact support.",
      "messageId": "806d8c14-d0c0-4eee-a26f-be7f74fb3ad7"
    }
  ],
  "tags": ["account", "security"],
  "createdAt": "2026-08-01T12:00:00.000Z",
  "updatedAt": "2026-08-01T12:00:00.000Z",
  "lastUpdatedBy": "ci-deploy-bot"
}
```

### Errors

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## UpdateKnowledgeBaseArticle

Updates an existing article. Only include fields you want to change.

### Input

| Parameter         | Type   | Required |
| ----------------- | ------ | -------- |
| `knowledgeBaseId` | string | Yes      |
| `articleId`       | string | Yes      |
| `question`        | object | No       |
| `responses`       | array  | No       |
| `articleMetadata` | object | No       |
| `payload`         | string | No       |
| `tags`            | array  | No       |

### Sample Request

```
await client.send(new UpdateKnowledgeBaseArticleCommand({
  knowledgeBaseId: "kb-a1b2c3d4-...",
  articleId: "art-e5f6g7h8-5678-90ab-cdef-1234567890ab",
  question: { text: "How do I reset or change my password?" },
  responses: [
    { type: "text", body: "Go to Settings > Security > Reset Password." },
    { type: "text", body: "You can also use the 'Forgot Password' link on the login page." },
  ],
  tags: ["account", "security"],
}));
```

### Output

```
{
  "knowledgeBaseId": "kb-a1b2c3d4-...",
  "articleId": "art-e5f6g7h8-5678-90ab-cdef-1234567890ab",
  "question": {
    "text": "How do I reset or change my password?",
    "messageId": "5f767bcd-462d-4d2e-9651-408459d06b42"
  },
  "responses": [
    {
      "type": "text",
      "body": "Go to Settings > Security > Reset Password.",
      "messageId": "b2edcfab-b436-4c4e-8d0d-7cbc4cba0643"
    },
    {
      "type": "text",
      "body": "You can also use the 'Forgot Password' link on the login page.",
      "messageId": "75c2d1b0-f98c-4db6-abfa-8e0aad41fa56"
    }
  ],
  "tags": ["account", "security"],
  "createdAt": "2026-08-01T12:00:00.000Z",
  "updatedAt": "2026-08-01T12:00:00.000Z",
  "lastUpdatedBy": "ci-deploy-bot"
}
```

### Errors

- `ResourceNotFoundException` (404)
- `ValidationException` (400)
- `InternalServerException` (500)

## DeleteKnowledgeBaseArticle

Deletes an article.

### Input

| Parameter         | Type   | Required |
| ----------------- | ------ | -------- |
| `knowledgeBaseId` | string | Yes      |
| `articleId`       | string | Yes      |

### Sample Request

```
await client.send(new DeleteKnowledgeBaseArticleCommand({
  knowledgeBaseId: "kb-a1b2c3d4-...",
  articleId: "art-e5f6g7h8-5678-90ab-cdef-1234567890ab",
}));
```

### Output

No response body.

### Errors

- `ResourceNotFoundException` (404)
- `ValidationException` (400)
- `InternalServerException` (500)

## Request Parameters

### knowledgeBaseId

Type: String

The knowledge base that contains the articles.

### articleId

Type: String

The article ID.

### question

Type: Object

### question.text

Type: String

Required. The article's question or title. This is what gets matched against user
queries.

### question.messageId

Type: String

Generated upon Create.

### question.skipTranslation

Type: Boolean

### question.translated

Type: Boolean

### responses

Type: Array

Response messages returned when this article matches. Each entry is a message
object with a `body` field.

**Example:**

```
[
  { "type": "text", "body": "Go to Settings > Security > Reset Password." },
  { "type": "text", "body": "If you still have trouble, contact support." }
]
```

### articleMetadata

Type: Object

Free-form metadata for the article (structure defined by the knowledge base's
`metadataSchema`).

### payload

Type: String

Raw content for the article. Max 10,000 characters.

### tags

Type: Array

Classification tags for the article (max 5, each max 256 characters).

### createdAt

Type: String

When the article was created (ISO 8601).

### updatedAt

Type: String

When the article was last modified (ISO 8601).

### lastUpdatedBy

Type: String

The identity of who last modified the article.

### nextToken

Type: String

Pagination token. See Common Types.

### maxResults

Type: Integer

Max items per page (1–100). See Common Types.
