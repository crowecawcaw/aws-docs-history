

# KnowledgeBase Documents
<a name="acxd-knowledge-base-documents"></a>

Manage uploaded files within a knowledge base. Documents are registered via the API and uploaded via pre-signed URLs.

**Topics**
+ [ListKnowledgeBaseDocuments](#acxd-knowledge-base-documents-listknowledgebasedocuments)
+ [GetKnowledgeBaseDocument](#acxd-knowledge-base-documents-getknowledgebasedocument)
+ [PutKnowledgeBaseDocument](#acxd-knowledge-base-documents-putknowledgebasedocument)
+ [DeleteKnowledgeBaseDocument](#acxd-knowledge-base-documents-deleteknowledgebasedocument)
+ [Request Parameters](#acxd-knowledge-base-documents-request-parameters)

## ListKnowledgeBaseDocuments
<a name="acxd-knowledge-base-documents-listknowledgebasedocuments"></a>

Lists all documents in a knowledge base.

### Input
<a name="acxd-knowledge-base-documents-listknowledgebasedocuments-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| knowledgeBaseId | string | Yes | 
| nextToken | string | No | 
| maxResults | integer | No | 

### Sample Request
<a name="acxd-knowledge-base-documents-listknowledgebasedocuments-sample-request"></a>

```
client.send(new ListKnowledgeBaseDocumentsCommand({
      knowledgeBaseId: KNOWLEDGE_BASE_ID,
    }));
```

### Output
<a name="acxd-knowledge-base-documents-listknowledgebasedocuments-output"></a>

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
<a name="acxd-knowledge-base-documents-listknowledgebasedocuments-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## GetKnowledgeBaseDocument
<a name="acxd-knowledge-base-documents-getknowledgebasedocument"></a>

Gets a pre-signed download URL for a document.

### Input
<a name="acxd-knowledge-base-documents-getknowledgebasedocument-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| knowledgeBaseId | string | Yes | 
| documentId | string | Yes | 

### Sample Request
<a name="acxd-knowledge-base-documents-getknowledgebasedocument-sample-request"></a>

```
await client.send(new GetKnowledgeBaseDocumentCommand({
      knowledgeBaseId: KNOWLEDGE_BASE_ID,
      documentId: "product-guide-v2.pdf",
    }));
```

### Output
<a name="acxd-knowledge-base-documents-getknowledgebasedocument-output"></a>

```
{
  "url": "https://s3.amazonaws.com/bucket/path/document.pdf?X-Amz-Signature=..."
}
```

### Errors
<a name="acxd-knowledge-base-documents-getknowledgebasedocument-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## PutKnowledgeBaseDocument
<a name="acxd-knowledge-base-documents-putknowledgebasedocument"></a>

Registers a document and returns a pre-signed upload URL. Use the returned URL and fields to upload the file content.

### Input
<a name="acxd-knowledge-base-documents-putknowledgebasedocument-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| knowledgeBaseId | string | Yes | 
| documentId | string | Yes | 
| contentType | string | Yes | 
| customerMetadata | object | No | 

### Sample Request
<a name="acxd-knowledge-base-documents-putknowledgebasedocument-sample-request"></a>

```
await client.send(new PutKnowledgeBaseDocumentCommand({
  knowledgeBaseId: KNOWLEDGE_BASE_ID,
  documentId: "product-guide-v2.pdf",
  contentType: "application/pdf",
  customerMetadata: { category: "guides", version: "2.0" },
}));
```

### Output
<a name="acxd-knowledge-base-documents-putknowledgebasedocument-output"></a>

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

**Note**  
Use the returned `url` and `fields` to perform a multipart form upload of your document content.

### Errors
<a name="acxd-knowledge-base-documents-putknowledgebasedocument-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## DeleteKnowledgeBaseDocument
<a name="acxd-knowledge-base-documents-deleteknowledgebasedocument"></a>

Deletes a document.

### Input
<a name="acxd-knowledge-base-documents-deleteknowledgebasedocument-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| knowledgeBaseId | string | Yes | 
| documentId | string | Yes | 

### Sample Request
<a name="acxd-knowledge-base-documents-deleteknowledgebasedocument-sample-request"></a>

```
await client.send(new DeleteKnowledgeBaseDocumentCommand({
  knowledgeBaseId: KNOWLEDGE_BASE_ID,
  documentId: "product-guide-v2.pdf",
}));
```

### Output
<a name="acxd-knowledge-base-documents-deleteknowledgebasedocument-output"></a>

No response body.

### Errors
<a name="acxd-knowledge-base-documents-deleteknowledgebasedocument-errors"></a>
+ `ResourceNotFoundException` (404)
+ `ValidationException` (400)
+ `InternalServerException` (500)

## Request Parameters
<a name="acxd-knowledge-base-documents-request-parameters"></a>

`knowledgeBaseId`  
Type: String  
The knowledge base that contains the documents.

`documentId`  
Type: String  
The document identifier. User-provided, max 255 characters (e.g., a filename like `product-guide-v2.pdf` ).

`contentType`  
Type: String  
MIME type of the document (e.g., `application/pdf` , `text/plain` , `text/html` ).

`customerMetadata`  
Type: Object  
Free-form metadata for the document (structure defined by the knowledge base's `metadataSchema` ).

`uploadStatus`  
Type: String  
The document's upload status. One of: `PENDING` (registered but not yet uploaded), `UPLOADED` (file received), `DELETED` .

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