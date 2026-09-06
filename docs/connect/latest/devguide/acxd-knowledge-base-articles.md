

# Knowledge Base Articles
<a name="acxd-knowledge-base-articles"></a>

Manage structured Q&A content within a knowledge base. Articles contain a question and one or more response messages.

**Topics**
+ [ListKnowledgeBaseArticles](#acxd-knowledge-base-articles-listknowledgebasearticles)
+ [CreateKnowledgeBaseArticle](#acxd-knowledge-base-articles-createknowledgebasearticle)
+ [GetKnowledgeBaseArticle](#acxd-knowledge-base-articles-getknowledgebasearticle)
+ [UpdateKnowledgeBaseArticle](#acxd-knowledge-base-articles-updateknowledgebasearticle)
+ [DeleteKnowledgeBaseArticle](#acxd-knowledge-base-articles-deleteknowledgebasearticle)
+ [Request Parameters](#acxd-knowledge-base-articles-request-parameters)

## ListKnowledgeBaseArticles
<a name="acxd-knowledge-base-articles-listknowledgebasearticles"></a>

Lists all articles in a knowledge base.

### Input
<a name="acxd-knowledge-base-articles-listknowledgebasearticles-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| knowledgeBaseId | string | Yes | 
| nextToken | string | No | 
| maxResults | integer | No | 

### Sample Request
<a name="acxd-knowledge-base-articles-listknowledgebasearticles-sample-request"></a>

```
await client.send(new ListKnowledgeBaseArticlesCommand({
      knowledgeBaseId: "kb-a1b2c3d4-...",
}));
```

### Output
<a name="acxd-knowledge-base-articles-listknowledgebasearticles-output"></a>

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
<a name="acxd-knowledge-base-articles-listknowledgebasearticles-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## CreateKnowledgeBaseArticle
<a name="acxd-knowledge-base-articles-createknowledgebasearticle"></a>

Creates a new article in a knowledge base.

### Input
<a name="acxd-knowledge-base-articles-createknowledgebasearticle-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| knowledgeBaseId | string | Yes | 
| question | object | Yes | 
| responses | array | Yes | 
| articleMetadata | object | No | 
| payload | string | No | 
| tags | array | No | 

### Sample Request
<a name="acxd-knowledge-base-articles-createknowledgebasearticle-sample-request"></a>

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
<a name="acxd-knowledge-base-articles-createknowledgebasearticle-output"></a>

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
<a name="acxd-knowledge-base-articles-createknowledgebasearticle-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## GetKnowledgeBaseArticle
<a name="acxd-knowledge-base-articles-getknowledgebasearticle"></a>

Gets a single article by ID.

### Input
<a name="acxd-knowledge-base-articles-getknowledgebasearticle-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| knowledgeBaseId | string | Yes | 
| articleId | string | Yes | 

### Sample Request
<a name="acxd-knowledge-base-articles-getknowledgebasearticle-sample-request"></a>

```
await client.send(new GetKnowledgeBaseArticleCommand({
  knowledgeBaseId: "kb-a1b2c3d4-...",
  articleId: "art-e5f6g7h8-5678-90ab-cdef-1234567890ab",
}));
```

### Output
<a name="acxd-knowledge-base-articles-getknowledgebasearticle-output"></a>

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
<a name="acxd-knowledge-base-articles-getknowledgebasearticle-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## UpdateKnowledgeBaseArticle
<a name="acxd-knowledge-base-articles-updateknowledgebasearticle"></a>

Updates an existing article. Only include fields you want to change.

### Input
<a name="acxd-knowledge-base-articles-updateknowledgebasearticle-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| knowledgeBaseId | string | Yes | 
| articleId | string | Yes | 
| question | object | No | 
| responses | array | No | 
| articleMetadata | object | No | 
| payload | string | No | 
| tags | array | No | 

### Sample Request
<a name="acxd-knowledge-base-articles-updateknowledgebasearticle-sample-request"></a>

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
<a name="acxd-knowledge-base-articles-updateknowledgebasearticle-output"></a>

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
<a name="acxd-knowledge-base-articles-updateknowledgebasearticle-errors"></a>
+ `ResourceNotFoundException` (404)
+ `ValidationException` (400)
+ `InternalServerException` (500)

## DeleteKnowledgeBaseArticle
<a name="acxd-knowledge-base-articles-deleteknowledgebasearticle"></a>

Deletes an article.

### Input
<a name="acxd-knowledge-base-articles-deleteknowledgebasearticle-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| knowledgeBaseId | string | Yes | 
| articleId | string | Yes | 

### Sample Request
<a name="acxd-knowledge-base-articles-deleteknowledgebasearticle-sample-request"></a>

```
await client.send(new DeleteKnowledgeBaseArticleCommand({
  knowledgeBaseId: "kb-a1b2c3d4-...",
  articleId: "art-e5f6g7h8-5678-90ab-cdef-1234567890ab",
}));
```

### Output
<a name="acxd-knowledge-base-articles-deleteknowledgebasearticle-output"></a>

No response body.

### Errors
<a name="acxd-knowledge-base-articles-deleteknowledgebasearticle-errors"></a>
+ `ResourceNotFoundException` (404)
+ `ValidationException` (400)
+ `InternalServerException` (500)

## Request Parameters
<a name="acxd-knowledge-base-articles-request-parameters"></a>

### knowledgeBaseId
<a name="acxd-knowledge-base-articles-request-parameters-knowledgebaseid"></a>

Type: String

The knowledge base that contains the articles.

### articleId
<a name="acxd-knowledge-base-articles-request-parameters-articleid"></a>

Type: String

The article ID.

### question
<a name="acxd-knowledge-base-articles-request-parameters-question"></a>

Type: Object

### question.text
<a name="acxd-knowledge-base-articles-request-parameters-question-text"></a>

Type: String

Required. The article's question or title. This is what gets matched against user queries.

### question.messageId
<a name="acxd-knowledge-base-articles-request-parameters-question-messageid"></a>

Type: String

Generated upon Create.

### question.skipTranslation
<a name="acxd-knowledge-base-articles-request-parameters-question-skiptranslation"></a>

Type: Boolean

### question.translated
<a name="acxd-knowledge-base-articles-request-parameters-question-translated"></a>

Type: Boolean

### responses
<a name="acxd-knowledge-base-articles-request-parameters-responses"></a>

Type: Array

Response messages returned when this article matches. Each entry is a message object with a `body` field.

**Example:**

```
[
  { "type": "text", "body": "Go to Settings > Security > Reset Password." },
  { "type": "text", "body": "If you still have trouble, contact support." }
]
```

### articleMetadata
<a name="acxd-knowledge-base-articles-request-parameters-articlemetadata"></a>

Type: Object

Free-form metadata for the article (structure defined by the knowledge base's `metadataSchema`).

### payload
<a name="acxd-knowledge-base-articles-request-parameters-payload"></a>

Type: String

Raw content for the article. Max 10,000 characters.

### tags
<a name="acxd-knowledge-base-articles-request-parameters-tags"></a>

Type: Array

Classification tags for the article (max 5, each max 256 characters).

### createdAt
<a name="acxd-knowledge-base-articles-request-parameters-createdat"></a>

Type: String

When the article was created (ISO 8601).

### updatedAt
<a name="acxd-knowledge-base-articles-request-parameters-updatedat"></a>

Type: String

When the article was last modified (ISO 8601).

### lastUpdatedBy
<a name="acxd-knowledge-base-articles-request-parameters-lastupdatedby"></a>

Type: String

The identity of who last modified the article.

### nextToken
<a name="acxd-knowledge-base-articles-request-parameters-nexttoken"></a>

Type: String

Pagination token. See Common Types.

### maxResults
<a name="acxd-knowledge-base-articles-request-parameters-maxresults"></a>

Type: Integer

Max items per page (1–100). See Common Types.