# KnowledgeBase Documents

Manage uploaded files within a knowledge base. Documents are registered via the
API and uploaded via pre-signed URLs.

###### Contents

- [ListKnowledgeBaseDocuments](#acxd-knowledge-base-documents-listknowledgebasedocuments "#acxd-knowledge-base-documents-listknowledgebasedocuments")
- [GetKnowledgeBaseDocument](#acxd-knowledge-base-documents-getknowledgebasedocument "#acxd-knowledge-base-documents-getknowledgebasedocument")
- [PutKnowledgeBaseDocument](#acxd-knowledge-base-documents-putknowledgebasedocument "#acxd-knowledge-base-documents-putknowledgebasedocument")
- [DeleteKnowledgeBaseDocument](#acxd-knowledge-base-documents-deleteknowledgebasedocument "#acxd-knowledge-base-documents-deleteknowledgebasedocument")
- [Request Parameters](#acxd-knowledge-base-documents-request-parameters "#acxd-knowledge-base-documents-request-parameters")

## ListKnowledgeBaseDocuments

Lists all documents in a knowledge base.

### Input

| Parameter         | Type    | Required |
| ----------------- | ------- | -------- |
| `knowledgeBaseId` | string  | Yes      |
| `nextToken`       | string  | No       |
| `maxResults`      | integer | No       |

### Sample Request

```
client.send(new ListKnowledgeBaseDocumentsCommand({
      knowledgeBaseId: KNOWLEDGE_BASE_ID,
    }));
```

### Output

```
{
  "items": [
    {
      "documentId": "product-guide-v2.pdf",
      "uploadStatus": "UPLOADED",
      "contentType": "application/pdf",
      "customerMetadata": { "category": "guides" },
      "createdAt": "2026-08-01T12:00:00.000Z"
    }
  ],
  "nextToken": null
}
```

### Errors

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## GetKnowledgeBaseDocument

Gets a pre-signed download URL for a document.

### Input

| Parameter         | Type   | Required |
| ----------------- | ------ | -------- |
| `knowledgeBaseId` | string | Yes      |
| `documentId`      | string | Yes      |

### Sample Request

```
await client.send(new GetKnowledgeBaseDocumentCommand({
      knowledgeBaseId: KNOWLEDGE_BASE_ID,
      documentId: "product-guide-v2.pdf",
    }));
```

### Output

```
{
  "url": "https://s3.amazonaws.com/bucket/path/document.pdf?X-Amz-Signature=..."
}
```

### Errors

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## PutKnowledgeBaseDocument

Registers a document and returns a pre-signed upload URL. Use the returned URL
and fields to upload the file content.

### Input

| Parameter          | Type   | Required |
| ------------------ | ------ | -------- |
| `knowledgeBaseId`  | string | Yes      |
| `documentId`       | string | Yes      |
| `contentType`      | string | Yes      |
| `customerMetadata` | object | No       |

### Sample Request

```
await client.send(new PutKnowledgeBaseDocumentCommand({
  knowledgeBaseId: KNOWLEDGE_BASE_ID,
  documentId: "product-guide-v2.pdf",
  contentType: "application/pdf",
  customerMetadata: { category: "guides", version: "2.0" },
}));
```

### Output

```
{
  "url": "https://s3.amazonaws.com/bucket/upload-path",
  "fields": {
    "key": "...",
    "policy": "...",
    "x-amz-signature": "..."
  }
}
```

###### Note

Use the returned `url` and `fields` to perform a multipart form upload of
your document content.

### Errors

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## DeleteKnowledgeBaseDocument

Deletes a document.

### Input

| Parameter         | Type   | Required |
| ----------------- | ------ | -------- |
| `knowledgeBaseId` | string | Yes      |
| `documentId`      | string | Yes      |

### Sample Request

```
await client.send(new DeleteKnowledgeBaseDocumentCommand({
  knowledgeBaseId: KNOWLEDGE_BASE_ID,
  documentId: "product-guide-v2.pdf",
}));
```

### Output

No response body.

### Errors

- `ResourceNotFoundException` (404)
- `ValidationException` (400)
- `InternalServerException` (500)

## Request Parameters

`knowledgeBaseId`

Type: String

The knowledge base that contains the documents.

`documentId`

Type: String

The document identifier. User-provided, max 255 characters (e.g., a filename like
`product-guide-v2.pdf` ).

`contentType`

Type: String

MIME type of the document (e.g., `application/pdf` , `text/plain` , `text/html` ).

`customerMetadata`

Type: Object

Free-form metadata for the document (structure defined by the knowledge base's
`metadataSchema` ).

`uploadStatus`

Type: String

The document's upload status. One of: `PENDING` (registered but not yet uploaded),
`UPLOADED` (file received), `DELETED` .

`url`

Type: String

Pre-signed S3 URL for upload or download.

`fields`

Type: Object

Form fields required for multipart upload (returned by PutKnowledgeBaseDocument).

`createdAt`

Type: String

When the document was registered (ISO 8601).

`nextToken`

Type: String

Pagination token. See Common Types.

`maxResults`

Type: Integer

Max items per page (1–100). See Common Types.
